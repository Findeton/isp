# Relativistic ISP V3 Paper 16: Nonperturbative Continuum Yang-Mills Closure From ISP Record Gates

Author: Felix Robles Elvira

## Abstract

Papers 13--15 reduce the actual nonperturbative `SU(N)` Yang-Mills problem
to finite record-law gates. Paper 13 defines the six-gate `ACSB` route.
Paper 14 proves the first, second, and sixth gates from finite-block entry
`FBE`. Paper 15 proves that positive numerical connected-polymer surface
certificate `nCPSC` supplies the remaining gates and exports
`X_15(s_0,L,rho)`.

Paper 16 asks the closure question:

```text
Do the finite-battery packages X_15 assemble into a nontrivial
reflection-positive Euclidean-covariant continuum Yang-Mills Wilson-loop
functional?
```

The answer of this paper is conditional but sharp:

```text
actual YM trajectory + positive compatible X_15 tower + loop-completion gates
=> continuum-facing SU(N) Yang-Mills Wilson-loop functional.
```

The paper does not prove the Clay-level existence/mass-gap theorem. It
identifies the exact additional gates needed after Paper 15 and proves that,
if those gates hold, the ISP whole-process record law reaches the
nonperturbative continuum Yang-Mills interface.

### Post-Paper-20 Source Boundary

Paper 16 is a conditional closure architecture. It does not supply the later
Paper-20 `SEL2` tree-rate source, and it must not be cited for

```text
P20-SEL2-TREE-RATE-GATE,
T_-^{SEL2} > Theta_T^tree(rho),
q_rho gamma_rho > Theta_esc^tree.
```

Those are actual same-record block-plaquette coefficient estimates that remain
parked in Paper 20 unless separately proved.

## 0. Compact Theorem Summary

The closure theorem is:

```text
Positive X_15 tower
+ projective battery compatibility
+ regulator/chart independence
+ reflection positivity and Euclidean covariance
+ loop-topology continuity
+ nontrivial Wilson-loop anchor
=> continuum-facing nontrivial SU(N) Wilson-loop functional.
```

The closure theorem is first proved in certificate form as Theorem 10.1:

```text
CYC => CYM_WL.
```

Here `CYC` is the continuum Yang-Mills closure certificate defined below, and
`CYM_WL` is the continuum Wilson-loop record functional.

After the actual-trajectory reduction in Section 9A, the strongest form is
Theorem 10.1A:

```text
AYM-CLOSE => CYM_WL.
```

### Paper 16 Output

The final output of the paper is the conditional closure chain:

```text
HK-CYC-CLOSE
=> AYM-CLOSE
=> strong CYC
=> CYM_WL.
```

Equivalently: if the named heat-kernel ledgers are proved on one common
actual `4D SU(N)` asymptotically-free tower, then ISP reaches a nontrivial
reflection-positive Euclidean-covariant continuum Wilson-loop record
functional.

The output is a closure theorem, not an unconditional construction. The hard
work left after Paper 16 is to prove the named heat-kernel ledgers on the
actual continuum trajectory.

## 0A. Barandes-Aligned Ontology

The primitive object is still one whole-process pushed-forward law of
declared records. The closure argument is not allowed to:

1. compose unrecorded partial kernels as if the process were Markovian;
2. treat gauge-fixed fields as ontology;
3. treat residual polymers as particles;
4. infer a Hilbert space, mass gap, or confinement before the OS/Wightman
   representation layer is reconstructed;
5. hide regulator or gauge-chart dependence inside informal continuum
   notation.

Everything in this paper is a statement about operational record functionals:
finite Wilson-loop records, block character records, their connected
cumulants, their finite-battery limits, and their continuum completion.

## 0B. What Paper 16 Tries To Close

Paper 15 exports:

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

Paper 16 studies a directed family of such packages as:

```text
a -> 0,       cutoff refinement,
L -> infinity, finite-volume exhaustion,
s_0 -> 0 or fixed physical test scale, depending on the loop battery,
rho in Rep_f(SU(N)), finite representation battery,
loops C in a declared continuum loop class.
```

The closure problem is not merely to have many finite packages. They must be
compatible as one continuum record law.

## 0C. Honest Boundary

Paper 16 does not prove:

1. positive `nCPSC` for actual four-dimensional continuum `SU(N)` Yang-Mills
   without additional constructive input;
2. the Yang-Mills mass gap;
3. confinement or a full area-law theorem for arbitrary large loops;
4. QCD with dynamical matter;
5. gravity or a stress-energy/geometry reconstruction.

It proves that if the actual trajectory satisfies the explicit continuum
closure certificate, then ISP reaches a nontrivial reflection-positive
Euclidean-covariant continuum Wilson-loop functional for pure gauge
`SU(N)` Yang-Mills.

## 1. Imports

### 1.1 Paper 11

Paper 11 supplies the conditional AF multiscale and covariance ledger:

```text
Theorem AF.14:
uniform AF local-RG summability + defect summability
=> summable local-RG residuals.
```

It also supplies the whole-process warning: finite-range or conditioned
covariance decompositions are certificate coordinates, not hidden Markov
subprocesses.

### 1.2 Paper 12

Paper 12 supplies the renormalized Wilson-loop finite-battery bridge:

```text
Theorem 3.6C:
AF trajectory gives the local connected-polymer criterion.

Theorem 3.7:
Paper-11 RG control + perimeter/cusp renormalization
=> finite cumulant envelope and product-boundedness.
```

Paper 16 uses Paper 12 in three specific places:

1. the admissible loop metric `d_adm` imported in Definition 9X.1;
2. the calibrated perimeter/cusp counterterm and smearing-removal ledgers
   used in `HK-LC-TRANSPORT`;
3. the AF loop-variation modulus imported through Definition 9X.1A and
   Theorem 9X.1E.

### 1.3 Paper 13

Paper 13 defines the six actual-continuum strong-block gates:

```text
BC, CE, RPF, KP_dec, SUB, WP.
```

Definition 7.30Y gives the gate decomposition. Theorem 7.30Z proves:

```text
BC + CE + RPF + KP_dec + SUB + WP
=> ACSB(s_0,rho,L).
```

The Section 7.30 route is:

```text
ACSB -> SB -> surface-polymer entry -> exact RG entry -> RSB.
```

Paper 16 uses Paper 13 for the nontriviality route: the scale-resolved
Creutz transport ledger and scalar loop-record extraction are imported in
Definition 9Y.1 and Definition 9Y.1A.

### 1.4 Paper 14

Paper 14 proves:

```text
Theorem 4.2:
FBE => BC + CE + WP.

Theorem 32.1:
finite-block entry closure gives FBE and exports X_14.
```

Paper 16 uses Paper 14 only through finite-block entry on the common
record-law tower. In the final closure chain this appears as the `FBE` input
inside `HK-X15-CLOSE`.

### 1.5 Paper 15

Paper 15 proves:

```text
Theorem 12.6:
Paper-14 FBE + positive nCPSC
=> BC + CE + WP + RPF + KP_dec + SUB
=> ACSB
=> RSB_route
=> X_15.
```

Paper 16 imports `X_15`, not the intermediate proofs, except when diagnosing
which `nCPSC` subgate remains open.

Paper 16 also imports the Paper-15 numerical margins by name:
`eta_res^{bd}`, `eta_dec^{bd}`, `M_SUB^{bd}`, and `M_15^{bd}`. These feed
the positive numerical branch, the Creutz reserve gate, and the
Paper-13/15 scalar-anchor package in Section 9Y.

## 2. Continuum Test Class

### Definition 2.1: Admissible Wilson-Loop Test Class

An admissible continuum Wilson-loop test class `Loop_adm` is a countable
nested family

```text
Loop_1 subset Loop_2 subset ...
```

where each `Loop_k` is finite and consists of piecewise `C^2` embedded
closed loops with:

1. bounded perimeter;
2. bounded curvature on smooth arcs;
3. finitely many cusps with angles bounded away from `0` and `pi`;
4. separation between distinct cusps and nonadjacent arcs;
5. declared lattice/block approximants compatible with Papers 12--15.

The union is dense in the declared loop topology `d_loop`.

### Definition 2.2: Wilson-Loop Record Algebra

For finite `k`, representation battery `Rep_k`, and volume `L`, define
`A_{k,L}` as the finite algebra generated by scalar records

```text
W_{rho}(C),
C in Loop_k, rho in Rep_k,
```

and finite products up to declared degree `p_k`.

The records are normalized scalar traces. They are not field configurations.

### Definition 2.3: Continuum Wilson-Loop Functional

A continuum Wilson-loop functional is a map

```text
W_infty : A_adm -> C
```

on the inductive algebra

```text
A_adm = union_k A_k
```

such that:

1. `W_infty(1)=1`;
2. `W_infty` is positive on the reflection-positive OS subalgebra;
3. `W_infty` is Euclidean covariant;
4. `W_infty` is gauge invariant because all records are scalar closed-loop
   records;
5. `W_infty` is continuous in `d_loop` on the declared loop class;
6. at least one nontrivial Wilson-loop record differs from the trivial
   functional by a positive amount.

This is a continuum-facing Yang-Mills Wilson-loop functional. A Hilbert-space
representation is a later reconstruction from this functional.

## 3. Towers Of `X_15`

### Definition 3.1: Finite Closure Tower

A finite closure tower is a directed family

```text
T = { X_15(k,L,s_0,rho) }
```

indexed by finite loop battery `k`, finite volume `L`, block/test scale
`s_0`, and representation battery `rho`, such that every node is a Paper-15
export package with positive `nCPSC`.

The tower is nested when restriction from a larger node to a smaller finite
battery agrees up to a declared projectivity defect.

### Definition 3.2: Tower Projectivity Defect

For nodes `i <= j`, let

```text
pi_{j->i}: A_j -> A_i
```

be restriction of records. Let `W_j` and `W_i` be the finite Wilson-loop
functionals induced by `X_15(j)` and `X_15(i)`. The projectivity defect is:

```text
eps_proj(i,j)
 =
 sup_{F in A_i, ||F||<=1}
 | W_j(pi_{j->i}^*F) - W_i(F) |.
```

The tower has summable projectivity if along every cofinal chain

```text
sum_n eps_proj(i_n,i_{n+1}) < infinity.
```

### Lemma 3.3: Summable Projectivity Gives Finite-Test Limits

If the tower has summable projectivity, then for every fixed finite test
`F in A_i`, the values along any cofinal chain form a Cauchy sequence.

Proof.

For `m>n`,

```text
|W_{i_m}(F)-W_{i_n}(F)|
<=
sum_{ell=n}^{m-1} eps_proj(i_ell,i_{ell+1}) ||F||.
```

The summable tail tends to zero. `square`

## 4. Continuum Closure Certificate

### Definition 4.1: Continuum Yang-Mills Closure Certificate `CYC`

The continuum Yang-Mills closure certificate `CYC` consists of:

1. **Positive `X_15` tower.** Every finite node has positive `nCPSC`, hence
   exports `X_15`.
2. **Summable projectivity.** The tower satisfies Definition 3.2.
3. **Volume exhaustion.** Finite-volume boundary defects vanish on every
   fixed local Wilson-loop battery.
4. **Regulator and chart independence.** Any two admissible regulator or
   gauge-chart ledgers have common refinements whose comparison defects
   vanish on every fixed finite battery.
5. **Reflection positivity.** The finite node functionals are
   reflection-positive up to summable defects.
6. **Euclidean covariance.** The finite node functionals are Euclidean
   covariant up to summable approximant defects.
7. **Loop continuity.** There is a modulus `omega(delta)->0` and errors
   `zeta_i->0` such that finite Wilson-loop records satisfy

   ```text
   |W_i(C)-W_i(C')| <= omega(d_loop(C,C')) + zeta_i
   ```

   for loops in the declared admissible class.
8. **Nontriviality anchor.** There is a fixed Wilson-loop record `T_*`, a
   trivial reference value `T_triv`, and `c_*>0` such that

   ```text
   |W_i(T_*)-T_triv| >= c_*
   ```

   on a cofinal tail.
9. **Whole-process compatibility.** All the above defects compare
   pushed-forward whole-process record laws, not unrecorded partial kernels.

### Definition 4.2: Strong And Weak `CYC`

`Strong CYC` means all limits exist along the full declared continuum path.

`Weak CYC` means all limits exist along at least one cofinal subsequence, with
the same compatibility, positivity, covariance, continuity, and nontriviality
conditions on that subsequence.

Strong `CYC` gives a unique functional on the declared path. Weak `CYC` gives
a subsequential continuum interface and a non-uniqueness warning.

## 5. Constructing The Continuum Functional

### Theorem 5.1: `CYC` Gives A Wilson-Loop Functional On The Countable Algebra

Assume strong `CYC`. Then there is a unique functional

```text
W_infty : A_adm -> C
```

defined by

```text
W_infty(F) = lim_i W_i(F)
```

for every finite test `F`.

Proof.

For any fixed `F`, choose a tower node containing it. Lemma 3.3 gives
Cauchy convergence along every cofinal chain. Summable projectivity makes the
limit independent of the chosen larger nodes. Linearity and normalization
pass to the limit because they hold at each finite node. `square`

### Theorem 5.2: Weak `CYC` Gives A Subsequence Functional

Assume weak `CYC`. Then every cofinal subsequence satisfying the weak
certificate has a continuum-facing subsequential Wilson-loop functional.

Proof.

Repeat Theorem 5.1 on the subsequence. `square`

## 6. Positivity, Covariance, And Gauge Invariance

### Theorem 6.1: Reflection Positivity Survives The Closure Limit

Assume `CYC` reflection-positivity defects are summable and vanish in the
tail. Then `W_infty` is reflection-positive on the declared OS subalgebra.

Proof.

For every finite OS-positive test `F`, the finite nodes satisfy

```text
W_i(theta F * F) >= -eps_RP(i) ||F||^2.
```

Taking the continuum limit and using `eps_RP(i)->0` gives
`W_infty(theta F * F)>=0`. `square`

### Theorem 6.2: Euclidean Covariance Survives The Closure Limit

Assume `CYC` Euclidean covariance defects vanish for the declared loop
approximants. Then

```text
W_infty(gC_1,...,gC_n) = W_infty(C_1,...,C_n)
```

for every Euclidean motion `g` preserving the admissible class.

Proof.

The finite approximants satisfy covariance up to defect
`eps_Euc(i,g,F)`. The defect vanishes on the cofinal tail, and loop
continuity removes the approximant error. `square`

### Proposition 6.3: Gauge Invariance Is Built Into The Record Class

The continuum functional is gauge invariant on `A_adm`.

Proof.

The generators of `A_adm` are scalar closed Wilson-loop traces and their
finite products. Gauge transformations act trivially on these scalar closed
records. `square`

## 7. Loop Completion And Continuity

### Definition 7.1: Loop Completion Gate `LC`

The loop completion gate holds if the countable admissible class is dense in
a loop space `Loop_comp`, and the finite functionals obey the `CYC` continuity
modulus uniformly enough that `W_infty` extends uniquely to `Loop_comp`.

### Theorem 7.2: Loop Continuity Gives Unique Extension

If `LC` holds, then `W_infty` extends uniquely from `Loop_adm` to the
completion `Loop_comp`.

Proof.

For any Cauchy sequence of admissible loops, the continuity modulus makes
the corresponding Wilson-loop values Cauchy. If two admissible sequences
converge to the same completed loop, the same modulus makes the two limits
agree. `square`

### Honest Boundary Of `LC`

The admissible class deliberately avoids arbitrarily sharp cusps,
self-intersections, and accumulating near-tangencies. Extending beyond that
class requires new renormalization data, not a notational completion trick.

## 8. Nontriviality

### Theorem 8.1: Anchored Nontriviality Survives

If the `CYC` nontriviality anchor holds, then `W_infty` is not the trivial
Wilson-loop functional.

Proof.

The inequality

```text
|W_i(T_*)-T_triv| >= c_*
```

is closed under the continuum limit. Hence

```text
|W_infty(T_*)-T_triv| >= c_*.
```

`square`

### Remark 8.2: This Is Not A Mass Gap

Nontriviality of a Wilson-loop functional is necessary for Yang-Mills
content. It is not a proof of a positive spectral gap. Paper 17 must add the
representation-level mass-gap gates.

## 9. Actual `nCPSC` Verification Ledger

Paper 16 must classify the Paper-15 numerical certificate on the actual
continuum trajectory.

| `nCPSC` component | Current source | Paper-16 status |
| --- | --- | --- |
| `AFRCE(A_AF,mu_AF,r_*)` | Papers 11--12 plus Paper 15 Section 6A | conditional on actual AF/local-polymer constants |
| `eta_res^{bd}<1` | Paper 15 Theorem 7.2A | conditional on positive raw margin and enough decay over entropy |
| `eta_dec^{bd}<1` | Paper 15 Theorem 8A.2 | conditional on Paper-14 character tail budget |
| `M_SUB^{bd}>0` | Paper 15 Theorem 10A.2 | conditional on surface entropy versus leading coefficient |
| `M_15^{bd}>0` | Paper 15 Theorem 11A.3 | conditional on nonzero Creutz reserve after transport |
| whole-process compatibility | Papers 11, 14, 15 | must be checked on common refinements |

### Definition 9.1: Verified Positive `nCPSC`

The actual continuum trajectory has verified positive `nCPSC` if every row
in the table above is proved on a cofinal tower of finite batteries, with
all constants computed for the same whole-process pushed-forward record law.

### Theorem 9.2: Verified Positive `nCPSC` Gives Positive `X_15` Tower

If Paper 14's `FBE` tower holds and the actual continuum trajectory has
verified positive `nCPSC`, then the tower of `X_15` packages is positive.

Proof.

This is Paper 15 Theorem 12.6 applied at every finite tower node, with the
same constants made compatible by the verified whole-process clause. `square`

## 9A. Actual-Trajectory Reduction

The phrase "actual 4D `SU(N)` Yang-Mills" is made precise in this paper by
starting from finite lattice gauge measures and then asking whether the
declared continuum trajectory satisfies the record-law certificates above.
This section proves the finite-cutoff part and isolates the nonperturbative
continuum part.

### Definition 9A.1: Cutoff Yang-Mills Record Law

Fix:

1. a compact gauge group `G=SU(N)`;
2. a four-dimensional hypercubic finite torus `Lambda_{a,L}` with lattice
   spacing `a` and physical side length `L`;
3. link variables `U_e in G`;
4. a standard gauge-invariant reflection-positive plaquette action
   `S_{a,L,beta}` such as the Wilson action or heat-kernel action;
5. a finite battery `B` of closed Wilson-loop traces, block character
   records, Creutz records, decoration records, and surface records.

The cutoff Yang-Mills probability measure is

```text
dmu_{a,L,beta}(U)
 =
 Z_{a,L,beta}^{-1} exp(-S_{a,L,beta}(U)) product_e dHaar(U_e).
```

The cutoff ISP record law is the pushed-forward law

```text
Gamma_{a,L,beta,B}
 =
 (R_B)_* dmu_{a,L,beta},
```

where `R_B` is the declared finite-battery record map.

This is the only primitive probabilistic object at cutoff. Gauge fields,
plaquette variables, and character expansions are coordinates used to prove
facts about `Gamma_{a,L,beta,B}`.

### Lemma 9A.2: Cutoff Record Laws Are Exact Whole-Process Laws

For every finite `a,L,beta,B`, the law `Gamma_{a,L,beta,B}` exists, is
normalized and positive, is gauge invariant on closed scalar Wilson-loop
records, and is compatible with the finite lattice symmetry group. If the
chosen plaquette action is reflection positive, then the cutoff Wilson-loop
functional is reflection positive at the lattice level.

Proof.

The finite link space is a finite product of compact groups. Haar measure is
finite and the Boltzmann weight is nonnegative and continuous for the
declared actions. Hence `Z_{a,L,beta}` is finite and positive, and the
normalized measure exists.

The map `R_B` is a finite collection of bounded continuous class functions
of link variables. Its pushforward is therefore a normalized positive record
law. Gauge invariance follows by changing variables with local gauge
transformations and using invariance of Haar measure together with
gauge-invariance of the action and of closed Wilson-loop traces. Finite
lattice covariance follows similarly from lattice automorphisms preserving
the action and the battery. Reflection positivity is inherited from the
chosen reflection-positive lattice action by applying the standard
half-lattice reflection-positivity inequality to functions generated by the
battery records. `square`

### Definition 9A.3: Actual-Trajectory Closure Certificate `AYM-CLOSE`

The actual `4D SU(N)` trajectory satisfies `AYM-CLOSE` if there is a cofinal
directed family

```text
i = (a_i,L_i,beta_i,B_i,Rep_i,Loop_i)
```

with `a_i -> 0`, `L_i -> infinity`, finite batteries increasing to
`A_adm`, representation batteries `Rep_i`, loop batteries `Loop_i`, and
running couplings `beta_i` on the intended asymptotically-free continuum
trajectory, such that all of the following hold for the same whole-process
cutoff laws `Gamma_i`:

1. **Finite cutoff law.** Each `Gamma_i` is the pushed-forward cutoff law of
   Definition 9A.1.
2. **Paper-14 entry.** The `FBE` tower holds on the same battery tower.
3. **AF residual envelope.** The actual connected record polymers satisfy
   `AFRCE(A_AF,mu_AF,r_*)` with scale-independent constants after the
   declared finite renormalizations.
4. **KP margin.** The residual activity satisfies the Paper-15 KP numerical
   inequality `eta_res^{bd}<1` with a positive uniform reserve.
5. **Character-tail margin.** The detail-character tail satisfies
   `eta_dec^{bd}<1` with a positive uniform reserve.
6. **Surface reserve.** The subcritical surface margin satisfies
   `M_SUB^{bd}>0` uniformly on the cofinal tower.
7. **Creutz reserve.** The transported Creutz margin satisfies
   `M_15^{bd}>0` uniformly on the cofinal tower.
8. **Projectivity.** For every fixed battery `B_j`, the pushed-forward
   marginals form a Cauchy family under refinement. Concretely, for
   `i>m>=j` there are adjacent-shell defects `delta_{j,k}` such that:

```text
|| Pi_{i->j,*}Gamma_i - Pi_{m->j,*}Gamma_m ||_{op,j}
 <=
 sum_{k=m}^{i-1} delta_{j,k},

sum_{k>=j} delta_{j,k} < infinity.
```

   after passing through the declared common refinements. If a canonical
   finite-battery reference law `Gamma_j^ref` has already been chosen, this
   may equivalently be written as convergence to `Gamma_j^ref` with a
   summable tail. It should not be read as convergence to the raw cutoff law
   at level `j`.
9. **Regulator and chart independence.** Wilson, heat-kernel, gauge-chart,
   and blocking choices connected by the declared comparison maps have
   summable record discrepancies.
10. **Reflection positivity and covariance transport.** Reflection-positivity
    and Euclidean-covariance defects vanish on the finite loop algebra after
    transport to the continuum test class.
11. **Loop continuity.** The renormalized Wilson-loop records obey the
    `CYC` continuity modulus on `Loop_adm`.
12. **Nontriviality anchor.** There is a declared finite record `T_*` and
    `c_*>0` such that the renormalized cutoff functionals obey
    `|W_i(T_*)-T_triv|>=c_*` eventually.
13. **Whole-process compatibility.** Every constant above is computed from
    the same pushed-forward laws `Gamma_i`; no estimate composes unrecorded
    partial kernels as if the process were divisible.

### Theorem 9A.4: `AYM-CLOSE` Proves Verified Positive `nCPSC`

If the actual trajectory satisfies `AYM-CLOSE`, then the actual continuum
trajectory has verified positive `nCPSC`.

Proof.

Clauses 3--7 of `AYM-CLOSE` are exactly the five numerical positivity
requirements in the Paper-15 `nCPSC` ledger: the AF residual envelope, the
KP residual margin, the character-tail margin, the subcritical surface
reserve, and the transported Creutz reserve. Clause 2 supplies the Paper-14
entry tower to which Paper 15 applies. Clause 13 supplies the verified
whole-process compatibility required in Definition 9.1. Therefore every row
of the actual `nCPSC` verification ledger is proved on the same cofinal
tower with compatible constants. `square`

### Theorem 9A.5: `AYM-CLOSE` Proves Strong `CYC`

If the actual trajectory satisfies `AYM-CLOSE`, then the resulting positive
`X_15` tower satisfies strong `CYC`.

Proof.

By Theorem 9A.4 and Theorem 9.2, clauses 2--7 and 13 give a positive
`X_15` tower. Clause 8 is the summable projectivity condition in Definition
4.1. Clause 9 gives regulator and chart independence. Clause 10 gives the
reflection-positivity and Euclidean-covariance parts of `CYC`. Clause 11
gives loop continuity. Clause 12 gives the nontriviality anchor.

Because all defects are summable or vanish along the full declared cofinal
trajectory, the limits are not merely subsequential. Thus the certificate is
strong `CYC`, not weak `CYC`. `square`

### Corollary 9A.6: Actual-Trajectory Closure Reduction

For pure `SU(N)` gauge theory, the following implication is now proved:

```text
AYM-CLOSE
=> verified positive nCPSC
=> positive X_15 tower
=> strong CYC.
```

The remaining hard problem is not a missing ISP step. It is the
nonperturbative constructive Yang-Mills task of proving the `AYM-CLOSE`
clauses for the actual asymptotically-free `4D SU(N)` continuum trajectory.

## 9B. `AYM-CLOSE` Verification Workbench

To work on `AYM-CLOSE` without losing track of the ontology, we split it into
subcertificates. Each subcertificate is a statement about the same
whole-process pushed-forward record laws `Gamma_i`.

### Definition 9B.1: Named `AYM-CLOSE` Subcertificates

For a cofinal actual trajectory `i=(a_i,L_i,beta_i,B_i)`, define:

| Name | Content |
| --- | --- |
| `AYM-LAW` | the cutoff laws are the pushed-forward finite lattice `SU(N)` record laws of Definition 9A.1 |
| `AYM-FBE` | Paper-14 finite-block entry holds on the same battery tower |
| `AYM-AFRCE` | the actual connected record polymers satisfy `AFRCE(A_AF,mu_AF,r_*)` |
| `AYM-KP` | the Paper-15 residual KP bound has `eta_res^{bd}<1` with positive reserve |
| `AYM-TAIL` | the character-tail bound has `eta_dec^{bd}<1` with positive reserve |
| `AYM-SURF` | the surface-subcritical reserve has `M_SUB^{bd}>0` |
| `AYM-CREUTZ` | the transported Creutz reserve has `M_15^{bd}>0` |
| `AYM-PROJ` | finite-battery marginals have summable projectivity defects |
| `AYM-REG` | regulator, gauge-chart, and blocking comparison defects are summable |
| `AYM-RP-COV` | reflection-positivity and Euclidean-covariance defects vanish in the continuum record algebra |
| `AYM-LC` | renormalized Wilson-loop records obey the declared loop-continuity modulus |
| `AYM-NT` | a nontrivial Wilson-loop anchor survives with positive reserve |
| `AYM-WP` | all constants are computed from one whole-process record law, with no undeclared partial-kernel composition |

### Theorem 9B.2: Workbench Equivalence

The conjunction of the subcertificates in Definition 9B.1 proves
`AYM-CLOSE`. Conversely, every clause of `AYM-CLOSE` is one of these
subcertificates.

Proof.

`AYM-LAW` is clause 1 of Definition 9A.3. `AYM-FBE` is clause 2.
`AYM-AFRCE`, `AYM-KP`, `AYM-TAIL`, `AYM-SURF`, and `AYM-CREUTZ` are clauses
3--7. `AYM-PROJ` is clause 8. `AYM-REG` is clause 9. `AYM-RP-COV`,
`AYM-LC`, `AYM-NT`, and `AYM-WP` are clauses 10--13. Hence the workbench is
just `AYM-CLOSE` with each proof obligation named separately. `square`

### Status After The Workbench Split

| Subcertificate | Status in Paper 16 after this section |
| --- | --- |
| `AYM-LAW` | proved at finite cutoff by Lemma 9A.2 |
| `AYM-REG` | primary heat-kernel trajectory chosen in Section 9C; reduced in Section 9V to summable finite-record comparison defects |
| `AYM-AFRCE` | reduced in Sections 9D--9F to heat-kernel small-field, large-field, and counterterm-stability bounds |
| `AYM-FBE`, `AYM-KP`, `AYM-TAIL`, `AYM-SURF`, `AYM-CREUTZ` | imported from Papers 14--15 once their actual-trajectory constants are verified |
| `AYM-PROJ` | reduced in Section 9U to summable finite-battery marginal defects |
| `AYM-RP-COV`, `AYM-LC`, `AYM-NT`, `AYM-WP` | reduced in Sections 9W--9Z to explicit RP/covariance, loop-continuity, anchor, and ledger-audit defects |

## 9C. Primary Regulator Path

The proof attempt needs one primary regulator. Wilson and heat-kernel lattice
actions may define the same continuum theory only after a comparison theorem;
using both at once would hide the regulator-independence burden. Paper 16
therefore chooses the heat-kernel action as the primary path and treats the
Wilson action as a later `AYM-REG` comparison chart.

### Definition 9C.1: Heat-Kernel Actual Trajectory `HK-AYM`

The heat-kernel actual trajectory `HK-AYM` is the cofinal family of finite
lattice record laws with plaquette weight

```text
K_t(U)
 =
 sum_{lambda in Irrep(SU(N))}
 dim(lambda) exp(-t C_2(lambda)/2) chi_lambda(U),
```

and cutoff measure

```text
dmu_i^{HK}(U)
 =
 Z_i^{-1} product_p K_{t_i}(U_p) product_e dHaar(U_e).
```

The bare heat-kernel time `t_i` is chosen on the intended pure-Yang-Mills
asymptotically-free trajectory. In the continuum normalization used here,
the running coupling satisfies

```text
g_i^{-2}
 =
 2 beta_0 log(1/(a_i Lambda))
 + (beta_1/beta_0) log log(1/(a_i Lambda))
 + O(1),
```

with

```text
beta_0 = 11 N/(48 pi^2),
beta_1 = 34 N^2/(3 (16 pi^2)^2),
```

and `t_i=g_i^2+O(g_i^4)` after the declared finite scheme choice. The `O(1)`
and `O(g_i^4)` terms are not ignored; they belong to `AYM-REG` and must be
controlled by summable comparison defects.

### Lemma 9C.2: Why Heat-Kernel Is The Primary Path

The heat-kernel path is better suited to the `AYM-CLOSE` proof attempt than
the Wilson path because:

1. its character expansion has positive coefficients;
2. its plaquette factor is central and gauge invariant;
3. the heat kernel has a convolution semigroup structure;
4. standard reflection-positivity arguments apply at finite cutoff;
5. blocking and character-tail estimates have a natural representation-space
   ledger.

This does not prove Wilson/heat-kernel universality. It only chooses the
coordinate system in which `AYM-AFRCE` is first attacked.

Proof.

The displayed character formula has nonnegative coefficients and is central.
Gauge invariance follows from centrality and Haar invariance. The heat-kernel
identity `K_{t+s}=K_t*K_s` supplies the semigroup bookkeeping that is absent
from the raw Wilson exponential. Reflection positivity is part of the
standard finite-cutoff heat-kernel lattice action package used in Lemma
9A.2. These are regulator-level advantages, not ontology. The primitive
object remains the pushed-forward record law. `square`

### Corollary 9C.3: `HK-AYM` Proves `AYM-LAW`

For every finite node of `HK-AYM`, `AYM-LAW` holds. Moreover the finite
cutoff laws have exact gauge invariance and finite lattice covariance, and
they have lattice reflection positivity for the declared reflection.

Proof.

Apply Lemma 9A.2 to the heat-kernel action. `square`

## 9D. First Attack On `AYM-AFRCE`

The `AYM-AFRCE` gate is the first serious continuum analytic bottleneck.
Finite cutoff cumulants are bounded for trivial compactness reasons. What is
hard is uniform, coefficient-normalized, connected-polymer decay along the
asymptotically-free continuum trajectory.

### Lemma 9D.1: Finite-Battery Cumulants Are Bounded At Cutoff

Let `F_1,...,F_n` be bounded scalar records in a finite battery at a finite
`HK-AYM` node. Their connected cumulant exists and obeys

```text
|kappa_i(F_1,...,F_n)|
 <=
 2^{n-1} (n-1)! product_{j=1}^n ||F_j||_infty.
```

Proof.

The cutoff record law is a probability measure on a compact finite record
space. The joint moment generating function of bounded records is analytic
near the origin. The connected cumulant is obtained by differentiating the
log of that generating function. The displayed bound is the standard
bounded-variable cumulant estimate obtained by expanding the logarithm over
set partitions and bounding every moment by the product of sup norms.
`square`

### Definition 9D.2: Heat-Kernel Local-Cluster Bound `HK-LCB`

Fix a block scale and let `Y` range over connected polymers in the block
graph. Let `K_i(Y)` denote the renormalized connected residual coefficient
of the whole-process record law after the declared local counterterms have
been removed. The heat-kernel local-cluster bound `HK-LCB` holds with
constants

```text
A_sf, A_lf, mu_sf, mu_lf, g_*, p, r_*
```

if, for every sufficiently fine node `i`, every RG scale in the declared
finite battery, and every `r>=r_*`, the residual coefficients split as

```text
K_i(Y) = K_i^{sf}(Y) + K_i^{lf}(Y)
```

and satisfy the coefficient-normalized tail bounds

```text
sup_x sum_{Y contains x, diam(Y)>=r} ||K_i^{sf}(Y)||_ren
 <=
 A_sf g_i^{2p} exp(-mu_sf r),

sup_x sum_{Y contains x, diam(Y)>=r} ||K_i^{lf}(Y)||_ren
 <=
 A_lf exp(-mu_lf r),

g_i^2 <= g_*^2.
```

The labels `sf` and `lf` mean small-field and large-field estimates inside
the proof coordinate system. They are not two subprocesses and are not
composed as Markov kernels.

### Theorem 9D.3: `HK-LCB` Proves `AYM-AFRCE`

Assume `HK-AYM` and `HK-LCB`. Then `AYM-AFRCE` holds with

```text
A_AF = A_sf g_*^{2p} + A_lf,
mu_AF = min(mu_sf, mu_lf),
```

and the same `r_*`.

Proof.

For `r>=r_*`, sum the small-field and large-field tail estimates in
Definition 9D.2:

```text
sup_x sum_{Y contains x, diam(Y)>=r} ||K_i(Y)||_ren
 <=
 A_sf g_i^{2p} exp(-mu_sf r)
 + A_lf exp(-mu_lf r).
```

Since `g_i^2<=g_*^2`, this is bounded by

```text
(A_sf g_*^{2p}+A_lf) exp(-min(mu_sf,mu_lf) r).
```

This is exactly the coefficient-normalized residual envelope
`AFRCE(A_AF,mu_AF,r_*)` required by `AYM-AFRCE`. The estimate is made on the
same cutoff record laws and therefore respects `AYM-WP`. `square`

### Corollary 9D.4: Current Status Of `AYM-AFRCE`

Paper 16 has not unconditionally proved `AYM-AFRCE` for actual continuum
`4D SU(N)` Yang-Mills. It has proved the sharp reduction:

```text
HK-AYM + HK-LCB => AYM-AFRCE.
```

Thus the next analytic target is not vague "RG control"; it is the concrete
heat-kernel local-cluster bound `HK-LCB` with constants strong enough to feed
the Paper-15 KP and surface-margin inequalities.

## 9E. Sufficient Conditions For `HK-LCB`

This section pushes Step 1 one layer deeper. The local-cluster bound
`HK-LCB` should not be treated as an opaque black box. It is proved if three
more primitive heat-kernel estimates hold:

```text
small-field Gaussian connected decay
+ large-field suppression
+ local counterterm stability
=> HK-LCB.
```

These estimates are still hard constructive Yang-Mills estimates. The point
of this section is to state them in a form that is strong enough for the ISP
record-law route and weak enough not to import a completed continuum theory.

### Definition 9E.1: Small-Field Gaussian Connected Decay `HK-SF-GCD`

Fix the heat-kernel trajectory `HK-AYM` and a block axial-tree gauge chart
used only as a proof coordinate system. Let `K_i^{sf}(Y)` denote the
small-field contribution to the renormalized connected residual coefficient
of a connected block polymer `Y`.

`HK-SF-GCD(C_sf,C_ent,theta_sf,mu_G,p,r_*)` holds if:

1. the gauge-fixed small-field covariance admits a connected graph
   domination by edge weights with exponential decay rate `mu_G`;
2. the renormalized local vertices left after the declared local
   counterterms carry at least the factor `g_i^{2p}`;
3. the connected graph/cluster expansion has tree activity
   `theta_sf<1`;
4. for every sufficiently fine node `i` and every `r>=r_*`,

```text
sup_x sum_{Y contains x, diam(Y)>=r} ||K_i^{sf}(Y)||_ren
 <=
 (C_sf C_ent/(1-theta_sf)) g_i^{2p} exp(-(mu_G/2) r).
```

The condition is phrased directly on the pushed-forward record coefficients.
The gauge chart, covariance, and tree expansion are proof coordinates, not
new ontology and not hidden subprocesses.

### Lemma 9E.2: Why `HK-SF-GCD` Is The Right Small-Field Target

Assume the small-field covariance has exponential edge decay and the
renormalized local vertices have tree activity `theta_sf<1`. Then the
standard tree-graph bound gives the last inequality in Definition 9E.1.

Proof.

The connected small-field coefficient is expanded over connected graphs
whose edges are covariance contractions and whose vertices are local
renormalized interaction records. The tree-graph inequality bounds the sum
over connected graphs by a sum over spanning trees times the convergent
activity factor `(1-theta_sf)^{-1}`. Exponential edge decay implies that any
tree connecting a polymer of diameter at least `r` has total edge length at
least `r`; allocating half of that decay to the tree distance and half to
the polymer-entropy sum gives the factor `exp(-(mu_G/2) r)`. The remaining
entropy is the declared constant `C_ent`. The vertex bound supplies
`g_i^{2p}`. `square`

### Definition 9E.3: Large-Field Suppression `HK-LFS`

Let `K_i^{lf}(Y)` be the large-field contribution to the renormalized
connected residual coefficient. `HK-LFS(C_lf,C_ent,sigma_lf,h_lf,r_*)` holds
if:

1. the probability/activity cost of a connected large-field polymer of block
   size `|Y|` is bounded by `C_lf exp(-sigma_lf |Y|)`;
2. the number of connected block polymers of size `n` containing a fixed
   block is bounded by `C_ent exp(h_lf n)`;
3. `sigma_lf>h_lf`;
4. for every sufficiently fine node `i`, large-field coefficients are
   dominated by those activities.

### Lemma 9E.4: `HK-LFS` Gives The Large-Field Half Of `HK-LCB`

If `HK-LFS(C_lf,C_ent,sigma_lf,h_lf,r_*)` holds, then for every `r>=r_*`,

```text
sup_x sum_{Y contains x, diam(Y)>=r} ||K_i^{lf}(Y)||_ren
 <=
 A_lf exp(-mu_lf r),
```

with

```text
mu_lf = sigma_lf - h_lf,
A_lf = C_lf C_ent/(1-exp(-(sigma_lf-h_lf))).
```

Proof.

Every connected polymer of diameter at least `r` has at least `r` blocks in
graph-distance units after increasing `r_*` once if necessary. Therefore the
large-field tail is bounded by

```text
sum_{n>=r} C_lf C_ent exp(-(sigma_lf-h_lf)n).
```

Since `sigma_lf>h_lf`, the geometric series converges and gives the stated
constants. `square`

### Definition 9E.5: Counterterm Stability `HK-CTS`

The counterterm-stability gate `HK-CTS(A_ct,mu_ct,p,r_*)` holds if the
declared local renormalizations and finite scheme changes alter the
connected residual coefficients only by a local part plus a summable tail:

```text
sup_x sum_{Y contains x, diam(Y)>=r} ||Delta K_i^{ct}(Y)||_ren
 <=
 A_ct g_i^{2p} exp(-mu_ct r)
```

for all `r>=r_*`. Purely local counterterms supported on polymers with
`diam(Y)<r_*` do not enter the residual tail.

### Theorem 9E.6: Small/Large Field Gates Prove `HK-LCB`

Assume `HK-AYM`, `HK-SF-GCD(C_sf,C_ent,theta_sf,mu_G,p,r_*)`,
`HK-LFS(C_lf,C_ent_lf,sigma_lf,h_lf,r_*)`, and
`HK-CTS(A_ct,mu_ct,p,r_*)`. Then `HK-LCB` holds with

```text
A_sf = C_sf C_ent/(1-theta_sf) + A_ct,
mu_sf = min(mu_G/2, mu_ct),
A_lf = C_lf C_ent_lf/(1-exp(-(sigma_lf-h_lf))),
mu_lf = sigma_lf - h_lf,
```

provided `theta_sf<1`, `sigma_lf>h_lf`, and `g_i^2<=g_*^2` eventually along
the asymptotically-free trajectory.

Proof.

Definition 9E.1 gives the small-field residual tail before counterterm-tail
corrections:

```text
sup_x sum_{Y contains x, diam(Y)>=r} ||K_i^{sf}(Y)||_ren
 <=
 (C_sf C_ent/(1-theta_sf)) g_i^{2p} exp(-(mu_G/2) r).
```

Definition 9E.5 adds at most

```text
A_ct g_i^{2p} exp(-mu_ct r).
```

Combining the two estimates gives the `HK-LCB` small-field bound with
`A_sf` and `mu_sf` as displayed. Lemma 9E.4 gives the `HK-LCB` large-field
bound with `A_lf` and `mu_lf`. Asymptotic freedom gives `g_i^2<=g_*^2` after
discarding finitely many coarse nodes. These are exactly the estimates in
Definition 9D.2. `square`

### Corollary 9E.7: Step-1 Reduction For `AYM-AFRCE`

For the heat-kernel trajectory,

```text
HK-SF-GCD + HK-LFS + HK-CTS
=> HK-LCB
=> AYM-AFRCE.
```

The proof of actual `AYM-AFRCE` is therefore reduced to proving three
coordinate-level constructive estimates with constants strong enough for
the Paper-15 numerical gates. The reduction is Barandes-aligned because the
estimates are always pushed back to coefficients of the same whole-process
record laws.

## 9F. Large-Field Gate `HK-LFS`

This section proves the tractable part of the large-field gate. The result is
not "large fields are impossible." It is the sharper statement needed by the
record-law expansion:

```text
heat-kernel block tail
+ large-field coefficient dominance
+ connected-polymer entropy bound
=> HK-LFS.
```

### Definition 9F.1: Bad Blocks And Large-Field Polymers

Fix a block size `b` in lattice units and a threshold `delta in (0,delta_0)`.
A plaquette `p` is `delta`-bad when

```text
d_G(U_p,1) >= delta,
```

where `d_G` is a fixed bi-invariant Riemannian distance on `SU(N)`. A block
is `delta`-bad when at least one plaquette in its declared interior is
`delta`-bad. A large-field polymer is a connected set of `delta`-bad blocks
after the collar assignment used by the block decomposition.

The collar assignment is part of the record map. It prevents a bad plaquette
on a boundary from being counted independently by two neighboring blocks.

### Lemma 9F.2: Heat-Kernel Plaquette Tail

For `SU(N)` and fixed `delta_0>0`, there are constants

```text
C_H, c_H, t_H > 0
```

such that for every `0<t<=t_H` and every `delta in (0,delta_0)`,

```text
int_{d_G(U,1)>=delta} K_t(U) dHaar(U)
 <=
 C_H exp(-c_H delta^2/t).
```

Proof.

The heat kernel on a compact Lie group obeys a short-time Gaussian upper
bound in geodesic distance:

```text
K_t(U) <= C t^{-d_Gp/2} exp(-d_G(U,1)^2/(C' t))
```

for `0<t<=t_H`, where `d_Gp=dim SU(N)`. Integrating over the complement of
the ball `d_G(U,1)<delta` and absorbing the polynomial prefactor into the
Gaussian by decreasing the exponent for small `t` gives the stated tail
bound. The constants depend on `N`, the chosen metric, and `delta_0`, not on
the lattice volume. `square`

### Definition 9F.3: Block Finite-Energy Tail `HK-BFE`

`HK-BFE(C_B,c_B,delta,b,t_B)` holds when, for every sufficiently fine
heat-kernel node with `t_i<=t_B`, every block `B`, and every allowed collar
conditioning in the declared block decomposition, the conditional probability
that `B` is `delta`-bad obeys

```text
P_i(B is delta-bad | collar records) <= C_B exp(-c_B delta^2/t_i).
```

This is a finite-dimensional local estimate for the heat-kernel action. It
is not a claim that the continuum field is pointwise small.

### Lemma 9F.4: Plaquette Tails Reduce `HK-BFE` To A Local Denominator Bound

Suppose the block conditional density has:

1. a numerator bound obtained by applying Lemma 9F.2 to at least one
   interior bad plaquette;
2. a collar-uniform small-field denominator lower bound

```text
Z_B(collar) >= C_D^{-1} exp(-a_D/t_i);
```

3. at most `P_b` interior plaquettes that can trigger the bad-block event.

Then `HK-BFE` holds with

```text
C_B = C_D P_b C_H,
c_B = c_H - a_D/delta^2,
```

provided `c_B>0`.

Proof.

The bad-block numerator is bounded by the union bound over the `P_b`
interior plaquettes and the heat-kernel tail from Lemma 9F.2. The local
denominator lower bound converts this numerator estimate into a conditional
probability estimate. Combining constants gives `C_B`; combining exponents
gives `c_B`. Positivity of `c_B` is the local finite-energy margin. `square`

### Definition 9F.5: Large-Field Coefficient Dominance `HK-LF-DOM`

`HK-LF-DOM(M_L)` holds when the large-field residual coefficient of a
connected polymer `Y` is dominated by the activity of its bad-block event:

```text
||K_i^{lf}(Y)||_ren
 <=
 M_L^{|Y|} P_i(Y is a connected delta-bad polymer).
```

The constant `M_L` includes the finite-battery record norm, collar
partition, and local Jacobian factors. It must be computed from the same
whole-process law `Gamma_i`.

### Theorem 9F.6: `HK-BFE` And Dominance Prove `HK-LFS`

Assume:

1. `HK-BFE(C_B,c_B,delta,b,t_B)`;
2. `HK-LF-DOM(M_L)`;
3. connected block polymers of size `n` containing a fixed block are bounded
   by `C_ent exp(h_poly n)`;
4. for sufficiently fine nodes, `t_i<=t_L<t_B`;
5. the large-field margin is positive:

```text
sigma_lf = c_B delta^2/t_L - log(C_B M_L) > h_poly.
```

Then `HK-LFS(C_lf,C_ent,sigma_lf,h_lf,r_*)` holds with

```text
C_lf = 1,
C_ent = C_ent,
h_lf = h_poly,
sigma_lf = c_B delta^2/t_L - log(C_B M_L).
```

Proof.

By `HK-BFE`, every bad block carries conditional activity at most

```text
C_B exp(-c_B delta^2/t_i).
```

Using the collar assignment, a connected large-field polymer of size `|Y|`
has one assigned bad-block event per block. Iterating the finite-energy
estimate over an ordering of the blocks gives

```text
P_i(Y is a connected delta-bad polymer)
 <=
 (C_B exp(-c_B delta^2/t_i))^{|Y|}.
```

`HK-LF-DOM` then gives

```text
||K_i^{lf}(Y)||_ren
 <=
 (C_B M_L exp(-c_B delta^2/t_i))^{|Y|}.
```

Since `t_i<=t_L`, this is bounded by

```text
exp(-sigma_lf |Y|).
```

The connected-polymer counting assumption supplies the entropy factor
`C_ent exp(h_poly n)`. The positivity condition `sigma_lf>h_poly` is exactly
the `HK-LFS` margin. `square`

### Corollary 9F.7: Large-Field Gate Status

For the heat-kernel trajectory, the large-field gate is reduced to two local
finite-dimensional estimates and one entropy margin:

```text
HK-BFE + HK-LF-DOM + sigma_lf>h_poly
=> HK-LFS.
```

The expected behavior is favorable because `t_i -> 0` along the
asymptotically-free trajectory, so the term `c_B delta^2/t_i` grows on fine
nodes. The remaining proof burden is to establish the collar-uniform block
denominator lower bound and the coefficient dominance constant `M_L` for the
actual block decomposition.

## 9G. Further Reduction Of `HK-BFE`

This section pushes `HK-BFE` below Lemma 9F.4. The finite-energy estimate is
reduced to:

```text
compact heat-kernel lower bound
+ finite block geometry
+ positive finite-energy margin
=> HK-BFE.
```

The proof is finite-dimensional and regulator-level. It does not construct
the continuum theory, but it makes the large-field denominator issue explicit.

### Lemma 9G.1: Compact Heat-Kernel Lower Bound

For `SU(N)` with the chosen bi-invariant metric, there are constants

```text
C_-, a_-, t_- > 0
```

such that for every `0<t<=t_-` and every `U in SU(N)`,

```text
K_t(U) >= C_- exp(-a_-/t).
```

Proof.

The heat kernel on a compact Riemannian manifold satisfies two-sided
short-time Gaussian bounds. Since `SU(N)` is compact, its diameter is finite.
The lower Gaussian bound has the form

```text
K_t(U) >= c t^{-d_Gp/2} exp(-d_G(U,1)^2/(c' t)).
```

Using `d_G(U,1)<=diam(SU(N))` gives a uniform exponential lower bound.
The polynomial prefactor is positive and can be absorbed into the constant
and, for small `t`, into a slightly larger exponent. This gives the stated
constants. `square`

### Definition 9G.2: Block Denominator Lower Bound `HK-BDLB`

Let `B` be a block with `E_B` interior links and `P_B` plaquette factors in
the local conditional density after the collar records are fixed. Write the
local denominator as

```text
Z_B(collar)
 =
 int_{G^{E_B}} product_{p in P_B} K_{t_i}(U_p(U_int,collar)) dHaar(U_int).
```

`HK-BDLB(C_D,a_D,b,t_D)` holds when, uniformly in all allowed collar records,

```text
Z_B(collar) >= C_D^{-1} exp(-a_D/t_i)
```

for every sufficiently fine node with `t_i<=t_D`.

### Lemma 9G.3: Compact Lower Bound Proves `HK-BDLB`

Assume the block has at most `P_b^{loc}` plaquette factors in its local
conditional density. Then Lemma 9G.1 implies `HK-BDLB` with

```text
C_D = C_-^{-P_b^{loc}},
a_D = P_b^{loc} a_-,
t_D = t_-.
```

Proof.

For every interior-link configuration and every collar record, Lemma 9G.1
gives

```text
product_{p in P_B} K_{t_i}(U_p)
 >=
 C_-^{P_B} exp(-P_B a_-/t_i).
```

Since `P_B<=P_b^{loc}` and Haar measure on `G^{E_B}` is normalized, the
integral over interior links obeys

```text
Z_B(collar)
 >=
 C_-^{P_b^{loc}} exp(-P_b^{loc} a_-/t_i).
```

This is exactly `HK-BDLB` with the displayed constants. `square`

### Theorem 9G.4: `HK-BDLB` Closes `HK-BFE` Under A Positive Margin

Assume:

1. the heat-kernel plaquette tail of Lemma 9F.2 with constants `C_H,c_H,t_H`;
2. `HK-BDLB(C_D,a_D,b,t_D)`;
3. at most `P_b` interior plaquettes can trigger the bad-block event;
4. the finite-energy margin is positive:

```text
m_B(delta) = c_H delta^2 - a_D > 0.
```

Then `HK-BFE(C_B,c_B,delta,b,t_B)` holds with

```text
C_B = C_D P_b C_H,
c_B = m_B(delta)/delta^2,
t_B = min(t_H,t_D).
```

Proof.

The numerator of the conditional bad-block probability is bounded by the
union bound over the `P_b` triggering plaquettes and Lemma 9F.2:

```text
bad numerator <= P_b C_H exp(-c_H delta^2/t_i).
```

The denominator is bounded below by `HK-BDLB`:

```text
Z_B(collar) >= C_D^{-1} exp(-a_D/t_i).
```

Dividing numerator by denominator gives

```text
P_i(B is delta-bad | collar records)
 <=
 C_D P_b C_H exp(-(c_H delta^2-a_D)/t_i).
```

Using `c_B=(c_H delta^2-a_D)/delta^2` gives the `HK-BFE` form. `square`

### Corollary 9G.5: Generic `HK-BFE` Reduction

For the heat-kernel block decomposition,

```text
compact heat-kernel lower bound
+ finite block geometry
+ m_B(delta)>0
=> HK-BFE.
```

The generic compact-denominator proof is rigorous but may be numerically
crude: if `a_D` is too large compared with `c_H delta^2`, the margin
`m_B(delta)` is nonpositive and this route does not close `HK-BFE`. In that
case the next task is to prove a sharper collar-adapted denominator lower
bound, not to change the ontology or introduce hidden subprocesses.

## 9H. Generic-Margin Test And Collar-Adapted Denominators

This section performs the promised test of the generic denominator route and
gives the sharper replacement when the generic margin is too crude.

### Definition 9H.1: Generic `HK-BFE` Margin Test

For the compact-denominator route of Section 9G, define

```text
delta_crit^2 = P_b^{loc} a_- / c_H.
```

The generic `HK-BFE` margin test passes at threshold `delta` when

```text
delta^2 > delta_crit^2.
```

It fails on the declared large-field threshold range `(0,delta_0)` when

```text
delta_0^2 <= delta_crit^2.
```

### Proposition 9H.2: What The Generic Test Actually Shows

The compact global lower-bound route proves `HK-BFE` only in the region

```text
delta^2 > P_b^{loc} a_- / c_H.
```

If `delta_0^2 <= P_b^{loc} a_- / c_H`, then this route cannot certify
`HK-BFE` for any allowed `delta in (0,delta_0)`.

Proof.

By Lemma 9G.3, the generic denominator exponent is

```text
a_D = P_b^{loc} a_-.
```

Theorem 9G.4 requires

```text
m_B(delta)=c_H delta^2-a_D>0.
```

Substituting `a_D=P_b^{loc}a_-` gives exactly
`delta^2>P_b^{loc}a_-/c_H`. If the whole allowed threshold interval lies
below this critical value, the compact global lower-bound route has no
positive margin. `square`

### Interpretation

This is not a failure of `HK-BFE`; it is a failure of a crude proof. The
compact lower bound uses the worst possible group element on every plaquette
in the block denominator. It ignores the collar information and the fact that
the denominator only needs one reasonably probable local interior
configuration. For large blocks, `P_b^{loc}a_-` can easily dominate
`c_H delta^2`, so the generic proof should be expected to be only a fallback.

### Definition 9H.3: Collar Energy And Good-Collar Condition

For a block `B` and fixed collar record, define the local plaquette-energy
functional

```text
E_B(U_int; collar)
 =
 sum_{p in P_B} d_G(U_p(U_int,collar),1)^2
```

and the collar ground energy

```text
E_B^*(collar) = inf_{U_int in G^{E_B}} E_B(U_int; collar).
```

For constants `e_col>0` and `delta>0`, the collar is
`(e_col,delta)`-good when

```text
E_B^*(collar) <= e_col delta^2.
```

Collars that are not `(e_col,delta)`-good are assigned to the neighboring
large-field polymer by the collar assignment. Thus the conditional
finite-energy estimate below is only required on good collars; bad collars
are not ignored, they are charged to the large-field event.

### Definition 9H.4: Collar-Adapted Denominator Bound `HK-CAD`

`HK-CAD(C_ad,a_ad,e_col,delta,b,t_ad)` holds when every
`(e_col,delta)`-good collar satisfies

```text
Z_B(collar) >= C_ad^{-1} exp(-a_ad delta^2/t_i)
```

for every sufficiently fine heat-kernel node with `t_i<=t_ad`.

### Lemma 9H.5: Local-Minimizer Neighborhood Proves `HK-CAD`

Assume that for every `(e_col,delta)`-good collar:

1. there is an interior configuration `U_*` with
   `E_B(U_*;collar)<=e_col delta^2`;
2. the map from interior link variables to local plaquettes is Lipschitz on a
   neighborhood `N_alpha(U_*)` of radius `alpha delta`, with energy increase

```text
E_B(U_int;collar)
 <=
 (e_col + L_B alpha^2) delta^2
```

   on that neighborhood;
3. the Haar volume of the neighborhood obeys

```text
Vol(N_alpha(U_*)) >= v_B (alpha delta)^{D_B};
```

4. the heat kernel has the local lower bound

```text
K_t(U) >= C_loc t^{-d_Gp/2} exp(-q_loc d_G(U,1)^2/t)
```

   on the relevant small-distance range.

Then `HK-CAD` holds with any

```text
a_ad > q_loc (e_col + L_B alpha^2)
```

and a finite constant `C_ad` depending on the block geometry, `alpha`,
`delta_0`, and `N`, but not on volume, the cutoff node, or the good collar.

Proof.

Restrict the block denominator integral to `N_alpha(U_*)`. On this
neighborhood the local plaquette energy is bounded by
`(e_col+L_B alpha^2)delta^2`. The product of local heat-kernel lower bounds
therefore gives an integrand bounded below by an exponential of
`-q_loc(e_col+L_B alpha^2)delta^2/t_i`, times a polynomial power of `t_i`.
The neighborhood volume supplies `v_B(alpha delta)^{D_B}`. Since the block is
finite, all polynomial factors can be absorbed into the constant and into an
arbitrarily small increase of the exponent for sufficiently small `t_i`.
Choosing `a_ad` strictly larger than `q_loc(e_col+L_B alpha^2)` yields the
displayed denominator bound. `square`

### Theorem 9H.5A: Explicit `HK-CAD` Pass Criterion

Fix `delta in (0,delta_0)`. Suppose the good-collar minimizer construction
of Lemma 9H.5 is available with constants `e_col,L_B,q_loc`, and suppose
there is an `alpha>0` such that

```text
q_loc(e_col+L_B alpha^2)<c_H.
```

Choose any

```text
a_ad
```

with

```text
q_loc(e_col+L_B alpha^2)<a_ad<c_H.
```

Then `HK-CAD(C_ad,a_ad,e_col,delta,b,t_ad)` holds for some finite `C_ad`
and `t_ad>0`, and the collar-adapted finite-energy margin

```text
c_H-a_ad>0
```

is positive.

Equivalently, this CAD route is available whenever the collar-compatible
local minimizer can be chosen with

```text
e_col<c_H/q_loc
```

and then `alpha` is taken small enough that the displayed strict inequality
holds.

Proof.

Lemma 9H.5 gives `HK-CAD` for any
`a_ad>q_loc(e_col+L_B alpha^2)`. The present hypothesis leaves a nonempty
open interval between this lower bound and `c_H`; choosing `a_ad` in that
interval gives both the denominator estimate and `c_H-a_ad>0`. The final
statement follows by continuity in `alpha`. `square`

### Theorem 9H.5B: `HK-CAD` Falsifier For The Local-Minimizer Route

The local-minimizer proof of `HK-CAD` cannot produce a positive
collar-adapted margin if every admissible good-collar/minimizer neighborhood
satisfies

```text
q_loc(e_col+L_B alpha^2)>=c_H.
```

In that case Lemma 9H.5 may still give a denominator lower bound, but not
one strong enough for the margin `c_H>a_ad` required by Theorem 9H.6.

Proof.

Lemma 9H.5 requires `a_ad>q_loc(e_col+L_B alpha^2)`. If the displayed
inequality holds for every admissible neighborhood, then every admissible
`a_ad` satisfies `a_ad>=c_H` after taking the strict lower bound into
account. Thus `c_H-a_ad>0` cannot be certified by this local-minimizer
route. This does not disprove `HK-CAD`; it only says this particular
denominator proof is too weak. `square`

### Theorem 9H.6: Collar-Adapted Denominator Closes `HK-BFE` Under A Sharper Margin

Assume:

1. the heat-kernel plaquette tail of Lemma 9F.2;
2. `HK-CAD(C_ad,a_ad,e_col,delta,b,t_ad)`;
3. at most `P_b` interior plaquettes can trigger a good-collar bad-block
   event;
4. bad collars are assigned to the adjacent large-field polymer by the
   declared collar map;
5. the collar-adapted finite-energy margin is positive:

```text
m_B^sharp(delta) = (c_H-a_ad) delta^2 > 0.
```

Then the conditional block finite-energy estimate `HK-BFE` holds on the
collar-refined large-field decomposition with

```text
C_B^sharp = C_ad P_b C_H,
c_B^sharp = c_H-a_ad,
t_B^sharp = min(t_H,t_ad).
```

Proof.

For good collars, repeat the numerator estimate from Lemma 9F.4 and divide
by the sharper denominator `HK-CAD`:

```text
P_i(B is delta-bad | good collar)
 <=
 C_ad P_b C_H exp(-(c_H-a_ad)delta^2/t_i).
```

This is `HK-BFE` with the displayed constants. Bad collars are already
declared large-field events, so they are counted in the polymer activity
rather than used as conditioning under which the block must be proved small.
The estimate remains a statement about one pushed-forward record law because
the collar refinement is part of the declared record map. `square`

### Corollary 9H.7: Status Of `HK-BFE` After The Test

The generic compact route closes `HK-BFE` only if

```text
delta^2 > P_b^{loc} a_- / c_H.
```

If that fails, the sharper route is:

```text
HK-CAD + m_B^sharp(delta)>0
=> HK-BFE,

m_B^sharp(delta)=(c_H-a_ad)delta^2.
```

This is the preferred route for actual blocks, because `a_ad` measures the
best collar-compatible local configuration rather than the worst group
configuration on every plaquette.

## 9I. Large-Field Coefficient Dominance

This section proves the bookkeeping part of `HK-LF-DOM`. The point is simple
but important: a large-field residual coefficient is allowed to be large only
on the record event that declares a large-field polymer. If its local
extractor is uniformly bounded per block, then the coefficient is dominated
by the probability of that event.

### Definition 9I.1: Large-Field Event

For a connected block polymer `Y`, let

```text
A_Y^{lf}
```

be the event that `Y` is a connected `delta`-bad polymer in the
collar-refined decomposition, including bad collars assigned to `Y`.

The event `A_Y^{lf}` is a record event: it is measurable with respect to the
declared block/collar record map and therefore belongs to the same
whole-process law `Gamma_i`.

### Definition 9I.2: Local Large-Field Coefficient Representation `HK-LF-REP`

`HK-LF-REP(C_lab,C_coef,C_rec,C_ext)` holds if, for every connected polymer
`Y`, the renormalized large-field residual coefficient admits a finite
representation

```text
K_i^{lf}(Y)
 =
 sum_{alpha in I(Y)}
 c_{Y,alpha}
 E_i[ 1_{A_Y^{lf}} F_{Y,alpha} ],
```

where:

1. the label set obeys `|I(Y)| <= C_lab^{|Y|}`;
2. the scalar coefficient obeys `|c_{Y,alpha}| <= C_coef^{|Y|}`;
3. the finite-battery record insertion obeys
   `||F_{Y,alpha}||_infty <= C_rec^{|Y|}`;
4. the renormalized coefficient norm/extractor obeys
   `||L_{Y,alpha}|| <= C_ext^{|Y|}` if an explicit linear extractor
   `L_{Y,alpha}` is used; equivalently `C_ext=1` when the displayed
   expression already includes the extracted coefficient;
5. every term is supported on `A_Y^{lf}`.

Conditional collar expectations are allowed inside `E_i`; after integrating
over collars they must have the displayed unconditional form by the tower
property.

### Lemma 9I.3: Bounded Supported Insertions Are Probability Dominated

If `F` is a bounded record insertion and `A` is a record event, then

```text
|E_i[1_A F]| <= ||F||_infty P_i(A).
```

Proof.

Since `|1_A F| <= ||F||_infty 1_A`, positivity of the pushed-forward record
law gives the estimate. `square`

### Theorem 9I.4: `HK-LF-REP` Proves `HK-LF-DOM`

Assume `HK-LF-REP(C_lab,C_coef,C_rec,C_ext)`. Then `HK-LF-DOM(M_L)` holds
with

```text
M_L = C_lab C_coef C_rec C_ext.
```

Proof.

Using the representation in Definition 9I.2 and Lemma 9I.3,

```text
||K_i^{lf}(Y)||_ren
 <=
 sum_{alpha in I(Y)}
 C_ext^{|Y|} |c_{Y,alpha}|
 ||F_{Y,alpha}||_infty
 P_i(A_Y^{lf}).
```

The bounds on label count, coefficients, record insertions, and extractor
norm give

```text
||K_i^{lf}(Y)||_ren
 <=
 (C_lab C_coef C_rec C_ext)^{|Y|}
 P_i(A_Y^{lf}).
```

This is exactly `HK-LF-DOM(M_L)`. `square`

### Lemma 9I.5: Why `HK-LF-REP` Is A Finite-Battery Bookkeeping Gate

`HK-LF-REP` follows from the declared block/collar expansion if:

1. the large-field partition of unity uses factors bounded by `1` and
   supported on bad-block or bad-collar events;
2. each block contributes at most `C_lab` local labels;
3. local Jacobian, collar, and chart factors are bounded by `C_coef` per
   block;
4. all finite-battery records have sup norm bounded by `C_rec` per block;
5. the renormalized coefficient extractor is local and has operator norm
   bounded by `C_ext` per block.

Proof.

Expanding the local block/collar partition produces a finite sum over labels
with cardinality multiplicative in the number of blocks. The large-field
partition factors give support on `A_Y^{lf}`. The finite-battery record
norms, local Jacobians, chart factors, and local coefficient extractors are
bounded block-by-block by the displayed constants. Multiplying these bounds
over `|Y|` blocks gives Definition 9I.2. `square`

### Definition 9I.5A: Finite Source Ledger For `HK-LF-REP`

`HK-LF-REP-SRC(N_lab,J_blk,R_blk,E_blk)` holds when the declared
block/collar expansion has the following finite per-block bounds on the same
pushed-forward record law:

1. each block/collar cell contributes at most `N_lab` local labels;
2. the absolute product of local scalar chart, Jacobian, denominator, and
   partition coefficients is at most `J_blk` per block;
3. every finite-battery record insertion used by the large-field extractor
   has sup norm at most `R_blk` per block;
4. the renormalized coefficient extractor has operator norm at most `E_blk`
   per block;
5. every summand is multiplied by the large-field record event
   `1_{A_Y^{lf}}`.

The constants are finite because the battery, block template, collar
template, and local chart atlas are finite. The condition is explicitly a
record-law statement: the event `A_Y^{lf}` and the insertion
`F_{Y,alpha}` are functions of the same pushed-forward finite records.

### Theorem 9I.5B: Finite Source Ledger Proves `HK-LF-REP`

If `HK-LF-REP-SRC(N_lab,J_blk,R_blk,E_blk)` holds, then
`HK-LF-REP(C_lab,C_coef,C_rec,C_ext)` holds with

```text
C_lab=N_lab,
C_coef=J_blk,
C_rec=R_blk,
C_ext=E_blk.
```

Consequently

```text
HK-LF-DOM(M_L)
```

holds with

```text
M_L=N_lab J_blk R_blk E_blk.
```

Proof.

For a connected polymer `Y`, expanding the finite block/collar source ledger
gives at most `N_lab^{|Y|}` labels. The scalar coefficient, record
insertion, and extractor norms are bounded by
`J_blk^{|Y|}`, `R_blk^{|Y|}`, and `E_blk^{|Y|}`. The support condition gives
the required factor `1_{A_Y^{lf}}` in every summand. These are exactly the
five clauses of Definition 9I.2. The final dominance constant is Theorem
9I.4. `square`

### Theorem 9I.5C: `HK-LF-REP` Falsifier

The finite-source route to `HK-LF-REP` fails on a chosen battery if any one
of the following occurs on a cofinal tower:

```text
1. the label count per block is not uniformly finite;
2. a local chart/Jacobian/denominator coefficient has no finite per-block
   bound;
3. a finite-battery record insertion has unbounded sup norm;
4. the coefficient extractor norm grows faster than exponentially in |Y|;
5. a large-field summand is not supported on the declared event A_Y^{lf};
6. the event, insertion, or coefficient is computed on a different
   pushed-forward record law.
```

Items 1--5 are mathematical failures of this finite-battery representation.
Item 6 is a whole-process compatibility failure: it mixes proof-coordinate
or auxiliary estimates with operational record coefficients.

Proof.

Each item negates one clause of Definition 9I.5A or the multiplicative
finite-block argument in Theorem 9I.5B. Without those finite per-block
bounds, no uniform exponential constant `M_L^{|Y|}` is produced by this
route. `square`

### Corollary 9I.6: Large-Field Dominance Status

For the heat-kernel trajectory,

```text
HK-LF-REP
=> HK-LF-DOM.
```

Thus the remaining work for this subgate is not analytic decay. It is to
verify that the chosen block/collar residual-coefficient extractor has the
finite-battery representation and per-block bounds in Definition 9I.2. This
is expected to be tractable once the record map and collar partition are
fixed explicitly.

## 9J. Assembled Large-Field Branch

The previous sections can now be imported as one large-field theorem.

### Definition 9J.1: Large-Field Closure Certificate `HK-LF-CLOSE`

`HK-LF-CLOSE` holds for a heat-kernel trajectory when the following data are
available on the same collar-refined whole-process record law:

1. heat-kernel plaquette tail constants `C_H,c_H,t_H`;
2. a collar-adapted denominator certificate `HK-CAD(C_ad,a_ad,e_col,delta,b,t_ad)`;
3. at most `P_b` interior plaquettes can trigger a good-collar bad-block
   event;
4. bad collars are assigned to adjacent large-field polymers;
5. coefficient representation `HK-LF-REP(C_lab,C_coef,C_rec,C_ext)`;
6. connected-polymer entropy bound `C_ent exp(h_poly n)`;
7. a cutoff threshold `t_L<min(t_H,t_ad)`;
8. the two positive margins:

```text
c_H > a_ad,

sigma_lf^sharp
 =
 (c_H-a_ad) delta^2/t_L
 - log(C_ad P_b C_H C_lab C_coef C_rec C_ext)
 > h_poly.
```

### Definition 9J.1A: Ordered Large-Field Source Certificate `HK-LF-SRC`

`HK-LF-SRC(delta,t_L)` holds when the following source data are verified on
the same collar-refined whole-process record law:

1. the heat-kernel plaquette tail of Lemma 9F.2 supplies
   `C_H,c_H,t_H`;
2. the collar-adapted denominator source passes as in Theorem 9H.5A, so
   `HK-CAD(C_ad,a_ad,e_col,delta,b,t_ad)` holds and

   ```text
   c_H-a_ad>0;
   ```

3. at most `P_b` interior plaquettes can trigger a good-collar bad-block
   event, and bad collars are assigned to adjacent large-field polymers by
   the declared collar map;
4. the finite coefficient-representation source passes:

   ```text
   HK-LF-REP-SRC(N_lab,J_blk,R_blk,E_blk);
   ```

5. the block-polymer entropy is bounded by `C_ent exp(h_poly n)`;
6. the time cutoff satisfies

   ```text
   0<t_L<min(t_H,t_ad);
   ```

7. the scalar large-field margin passes:

   ```text
   sigma_lf^sharp
    =
    (c_H-a_ad)delta^2/t_L
    - log(C_ad P_b C_H N_lab J_blk R_blk E_blk)
    > h_poly.
   ```

All constants are constants of the pushed-forward record law. Gauge fixing,
collar conditioning, minimizer neighborhoods, and local coefficient
extractors are proof coordinates only.

### Theorem 9J.1B: `HK-LF-SRC` Proves `HK-LF-CLOSE`

If `HK-LF-SRC(delta,t_L)` holds, then `HK-LF-CLOSE` holds with

```text
C_lab=N_lab,
C_coef=J_blk,
C_rec=R_blk,
C_ext=E_blk,
```

and with `sigma_lf^sharp` as in Definition 9J.1A.

Proof.

Item 2 of `HK-LF-SRC` supplies the `HK-CAD` input and the positive
finite-energy margin `c_H>a_ad`. Items 3 and 5 are the collar assignment,
trigger count, and polymer entropy inputs of Definition 9J.1. Item 4 and
Theorem 9I.5B give `HK-LF-REP` with the displayed constants. Item 6 gives
the allowed time cutoff, and item 7 is exactly the final
`sigma_lf^sharp>h_poly` margin of Definition 9J.1. Thus all clauses of
`HK-LF-CLOSE` hold. `square`

### Theorem 9J.1C: The Entropy Margin Can Always Be Forced After `HK-CAD`

Assume the first five clauses of `HK-LF-SRC(delta,t_L)` hold and
`c_H>a_ad`. Define

```text
K_L:=C_ad P_b C_H N_lab J_blk R_blk E_blk.
```

For any desired margin `xi_lf>0`, choose `t_L` so that

```text
0<t_L<min(t_H,t_ad)
```

and

```text
(c_H-a_ad)delta^2/t_L
>=
h_poly+\log K_L+\xi_lf.
```

Then `HK-LF-SRC(delta,t_L)` holds and

```text
sigma_lf^sharp>=h_poly+\xi_lf>h_poly.
```

Equivalently, when `h_poly+log K_L+xi_lf>0`, it is enough to take

```text
t_L
<
{(c_H-a_ad)delta^2\over h_poly+\log K_L+\xi_lf}.
```

If `h_poly+log K_L+xi_lf<=0`, any sufficiently small positive
`t_L<min(t_H,t_ad)` already satisfies the margin.

Proof.

The expression for `sigma_lf^sharp` is

```text
(c_H-a_ad)delta^2/t_L-\log K_L.
```

The displayed choice of `t_L` makes this at least `h_poly+xi_lf`. Since
`c_H-a_ad>0`, such a positive `t_L` always exists below
`min(t_H,t_ad)`. The rest of `HK-LF-SRC` is unchanged. `square`

### Corollary 9J.1D: Ordered Large-Field Execution Route

The large-field part of `HK-AN-SRC` is closed by the following ordered
finite-source route:

```text
1. prove a good-collar minimizer neighborhood with
   q_loc(e_col+L_B alpha^2)<c_H;
2. choose a_ad with q_loc(e_col+L_B alpha^2)<a_ad<c_H;
3. verify HK-LF-REP-SRC(N_lab,J_blk,R_blk,E_blk);
4. choose t_L small enough that sigma_lf^sharp>h_poly.
```

Then

```text
HK-LF-SRC => HK-LF-CLOSE => HK-LFS.
```

The first two steps attack `HK-CAD`; the third attacks `HK-LF-REP`; the
fourth is the scalar entropy-margin choice.

### Theorem 9J.1E: Exact Falsifiers For The Large-Field Route

The ordered large-field route fails on a chosen tower if any one of the
following occurs:

```text
1. no good-collar minimizer neighborhood satisfies
   q_loc(e_col+L_B alpha^2)<c_H;
2. HK-LF-REP-SRC fails by one of the clauses in Theorem 9I.5C;
3. the polymer entropy bound C_ent exp(h_poly n) is unavailable;
4. the time cutoff cannot be taken below min(t_H,t_ad);
5. after the best available CAD and LF-REP constants, the inequality
   sigma_lf^sharp>h_poly is not achieved.
```

Items 1--2 are source failures for `HK-CAD` and `HK-LF-REP`. Items 3--5 are
entropy or scalar-margin failures. As usual, this is a falsifier for this
large-field proof route, not a claim that continuum Yang-Mills is false.

Proof.

The five items negate the five ingredients of Corollary 9J.1D. If item 1
holds, Theorem 9H.5B says the local-minimizer CAD proof has no positive
finite-energy margin. If item 2 holds, Theorem 9I.5B cannot produce
`HK-LF-REP`. If item 3 holds, the sum over connected polymers is not
controlled. If items 4 or 5 hold, Theorem 9J.1C cannot make
`sigma_lf^sharp` subcritical relative to entropy. `square`

### Theorem 9J.2: `HK-LF-CLOSE` Proves `HK-LFS`

If `HK-LF-CLOSE` holds, then `HK-LFS` holds with

```text
C_lf = 1,
C_ent = C_ent,
h_lf = h_poly,
sigma_lf = sigma_lf^sharp,
r_* = 1
```

after increasing `r_*` if the block graph uses a different
diameter-to-size normalization.

Proof.

By Theorem 9H.6, `HK-CAD` and `c_H>a_ad` imply the collar-refined
block finite-energy estimate `HK-BFE` with

```text
C_B^sharp = C_ad P_b C_H,
c_B^sharp = c_H-a_ad.
```

By Theorem 9I.4, `HK-LF-REP` implies `HK-LF-DOM` with

```text
M_L = C_lab C_coef C_rec C_ext.
```

Substituting these constants into Theorem 9F.6 gives

```text
sigma_lf
 =
 c_B^sharp delta^2/t_L - log(C_B^sharp M_L)
 =
 sigma_lf^sharp.
```

The final margin in Definition 9J.1 is exactly `sigma_lf>h_poly`. Hence
`HK-LFS` holds. `square`

### Corollary 9J.3: Large-Field Branch Status

The entire large-field branch is now reduced to:

```text
HK-LF-SRC => HK-LF-CLOSE => HK-LFS.
```

Unpacked, the remaining large-field work is:

1. prove the collar-adapted denominator source by finding
   `q_loc(e_col+L_B alpha^2)<c_H`;
2. choose `a_ad` in the strict interval
   `q_loc(e_col+L_B alpha^2)<a_ad<c_H`;
3. verify the finite-battery coefficient representation source
   `HK-LF-REP-SRC(N_lab,J_blk,R_blk,E_blk)`;
4. choose `t_L` so that

   ```text
   sigma_lf^sharp
    =
    (c_H-a_ad)delta^2/t_L
    - log(C_ad P_b C_H N_lab J_blk R_blk E_blk)
    > h_poly.
   ```

This is a major narrowing: the large-field problem no longer includes
small-field covariance, counterterm stability, continuum projectivity, or a
mass gap. Once `c_H>a_ad` and `HK-LF-REP-SRC` are proved, the entropy margin
is no longer a mystery: Theorem 9J.1C forces it by taking a sufficiently fine
large-field time cutoff `t_L`.

### Definition 9J.4: Standard Global Large-Field Template `HK-LF-TPL`

`HK-LF-TPL` holds when the heat-kernel tower uses a fixed finite family of
block/collar templates with the following data:

1. each lattice block is a translate, rotation, or boundary member of one of
   finitely many templates `T in T_blk`;
2. each template has a declared collar map assigning every collar failure to
   a unique adjacent large-field polymer record event;
3. each template has a strict axial-tree chart on the interior links and a
   finite collar chart on the boundary links;
4. the finite Wilson/Creutz/character battery used by the residual extractor
   meets only finitely many links per block;
5. the connected block-polymer entropy is bounded by

   ```text
   N_conn(n;x) <= C_ent exp(h_poly n)
   ```

   uniformly in the cutoff node and base block `x`;
6. all record events, partitions, and insertions are pushed-forward finite
   records of the same heat-kernel whole-process law.

Gauge charts and axial trees are proof coordinates. `HK-LF-TPL` exports only
finite constants and record events.

### Lemma 9J.5: Finite Templates Give Uniform Collar Extension

Assume `HK-LF-TPL` for the standard hypercubic block/collar family. For every
chosen `e_col>0`, there are finite constants

```text
Lambda_col,
delta_col,
L_col,
v_col,
D_col
```

such that every template has a collar-compatible minimizer neighborhood with
the following uniform properties. For every `0<delta<delta_col` and every
`(e_col,delta)`-good collar not already assigned to the adjacent large-field
event, the infimum in `E_B^*(collar)` is attained by an interior link
configuration `U_*` for which

```text
E_B(U_*;collar) <= e_col delta^2
```

and, on an axial-tree neighborhood of radius `alpha delta`,

```text
E_B(U_int;collar)
 <=
(e_col+L_col alpha^2)delta^2,
```

with Haar volume at least

```text
v_col (alpha delta)^{D_col}.
```

Proof.

Fix one template. In axial-tree coordinates the map from interior link
increments to the local plaquette logarithms is a smooth finite-dimensional
map. Its differential at the identity is the cellular coboundary map with
the axial-tree gauge fixed. On the subspace satisfying the linearized
boundary Bianchi constraints, the standard cellular homotopy gives a bounded
right inverse: fill plaquettes shell by shell from the tree root and assign
the remaining curvature by the finite Bianchi relations. Since the template
is finite, the right-inverse norm is finite.

The exact nonabelian plaquette map differs from its differential by a BCH
remainder bounded quadratically on a sufficiently small chart ball. The exact
lattice Bianchi identities imply that the linear Bianchi defect of an actual
collar record is also quadratic in the collar size. Since a good collar has
`E_B^*(collar)<=e_col delta^2`, compactness of the finite interior-link
space gives an attaining minimizer. After possibly shrinking `delta_col`
depending on the chosen `e_col`, the bounded linear right inverse and BCH
control keep that minimizer inside the selected axial-tree chart. Smoothness
then gives the quadratic neighborhood bound
`L_col alpha^2 delta^2`, and compactness of a finite-dimensional chart ball
gives the stated Haar-volume lower bound.

There are only finitely many templates. Take the maximum of the right-inverse
and Lipschitz constants, the minimum of the admissible radii and volume
constants, and the maximum of the chart dimensions. This gives the displayed
uniform constants. The construction is performed in proof coordinates, but
the conclusion is a statement about the declared collar record events.
`square`

### Theorem 9J.6: Global Collar-Adapted Denominator Source

Assume `HK-LF-TPL` and the heat-kernel constants of Lemma 9F.2 and Lemma
9H.5 are evaluated with the same bi-invariant metric. Let `q_loc` be the
local heat-kernel exponent. Choose

```text
e_col = c_H/(4q_loc).
```

Using Lemma 9J.5, choose `alpha>0` small enough that

```text
q_loc L_col alpha^2 <= c_H/4.
```

Then

```text
q_loc(e_col+L_col alpha^2) <= c_H/2 < c_H.
```

Consequently one may choose

```text
a_ad = 3c_H/4,
```

and the global collar-adapted denominator certificate

```text
HK-CAD(C_ad,a_ad,e_col,delta,b,t_ad)
```

holds on a cofinal heat-kernel tail for every fixed
`0<delta<min(delta_0,delta_col)`. Moreover the collar-adapted finite-energy
margin is

```text
c_H-a_ad = c_H/4 > 0.
```

Proof.

Lemma 9J.5 supplies the minimizer neighborhood, Lipschitz energy bound, and
volume bound uniformly over the finite template family. With the displayed
choice of `e_col` and `alpha`, the hypothesis of Theorem 9H.5A is satisfied:

```text
q_loc(e_col+L_col alpha^2)<c_H.
```

The value `a_ad=3c_H/4` lies strictly between the left side and `c_H`, so
Theorem 9H.5A gives `HK-CAD` with a finite constant `C_ad` and positive
finite-energy margin `c_H/4`. Bad collars are not discarded; by
`HK-LF-TPL` they are charged to the adjacent large-field polymer event in
the same pushed-forward record law. `square`

### Theorem 9J.7: Global Finite-Battery Large-Field Representation Source

Assume `HK-LF-TPL`. Then the finite source ledger

```text
HK-LF-REP-SRC(N_lab,J_blk,R_blk,E_blk)
```

holds for finite constants obtained by taking maxima over the finite template
family and the finite residual battery.

Proof.

For each template, the block/collar partition has finitely many local cells,
the axial-tree chart has a compact selected domain, and the residual battery
uses finitely many character/Wilson/Creutz insertions. Hence the number of
local labels per block is finite. The chart Jacobians, partition
coefficients, denominator-normalization factors, and local extractor norms
are continuous on compact selected chart domains and therefore have finite
suprema. Character records in a finite battery have finite sup norm after the
declared normalization. Finally, by construction of the large-field
partition every summand carries the indicator of the declared bad-block or
bad-collar record event.

Taking the maximum over finitely many templates gives uniform constants
`N_lab,J_blk,R_blk,E_blk`. The event support, insertion, and extractor all
live on the same pushed-forward record law; no gauge-fixed variable is being
exported as ontology. `square`

### Theorem 9J.8: Global `HK-LF-CLOSE` For The Standard Heat-Kernel Tower

Assume:

1. `HK-LF-TPL` for the standard finite block/collar templates;
2. the heat-kernel plaquette tail constants `C_H,c_H,t_H` and local lower
   constants are evaluated with one bi-invariant metric;
3. the heat-kernel time satisfies `t_i->0` along the AF tail.

Choose `delta`, `e_col`, `alpha`, and `a_ad` as in Theorem 9J.6, and let
`N_lab,J_blk,R_blk,E_blk` be the finite constants of Theorem 9J.7. Define

```text
K_L:=C_ad P_b C_H N_lab J_blk R_blk E_blk.
```

For any desired `xi_lf>0`, choose `t_L` so that

```text
0<t_L<min(t_H,t_ad)
```

and

```text
(c_H-a_ad)delta^2/t_L
>=
h_poly+\log K_L+\xi_lf.
```

Then `HK-LF-SRC(delta,t_L)` holds. Hence

```text
HK-LF-CLOSE
```

holds with

```text
sigma_lf^sharp>=h_poly+\xi_lf>h_poly.
```

Proof.

Theorem 9J.6 supplies the global `HK-CAD` input and the positive margin
`c_H-a_ad=c_H/4`. The trigger count `P_b`, bad-collar assignment, and
polymer entropy are part of `HK-LF-TPL`. Theorem 9J.7 supplies
`HK-LF-REP-SRC`, and therefore the coefficient dominance constants in
Definition 9J.1A. The displayed choice of `t_L` is exactly the entropy-margin
choice of Theorem 9J.1C. Since `t_i->0`, restrict to the cofinal tail on
which `t_i<=t_L`. Therefore every clause of `HK-LF-SRC(delta,t_L)` holds,
and Theorem 9J.1B gives `HK-LF-CLOSE`. `square`

### Corollary 9J.9: Updated Large-Field Status

For the standard finite block/collar heat-kernel tower, the global
large-field analytic input is no longer an open structural gate. It is closed
by the finite-template theorem:

```text
HK-LF-TPL
+ common heat-kernel metric
+ AF tail with t_i<=t_L
=> HK-LF-CLOSE
+ sigma_lf^sharp>h_poly.
```

The remaining possible failures are now explicit:

```text
1. the tower does not admit a finite block/collar template ledger;
2. the heat-kernel metric used for tails and local lower bounds is not the
   same metric;
3. the residual extractor is not a finite pushed-forward battery;
4. the AF heat time cannot be restricted below the required t_L.
```

These are record-law or source-ledger failures, not hidden gauge-ontology
failures.

### Corollary 9J.10: Common-Record Audit For The Analytic Branch

Let `T_HK` be the heat-kernel whole-process tower after the declared
block/collar decomposition and finite-battery pushforward. The analytic
source constants pass the common-record audit when the following are all
computed from the same restrictions of `T_HK`:

```text
HK-SF-SRC constants:
  C_G, mu_G, C_v, p, C_E, C_ent;

HK-LF-CLOSE constants:
  C_H, c_H, C_ad, a_ad, delta, t_L,
  N_lab, J_blk, R_blk, E_blk, sigma_lf^sharp;

HK-CT-CLOSE constants:
  A_tail, mu_tail, A_scheme, mu_scheme, p, r_ct;

KP constants:
  A_res, mu_res, C_KP, h_KP, r_res, m.
```

The audit fails if one of these constants is computed in a different
regulator tower, different collar assignment, different metric normalization,
different finite battery, or different local counterterm/scheme ledger.

Proof.

Definitions 9L.1A, 9J.1A, 9K.1, and 9N.1A each include a same-law clause.
Taking their intersection gives exactly the displayed list. This is the
Barandes-aligned bookkeeping point: gauge charts, axial trees, Gaussian
conditional variables, counterterm coordinates, and scheme coordinates are
proof coordinates. The exported constants are scalar bounds on pushed-forward
finite record laws. `square`

### Definition 9J.11: Frozen Standard Heat-Kernel Row `T_HK^std`

For the analytic branch, `T_HK^std` denotes the following single common
record row:

1. the heat-kernel plaquette tower for fixed `SU(N)` with one bi-invariant
   metric normalization;
2. one declared block/collar template and the collar-assignment convention
   used by `HK-LF-TPL`;
3. one finite pushed-forward battery containing the small-field records,
   large-field residual extractor records, counterterm/scheme records, and
   KP residual records;
4. one matched heat-time/coupling coordinate for the Yang-Mills relevant
   direction;
5. one local counterterm convention: relevant/marginal pure-gauge
   counterterms are absorbed into heat-time, normalization, boundary, or
   finite-volume local records, and are not residual polymers;
6. one local scheme convention: finite scheme coordinates are proof
   coordinates for the same pushed-forward law, with no independent process
   branch.

The row is **clean minimal** when, after items 4--6 are imposed, no nonlocal
counterterm or scheme-change polymer remains. Equivalently, the
counterterm/scheme label sets entering `HK-CT-RATE` are empty:

```text
I_irr=empty,
I_sch=empty.
```

If a nonlocal counterterm or scheme-change polymer remains, the row is not
clean minimal; it must be handled by the finite rate audit of Definition
9K.2E.

### Corollary 9J.12: Common-Row Freeze

On `T_HK^std`, the constants in Corollary 9J.10 are comparable without
additional transport. In particular, a constant may enter `HK-AN-SRC(m)`
only if it is evaluated on this row or is transported to this row by an
explicit finite-record comparison theorem.

Proof.

All six clauses of Definition 9J.11 specify operational record data:
cutoff law, block/collar map, finite battery, local heat-time coordinate,
counterterm convention, and scheme convention. A gauge chart, axial tree,
Gaussian conditional variable, or local scheme coordinate is therefore only
a proof coordinate inside this row. Since `HK-AN-SRC(m)` is a statement
about the pushed-forward finite record law, constants from another row would
refer to another finite probability law and cannot be multiplied or
minimized with the constants of `T_HK^std`. `square`

## 9K. Counterterm Stability `HK-CTS`

Counterterm stability is the next local gate. It says that changing local
renormalization coordinates removes local coefficients but does not create
long residual tails.

### Definition 9K.1: Counterterm Closure Certificate `HK-CT-CLOSE`

`HK-CT-CLOSE(A_tail,mu_tail,A_scheme,mu_scheme,p,r_ct)` holds when the
counterterm ledger has the following form on the same heat-kernel
whole-process record laws:

1. **Strictly local part.** All declared relevant/marginal counterterms are
   supported on polymers with `diam(Y)<r_ct`.
2. **Irrelevant tail.** The nonlocal remainder generated by integrating out
   finite blocks satisfies

```text
sup_x sum_{Y contains x, diam(Y)>=r} ||Delta K_i^{irr}(Y)||_ren
 <=
 A_tail g_i^{2p} exp(-mu_tail r).
```

3. **Scheme-change tail.** Finite changes between allowed local
   renormalization schemes satisfy

```text
sup_x sum_{Y contains x, diam(Y)>=r} ||Delta K_i^{scheme}(Y)||_ren
 <=
 A_scheme g_i^{2p} exp(-mu_scheme r).
```

for all `r>=r_ct`.

The local part is not a residual error; it is absorbed into the declared
renormalized local action and record normalization.

### Theorem 9K.2: `HK-CT-CLOSE` Proves `HK-CTS`

If `HK-CT-CLOSE(A_tail,mu_tail,A_scheme,mu_scheme,p,r_ct)` holds, then
`HK-CTS(A_ct,mu_ct,p,r_*)` holds with

```text
A_ct = A_tail + A_scheme,
mu_ct = min(mu_tail,mu_scheme),
r_* = r_ct.
```

Proof.

For `r>=r_ct`, strictly local counterterms have no support in the residual
tail. The only contributions are the irrelevant tail and the scheme-change
tail. Summing the two displayed estimates in Definition 9K.1 gives

```text
sup_x sum_{Y contains x, diam(Y)>=r} ||Delta K_i^{ct}(Y)||_ren
 <=
 (A_tail + A_scheme) g_i^{2p} exp(-min(mu_tail,mu_scheme) r).
```

This is exactly `HK-CTS`. `square`

### Definition 9K.2A: Counterterm Source Ledger `HK-CT-SRC`

`HK-CT-SRC(A_tail,mu_tail,A_scheme,mu_scheme,p,r_ct)` holds on the
heat-kernel tower when the declared local renormalization and scheme ledger
has the following same-record data.

1. **Pure-gauge relevant/marginal split.** The only relevant or marginal
   gauge-invariant pure-gauge coupling is the Yang-Mills heat-time/coupling
   coordinate. Vacuum, boundary, and finite-volume normalization terms are
   either fixed to zero on the tested finite battery or supported on polymers
   with `diam(Y)<r_ct`.
2. **Irrelevant coupling ledger.** Every nonlocal irrelevant counterterm
   remainder has a connected-polymer expansion

   ```text
   Delta K_i^{irr}(Y)
   =
   g_i^{2p}
   sum_{a in I_irr} h_{a,i} Phi_{a,i}(Y),
   ```

   with a finite label set `I_irr`, finite amplitudes `H_a`, and positive
   diameter rates `mu_a` such that

   ```text
   sup_x sum_{Y contains x, diam(Y)>=r} ||Phi_{a,i}(Y)||_ren
   <=
   H_a exp(-mu_a r).
   ```

3. **Irrelevant coupling bound.** On the chosen AF tail,

   ```text
   |h_{a,i}| <= H_a'
   ```

   for all `a in I_irr`. Paper 11's perturbative trajectory ledger supplies
   this after the local ansatz absorbs the strictly local running couplings;
   if the irrelevant coupling decays, the bound is obtained by increasing
   `H_a'` on the finite initial segment.
4. **Scheme-change ledger.** Every finite change between allowed local
   schemes has a connected-polymer expansion

   ```text
   Delta K_i^{scheme}(Y)
   =
   g_i^{2p}
   sum_{b in I_sch} s_{b,i} Psi_{b,i}(Y),
   ```

   with finite `I_sch`, finite amplitudes `S_b`, positive rates `nu_b`, and

   ```text
   sup_x sum_{Y contains x, diam(Y)>=r} ||Psi_{b,i}(Y)||_ren
   <=
   S_b exp(-nu_b r),
   \qquad
   |s_{b,i}|<=S_b'.
   ```

5. **No hidden process switch.** The counterterm, irrelevant-tail, and
   scheme-tail expansions are all coefficients of the same pushed-forward
   heat-kernel record law used by the small-field and large-field sources.

Define

```text
A_tail := sum_{a in I_irr} H_a H_a',
\qquad
mu_tail := min_{a in I_irr} mu_a,
```

and

```text
A_scheme := sum_{b in I_sch} S_b S_b',
\qquad
mu_scheme := min_{b in I_sch} nu_b.
```

If a label set is empty, its amplitude is `0`; its decay rate may be any
positive number larger than the rates needed by the nonempty part.

### Theorem 9K.2B: Paper-11 Ledger Supplies The Counterterm Source

Assume the ledger-compatible block-conditioned pure-gauge trajectory of
Paper 11, Definition AF.28, on the same heat-kernel record tower, and assume
the finite local ansatz includes all relevant/marginal pure-gauge local
terms. Assume also that the omitted irrelevant and scheme-change local
tails admit the exponential polymer bounds listed in Definition 9K.2A.
Then `HK-CT-SRC(A_tail,mu_tail,A_scheme,mu_scheme,p,r_ct)` holds with

```text
mu_tail>0,
\qquad
mu_scheme>0.
```

Proof.

Paper 11 Definition AF.28 states that no relevant gauge-invariant pure-gauge
coupling is generated other than the Yang-Mills coupling, except for
declared finite-volume or boundary terms. The Yang-Mills coupling is the
heat-time/coupling coordinate already separated in the analytic ledger; the
declared normalization terms are strictly local and therefore have support
below `r_ct` after increasing `r_ct` to cover the finite block/collar
template.

For irrelevant couplings, Paper 11 Definition AF.28 gives contraction
factors `s^{-Delta_j}` with `Delta_j>0` and summable forcing errors. The
iteration in Paper 11 Theorem AF.29 gives a bounded tail on any cofinal AF
subsequence, and in the usual case a decaying tail. Combining those bounded
couplings with the assumed exponential connected-polymer locality of the
omitted irrelevant terms gives clauses 2 and 3 of Definition 9K.2A with
positive `mu_tail`.

Finite scheme changes are changes of local proof coordinates inside the same
renormalized local ansatz. By assumption their nonlocal remainders have the
same exponential polymer locality and bounded finite coefficients, giving
clause 4 with positive `mu_scheme`. Paper 11's ledger-compatible exact
disintegration theorem keeps these coefficients on the same whole-process
pushforward; hence clause 5 holds. `square`

### Theorem 9K.2C: `HK-CT-SRC` Proves `HK-CT-CLOSE`

If `HK-CT-SRC(A_tail,mu_tail,A_scheme,mu_scheme,p,r_ct)` holds, then

```text
HK-CT-CLOSE(A_tail,mu_tail,A_scheme,mu_scheme,p,r_ct)
```

holds. In particular, when the source rates of Definition 9K.2A are
positive, the counterterm closure has

```text
mu_tail>0,
\qquad
mu_scheme>0.
```

Proof.

The relevant/marginal part of `HK-CT-SRC` is strictly local after the
Yang-Mills time/coupling coordinate and declared normalizations are
absorbed; hence it contributes nothing to residual polymers with
`diam(Y)>=r_ct`. For the irrelevant part, use the expansion in Definition
9K.2A and the triangle inequality:

```text
sup_x sum_{Y contains x, diam(Y)>=r} ||Delta K_i^{irr}(Y)||_ren
 <=
g_i^{2p}
sum_{a in I_irr}
|h_{a,i}|
H_a exp(-mu_a r).
```

Using `|h_{a,i}|<=H_a'` and
`mu_tail=min_a mu_a` gives

```text
<= A_tail g_i^{2p} exp(-mu_tail r).
```

The scheme-change estimate is identical with
`A_scheme` and `mu_scheme`. These are precisely the two tail inequalities in
Definition 9K.1, and the strictly local clause has already been checked.
Thus `HK-CT-CLOSE` holds. `square`

### Corollary 9K.2D: Counterterm Source Step Is Closed

Under the Paper-11 ledger-compatible pure-gauge trajectory and the
same-record exponential irrelevant/scheme-tail bounds of Definition 9K.2A,
the counterterm source step of `HK-AN-SRC(m)` is proved:

```text
HK-CT-RATE
=> HK-CT-SRC
=> HK-CT-CLOSE
=> HK-CTS.
```

Without the explicit rate audit, the logical reduction remains:

```text
HK-CT-SRC
=> HK-CT-CLOSE
=> HK-CTS.
```

The only honest falsifiers for this step are:

```text
1. a surviving relevant/marginal transverse pure-gauge counterterm not equal
   to the Yang-Mills time/coupling coordinate;
2. an irrelevant or scheme-change tail with no positive exponential rate;
3. unbounded tail coefficients on every cofinal AF subsequence;
4. a counterterm or scheme ledger computed on a different pushed-forward
   record law.
```

These are source-ledger failures. They are not repaired by reinterpreting
counterterms as hidden degrees of freedom.

### Definition 9K.2E: Same-Record Counterterm Rate Audit `HK-CT-RATE`

`HK-CT-RATE` is the finite audit which turns the abstract source ledger
`HK-CT-SRC` into a concrete same-record constant list. It consists of:

1. the same heat-kernel tower, block/collar template, finite record battery,
   and pushed-forward law used by `HK-SF-SRC` and `HK-LF-CLOSE`;
2. the Paper-11 relevant/marginal pure-gauge split: the Yang-Mills
   heat-time/coupling coordinate is the only pure-gauge relevant/marginal
   direction, apart from declared normalization, boundary, or finite-volume
   terms supported below `r_ct`;
3. finite irrelevant-tail labels `I_irr` with constants
   `H_a,H_a',mu_a` satisfying

   ```text
   mu_a>0,
   |h_{a,i}|<=H_a',
   sup_x sum_{Y contains x, diam(Y)>=r} ||Phi_{a,i}(Y)||_ren
    <= H_a exp(-mu_a r);
   ```

4. finite scheme-tail labels `I_sch` with constants
   `S_b,S_b',nu_b` satisfying

   ```text
   nu_b>0,
   |s_{b,i}|<=S_b',
   sup_x sum_{Y contains x, diam(Y)>=r} ||Psi_{b,i}(Y)||_ren
    <= S_b exp(-nu_b r);
   ```

5. a support declaration separating strictly local proof-coordinate
   changes from residual tails: strictly local counterterms and finite local
   scheme coordinates are absorbed into the local action, heat-time
   coordinate, or record normalization, while only the displayed connected
   polymer tails enter `HK-CT-SRC`.

The audit exports exactly

```text
A_tail = sum_{a in I_irr} H_a H_a',
mu_tail = min_{a in I_irr} mu_a,
A_scheme = sum_{b in I_sch} S_b S_b',
mu_scheme = min_{b in I_sch} nu_b.
```

If `I_irr` or `I_sch` is empty, the corresponding amplitude is `0`, and its
rate is any fixed positive bookkeeping rate larger than the nonempty
minimums used in the residual ledger. In the coefficient-only time-branch
local row of Paper 19, the strictly local counterterm and scheme pieces are
therefore not counterterm tails: they have already been absorbed or shown to
have zero transverse projection on that row.

### Theorem 9K.2F: `HK-CT-RATE` Proves The Counterterm Source Ledger

Assume the Paper-11 ledger-compatible pure-gauge trajectory of Definition
AF.28 on the same heat-kernel record tower. If `HK-CT-RATE` holds, then

```text
HK-CT-SRC(A_tail,mu_tail,A_scheme,mu_scheme,p,r_ct)
```

holds with the exported constants, and any nonempty source tail has positive
decay rate.

Proof.

Clause 2 of `HK-CT-RATE` is exactly the relevant/marginal split required by
Definition 9K.2A. Paper 11 Definition AF.28 and Theorem AF.29 supply the
bounded irrelevant-coupling tail on the AF subsequence; the audit records
the finite constants after the strictly local local-action part has been
removed. Clauses 3 and 4 are precisely the two connected-polymer tail
estimates required by `HK-CT-SRC`, with the amplitudes and rates displayed
above. Clause 5 prevents a process switch: all counterterm and scheme
coordinates are proof coordinates for the same pushed-forward record law.

The triangle inequality then gives the two estimates in Definition 9K.2A,
with `A_tail`, `mu_tail`, `A_scheme`, and `mu_scheme` as exported by the
audit. Empty label sets contribute zero amplitude and no residual tail.
`square`

### Theorem 9K.2G: Clean Minimal Row Passes `HK-CT-RATE`

Assume:

1. the analytic branch is evaluated on the frozen row `T_HK^std`;
2. the Paper-11 ledger-compatible pure-gauge trajectory of Definition AF.28
   holds on that row;
3. the relevant/marginal pure-gauge part is exhausted by the Yang-Mills
   heat-time/coupling coordinate and declared local normalization,
   boundary, or finite-volume records;
4. after this local absorption, the row is clean minimal in the sense of
   Definition 9J.11:

   ```text
   I_irr=empty,
   I_sch=empty.
   ```

Then `HK-CT-RATE` holds with

```text
A_tail=0,
A_scheme=0,
```

and with arbitrary positive bookkeeping rates

```text
mu_tail=mu_ct^0>0,
mu_scheme=mu_sch^0>0.
```

Consequently,

```text
HK-CT-CLOSE(0,mu_ct^0,0,mu_sch^0,p,r_ct)
```

holds on `T_HK^std`.

Proof.

Clauses 1 and 2 of `HK-CT-RATE` are exactly clauses 1--6 of
Definition 9J.11 plus Paper 11's relevant/marginal split: the only
pure-gauge relevant/marginal direction is the Yang-Mills heat-time/coupling
coordinate, while declared local normalization, boundary, and finite-volume
terms are not residual polymers once `r_ct` covers the finite block/collar
template.

Because the row is clean minimal, there are no nonlocal irrelevant
counterterm labels and no nonlocal scheme-change labels. Thus the sums
defining `A_tail` and `A_scheme` are empty, hence both amplitudes are zero.
For every `r>=r_ct`,

```text
sup_x sum_{Y contains x, diam(Y)>=r} ||Delta K_i^{irr}(Y)||_ren = 0
```

and likewise for the scheme-change tail. These zero bounds satisfy the
`HK-CT-RATE` estimates for any positive bookkeeping rates. Theorem 9K.2F and
Theorem 9K.2C then give `HK-CT-CLOSE`. `square`

### Theorem 9K.2H: Exact Obstruction To The Clean Counterterm Pass

On `T_HK^std`, the clean minimal counterterm pass fails exactly when, after
absorbing the Yang-Mills heat-time/coupling direction and declared local
normalizations, at least one of the following survives:

```text
1. a nonlocal irrelevant counterterm tail with no finite positive-rate
   HK-CT-RATE bound;
2. a nonlocal scheme-change tail with no finite positive-rate HK-CT-RATE
   bound;
3. a relevant/marginal transverse pure-gauge direction not equal to the
   Yang-Mills heat-time/coupling coordinate;
4. a counterterm or scheme coefficient computed on a pushed-forward law
   different from T_HK^std.
```

If a nonlocal tail survives but admits the finite constants of
Definition 9K.2E, the branch is no longer clean minimal but still passes
`HK-CT-RATE` by Theorem 9K.2F with nonzero `A_tail` and/or `A_scheme`.

Proof.

The four displayed items are exactly the negations of the four kinds of data
required by Definition 9K.2E after the local split of Definition 9J.11:
same row, relevant/marginal split, finite positive-rate irrelevant tails,
and finite positive-rate scheme tails. If none occurs, either the tail label
sets are empty, so Theorem 9K.2G applies, or the nonempty label sets have
finite positive-rate constants, so Theorem 9K.2F applies. If one occurs,
the corresponding clause of `HK-CT-RATE` is absent. This is a finite
record-law obstruction, not a hidden-variable or gauge-chart issue. `square`

### Corollary 9K.3: Counterterm Status

The counterterm gate is now closed under the explicit local renormalization
ledger:

```text
HK-CT-RATE => HK-CT-SRC => HK-CT-CLOSE => HK-CTS.
```

For the standard Paper-11 ledger-compatible pure-gauge trajectory, the
clean minimal row closes the counterterm source immediately by Theorem
9K.2G. If the actual branch is not clean minimal, the remaining burden is
exactly the finite rate audit of Definition 9K.2E: positive exponential
irrelevant and scheme-tail rates on the same pushed-forward record law,
after strictly local proof-coordinate changes have been absorbed. This is a
locality statement about record coefficients, not an assumption about
fundamental fields.

## 9L. Small-Field Gate `HK-SF-GCD`

The small-field gate is the hardest part of the analytic program. A naive
unsmeared massless gauge covariance does not have exponential decay in four
dimensions. Paper 16 therefore states the exact block-conditioned substitute
needed by the finite-battery record route.

### Definition 9L.1: Block-Conditioned Small-Field Closure `HK-SF-CLOSE`

`HK-SF-CLOSE(C_G,mu_G,C_v,p,theta_sf,C_ent,r_*)` holds when the
small-field coordinate proof supplies:

1. a gauge-fixed, block-conditioned covariance for neutral finite-battery
   record derivatives with connected edge bound

```text
||C_i(B_1,B_2)|| <= C_G exp(-mu_G d(B_1,B_2));
```

2. renormalized local small-field vertices bounded by `C_v g_i^{2p}` per
   connected local insertion;
3. a tree activity bound `theta_sf<1` after summing local labels and block
   entropies;
4. the polymer entropy constant `C_ent` used in Definition 9E.1;
5. all estimates are made on the same finite-battery pushed-forward record
   law after the declared gauge chart is forgotten.

### Definition 9L.1A: Covariance-Vertex Source Ledger `HK-SF-SRC`

`HK-SF-SRC(C_G,mu_G,C_v,p,C_E,r_*)` holds when the same small-field
coordinate proof supplies:

1. the block-conditioned covariance edge bound

   ```text
   ||C_i(B_1,B_2)|| <= C_G exp(-mu_G d(B_1,B_2));
   ```

2. a summable edge-count constant

   ```text
   S_G(mu_G/2)
   :=
   sup_B sum_{B'} exp(-(mu_G/2)d(B,B'))
   <= C_E < infinity;
   ```

3. all nonabsorbed renormalized local small-field vertices on the finite
   battery have total local-label norm at most

   ```text
   C_v g_i^{2p}
   ```

   per connected insertion, after the declared local counterterms and
   time-tangent directions have been removed;
4. the same pushed-forward finite record law, block/collar map, and
   gauge-forgetting map are used for the covariance estimate and the local
   vertex estimate.

The phrase "total local-label norm" means that the finite list of local
Taylor, Jacobian, chart, and record-derivative labels has already been
summed. Thus no hidden infinite species count is left outside `C_v`.

### Theorem 9L.1B: Explicit Tree Activity Bound

Assume `HK-SF-SRC(C_G,mu_G,C_v,p,C_E,r_*)` and let the AF tail be chosen so
that `g_i<=g_*`. Define

```text
theta_sf^{src}
:=
e C_v C_G C_E g_*^{2p}.
```

If

```text
theta_sf^{src}<1,
```

then `HK-SF-CLOSE(C_G,mu_G,C_v,p,theta_sf,C_ent,r_*)` holds with

```text
theta_sf=theta_sf^{src}.
```

In particular, if `p>0` and the constants `C_G,C_v,C_E` are finite, then
there exists an asymptotically-free tail on which `theta_sf<1`.

Proof.

For a connected graph expansion, attach each new local insertion to the
previous tree by one covariance edge. The finite local-label norm contributes
at most `C_v g_i^{2p}` per insertion. The edge attached to that insertion
contributes at most

```text
C_G exp(-mu_G d(B,B')).
```

Half of the exponential decay is reserved for the final polymer-diameter
decay in Definition 9E.1; the other half is summed over possible locations:

```text
sup_B sum_{B'} exp(-(mu_G/2)d(B,B')) <= C_E.
```

The standard tree-graph/KP estimate contributes the harmless factor `e`.
Thus the per-insertion tree activity is bounded by

```text
e C_v C_G C_E g_i^{2p}
<=
e C_v C_G C_E g_*^{2p}
= theta_sf^{src}.
```

If this is below one, the tree expansion is subcritical and gives exactly
the `theta_sf<1` item in Definition 9L.1. The final assertion follows from
`g_i->0` along the asymptotically-free tail and `p>0`. `square`

### Theorem 9L.1C: Paper-11 Block-Conditioned Covariance Import

Assume the Paper-11 fixed-ratio block-conditioned scheme with the uniform
Dirichlet Poincare bound

```text
<A_I,H_{II}^{(b)}A_I> >= lambda_D ||A_I||_{1,b}^2,
lambda_D>0.
```

Then the covariance part of `HK-SF-SRC` holds with, for example,

```text
C_G=lambda_D^{-1},
mu_G=1,
```

after normalizing the covariance edge bound by the explicit factor `g_i^2`
or, equivalently, using `g_i<=1` on the weak-coupling tail.

Moreover, for a bounded-degree block graph with ball-count constants

```text
N_B(n) <= C_B exp(h_B n),
```

one may take

```text
C_E
=
C_B/(1-exp(-(mu_G/2-h_B)))
```

whenever `mu_G/2>h_B`. In the strict finite-range same-block conditional
branch of Paper 11 Theorem AF.18, one may instead use the finite direct-sum
edge count of the block template for `C_E`.

Proof.

Paper 11 Theorem AF.18 gives the conditional covariance

```text
C_{I|B}^{(r)}=g_r^2 H_{I_rI_r}^{-1}
```

and the bound `||H_{II}^{-1}||<=lambda_D^{-1}` on each finite block
template. It also gives zero covariance between distinct block interiors
once the collar boundary variables are conditioned. This is stronger than an
exponential edge bound; using `g_i<=1` gives the displayed `C_G,mu_G`
convention, while retaining the explicit `g_i^2` only improves the activity.

The displayed formula for `C_E` is the geometric sum

```text
sum_{n>=0} C_B exp(h_B n) exp(-(mu_G/2)n).
```

In the finite-range branch the sum is over one finite template
neighborhood, so the corresponding finite template count is enough. `square`

### Definition 9L.1C.1: Finite-Range Covariance Source `HK-COV-FR-SRC`

On a frozen pushed-forward row `T_HK^std`, the finite-range covariance source

```text
HK-COV-FR-SRC(C_0,R_G)
```

holds when the block-conditioned proof-coordinate covariance used for
neutral finite-battery record derivatives satisfies, after gauge-forgetting,

```text
||C_i(B,B')|| <= C_0
```

for all allowed finite record labels, and

```text
C_i(B,B')=0
\quad\text{whenever}\quad
d(B,B')>R_G.
```

The constants `C_0` and `R_G` are constants of the finite pushed-forward
row. The covariance is still a proof-coordinate covariance; the exported
record law contains only the induced scalar bounds.

### Theorem 9L.1C.2: Paper-11 Block Conditioning Supplies `HK-COV-FR-SRC`

Assume the Paper-11 fixed-ratio block-conditioned scheme used in Theorem
9L.1C, with uniform Dirichlet/Poincare lower bound `lambda_D>0`, and assume
the collar-conditioned covariance is supported inside a finite template
neighborhood of block radius `R_blk`. Then

```text
HK-COV-FR-SRC(C_0,R_G)
```

holds with

```text
C_0=lambda_D^{-1},
\qquad
R_G=R_blk.
```

In the strict same-block conditional branch, one may take `R_blk=0` for
interior block variables; if the readout/collar convention keeps one finite
collar layer, take `R_blk` to be that finite collar-template radius.

Proof.

Theorem 9L.1C imports Paper 11 Theorem AF.18: after conditioning on the
declared collar/boundary variables, the covariance is

```text
C_{I|B}^{(r)}=g_r^2 H_{I_rI_r}^{-1}
```

on each finite block template, with

```text
||H_{I_rI_r}^{-1}|| <= lambda_D^{-1}.
```

On the weak-coupling tail `g_r<=1`, this gives the uniform operator bound
`C_0=lambda_D^{-1}`. The same conditioning makes covariance between
unconnected template neighborhoods vanish. The finite block/collar template
therefore gives the support radius `R_G=R_blk`. Pushing the estimate forward
to the finite neutral record law changes neither the scalar norm bound nor
the finite support statement, because the pushforward is a bounded finite
record map already included in the row. `square`

### Corollary 9L.1D: `theta_sf<1` From Paper-11 Covariance And Finite Vertices

Assume:

1. the Paper-11 block-conditioned covariance import of Theorem 9L.1C;
2. the nonabsorbed local small-field vertex ledger has finite total
   local-label norm `C_v g_i^{2p}` with `p>0`;
3. the covariance and vertex ledgers are pushed to the same finite record law.

Then for any target `0<theta_*<1` there is a cofinal weak-coupling tail with

```text
theta_sf
<=
theta_*.
```

It is enough to choose the tail so that

```text
g_*^{2p}
<
theta_*/(e C_v C_G C_E).
```

On that tail `HK-SF-CLOSE` holds with

```text
theta_sf=e C_v C_G C_E g_*^{2p}<1.
```

Proof.

Theorem 9L.1C supplies `C_G,mu_G,C_E`. The finite local vertex ledger
supplies `C_v,p`. Theorem 9L.1B gives the displayed activity bound. Since
`g_i->0`, one can pass to a cofinal tail satisfying the displayed
inequality. `square`

### Theorem 9L.1E: Small-Field Falsifier For This Route

The covariance-vertex route to `HK-SF-CLOSE` fails on a chosen tail if any
of the following holds:

1. the pushed-forward block-conditioned covariance has no finite
   `C_G,mu_G,C_E` edge ledger on that tail;
2. the nonabsorbed local vertex ledger contains a transverse term of order
   `g_i^q` with `q<=0`, so no positive `p` exists;
3. after all legitimate local absorptions, the best available tail still has

   ```text
   e C_v C_G C_E g_*^{2p} >= 1.
   ```

The third item is a failure of this proof route, not by itself a
falsification of Yang-Mills. It says that the declared finite constants and
tail are not strong enough to make the small-field tree expansion
subcritical.

Proof.

Each item negates one hypothesis of Theorem 9L.1B or Corollary 9L.1D.
Without finite edge summability there is no finite `C_E`; without a positive
vertex power there is no asymptotic small parameter; and if the displayed
activity is at least one, the tree/KP geometric sum is not certified by this
criterion. `square`

### Definition 9L.1F: Finite Local Vertex Ledger `HK-SF-VERT`

`HK-SF-VERT(I_v,q_a,C_a,C_{rem},\epsilon_v)` holds when, after:

1. the Gaussian quadratic part has been extracted;
2. all declared relevant/marginal local counterterms have been inserted;
3. the heat-kernel time tangent and pure normalization coordinates have been
   separated;
4. the gauge-fixed proof chart has been pushed to the finite record law;

the nonabsorbed local small-field insertion at a single block/collar admits a
finite expansion

```text
V_i^{loc}(B)
=
sum_{a in I_v} g_i^{q_a} V_{a,i}(B)
+ Q_i(B),
```

with

```text
||V_{a,i}(B)||_ren <= C_a,
||Q_i(B)||_ren <= C_{rem} g_i^{q_*+\epsilon_v},
```

where

```text
q_*:=min_{a in I_v} q_a,
\qquad
q_*>0,
\qquad
\epsilon_v>0.
```

The finite set `I_v` is the complete list of nonabsorbed local Taylor,
Jacobian, chart, covariance-drift, record-expansion, and normalization
labels in the chosen finite battery. Any local label not in `I_v` is either
absorbed into a declared local coordinate or included in the remainder.

### Lemma 9L.1G: Finite Vertex Ledger Produces `C_v,p`

Assume `HK-SF-VERT(I_v,q_a,C_a,C_{rem},epsilon_v)` and choose a weak-coupling
tail with `g_i<=g_*<=1`. Set

```text
p_v:=q_*/2,
```

and

```text
C_v^{vert}
:=
sum_{a in I_v} C_a g_*^{q_a-q_*}
+ C_{rem}g_*^{\epsilon_v}.
```

Then the nonabsorbed local small-field insertion satisfies

```text
||V_i^{loc}(B)||_ren
<=
C_v^{vert} g_i^{2p_v}.
```

Consequently the vertex part of `HK-SF-SRC` holds with

```text
C_v=C_v^{vert},
\qquad
p=p_v.
```

Proof.

Since `q_a>=q_*` and `g_i<=g_*<=1`,

```text
g_i^{q_a}
=
g_i^{q_*}g_i^{q_a-q_*}
<=
g_i^{q_*}g_*^{q_a-q_*}.
```

Similarly,

```text
g_i^{q_*+\epsilon_v}
<=
g_i^{q_*}g_*^{\epsilon_v}.
```

Insert these two bounds into the finite expansion and use the triangle
inequality. Since `q_*=2p_v`, the displayed result follows. `square`

### Definition 9L.1H: Yang-Mills Second-Order Vertex List `HK-SF-YM2`

`HK-SF-YM2` is the following specialization of `HK-SF-VERT` for the
neutral pure-gauge finite battery:

1. every order-`g_i` cubic or odd chart contribution has zero pushed-forward
   transverse record coefficient, or is absorbed as a pure proof-coordinate
   artifact;
2. every time-tangent quadratic coefficient is absorbed into the declared
   heat-kernel time coordinate;
3. every remaining nonabsorbed local label starts at order `g_i^2`;
4. the finite second-order label list is

   ```text
   I_v^{YM2}={4,33,J2,gf2,cov2,rec2,norm2};
   ```

5. the corresponding local-label constants satisfy

   ```text
   C_4^{loc}     <= 24 C_4 C_cov^2,
   C_33^{loc}    <= 18 C_3^2 C_cov^3,
   C_J2^{loc}    <= C_J C_cov,
   C_gf2^{loc}   < infinity,
   C_cov2^{loc}  < infinity,
   C_rec2^{loc}  < infinity,
   C_norm2^{loc} < infinity.
   ```

The constants are local insertion constants before any optional
finite-record projection. Paper 19's `SEL_0` constants are obtained by
applying the finite pushed-forward projection maps to these local labels.

### Theorem 9L.1I: `HK-SF-YM2` Closes The Finite Vertex Ledger With `p=1`

Assume `HK-SF-YM2` on the same pushed-forward finite record law. Then
`HK-SF-VERT` holds with

```text
q_*=2,
\qquad
p=1,
```

and one may take

```text
C_v^{YM2}
:=
24 C_4 C_cov^2
+18 C_3^2 C_cov^3
+C_J C_cov
+C_gf2^{loc}
+C_cov2^{loc}
+C_rec2^{loc}
+C_norm2^{loc}
+C_{rem}g_*^{\epsilon_v}.
```

Consequently the vertex part of `HK-SF-SRC` holds with

```text
C_v=C_v^{YM2},
\qquad
p=1.
```

In the strict axial-tree, exact-covariance, connected/cumulant,
minimal-record branch, the optional local labels may be set to

```text
C_gf2^{loc}=C_cov2^{loc}=C_rec2^{loc}=C_norm2^{loc}=0,
```

so the reduced local vertex constant is

```text
C_v^{YM2,min}
=
24 C_4 C_cov^2
+18 C_3^2 C_cov^3
+C_J C_cov
+C_{rem}g_*^{\epsilon_v}.
```

Proof.

The order-`g_i` labels do not enter the nonabsorbed transverse finite record
ledger by clause 1 of `HK-SF-YM2`; the time-tangent quadratic part is removed
by clause 2. Clauses 3--5 give a finite expansion whose smallest surviving
power is `q_*=2`. Lemma 9L.1G then gives `p=q_*/2=1` and the displayed
constant. The minimal-branch reductions are exactly the declared axial-tree,
exact-covariance, connected/cumulant, and minimal-record normalizations.
`square`

### Corollary 9L.1J: Finite Vertex Ledger Completes The Small-Field Source Route

Assume:

1. the Paper-11 covariance import of Theorem 9L.1C;
2. `HK-SF-YM2`;
3. all covariance, vertex, counterterm, time-tangent, and record-pushforward
   operations are evaluated on the same finite whole-process record law.

Then `HK-SF-SRC(C_G,mu_G,C_v,1,C_E,r_*)` holds with

```text
C_v=C_v^{YM2}.
```

Hence

```text
theta_sf
<=
e C_v^{YM2} C_G C_E g_*^2.
```

For any `0<theta_*<1`, passing to a sufficiently fine AF tail with

```text
g_*^2 < theta_*/(e C_v^{YM2} C_G C_E)
```

proves `theta_sf<=theta_*<1` and therefore `HK-SF-CLOSE`.

Proof.

Theorem 9L.1C supplies the covariance and edge-summability parts of
`HK-SF-SRC`. Theorem 9L.1I supplies the finite vertex part with `p=1`.
The common-record-law clause ensures these are estimates on one
whole-process record law. The tree-activity estimate is Theorem 9L.1B.
`square`

### Corollary 9L.1K: Relation To The Paper-19 `SEL_0` Worksheet

On the `SEL_0` one-block battery of Paper 19, the projected constants

```text
C_sf,4, C_sf,33, C_sf,J2, C_sf,gf2,
C_sf,cov2, C_sf,rec2, C_sf,norm2
```

are the images of the seven `HK-SF-YM2` local labels under the finite
`SEL_0` pushforward/projection map. Thus Paper 19's worksheet is the
one-block coefficient specialization of the generic Paper-16 vertex ledger,
while `C_v^{YM2}` is the upstream tree-expansion constant used to prove
`HK-SF-SRC`.

### Theorem 9L.2: `HK-SF-CLOSE` Proves `HK-SF-GCD`

If `HK-SF-CLOSE(C_G,mu_G,C_v,p,theta_sf,C_ent,r_*)` holds, then
`HK-SF-GCD(C_sf,C_ent,theta_sf,mu_G,p,r_*)` holds with

```text
C_sf = C_v C_G.
```

Proof.

The covariance edge bound and the local vertex bound give the connected
graph expansion assumed in Lemma 9E.2, with edge constant `C_G` and vertex
constant `C_v g_i^{2p}`. The tree activity hypothesis is exactly
`theta_sf<1`. Lemma 9E.2 then yields Definition 9E.1 with
`C_sf=C_v C_G`. All estimates are finally pushed to the record coefficients,
so the gauge chart is only a proof coordinate. `square`

### Corollary 9L.3: Small-Field Status

The small-field branch is reduced to:

```text
HK-SF-CLOSE => HK-SF-GCD.
```

The tree-activity part of `HK-SF-CLOSE` is now reduced further:

```text
Paper-11 block-conditioned covariance
+ HK-SF-YM2 finite vertex ledger
+ common pushed-forward record law
=> theta_sf <= e C_v^{YM2} C_G C_E g_*^2.
```

Thus `theta_sf<1` follows on a sufficiently fine AF tail whenever the
covariance constants and the finite second-order Yang-Mills vertex constants
are finite. The strict axial-tree, exact-covariance, connected/cumulant,
minimal-record branch has the reduced constant

```text
C_v^{YM2,min}
=24C_4C_cov^2+18C_3^2C_cov^3+C_JC_cov
 + C_rem g_*^{epsilon_v}.
```

This does not finish the whole small-field gate automatically: one still has
to verify the common record-law pushforward and the `HK-SF-YM2` clauses on
each chosen finite battery after the declared local counterterms/time-tangent
terms have been removed. Paper 19 verifies this for the frozen `SEL_0`
one-block battery by proving the odd order-`g_i` cancellation, the
time-tangent absorption, the seven-label second-order vertex list, and the
finite pushed-forward projection constants on one common record law.
If only a power-law block covariance is available, the present exponential
`HK-SF-GCD` route fails and must be replaced by a KP-weighted summability
theorem with a different entropy ledger.

## 9M. KP Threshold From The Current Constants

The Paper-15 KP gate requires more than decay in words. It requires the
weighted residual activity to stay below one.

### Definition 9M.1: KP-Weighted Residual Test `HK-KP-TEST`

Let `m>=0` be the KP weight. A size-resolved residual envelope with constants
`A_res,mu_res,C_KP,h_KP,r_*` passes `HK-KP-TEST(m)` when

```text
mu_res > h_KP + m
```

and

```text
eta_res^{bd}(m)
 =
 C_KP A_res
 exp(-(mu_res-h_KP-m) r_*)
 /
 (1-exp(-(mu_res-h_KP-m)))
 < 1.
```

Here `C_KP exp(h_KP n)` bounds the number of connected polymers of size `n`
containing a fixed block after all finite-battery labels are included.

### Theorem 9M.1A: Sharp Scalar Decision For `HK-KP-TEST`

Set

```text
D_0 := mu_res - h_KP,
B_res := C_KP A_res.
```

For `0<=m<D_0`, write

```text
delta(m):=D_0-m,
E_m:=
B_res exp(-delta(m) r_*)/(1-exp(-delta(m))).
```

Then:

1. `HK-KP-TEST(m)` holds exactly when `0<=m<D_0` and `E_m<1`;
2. the function `m -> E_m` is strictly increasing on `[0,D_0)`;
3. therefore some nonnegative `m` passes if and only if the zero-weight test
   passes:

   ```text
   E_0=
   B_res exp(-D_0 r_*)/(1-exp(-D_0))
   <1;
   ```

4. if `E_0>=1`, no choice of `m>=0` can make `HK-KP-TEST(m)` true with
   these constants.

If `E_0<1`, let `x_*=x_*(B_res,r_*)` be the unique number in `(0,1)`
solving

```text
B_res x_*^{r_*}+x_*=1.
```

Then all admissible KP weights are exactly

```text
0<=m<m_max,
\qquad
m_max:=D_0+\log x_*,
```

with the endpoint excluded because the KP inequality is strict.

Proof.

The first statement is just Definition 9M.1 with
`delta(m)=mu_res-h_KP-m`. For monotonicity, regard

```text
E(delta)=B_res exp(-delta r_*)/(1-exp(-delta)).
```

Then

```text
d/delta log E(delta)
=
-r_*-exp(-delta)/(1-exp(-delta))<0,
```

so `E(delta)` is strictly decreasing in `delta`. Since
`delta(m)=D_0-m` is strictly decreasing in `m`, `E_m` is strictly increasing
in `m`. Hence the smallest possible KP activity occurs at `m=0`, proving
the zero-weight pass/fail criterion.

For the final formula, put `x=exp(-delta)`. The inequality `E(delta)<1`
becomes

```text
B_res x^{r_*}<1-x.
```

The function `B_res x^{r_*}+x` is continuous and strictly increasing from
`0` to `B_res+1>1` on `[0,1]`, so it has a unique root `x_*` in `(0,1)`.
The strict inequality is equivalent to `x<x_*`, i.e.
`exp(-(D_0-m))<x_*`, which is exactly `m<D_0+\log x_*`. `square`

### Corollary 9M.1B: Positive-Weight And Reserve Criteria

Suppose an external Paper-15 or marked-battery ledger requires a KP weight
at least `m_req>=0`. With the same constants,
`HK-KP-TEST(m_req)` holds exactly when

```text
m_req<D_0
```

and

```text
B_res exp(-(D_0-m_req)r_*)/
(1-exp(-(D_0-m_req)))<1.
```

Equivalently, in the notation of Theorem 9M.1A,

```text
m_req<m_max.
```

For a desired strict residual reserve `0<eta_*<1`, the zero-weight KP
activity satisfies

```text
eta_res^{bd}(0)<=eta_*
```

provided

```text
r_*
\ge
{1\over D_0}
\log\left(
{B_res\over \eta_*(1-exp(-D_0))}
\right).
```

The same formula with `D_0` replaced by `D_0-m_req` gives the required
range for a prescribed positive `m_req`.

Proof.

The positive-weight statement is Theorem 9M.1A evaluated at `m_req`. The
reserve estimate is the inequality

```text
B_res exp(-D_0r_*)/(1-exp(-D_0))<=eta_*
```

solved for `r_*`. `square`

### Theorem 9M.1C: Range-Absorption Route To The KP Test

Assume the residual decomposition has a local-absorption certificate:
for every integer `R>=r_*`, all connected residual polymers of size
`<R` can be absorbed into the declared local action, counterterm, or finite
record normalization on the same block/collar tower, while the size-resolved
tail for polymers of size `>=R` keeps the same constants
`A_res,mu_res,C_KP,h_KP`.

Let `D_0=mu_res-h_KP>0`. For any required weight `m_req<D_0` and any desired
reserve `0<eta_*<1`, choose

```text
R
\ge
{1\over D_0-m_req}
\log\left(
{B_res\over \eta_*(1-exp(-(D_0-m_req)))}
\right).
```

Then the absorbed residual decomposition satisfies

```text
eta_res^{bd}(m_req)\le eta_*<1,
```

and hence passes `HK-KP-TEST(m_req)`.

Proof.

After local absorption, the KP summation starts at `R` instead of the
original `r_*`. Apply Corollary 9M.1B with `r_*=R` and
`D_0` replaced by `D_0-m_req`. The local-absorption hypothesis is essential:
without it, moving the lower summation range would discard actual residual
polymers rather than moving them into the declared local ledger. `square`

### Definition 9M.1D: Same-Row Finite Counting Data `HK-FIN-COUNT`

Fix the frozen pushed-forward row `T_HK^std`. The finite counting data

```text
HK-FIN-COUNT(Delta_B,L_ent,L_KP)
```

hold when:

1. the block graph used by the residual polymers has maximum degree at most
   `Delta_B>=1`;
2. after gauge-forgetting and projection to the finite record battery, the
   small-field connected-graph entropy labels have at most `L_ent>=1`
   choices per block;
3. after the declared local counterterms, scheme choices, collar variables,
   and readout records are pushed to the same finite battery, the residual
   KP polymer labels have at most `L_KP>=1` choices per block;
4. the labels counted by `L_ent` and `L_KP` are finite-record labels, not
   gauge-coordinate field values.

This is a combinatorial certificate for one record row. It is not a
continuum compactness assumption and it is not a hidden discretized ontology:
the only exported objects are the finite label counts of the
pushed-forward record law.

### Theorem 9M.1E: Finite Counting Gives `C_E`, `C_ent`, `C_KP`, And `h_KP`

Assume `HK-FIN-COUNT(Delta_B,L_ent,L_KP)`. Then:

1. for every `mu>2 log Delta_B`, the edge-summability constant in
   `HK-SF-SRC` may be taken as

   ```text
   C_E(mu)
   =
   1/(1-Delta_B exp(-mu/2));
   ```

2. the connected-polymer entropy used by the small-field and large-field
   estimates may be taken as

   ```text
   C_ent=1,
   h_ent=log(e Delta_B L_ent);
   ```

3. the KP residual counting constants may be taken as

   ```text
   C_KP=1,
   h_KP=log(e Delta_B L_KP).
   ```

More generally, if the row carries harmless global finite prefactors
`P_ent` and `P_KP`, replace `C_ent` and `C_KP` by those prefactors and leave
the rates unchanged.

Proof.

For the edge sum, the number of block vertices at graph distance `n` from a
fixed block is bounded by `Delta_B^n`. Therefore

```text
sup_B sum_{B'} exp(-(mu/2)d(B,B'))
<=
sum_{n>=0} Delta_B^n exp(-mu n/2)
=
1/(1-Delta_B exp(-mu/2)),
```

which is finite exactly under the displayed condition.

For connected polymers, use the standard depth-first exploration bound:
the number of connected vertex sets of size `n` containing a fixed root in
a graph of degree at most `Delta_B` is bounded by `(e Delta_B)^{n-1}`,
hence by `(e Delta_B)^n`. Multiplying by at most `L_ent^n` small-field
entropy labels gives

```text
(e Delta_B L_ent)^n
=
exp(log(e Delta_B L_ent)n),
```

so `C_ent=1` and `h_ent=log(e Delta_B L_ent)` are valid. Multiplying
instead by the finite residual label count `L_KP^n` gives

```text
(e Delta_B L_KP)^n
=
exp(log(e Delta_B L_KP)n),
```

which is the stated KP counting ledger. Finite global prefactors are
absorbed into `C_ent` or `C_KP`. Every count is made after projection to the
same finite record law, so no gauge-coordinate species is exported.
`square`

### Corollary 9M.1F: Fully Explicit Clean KP Counting Constants

On a row with `HK-FIN-COUNT(Delta_B,L_ent,L_KP)`, the clean worksheet may
use

```text
C_E(mu)=1/(1-Delta_B exp(-mu/2)),
C_ent=1,
C_KP=1,
h_KP=log(e Delta_B L_KP),
```

for every `mu>2 log Delta_B`. If global finite prefactors are kept, replace
`C_ent` and `C_KP` by those prefactors. Thus the remaining clean KP
calculation has no unnamed entropy constants: the only inputs are the
same-row finite degree and finite label counts.

### Theorem 9M.2: Current Constants Feed The KP Gate Under `HK-KP-TEST`

Assume:

1. `HK-SF-CLOSE`;
2. `HK-LF-CLOSE`;
3. `HK-CT-CLOSE`;
4. the resulting residual coefficients obey the size-resolved envelope with

```text
A_res
 =
 (C_v C_G C_ent/(1-theta_sf) + A_tail + A_scheme) g_*^{2p}
 + 1,

mu_res
 =
 min(mu_G/2, mu_tail, mu_scheme, sigma_lf^sharp),
```

where the `+1` is the normalized large-field amplitude from Theorem 9J.2;
5. `HK-KP-TEST(m)` holds for these constants.

Then the Paper-15 residual KP gate `AYM-KP` holds with positive reserve

```text
1 - eta_res^{bd}(m).
```

Proof.

Theorems 9K.2, 9L.2, and 9J.2 supply the counterterm, small-field, and
large-field parts of the residual envelope. The displayed `A_res` and
`mu_res` are the combined amplitude and the slowest exponential rate.
Summing the KP-weighted activities over connected polymers of size at least
`r_*` gives the geometric series in Definition 9M.1. If that series is less
than one, the residual KP criterion holds with the displayed reserve.
`square`

### Honest Boundary Of The KP Test

The KP test uses a size-resolved envelope. The earlier `AFRCE` tail bound is
not automatically enough if it does not control the KP weight
`exp(m|Y|)`. Theorem 9M.1A now makes the scalar threshold sharp: for fixed
constants, the best possible choice is `m=0`, and any positive required
weight must satisfy `m_req<m_max`. If the zero-weight activity is already
`>=1`, this residual envelope cannot prove the KP gate for any
`m>=0`.

Theorem 9M.1C gives the only honest way to improve the range factor: absorb
all polymers below a larger range `R` into the declared local
action/counterterm/record normalization, then sum only the true residual
tail. Without that local-absorption certificate, increasing `r_*` would just
hide residual polymers.

Thus Paper 16 has derived the correct scalar threshold and the correct
range-absorption route. Proving the threshold for actual `4D SU(N)` still
requires the size-resolved constants from `HK-SF-CLOSE`, `HK-LF-CLOSE`, and
`HK-CT-CLOSE`, plus any local-absorption certificate used to raise the
effective residual range.

## 9N. Assembled Analytic Branch

The small-field, large-field, counterterm, and KP estimates can now be
imported as one analytic certificate.

### Definition 9N.1: Analytic Closure Certificate `HK-AN-CLOSE`

`HK-AN-CLOSE(m)` holds when all of the following are verified on the same
heat-kernel whole-process record-law tower:

1. `HK-SF-CLOSE(C_G,mu_G,C_v,p,theta_sf,C_ent,r_*)`;
2. `HK-LF-CLOSE` with sharp rate `sigma_lf^sharp`;
3. `HK-CT-CLOSE(A_tail,mu_tail,A_scheme,mu_scheme,p,r_ct)`;
4. the size-resolved residual constants are compatible on a common block
   graph, with

```text
A_res
 =
 (C_v C_G C_ent/(1-theta_sf) + A_tail + A_scheme) g_*^{2p}
 + 1,

mu_res
 =
 min(mu_G/2, mu_tail, mu_scheme, sigma_lf^sharp),

r_res = max(r_*,r_ct);
```

5. `HK-KP-TEST(m)` holds with `A_res,mu_res,C_KP,h_KP,r_res`;
6. all constants are computed from the same pushed-forward record laws and
   the same collar/block decomposition.

### Definition 9N.1A: Ordered Analytic Source Certificate `HK-AN-SRC`

`HK-AN-SRC(m)` is the following dependency-ordered source certificate for
`HK-AN-CLOSE(m)`. All entries are evaluated on one heat-kernel
whole-process record-law tower, with one block/collar decomposition and one
pushed-forward finite-battery readout ledger.

1. **Small-field source.** `HK-SF-SRC(C_G,mu_G,C_v,p,C_E,r_*)` holds, the
   small-field polymer entropy constant `C_ent` of Definition 9E.1 is
   finite, and the AF tail is chosen with `g_i<=g_*` so that

   ```text
   theta_sf := e C_v C_G C_E g_*^{2p} < 1.
   ```

2. **Large-field source.** `HK-LF-CLOSE` holds with

   ```text
   sigma_lf^sharp
    =
    (c_H-a_ad)delta^2/t_L
    - log(C_ad P_b C_H C_lab C_coef C_rec C_ext)
    > h_poly.
   ```

3. **Counterterm source.** `HK-CT-CLOSE(A_tail,mu_tail,A_scheme,mu_scheme,p,r_ct)`
   holds with finite constants and positive decay rates.

4. **Common residual constants.** Define

   ```text
   A_res
    =
    (C_v C_G C_ent/(1-theta_sf) + A_tail + A_scheme) g_*^{2p}
    + 1,

   mu_res
    =
    min(mu_G/2, mu_tail, mu_scheme, sigma_lf^sharp),

   r_res = max(r_*,r_ct).
   ```

5. **KP scalar pass.** With

   ```text
   D_0 := mu_res-h_KP,
   B_res := C_KP A_res,
   delta_m := D_0-m,
   ```

   one has

   ```text
   delta_m>0
   ```

   and

   ```text
   eta_res^{bd}(m)
    =
    B_res exp(-delta_m r_res)/(1-exp(-delta_m))
    < 1.
   ```

6. **No hidden process switch.** The covariance, vertex, large-field,
   counterterm, scheme, entropy, and KP constants are all constants of the
   same pushed-forward record laws. Gauge-fixed charts and block-conditioned
   Gaussian variables are proof coordinates only.

In the `HK-SF-YM2` branch, item 1 may be supplied by Corollary 9L.1J with
`p=1` and `C_v=C_v^{YM2}`. For a finite battery whose optional projected
labels vanish, one may use the reduced constant `C_v^{YM2,min}`.

### Theorem 9N.1B: Ordered Source Certificate Proves `HK-AN-CLOSE`

If `HK-AN-SRC(m)` holds, then `HK-AN-CLOSE(m)` holds with the constants
defined in Definition 9N.1A.

Proof.

Item 1 and Theorem 9L.1B give
`HK-SF-CLOSE(C_G,mu_G,C_v,p,theta_sf,C_ent,r_*)`. Item 2 is exactly the
assembled large-field certificate `HK-LF-CLOSE`; Theorem 9J.2 later pushes it
to `HK-LFS`, but Definition 9N.1 only needs the closure certificate and the
sharp rate. Item 3 is exactly `HK-CT-CLOSE`.

Item 4 is the residual-constant compatibility clause of Definition 9N.1,
with the small-field amplitude, counterterm/scheme tails, and normalized
large-field contribution combined on the same block graph. Item 5 is
`HK-KP-TEST(m)` written in the scalar variables of Theorem 9M.1A. Item 6 is
the whole-process compatibility clause. Therefore every clause of
Definition 9N.1 holds. `square`

### Corollary 9N.1C: Execution Order For Proving `HK-AN-CLOSE`

The ordered proof route is:

```text
1. prove HK-SF-SRC and choose the AF tail so theta_sf<1;
2. prove HK-LF-CLOSE and its margin sigma_lf^sharp>h_poly;
3. run HK-CT-RATE, hence HK-CT-SRC and HK-CT-CLOSE, with positive source
   rates for every nonempty tail;
4. assemble A_res, mu_res, r_res on the same record tower via
   HK-AN-RES-COMMON;
5. test the scalar KP inequality eta_res^{bd}(m)<1.
```

This order matters. The small-field step fixes `p`, `C_v`, `theta_sf`, and
the first part of `A_res`; the large-field and counterterm steps fix
`mu_res`; only after those constants are known is the KP test a meaningful
scalar decision.

### Theorem 9N.1D: Exact Falsifiers For This Analytic Route

The ordered route through `HK-AN-SRC(m)` fails on a chosen heat-kernel tower
if any one of the following occurs:

```text
1. no common pushed-forward record law carries all source constants;
2. HK-SF-SRC fails, or theta_sf>=1 on every admissible AF tail;
3. HK-LF-CLOSE fails, or sigma_lf^sharp<=h_poly;
4. HK-CT-CLOSE fails, or one of mu_tail,mu_scheme is nonpositive;
5. D_0=mu_res-h_KP<=m;
6. eta_res^{bd}(m)>=1 after all legitimate local absorption has been used.
```

Items 1--4 are source-certificate failures. Items 5--6 are scalar KP
failures for the constants actually produced by the source certificates. A
failure of this route is not automatically a disproof of continuum
Yang-Mills; it is a precise obstruction to this heat-kernel analytic branch.

Proof.

Items 1--4 negate one of the source clauses required by Definition 9N.1A.
If item 5 holds, then `delta_m<=0`, so the KP sum has no positive
exponential decay after entropy and weight. If item 6 holds, the geometric
KP activity is not subcritical. By Theorem 9M.1A, with fixed constants and
fixed effective range this scalar obstruction is sharp. `square`

### Corollary 9N.1E: Step 1 Pass For The Small-Field Source

Assume:

1. the Paper-11 block-conditioned covariance import of Theorem 9L.1C;
2. `HK-SF-YM2` on the same pushed-forward finite record law;
3. a finite small-field polymer entropy constant `C_ent`.

Then the first source input of `HK-AN-SRC(m)` is satisfied with

```text
p=1,
C_v=C_v^{YM2},
theta_sf=e C_v^{YM2} C_G C_E g_*^2.
```

For any target `0<theta_*<1`, choosing the AF tail so that

```text
g_*^2 < theta_*/(e C_v^{YM2} C_G C_E)
```

gives

```text
theta_sf<=theta_*<1.
```

Consequently the small-field execution step is closed on every finite
battery for which the common-record `HK-SF-YM2` verification has been
performed. In particular, Paper 19 supplies this verification for the
coefficient-only frozen `SEL_0` one-block battery.

Proof.

Theorem 9L.1C gives the covariance and finite edge-summability constants.
Theorem 9L.1I gives the vertex ledger with `p=1` and `C_v=C_v^{YM2}`.
Corollary 9L.1J then gives `HK-SF-SRC` and the displayed tree activity.
The AF tail inequality makes the activity strictly subcritical. `square`

### Corollary 9N.1F: Step 2 Pass For The Large-Field Source

Assume:

1. `HK-LF-TPL` on the same heat-kernel whole-process record-law tower used
   by the small-field source;
2. the heat-kernel plaquette-tail and local-lower-bound constants use the
   same bi-invariant metric;
3. the AF heat-kernel time can be restricted cofinally below the cutoff
   `t_L` chosen in Theorem 9J.8.

Then the second source input of `HK-AN-SRC(m)` is satisfied. More precisely,
for every desired `xi_lf>0`, Theorem 9J.8 gives

```text
HK-LF-CLOSE
```

with

```text
sigma_lf^sharp>=h_poly+xi_lf>h_poly.
```

Proof.

Theorem 9J.8 is exactly the global large-field source theorem on a standard
finite block/collar heat-kernel tower. Its hypotheses are the three displayed
assumptions, and its conclusion is `HK-LF-CLOSE` with a strict entropy
margin. This is precisely item 2 of Definition 9N.1A. The use of axial-tree
charts, collar minimizers, and BCH estimates remains internal to the proof;
the exported object is a large-field coefficient bound for the pushed-forward
record law. `square`

### Corollary 9N.1G: Step 3 Pass For The Counterterm Source

Assume:

1. the Paper-11 ledger-compatible block-conditioned pure-gauge trajectory on
   the frozen row `T_HK^std`;
2. the relevant/marginal pure-gauge local ansatz includes the Yang-Mills
   heat-time/coupling coordinate and all declared local normalizations;
3. either the branch is clean minimal, or `HK-CT-RATE` holds with finite
   constants for every nonempty irrelevant or scheme tail.

Then the third source input of `HK-AN-SRC(m)` is satisfied:

```text
HK-CT-CLOSE(A_tail,mu_tail,A_scheme,mu_scheme,p,r_ct)
```

with

```text
mu_tail>0,
\qquad
mu_scheme>0.
```

Proof.

If the branch is clean minimal, Theorem 9K.2G gives `HK-CT-RATE` with
`A_tail=A_scheme=0` and positive bookkeeping rates. Otherwise the assumed
finite rate audit gives `HK-CT-RATE` with the exported constants. In either
case, Theorem 9K.2F turns the same-record rate audit into
`HK-CT-SRC(A_tail,mu_tail,A_scheme,mu_scheme,p,r_ct)`, and Theorem 9K.2C
proves `HK-CT-CLOSE` with the displayed positive rates. This is precisely
item 3 of Definition 9N.1A. Empty tail sectors contribute zero amplitude and
do not create residual polymers; strictly local counterterm and scheme
coordinates remain local proof coordinates, not hidden variables. `square`

### Definition 9N.1H: Common Residual Constant Ledger `HK-AN-RES-COMMON`

`HK-AN-RES-COMMON(A_res,mu_res,r_res)` holds when the first three source
steps have been verified on the common record law of Corollary 9J.10 and the
following constants are the constants of that same law:

```text
theta_sf=e C_v C_G C_E g_*^{2p},
```

with `theta_sf<1`,

```text
sigma_lf^sharp>h_poly,
```

and

```text
A_tail, mu_tail, A_scheme, mu_scheme, r_ct
```

from `HK-CT-RATE`. The residual envelope constants are then declared to be

```text
A_res
 =
 (C_v C_G C_ent/(1-theta_sf) + A_tail + A_scheme) g_*^{2p}
 + 1,

mu_res
 =
 min(mu_G/2, mu_tail, mu_scheme, sigma_lf^sharp),

r_res = max(r_*,r_ct).
```

The `+1` is the normalized large-field amplitude after Theorem 9J.2, where
`HK-LF-CLOSE` gives `HK-LFS` with `C_lf=1` and rate
`sigma_lf^sharp`. If a counterterm or scheme tail sector has zero amplitude,
its positive bookkeeping rate is ignored by replacing it with any rate not
smaller than the nonzero minimum; equivalently, zero-amplitude sectors do
not lower `mu_res`.

### Theorem 9N.1I: Steps 1--4 Give The Common Residual Envelope

Assume:

1. the common-record audit of Corollary 9J.10;
2. the small-field source pass of Corollary 9N.1E;
3. the large-field source pass of Corollary 9N.1F;
4. the counterterm source pass of Corollary 9N.1G.

Then `HK-AN-RES-COMMON(A_res,mu_res,r_res)` holds, and item 4 of
Definition 9N.1A is satisfied.

Proof.

The small-field source gives the subcritical tree sum. Summing the
tree-expanded small-field coefficients over connected polymers of diameter
at least `r` gives the amplitude

```text
C_v C_G C_ent g_*^{2p}/(1-theta_sf)
```

and rate `mu_G/2`. The large-field source gives `HK-LFS` by Theorem 9J.2,
with normalized amplitude `1` and rate `sigma_lf^sharp`. The counterterm
source gives the irrelevant and scheme tail amplitudes `A_tail g_*^{2p}`
and `A_scheme g_*^{2p}`, with rates `mu_tail` and `mu_scheme`.

Because all four bounds are bounds on the same pushed-forward finite-record
law, the residual coefficient is bounded by the sum of those four envelopes.
Taking the minimum of the positive rates and the maximum of the starting
radii gives exactly the constants in Definition 9N.1H. The proof uses only
record-law coefficients; Gaussian coordinates, counterterm coordinates, and
scheme coordinates are internal proof charts. `square`

### Corollary 9N.1J: Only The Scalar KP Decision Remains After Step 4

Once `HK-AN-RES-COMMON(A_res,mu_res,r_res)` is verified, the analytic branch
has no further structural source gate before KP. The remaining decision is
the sharp scalar test

```text
D_0=mu_res-h_KP,
B_res=C_KP A_res,
delta_m=D_0-m,
eta_res^{bd}(m)
 =
 B_res exp(-delta_m r_res)/(1-exp(-delta_m))<1,
```

with `delta_m>0`. If this inequality passes, `HK-AN-SRC(m)` holds. If it
fails for the assembled constants, Theorem 9M.1A gives the exact KP
obstruction for this heat-kernel analytic branch unless a legitimate local
absorption certificate raises the effective residual range.

### Definition 9N.1K: Clean Minimal Analytic KP Worksheet

The clean minimal analytic worksheet is the specialization of
`HK-AN-RES-COMMON` to the frozen row `T_HK^std` with:

1. `HK-SF-YM2` on the same pushed-forward finite record law, with
   `p=1` and finite vertex constant `C_v^{row}`. In the strict
   minimal branch one may take `C_v^{row}=C_v^{YM2,min}`;
2. `HK-LF-CLOSE` on the same row, with
   `sigma_lf^sharp>h_poly`;
3. the clean minimal counterterm branch of Theorem 9K.2G, so

   ```text
   A_tail=0,
   A_scheme=0;
   ```

4. a KP entropy ledger on the same residual battery:

   ```text
   C_KP exp(h_KP n)
   ```

   bounds the number of connected residual polymers of size `n` containing
   a fixed block, including the finite residual labels of this same row.

The worksheet constants are:

```text
theta_clean
 =
 e C_v^{row} C_G C_E g_*^2,

A_res^clean
 =
 C_v^{row} C_G C_ent g_*^2/(1-theta_clean)
 + 1,

mu_res^clean
 =
 min(mu_G/2, sigma_lf^sharp),

r_res^clean=max(r_*,r_ct).
```

For a required KP weight `m>=0`, define

```text
D_clean := mu_res^clean-h_KP,
B_clean := C_KP A_res^clean,
delta_clean(m):=D_clean-m,
```

and

```text
eta_clean(m)
 =
 B_clean exp(-delta_clean(m) r_res^clean)
 /(1-exp(-delta_clean(m))).
```

All constants in this worksheet are finite-record constants of `T_HK^std`.
Gauge charts, axial trees, counterterm coordinates, and scheme coordinates
do not appear in the exported worksheet except through these scalar bounds.

### Theorem 9N.1L: Clean Minimal Row Reduces `HK-AN-SRC` To One KP Inequality

Assume the clean minimal analytic worksheet of Definition 9N.1K. Then the
clean minimal branch proves `HK-AN-SRC(m)` if and only if

```text
theta_clean<1,
delta_clean(m)>0,
eta_clean(m)<1.
```

In that case,

```text
HK-AN-SRC(m)
=> HK-AN-CLOSE(m)
=> AYM-AFRCE + AYM-KP,
```

and the exported residual decay margin is

```text
Delta_res=delta_clean(m)>0,
\qquad
K_res=C_KP A_res^clean/(1-exp(-Delta_res)).
```

Proof.

The small-field source is Corollary 9N.1E with `p=1` and
`C_v=C_v^{row}`; its only scalar requirement is `theta_clean<1`. The
large-field source is Corollary 9N.1F. The counterterm source is Corollary
9N.1G, using Theorem 9K.2G to set `A_tail=A_scheme=0`; zero-amplitude
counterterm/scheme sectors do not lower `mu_res`. Theorem 9N.1I then gives
`HK-AN-RES-COMMON` with exactly the constants displayed in Definition
9N.1K.

It remains only to apply Definition 9M.1 to those constants. That definition
is precisely the two scalar inequalities `delta_clean(m)>0` and
`eta_clean(m)<1`. The implication to `AYM-AFRCE + AYM-KP` is Theorem 9N.2,
and the exported `Delta_res,K_res` are Theorem 9N.2A with the clean
constants substituted. `square`

### Corollary 9N.1M: Exact Clean-Branch KP Falsifier

For fixed clean minimal constants on `T_HK^std`, no choice of nonnegative
KP weight can prove `HK-KP-TEST` by this envelope if the zero-weight
quantity

```text
eta_clean(0)
 =
 B_clean exp(-D_clean r_res^clean)/(1-exp(-D_clean))
```

is at least `1`, or if `D_clean<=0`. If `D_clean>0` and
`eta_clean(0)<1`, all admissible KP weights are those described by Theorem
9M.1A with `B_res=B_clean` and `r_*=r_res^clean`.

Thus the next actual calculation is completely explicit: compute the
same-row constants `C_KP,h_KP,C_G,mu_G,C_E,C_ent,C_v^{row},
sigma_lf^sharp,r_*,r_ct,g_*`, choose the required `m`, and evaluate the
three inequalities in Theorem 9N.1L. If the test fails, the only honest
repairs are sharper same-row constants or a proven local-absorption
certificate of Theorem 9M.1C.

### Definition 9N.1N: Clean Minimal Constants Table

For the clean minimal row `T_HK^std`, the constants needed by the worksheet
are fixed in the following order.

| Constant | Source on `T_HK^std` | Role |
| --- | --- | --- |
| `C_v^{row}` | finite `HK-SF-YM2` vertex list; `C_v^{YM2,min}` in the strict minimal branch | local vertex amplitude |
| `C_G,mu_G` | block-conditioned covariance import | small-field graph amplitude and decay |
| `C_E,C_ent` | finite edge/polymer entropy ledger | tree activity and polymer counting |
| `g_*` | chosen cofinal AF tail cutoff | small-field small parameter |
| `sigma_lf^sharp` | `HK-LF-CLOSE` large-field margin | large-field decay rate |
| `C_KP,h_KP` | same residual battery KP counting ledger | KP entropy constants |
| `r_*,r_ct` | small-field/counterterm starting radii | residual starting range |
| `m` | Paper-15 or marked-battery required KP weight | residual weight to be carried |

The table is valid only when every entry is computed on the same
pushed-forward record law. In particular, `C_KP,h_KP` must count the same
residual labels whose coefficients are bounded by `A_res^clean` and
`mu_res^clean`; otherwise the KP test is mixing different record laws.

### Theorem 9N.1O: First Clean Inequality, `theta_clean<1`

Assume the constants `C_v^{row},C_G,C_E` in Definition 9N.1N are finite on
`T_HK^std`. For any chosen `0<theta_*<1`, if the AF tail is restricted so
that

```text
g_*^2
<
theta_*/(e C_v^{row} C_G C_E),
```

then

```text
theta_clean<=theta_*<1.
```

Thus the first clean worksheet inequality is not a dynamical obstruction
once the same-row constants are finite and the asymptotically-free tail can
be taken cofinally.

Proof.

By Definition 9N.1K,

```text
theta_clean=e C_v^{row} C_G C_E g_*^2.
```

Substitution of the displayed AF-tail bound gives the claim. The step uses
only the scalar value of `g_*` on the chosen cofinal tail; no gauge chart or
local scheme coordinate is part of the exported statement. `square`

### Theorem 9N.1P: Second Clean Inequality, The Decay Margin

For the clean minimal worksheet, define

```text
D_clean=mu_res^clean-h_KP
       =min(mu_G/2,sigma_lf^sharp)-h_KP.
```

For a required KP weight `m>=0`,

```text
delta_clean(m)>0
```

is equivalent to the pair of strict inequalities

```text
mu_G>2(h_KP+m),
\qquad
sigma_lf^sharp>h_KP+m.
```

Consequently, once `HK-LF-CLOSE` has chosen
`sigma_lf^sharp>h_KP+m`, the actual decay bottleneck is

```text
mu_G/2>h_KP+m.
```

If this fails on `T_HK^std`, the clean minimal envelope cannot prove
`HK-KP-TEST(m)` for the required weight, regardless of how small `g_*` is.

Proof.

By definition,

```text
delta_clean(m)
=min(mu_G/2,sigma_lf^sharp)-h_KP-m.
```

The minimum exceeds `h_KP+m` exactly when both entries exceed `h_KP+m`.
The large-field rate can be made part of the source target through the
finite-template margin theorem, but the small-field covariance decay
`mu_G` is a separate same-row source constant. Decreasing `g_*` improves
the amplitude `A_res^clean`, not the decay exponent `mu_G`; hence it cannot
repair a nonpositive `delta_clean(m)`. `square`

### Theorem 9N.1P.1: Finite-Range Covariance Forces The Decay Margin

Assume the block-conditioned covariance on `T_HK^std` has finite interaction
range `R_G` in the block graph after collar conditioning:

```text
C_i(B,B')=0
\quad\text{if}\quad
d(B,B')>R_G,
```

and has same-row operator norm bound

```text
||C_i(B,B')||<=C_0
```

on the allowed finite record labels. Then for every chosen envelope rate
`mu>0`, the same covariance satisfies the exponential edge bound

```text
||C_i(B,B')||
<=
C_0 exp(mu R_G) exp(-mu d(B,B')).
```

Consequently, for any finite KP entropy and weight constants `h_KP,m`, one
may choose

```text
mu_G>2(h_KP+m)
```

and the clean decay margin

```text
delta_clean(m)>0
```

holds once the large-field source is chosen with
`sigma_lf^sharp>h_KP+m`.

Proof.

If `d(B,B')>R_G`, the covariance is zero and the displayed exponential bound
is trivial. If `d(B,B')<=R_G`, then

```text
1<=exp(mu R_G)exp(-mu d(B,B')),
```

so the operator norm bound gives the displayed edge estimate. This proves
`HK-SF-SRC` with the chosen envelope rate `mu_G=mu` and amplitude
`C_G=C_0 exp(mu R_G)`. Choosing `mu>2(h_KP+m)` gives
`mu_G/2>h_KP+m`. The large-field rate can be forced above `h_KP+m` by the
finite-template time-cutoff theorem, so Theorem 9N.1P gives
`delta_clean(m)>0`. `square`

### Corollary 9N.1P.2: Cost Of Forcing The Decay Margin

The finite-range proof of Theorem 9N.1P.1 does not make KP automatic. It
increases the clean amplitude through

```text
C_G(mu)=C_0 exp(mu R_G)
```

and through the edge-summability constant `C_E(mu)`. Thus forcing
`delta_clean(m)>0` may make the later activity
`eta_clean(m)` harder. The order of work is therefore:

```text
1. choose the smallest useful mu_G with mu_G>2(h_KP+m);
2. choose sigma_lf^sharp>h_KP+m;
3. choose the AF tail so theta_clean<1 despite the larger C_G(mu_G)C_E(mu_G);
4. test eta_clean(m)<1 with the resulting B_clean and r_res^clean.
```

This is an envelope optimization inside one finite record law, not a change
of physical process. The adjustable `mu_G` is a bound on a finite-range
proof-coordinate covariance, not an ontic mass gap.

### Theorem 9N.1Q: Third Clean Inequality, The KP Activity Threshold

Assume `theta_clean<1` and `delta_clean(m)>0`. Let

```text
B_clean
 =
C_KP
\left(
 C_v^{row} C_G C_ent g_*^2/(1-theta_clean)
 +1
\right),
```

and set `delta=delta_clean(m)`. Then

```text
eta_clean(m)<1
```

is equivalent to

```text
r_res^clean
>
{1\over delta}
log\left({B_clean\over 1-exp(-delta)}\right)
```

when the logarithm is positive; if the logarithm is nonpositive, every
positive starting range passes the activity inequality.

For an integer polymer range, it is enough to require

```text
r_res^clean
>=
1+
floor\left[
{1\over delta}
log\left({B_clean\over 1-exp(-delta)}\right)
\right]
```

whenever the displayed logarithm is positive.

Proof.

With `delta>0`, Definition 9N.1K gives

```text
eta_clean(m)
=
B_clean exp(-delta r_res^clean)/(1-exp(-delta)).
```

The strict inequality `eta_clean(m)<1` is therefore equivalent to

```text
exp(-delta r_res^clean)
<
(1-exp(-delta))/B_clean.
```

Taking logarithms and dividing by `-delta` gives the displayed strict lower
bound on `r_res^clean`. If the logarithm is nonpositive, the right side is
nonpositive, and any positive residual starting range satisfies the strict
bound. The integer version is the corresponding strict integer lower bound.
`square`

### Theorem 9N.1Q.1: Evaluating `eta_clean(m)` From Finite-Range Source Constants

Work on one frozen pushed-forward row `T_HK^std`. Assume:

1. the strict finite-range covariance hypotheses of Theorem 9N.1P.1 hold
   with same-record constants `C_0` and `R_G`;
2. the edge, vertex, and KP counting constants
   `C_E(mu), C_v^{row}, C_ent, C_KP, h_KP` are finite on the same row for
   the envelope rates used below;
3. the required KP weight is `m>=0`;
4. `r_res^clean>=1`;
5. the AF tail can be restricted to any prescribed `g_*^2>0`;
6. the large-field source can be chosen with
   `sigma_lf^sharp>h_KP+m+delta` for the `delta` chosen below.

Put

```text
H:=h_KP+m.
```

For any `delta>0`, choose the finite-range covariance envelope

```text
mu_G(delta):=2(H+delta),
C_G(delta):=C_0 exp(2R_G(H+delta)),
C_E(delta):=C_E(mu_G(delta)).
```

Then, on this row,

```text
delta_clean(m)=delta
```

provided `sigma_lf^sharp>=H+delta`, and

```text
theta_delta(g_*)
 =
 e C_v^{row} C_0 exp(2R_G(H+delta)) C_E(delta) g_*^2,
```

```text
A_delta(g_*)
 =
 1+
 {C_v^{row} C_0 exp(2R_G(H+delta)) C_ent g_*^2
  \over
  1-theta_delta(g_*)},
```

```text
eta_delta(g_*)
 =
 C_KP A_delta(g_*)
 {exp(-delta r_res^clean)\over 1-exp(-delta)}.
```

Thus the actual clean KP decision for these source constants is:

```text
there exists delta>0 and a cofinal AF tail g_*
such that theta_delta(g_*)<1 and eta_delta(g_*)<1.
```

Moreover, under the six hypotheses above this decision always has a
constructive pass. Choose `delta>0` so large that

```text
2 C_KP {exp(-delta r_res^clean)\over 1-exp(-delta)} < 1.
```

Then choose the AF tail so that

```text
g_*^2
<=
min\left\{
 {1\over
  2e C_v^{row} C_0 exp(2R_G(H+delta)) C_E(delta)},
 {1\over
  2C_v^{row} C_0 exp(2R_G(H+delta)) C_ent}
\right\}.
```

For this choice,

```text
theta_delta(g_*)<=1/2,
\qquad
A_delta(g_*)<=2,
```

and therefore

```text
eta_clean(m)=eta_delta(g_*)<1.
```

Proof.

Theorem 9N.1P.1 gives the covariance edge estimate with
`mu_G=mu_G(delta)` and `C_G=C_G(delta)`. Since
`mu_G/2=H+delta=h_KP+m+delta`, and the large-field rate is at least
`H+delta`, the clean decay margin is exactly

```text
delta_clean(m)
=min(mu_G/2,sigma_lf^sharp)-h_KP-m
=delta
```

when the large-field rate is matched to the same lower bound, and is at
least `delta` if the large-field rate is larger. Substituting
`C_G(delta)` into Definition 9N.1K gives the displayed
`theta_delta`, `A_delta`, and `eta_delta`.

It remains to show that the inequality can be made strict. Because
`r_res^clean>=1`,

```text
{exp(-delta r_res^clean)\over 1-exp(-delta)}
```

tends to zero as `delta -> infinity`. Hence some `delta` satisfies the
displayed `2C_KP` inequality. The first AF-tail bound gives
`theta_delta(g_*)<=1/2`. The second gives

```text
{C_v^{row} C_0 exp(2R_G(H+delta)) C_ent g_*^2
 \over
 1-theta_delta(g_*)}
<=1,
```

so `A_delta(g_*)<=2`. The displayed choice of `delta` then gives
`eta_delta(g_*)<1`. Every constant used here is attached to the same
pushed-forward record law; the covariance rate is an envelope parameter for
a finite-range proof-coordinate covariance, not an extra ontic process.
`square`

### Corollary 9N.1Q.2: Finite Template Evaluation Of The Clean KP Threshold

Assume the hypotheses of Theorem 9N.1Q.1 and, in addition,
`HK-FIN-COUNT(Delta_B,L_ent,L_KP)` on the same row. Then the clean worksheet
may take

```text
h_KP=log(e Delta_B L_KP),
C_KP=1,
C_ent=1,
C_E(mu)=1/(1-Delta_B exp(-mu/2)).
```

For a required KP weight `m>=0`, put

```text
H:=log(e Delta_B L_KP)+m.
```

Choose any `delta>0` satisfying

```text
2 exp(-delta r_res^clean)/(1-exp(-delta))<1.
```

Then set

```text
mu_G=2(H+delta),
C_G=C_0 exp(2R_G(H+delta)),
C_E=1/(1-Delta_B exp(-(H+delta))).
```

Since `H+delta>log Delta_B`, this `C_E` is finite. If
`sigma_lf^sharp>=H+delta` and the AF tail is chosen so that

```text
g_*^2
<=
min\left\{
 {1\over
  2e C_v^{row} C_0 exp(2R_G(H+delta)) C_E},
 {1\over
  2C_v^{row} C_0 exp(2R_G(H+delta))}
\right\},
```

then

```text
theta_clean<1,
delta_clean(m)>0,
eta_clean(m)<1.
```

Thus the clean minimal branch proves

```text
HK-AN-SRC(m)
=> HK-AN-CLOSE(m)
=> AYM-AFRCE + AYM-KP
```

from the finite-template constants

```text
Delta_B,L_ent,L_KP,C_0,R_G,C_v^{row},r_res^clean,m
```

together with the large-field margin and cofinal AF tail.

If global finite prefactors `P_ent` or `P_KP` are retained in Theorem
9M.1E, replace the two displayed occurrences of `1` by those prefactors
and use Theorem 9N.1Q.1 without changing the logic.

Proof.

The constants are exactly those supplied by Corollary 9M.1F. Substituting
`mu_G=2(H+delta)` gives `mu_G/2=H+delta`, hence the edge sum is

```text
C_E(mu_G)
=
1/(1-Delta_B exp(-(H+delta))).
```

Because `H=log(e Delta_B L_KP)+m` and `Delta_B,L_KP>=1`, one has
`H+delta>log Delta_B`; therefore the edge sum is finite. The displayed
condition on `delta` is Theorem 9N.1Q.1 with `C_KP=1`; the displayed
condition on `g_*` is Theorem 9N.1Q.1 with `C_ent=1`. The conclusion is
Theorem 9N.1L. `square`

### Theorem 9N.1Q.3: Steps 1--5 Close The Clean Analytic Branch

Fix one frozen pushed-forward row `T_HK^std`. Assume:

1. **finite-template inputs:** `HK-FIN-COUNT(Delta_B,L_ent,L_KP)` holds,
   `r_res^clean>=1`, and the required KP weight is `m>=0`;
2. **finite-range covariance:** `HK-COV-FR-SRC(C_0,R_G)` holds on the same
   row;
3. **finite vertex source:** `HK-SF-YM2` holds on the same row, with
   finite vertex constant `C_v^{row}` equal to either `C_v^{YM2}` or the
   strict minimal constant `C_v^{YM2,min}`;
4. **large-field margin:** the finite-template large-field source can be
   run with any prescribed strict margin;
5. **clean counterterm row:** the nonlocal counterterm and scheme tail
   amplitudes are zero, as in Theorem 9K.2G;
6. **cofinal AF freedom:** the asymptotically-free tail can be restricted
   to any prescribed `g_*^2>0`.

Define

```text
H:=log(e Delta_B L_KP)+m.
```

Choose `delta>0` so that

```text
2 exp(-delta r_res^clean)/(1-exp(-delta))<1.
```

Set

```text
mu_G:=2(H+delta),
C_G:=C_0 exp(2R_G(H+delta)),
C_E:=1/(1-Delta_B exp(-(H+delta))),
sigma_lf^sharp:=H+delta.
```

Finally choose the AF tail so that

```text
g_*^2
<=
min\left\{
 {1\over
  2e C_v^{row} C_0 exp(2R_G(H+delta)) C_E},
 {1\over
  2C_v^{row} C_0 exp(2R_G(H+delta))}
\right\}.
```

Then the first five execution steps are closed:

```text
HK-SF-SRC with theta_clean<1,
HK-LF-CLOSE with sigma_lf^sharp>=H+delta,
HK-CT-CLOSE on the clean counterterm row,
HK-AN-RES-COMMON with the clean residual constants,
HK-KP-TEST(m) with eta_clean(m)<1.
```

Consequently,

```text
HK-AN-SRC(m)
=> HK-AN-CLOSE(m)
=> AYM-AFRCE + AYM-KP.
```

If the finite-range covariance source is imported through Theorem 9L.1C.2,
then the covariance constants may be taken as

```text
C_0=lambda_D^{-1},
R_G=R_blk.
```

Thus the clean analytic branch is reduced to the actual verification of the
finite-template row data

```text
Delta_B,L_ent,L_KP,lambda_D,R_blk,C_v^{row},r_res^clean,m
```

on one pushed-forward heat-kernel row.

Proof.

Item 1 and Corollary 9M.1F give the explicit counting constants
`C_KP=1`, `C_ent=1`, `h_KP=log(e Delta_B L_KP)`, and the displayed
`C_E`. Item 2 and Theorem 9N.1P.1 give the finite-range covariance envelope
with the displayed `mu_G` and `C_G`. Item 3 and Theorem 9L.1I give the
finite vertex part with `p=1` and `C_v=C_v^{row}`. Item 4 supplies the
large-field rate at least `H+delta`; item 5 removes nonlocal
counterterm/scheme amplitudes from the clean residual envelope.

Corollary 9N.1Q.2 now gives

```text
theta_clean<1,
delta_clean(m)>0,
eta_clean(m)<1.
```

Theorem 9N.1L converts these three scalar inequalities into
`HK-AN-SRC(m)`, Theorem 9N.1B gives `HK-AN-CLOSE(m)`, and Theorem 9N.2
exports `AYM-AFRCE + AYM-KP`. All constants are attached to the same
pushed-forward record law; the gauge chart, covariance, and collar
conditioning remain proof coordinates only. `square`

### Paper 16 Analytic Export Box

The clean finite-template analytic export of Paper 16 is:

```text
verified finite row-data on one T_HK^std
=> HK-AN-FINTPL-CLOSE(m)
=> HK-AN-CLOSE(m)
=> AYM-AFRCE + AYM-KP.
```

The finite row-data are exactly:

```text
Delta_B,L_ent,L_KP,lambda_D,R_blk,C_v^{row},r_res^clean,m.
```

No gauge-coordinate field, axial tree, covariance variable, or local scheme
coordinate is exported as ontology. Those objects only certify the scalar
finite-row constants above.

### Definition 9N.1Q.4: Finite-Template Analytic Certificate `HK-AN-FINTPL-CLOSE`

`HK-AN-FINTPL-CLOSE(m)` holds on a frozen pushed-forward row `T_HK^std`
when the following finite row-data have been verified on that same row.

| Row datum | Source certificate | Exported role |
| --- | --- | --- |
| `Delta_B` | maximum degree of the block graph in `HK-FIN-COUNT` | edge and connected-set counting |
| `L_ent` | finite small-field entropy label count in `HK-FIN-COUNT` | small-field/polymer entropy |
| `L_KP` | finite residual KP label count in `HK-FIN-COUNT` | `h_KP=log(e Delta_B L_KP)` |
| `lambda_D` | uniform Dirichlet/Poincare lower bound in the Paper-11 block-conditioned row | covariance norm `C_0=lambda_D^{-1}` |
| `R_blk` | finite collar-template covariance radius | covariance support radius `R_G=R_blk` |
| `C_v^{row}` | pushed-forward `HK-SF-YM2` vertex ledger | local vertex amplitude |
| `r_res^clean` | maximum of the clean small-field/counterterm starting radii | KP lower summation range |
| `m` | required Paper-15/Paper-19 residual KP weight | carried residual weight |

In addition, the row must use the clean counterterm convention of Theorem
9K.2G and a finite-template large-field source whose margin can be raised
to the value required by Theorem 9N.1Q.3.

### Theorem 9N.1Q.5: `HK-AN-FINTPL-CLOSE` Exports The Analytic Branch

If `HK-AN-FINTPL-CLOSE(m)` holds, then

```text
HK-AN-CLOSE(m)
=> AYM-AFRCE + AYM-KP.
```

More explicitly, `HK-AN-FINTPL-CLOSE(m)` supplies the hypotheses of Theorem
9N.1Q.3 with

```text
C_0=lambda_D^{-1},
R_G=R_blk,
h_KP=log(e Delta_B L_KP),
C_E(mu)=1/(1-Delta_B exp(-mu/2)).
```

Hence Theorem 9N.1Q.3 proves `HK-AN-SRC(m)`, Theorem 9N.1B proves
`HK-AN-CLOSE(m)`, and Theorem 9N.2 exports `AYM-AFRCE + AYM-KP`.

Proof.

The table in Definition 9N.1Q.4 is exactly the source list needed by
Theorem 9N.1Q.3. The finite counting data give the entropy and edge-count
constants; the Dirichlet and collar-template data give the finite-range
covariance source by Theorem 9L.1C.2; the pushed-forward `HK-SF-YM2` ledger
gives the vertex constant; the clean counterterm convention removes
nonlocal counterterm/scheme amplitudes; and the large-field source supplies
the chosen margin. Applying Theorems 9N.1Q.3, 9N.1B, and 9N.2 in order
gives the displayed export. `square`

### Corollary 9N.1R: Clean Worksheet Status After The Three Attacks

On the clean minimal row:

1. `theta_clean<1` is closed by AF tail selection once the same-row
   constants `C_v^{row},C_G,C_E` are finite;
2. `delta_clean(m)>0` is the genuine decay-vs-entropy source test

   ```text
   min(mu_G/2,sigma_lf^sharp)>h_KP+m;
   ```

   On the strict finite-range block-conditioned branch, Theorem 9N.1P.1
   closes this margin by choosing `mu_G>2(h_KP+m)` and
   `sigma_lf^sharp>h_KP+m`, at the cost of a larger amplitude.
3. `eta_clean(m)<1` is the exact range/amplitude test of Theorem 9N.1Q.
   Under the finite-range and finite-counting hypotheses of Theorem
   9N.1Q.1, and concretely under the finite-template constants of
   Corollary 9N.1Q.2, the test is constructively passed by first choosing
   `delta`, then choosing the cofinal AF tail `g_*`.

Thus the remaining actual computation is narrowed to:

```text
compute or import Delta_B,L_ent,L_KP,C_0,R_G,C_v^{row},r_res^clean,m,
choose delta with
  2 exp(-delta r_res^clean)/(1-exp(-delta))<1
  (or the prefactor version if C_KP!=1),
choose mu_G=2(log(e Delta_B L_KP)+m+delta),
choose sigma_lf^sharp>=log(e Delta_B L_KP)+m+delta,
choose the AF tail g_* below the bounds of Corollary 9N.1Q.2.
```

If `delta_clean(m)>0` holds but `eta_clean(m)>=1`, the next honest move is
not a new ontology. It is either sharper same-row constants or a
local-absorption certificate proving that all polymers below a larger
effective range have been absorbed into the declared local record ledger.

### Theorem 9N.2: `HK-AN-CLOSE` Gives `AYM-AFRCE` And `AYM-KP`

If `HK-AN-CLOSE(m)` holds, then:

```text
AYM-AFRCE
and
AYM-KP
```

hold for the actual heat-kernel analytic branch, with positive KP reserve
`1-eta_res^{bd}(m)`.

Proof.

`HK-SF-CLOSE` gives `HK-SF-GCD` by Theorem 9L.2. `HK-LF-CLOSE` gives
`HK-LFS` by Theorem 9J.2. `HK-CT-CLOSE` gives `HK-CTS` by Theorem 9K.2.
Theorem 9E.6 then gives `HK-LCB`, and Theorem 9D.3 gives `AYM-AFRCE`.

The compatible size-resolved constants in Definition 9N.1 give the residual
envelope required by Theorem 9M.2. Since `HK-KP-TEST(m)` holds, Theorem 9M.2
gives `AYM-KP` with reserve `1-eta_res^{bd}(m)`. The whole-process
compatibility clause ensures these are estimates on one record-law tower,
not a composition of separate subprocesses. `square`

### Theorem 9N.2A: Positive Residual Decay Export

Assume `HK-AN-CLOSE(m)`. Define the residual constants exported by
Definition 9N.1:

```text
A_res
 =
 (C_v C_G C_ent/(1-theta_sf) + A_tail + A_scheme) g_*^{2p}
 + 1,

mu_res
 =
 min(mu_G/2, mu_tail, mu_scheme, sigma_lf^sharp),

r_res = max(r_*,r_ct).
```

Then the Paper-19 residual-tail decay margin

```text
Delta_res := mu_res - h_KP - m
```

is strictly positive. Moreover, for every `r>=r_res`,

```text
sum_{n>=r}
 C_KP A_res exp(-(mu_res-h_KP-m)n)
 <=
 K_res exp(-Delta_res r),
```

where

```text
K_res :=
 C_KP A_res/(1-exp(-Delta_res)).
```

Thus `HK-AN-CLOSE(m)` exports the exact residual constants

```text
(A_res,mu_res,C_KP,h_KP,m,r_res,Delta_res,K_res)
```

needed by the Paper-19 cross-residual collar estimate.

Proof.

Clause 5 of `HK-AN-CLOSE(m)` is precisely `HK-KP-TEST(m)` with the
constants displayed above. By Definition 9M.1, `HK-KP-TEST(m)` includes

```text
mu_res > h_KP + m.
```

Therefore `Delta_res=mu_res-h_KP-m>0`. The tail estimate is the geometric
series

```text
sum_{n>=r}
 C_KP A_res exp(-Delta_res n)
 =
 C_KP A_res exp(-Delta_res r)/(1-exp(-Delta_res)).
```

The compatibility clause in Definition 9N.1 says these constants live on the
same heat-kernel whole-process record-law tower, so they can be exported to
Paper 19 without changing process, chart, or battery. `square`

### Corollary 9N.3: Analytic Branch Status

The analytic side of Paper 16 is now packaged as:

```text
HK-AN-SRC => HK-AN-CLOSE
=> AYM-AFRCE + AYM-KP.
```

In execution order:

```text
HK-SF-SRC with theta_sf<1
+ HK-LF-CLOSE with sigma_lf^sharp>h_poly
+ HK-CT-RATE => HK-CT-CLOSE
+ HK-AN-RES-COMMON common residual constants
+ eta_res^{bd}(m)<1
=> HK-AN-CLOSE(m).
```

Equivalently, the final KP scalar is

```text
D_0=mu_res-h_KP,
B_res=C_KP A_res,
eta_res^{bd}(m)
=B_res exp(-(D_0-m)r_res)/(1-exp(-(D_0-m)))<1.
```

The previous import remains:

```text
HK-AN-CLOSE => AYM-AFRCE + AYM-KP.
```

This is the clean import for the next Paper-15 and Paper-19 numerical gates.
Theorem 9N.2A additionally exports a positive residual decay margin
`Delta_res>0` and the scalar tail constant `K_res`. The remaining analytic
work is now ordered by Corollary 9N.1C. The first execution step is closed
by Corollary 9N.1E on any finite battery with a verified common-record
`HK-SF-YM2` import, including Paper 19's frozen `SEL_0` one-block battery.
The second execution step is closed by Corollary 9N.1F on the standard finite
block/collar heat-kernel tower:

```text
HK-LF-TPL
+ common heat-kernel metric
+ cofinal AF time cutoff
=> HK-LF-CLOSE with sigma_lf^sharp>h_poly.
```

The third execution step is closed by Corollary 9N.1G. On the clean minimal
row it is immediate by Theorem 9K.2G; otherwise it is closed by the
same-record counterterm rate audit:

```text
HK-CT-RATE
=> HK-CT-SRC
=> HK-CT-CLOSE with mu_tail>0 and mu_scheme>0.
```

The first five execution steps are closed on the clean finite-template
branch by Theorem 9N.1Q.3:

```text
HK-FIN-COUNT
+ HK-COV-FR-SRC
+ HK-SF-YM2
+ HK-LF-CLOSE at the chosen margin
+ clean HK-CT-CLOSE
+ cofinal AF tail
=> HK-AN-SRC(m)
=> HK-AN-CLOSE(m)
=> AYM-AFRCE + AYM-KP.
```

If `HK-COV-FR-SRC` is imported from Paper 11 through Theorem 9L.1C.2, the
remaining actual row data are exactly

```text
Delta_B,L_ent,L_KP,lambda_D,R_blk,C_v^{row},r_res^clean,m
```

on one pushed-forward heat-kernel row.

The fourth execution step is now a theorem: Corollary 9N.1H and Theorem
9N.1I assemble the common residual constants on the audited record law.
After that, Corollary 9N.1J leaves only the scalar KP decision. The
clean minimal version of that decision is the worksheet in Definition
9N.1K:

```text
theta_clean<1,
delta_clean(m)>0,
eta_clean(m)<1.
```

Theorem 9N.1L proves that these three inequalities are exactly the remaining
clean-branch pass conditions. Theorems 9N.1O, 9N.1P.1, and 9N.1Q.1 then
evaluate them on the finite-range finite-counting branch: choose the
covariance envelope rate, large-field margin, and cofinal AF tail in that
order. Corollary 9N.1M gives the matching falsifier when those finite-source
hypotheses are not available. The general-route falsifiers are listed in
Theorem 9N.1D.

## 9O. Character-Tail Gate `AYM-TAIL`

The next Paper-15 numerical gate is the decoration or character-tail margin.
For the heat-kernel trajectory this gate must be handled with a growing
finite representation battery. A fixed representation cutoff is not adequate
as `t_i -> 0`, because heat-kernel mass moves through higher representations
at the scale `C_2(lambda) ~ 1/t_i`.

### Definition 9O.1: Casimir Representation Battery

For `R>0`, define the finite Casimir battery

```text
Rep_R(SU(N)) = { lambda in Irrep(SU(N)) : C_2(lambda) <= R }.
```

At heat-kernel node `i`, a representation cutoff schedule is a choice

```text
R_i -> infinity
```

with `Rep_{R_i}` finite for each node. The character-tail record is the
portion of the declared character/decorated battery carried by
`lambda notin Rep_{R_i}`.

### Definition 9O.2: Heat-Kernel Representation Tail

For constants `q_ch>=0`, `a_ch>0`, define the heat-kernel representation tail

```text
Tail_ch(t,R)
 =
 sum_{lambda: C_2(lambda)>R}
 dim(lambda)^{q_ch} exp(-a_ch t C_2(lambda)).
```

The exponent `q_ch` records finite-battery products, Clebsch-Gordan
multiplicities, and local label overhead. The constant `a_ch` records the
available heat-kernel decay after all comparison inequalities have been
applied.

### Lemma 9O.3: Weyl-Casimir Tail Bound

For `SU(N)` and fixed `q_ch,a_ch`, there are constants

```text
C_W, nu_W, R_W, t_W > 0
```

such that, for `0<t<=t_W` and `R>=R_W/t`,

```text
Tail_ch(t,R)
 <=
 C_W t^{-nu_W} exp(-(a_ch/2) t R).
```

Proof.

Weyl's dimension formula and Casimir growth imply polynomial growth of the
weighted representation count: there are constants `C,s` such that the
number of irreducibles with `C_2(lambda) in [u,u+1]`, weighted by
`dim(lambda)^{q_ch}`, is at most `C(1+u)^s`. Hence

```text
Tail_ch(t,R)
 <=
 C sum_{n>=R} (1+n)^s exp(-a_ch t n).
```

For `R>=R_W/t`, the polynomial factor can be absorbed into
`exp((a_ch/2)t n)` uniformly in the tail, leaving a geometric/integral bound
of order `t^{-nu_W} exp(-(a_ch/2)tR)`. The constants depend on `N`,
`q_ch`, and `a_ch`, not on volume or the cutoff node. `square`

### Theorem 9O.4: Growing Finite Battery Makes The Character Tail Small

Fix a target `epsilon_ch in (0,1)`. If the cutoff schedule obeys

```text
R_i
 >=
 (2/(a_ch t_i))
 (nu_W log(1/t_i) + log(C_W/epsilon_ch)),
```

for all sufficiently fine nodes, then

```text
Tail_ch(t_i,R_i) <= epsilon_ch.
```

Proof.

Substitute the lower bound on `R_i` into Lemma 9O.3:

```text
C_W t_i^{-nu_W} exp(-(a_ch/2)t_i R_i)
 <=
 C_W t_i^{-nu_W}
 exp(-nu_W log(1/t_i)-log(C_W/epsilon_ch))
 =
 epsilon_ch.
```

`square`

### Definition 9O.5: Character-Tail Closure `HK-CH-CLOSE`

`HK-CH-CLOSE(epsilon_ch,C_dec)` holds when:

1. the declared growing representation battery satisfies Theorem 9O.4, so
   `Tail_ch(t_i,R_i)<=epsilon_ch`;
2. the finite-battery decoration map converts the raw representation tail
   into the Paper-15 character loss by

```text
eta_ch^{bd} <= C_dec epsilon_ch;
```

3. the same representation schedule is used in the block, decoration,
   surface, and Creutz records.

### Theorem 9O.6: Character-Tail Closure Gives The Character Loss Bound

If `HK-CH-CLOSE(epsilon_ch,C_dec)` holds, then

```text
eta_ch^{bd} <= C_dec epsilon_ch.
```

Proof.

This is clause 2 of Definition 9O.5, with clause 1 supplying the tail bound
and clause 3 ensuring the same finite-battery schedule is used in every
record family. `square`

## 9P. Assembled Decoration Margin

The Paper-15 decoration margin combines residual KP loss and character-tail
loss.

### Definition 9P.1: Decoration Closure Certificate `HK-DEC-CLOSE`

`HK-DEC-CLOSE(m,epsilon_ch,C_dec)` holds when:

1. `HK-AN-CLOSE(m)` holds, giving residual KP loss `eta_res^{bd}(m)`;
2. `HK-CH-CLOSE(epsilon_ch,C_dec)` holds;
3. the decoration margin is positive:

```text
eta_dec^{bd}
 =
 eta_res^{bd}(m) + C_dec epsilon_ch
 < 1.
```

### Theorem 9P.2: `HK-DEC-CLOSE` Proves `AYM-TAIL`

If `HK-DEC-CLOSE(m,epsilon_ch,C_dec)` holds, then the Paper-15
character-tail/decoration gate `AYM-TAIL` holds with positive reserve

```text
1 - eta_dec^{bd}.
```

Proof.

By Theorem 9N.2, `HK-AN-CLOSE(m)` gives `AYM-KP` and the residual loss
`eta_res^{bd}(m)`. By Theorem 9O.6, `HK-CH-CLOSE` gives
`eta_ch^{bd}<=C_dec epsilon_ch`. Clause 3 of Definition 9P.1 gives

```text
eta_dec^{bd}
 =
 eta_res^{bd}(m) + eta_ch^{bd}
 <=
 eta_res^{bd}(m) + C_dec epsilon_ch
 < 1.
```

This is the Paper-15 decoration smallness gate, with reserve
`1-eta_dec^{bd}`. `square`

### Corollary 9P.3: Character-Tail Branch Status

The character-tail branch is now packaged as:

```text
HK-DEC-CLOSE => AYM-TAIL.
```

The remaining work is to choose a growing representation schedule `R_i`,
prove the finite-battery decoration conversion constant `C_dec`, and keep the
same representation schedule compatible with surface and Creutz records.

## 9Q. Surface Reserve Gate `AYM-SURF`

The surface gate is the Paper-15 subcriticality reserve. It says that the
leading sheet suppression still beats surface entropy after analytic and
decoration losses are charged.

### Definition 9Q.1: Surface Reserve Certificate `HK-SURF-CLOSE`

`HK-SURF-CLOSE(kappa_sheet,h_surf,L_dec,R_surf,m,epsilon_ch,C_dec)` holds
when:

1. `HK-DEC-CLOSE(m,epsilon_ch,C_dec)` holds, with decoration loss
   `eta_dec^{bd}`;
2. the leading sheet coefficient has normalized sheet suppression
   `kappa_sheet`;
3. the number of admissible surface sheets of area `A` containing a fixed
   block is bounded by `C_surf exp(h_surf A)`;
4. decoration attachments reduce the sheet margin by at most
   `L_dec eta_dec^{bd}`;
5. analytic residual and collar transport errors reduce the sheet margin by
   at most `R_surf`;
6. the surface reserve is positive:

```text
M_SUB^{bd}
 =
 kappa_sheet - h_surf - L_dec eta_dec^{bd} - R_surf
 > 0.
```

The constants are normalized in the same block-area units as the Paper-15
surface-polymer expansion.

### Theorem 9Q.2: `HK-SURF-CLOSE` Proves `AYM-SURF`

If `HK-SURF-CLOSE` holds, then the Paper-15 surface-subcritical gate
`AYM-SURF` holds with reserve `M_SUB^{bd}`.

Proof.

The leading sheet contributes suppression `kappa_sheet` per block-area unit.
Surface entropy consumes `h_surf`. Decoration records consume at most
`L_dec eta_dec^{bd}` by clause 4, and analytic/collar transport consumes at
most `R_surf` by clause 5. Clause 6 states exactly that the remaining
subcriticality margin is positive. This is the Paper-15 condition
`M_SUB^{bd}>0`. `square`

### Corollary 9Q.3: Surface Branch Status

The surface gate is packaged as:

```text
HK-SURF-CLOSE => AYM-SURF.
```

The remaining work is to prove a leading sheet coefficient, a surface entropy
bound, and explicit loss constants in the same block units as the analytic
and decoration gates.

## 9R. Creutz Reserve Gate `AYM-CREUTZ`

The Creutz gate transports the surface reserve to a finite determining
Wilson-loop/Creutz battery. It is the last Paper-15 numerical positivity
gate before assembling positive `nCPSC`.

### Definition 9R.1: Creutz Reserve Certificate `HK-CREUTZ-CLOSE`

`HK-CREUTZ-CLOSE(M_SUB^{bd},L_bat,L_reg,L_vol,L_shape)` holds when:

1. `AYM-SURF` holds with surface reserve `M_SUB^{bd}`;
2. the finite Creutz battery extraction loses at most `L_bat`;
3. regulator and blocking transport to the Creutz record loses at most
   `L_reg`;
4. finite-volume/exhaustion defects lose at most `L_vol`;
5. loop-shape and cusp discretization defects lose at most `L_shape`;
6. the transported Creutz reserve is positive:

```text
M_15^{bd}
 =
 M_SUB^{bd} - L_bat - L_reg - L_vol - L_shape
 > 0.
```

All losses are evaluated on the same declared finite Creutz-character
battery and the same growing representation schedule used in `HK-DEC-CLOSE`.

### Theorem 9R.2: `HK-CREUTZ-CLOSE` Proves `AYM-CREUTZ`

If `HK-CREUTZ-CLOSE` holds, then the Paper-15 transported Creutz reserve gate
`AYM-CREUTZ` holds with reserve `M_15^{bd}`.

Proof.

Starting from the surface reserve `M_SUB^{bd}`, subtract the declared losses
for battery extraction, regulator/blocking transport, finite-volume
exhaustion, and loop-shape/cusp discretization. Clause 6 states that the
remaining transported reserve is positive. This is exactly the Paper-15 gate
`M_15^{bd}>0`. `square`

### Corollary 9R.3: Creutz Branch Status

The Creutz gate is packaged as:

```text
HK-CREUTZ-CLOSE => AYM-CREUTZ.
```

The remaining work is to bound the four transport losses for the actual
Creutz-character battery and to keep those bounds compatible with the
surface and decoration schedules.

## 9S. Positive `nCPSC` From Heat-Kernel Gates

We can now assemble the Paper-15 numerical certificate.

### Definition 9S.1: Heat-Kernel Positive Certificate `HK-NCPSC-CLOSE`

`HK-NCPSC-CLOSE` holds when all of the following are true on one cofinal
heat-kernel whole-process record-law tower:

1. `HK-AN-CLOSE(m)`;
2. `HK-DEC-CLOSE(m,epsilon_ch,C_dec)`;
3. `HK-SURF-CLOSE(kappa_sheet,h_surf,L_dec,R_surf,m,epsilon_ch,C_dec)`;
4. `HK-CREUTZ-CLOSE(M_SUB^{bd},L_bat,L_reg,L_vol,L_shape)`;
5. the same block/collar decomposition, growing representation schedule, and
   finite Creutz-character battery are used in all four certificates;
6. all constants are computed from the same pushed-forward laws `Gamma_i`.

### Theorem 9S.2: `HK-NCPSC-CLOSE` Proves Verified Positive `nCPSC`

If `HK-NCPSC-CLOSE` holds, then the actual heat-kernel trajectory has
verified positive `nCPSC`.

Proof.

By Theorem 9N.2, `HK-AN-CLOSE` gives `AYM-AFRCE` and `AYM-KP`. By Theorem
9P.2, `HK-DEC-CLOSE` gives `AYM-TAIL`, equivalently
`eta_dec^{bd}<1`. By Theorem 9Q.2, `HK-SURF-CLOSE` gives `AYM-SURF`, namely
`M_SUB^{bd}>0`. By Theorem 9R.2, `HK-CREUTZ-CLOSE` gives `AYM-CREUTZ`,
namely `M_15^{bd}>0`.

Clauses 5 and 6 of Definition 9S.1 supply the whole-process compatibility
row in Definition 9.1. Therefore every row of the actual `nCPSC`
verification ledger is proved on the same cofinal tower with compatible
constants. `square`

### Corollary 9S.3: Positive `nCPSC` Status

The Paper-15 numerical side is now packaged as:

```text
HK-NCPSC-CLOSE => verified positive nCPSC.
```

This still does not prove `AYM-CLOSE`; it proves the finite-battery
positivity package needed by Theorem 9.2. Continuum projectivity,
regulator/chart independence, RP/covariance transport, loop continuity, and
nontriviality remain separate `CYC` gates.

## 9T. Positive `X_15` Tower From Heat-Kernel Gates

The next lift is finite-battery, not yet continuum. It says that the
Paper-15 positive numerical certificate becomes the Paper-15 export tower
once the Paper-14 entry tower is on the same record-law family.

### Definition 9T.1: Heat-Kernel Export Closure `HK-X15-CLOSE`

`HK-X15-CLOSE` holds when:

1. Paper 14's `FBE` tower holds on the same cofinal heat-kernel tower
   `Gamma_i`;
2. `HK-NCPSC-CLOSE` holds on that tower;
3. the batteries, collars, restriction maps, and renormalized loop records
   used by `FBE` and `HK-NCPSC-CLOSE` are the same finite record batteries,
   not merely isomorphic after an undeclared change of coordinates;
4. all exported constants are evaluated from the same pushed-forward
   whole-process laws `Gamma_i`.

### Theorem 9T.2: `HK-X15-CLOSE` Proves A Positive `X_15` Tower

If `HK-X15-CLOSE` holds, then the heat-kernel actual trajectory has a
positive `X_15` tower.

Proof.

Clause 1 supplies the Paper-14 finite-block entry tower. Clause 2 gives
verified positive `nCPSC` by Theorem 9S.2. Clauses 3 and 4 supply the
compatibility rows needed to apply the Paper-15 export theorem on one
common record-law tower. Therefore the Paper-15 export package `X_15` is
defined with positive finite-battery constants on the heat-kernel tower.
`square`

### Corollary 9T.3: Export Status

The finite-battery export is now packaged as:

```text
HK-X15-CLOSE => positive X_15 tower.
```

This still does not assert projective continuum uniqueness, regulator
independence, or nontriviality. It gives the positive finite-battery input
for those continuum gates.

## 9U. Projectivity Gate `HK-PROJ-CLOSE`

The first continuum gate is projectivity. It asks whether the finite record
laws become one continuum record law when batteries are refined.

### Definition 9U.1: Heat-Kernel Projectivity Certificate `HK-PROJ-CLOSE`

Let `Pi_{i->j}` be the declared restriction map from the larger finite
battery `B_i` to the smaller finite battery `B_j`, with `j<=i`.
`HK-PROJ-CLOSE` holds when, for every fixed `j`, there are nonnegative
adjacent-shell defects `delta_{j,k}` and `delta^X_{j,k}` such that, for
`i>m>=j`,

```text
|| Pi_{i->j,*} Gamma_i - Pi_{m->j,*} Gamma_m ||_{op,j}
 <=
 sum_{k=m}^{i-1} delta_{j,k},

max_ell | c_i^ell restricted to B_j - c_m^ell restricted to B_j |
 <=
 sum_{k=m}^{i-1} delta^X_{j,k},

sum_{k>=j} (delta_{j,k}+delta^X_{j,k}) < infinity.
```

The displayed norm is the operational finite-battery norm. For finite
precision records it is ordinary total variation on the finite readout
space. For unbinned scalar loop records it is the declared bounded-cylinder
norm on the finite algebra generated by the battery. We keep the notation
`TV` because every laboratory readout version is finite precision.

Here `delta^X_{j,k}` bounds the one-shell drift of every finite list of
`X_15` constants after restriction to `B_j`. The maps `Pi_{i->j}` are
maps of declared records. They are not transition kernels between hidden
intermediate states.

### Theorem 9U.2: `HK-PROJ-CLOSE` Proves `AYM-PROJ`

If `HK-PROJ-CLOSE` holds, then the heat-kernel actual trajectory satisfies
the `AYM-PROJ` subcertificate.

Proof.

Fix a finite battery `B_j` and a bounded record observable `F` with
`||F||_infty<=1`. For `i>m>=j`,

```text
| E_{Gamma_i}[F o Pi_{i->j}]
  - E_{Gamma_m}[F o Pi_{m->j}] |
 <=
 sum_{k=m}^{i-1} delta_{j,k}.
```

The summable tail tends to zero as `m->infinity`, uniformly for `i>m`.
Hence the finite-battery expectations are Cauchy under refinement and have a
unique limit on each declared finite record algebra. The same argument with
`delta^X_{j,k}` proves that the positive `X_15` constants restrict
consistently on the same projective system. This is exactly the projectivity
clause in Definition 9A.3. `square`

### Corollary 9U.3: Projective Positive Tower

The heat-kernel finite-battery tower reaches the first continuum gate as:

```text
HK-X15-CLOSE + HK-PROJ-CLOSE
=> projective positive X_15 tower.
```

This is still not strong `CYC`; it has not yet transported regulator/chart
independence, reflection positivity, Euclidean covariance, loop continuity,
or nontriviality.

### Definition 9U.4: Concrete Heat-Kernel Projective Readout Scheme

A concrete heat-kernel projective readout scheme consists of:

1. a cofinal sequence `i_n=(a_n,L_n,beta_n,B_n)` with
   `a_n -> 0`, `L_n -> infinity`, and `B_n subset B_{n+1}`;
2. a countable list of continuum record labels
   `alpha=(C,rho,type,precision)`, where `C in Loop_adm`, `rho` is a finite
   representation label, and `type` records whether the readout is a loop,
   block character, Creutz, surface, decoration, or counterterm-ledger
   record;
3. for every `alpha in B_j` and every `i>=j`, a cutoff approximant
   `R_{i,alpha}` on the lattice `Lambda_{a_i,L_i}`;
4. renormalized records

```text
T_{i,alpha}
 =
 Z_{i,alpha} R_{i,alpha} + C_{i,alpha},
```

   where `Z_{i,alpha}` and `C_{i,alpha}` include the declared perimeter,
   cusp, block, and scheme counterterms for that record;
5. a finite readout map

```text
R_{i,B_j}^{op}
 =
 (Q_alpha(T_{i,alpha}))_{alpha in B_j},
```

   where `Q_alpha` is the declared finite-precision binning map, or the
   identity when the bounded-cylinder norm is used;
6. the restriction map `Pi_{i->j}` is coordinate deletion:

```text
Pi_{i->j}
  ( (x_alpha)_{alpha in B_i} )
 =
  (x_alpha)_{alpha in B_j}.
```

The finite readout law on `B_j` at cutoff `i` is

```text
Gamma_i^{B_j}
 =
 (R_{i,B_j}^{op})_* mu_i^{HK}.
```

With this convention,

```text
Pi_{i->j,*} Gamma_i = Gamma_i^{B_j}
```

exactly. The only nonzero projectivity defect is the cross-scale difference
between successive restricted laws `Gamma_k^{B_j}` and `Gamma_{k+1}^{B_j}`.

### Definition 9U.5: Generator Drift Envelope `HK-PROJ-DRIFT`

For a finite battery `B_j`, let `Alg_1(B_j)` be the unit ball of bounded
finite readout observables on `B_j`. The scheme satisfies
`HK-PROJ-DRIFT(A_proj,mu_proj,r_proj)` if, for every `j` and every `k>=j`,

```text
sup_{F in Alg_1(B_j)}
| E_{Gamma_{k+1}^{B_j}} F - E_{Gamma_k^{B_j}} F |
 <=
 A_proj(j) exp(-mu_proj d(k,j)) + r_proj(j,k),
```

where:

```text
sum_{k>=j} A_proj(j) exp(-mu_proj d(k,j)) < infinity,
sum_{k>=j} r_proj(j,k) < infinity,
r_proj(j,k) -> 0.
```

Here `d(i,j)` is the declared refinement distance, for example the number of
RG blocking steps between `a_j` and `a_i`. The remainder `r_proj` contains
only named operational defects: finite-volume exhaustion, loop-approximant
drift, perimeter/cusp counterterm drift, representation-tail truncation, and
finite precision refinement. It may not include an unnamed continuum
limit error.

### Definition 9U.6: `X_15` Constant Drift Envelope `HK-XDRIFT`

Let `c_i^ell` denote the finite list of `X_15` constants exported by node
`i` and needed on the smaller battery `B_j`. The tower satisfies
`HK-XDRIFT` when there are nonnegative adjacent-shell defects `x_{j,k}` such
that, for every `k>=j`,

```text
max_ell | c_{k+1}^ell restricted to B_j - c_k^ell restricted to B_j |
 <= x_{j,k},

sum_{k>=j} x_{j,k} < infinity,
x_{j,k} -> 0.
```

The constants include the residual envelope constants, KP margin,
decoration margin, surface reserve, Creutz reserve, and the finite
renormalization constants used to define the records.

### Theorem 9U.7: Concrete Projectivity Criterion

If the concrete readout scheme of Definition 9U.4 satisfies
`HK-PROJ-DRIFT` and `HK-XDRIFT`, then `HK-PROJ-CLOSE` holds with

```text
delta_{j,k}
 =
 A_proj(j) exp(-mu_proj d(k,j)) + r_proj(j,k),

delta^X_{j,k}
 =
 x_{j,k}.
```

Proof.

By Definition 9U.4, restriction from the larger battery to `B_j` is
coordinate deletion. Therefore

```text
Pi_{i->j,*} Gamma_i = Gamma_i^{B_j}
```

exactly. Applying `HK-PROJ-DRIFT` to the unit ball of the operational
finite-battery algebra gives

```text
|| Pi_{k+1->j,*} Gamma_{k+1} - Pi_{k->j,*} Gamma_k ||_{op,j}
 <=
 A_proj(j) exp(-mu_proj d(k,j)) + r_proj(j,k).
```

Summing this adjacent-shell bound from `m` to `i-1` gives the first defect in
Definition 9U.1. The summability and vanishing tail follow from the two
summability assumptions in Definition 9U.5. `HK-XDRIFT` supplies
`delta^X_{j,k}=x_{j,k}` with the required summability and vanishing tail.
Thus all clauses of `HK-PROJ-CLOSE` hold. `square`

### Corollary 9U.8: What Remains To Prove For Projectivity

The projectivity task is now concrete:

```text
concrete readout scheme
+ HK-PROJ-DRIFT
+ HK-XDRIFT
=> HK-PROJ-CLOSE
=> AYM-PROJ.
```

The exact projection part is solved by coordinate deletion on declared
records. The remaining hard part is proving the drift envelopes from the
actual heat-kernel RG ledger, including finite-volume, loop-approximant,
counterterm, representation-tail, and finite-precision losses.

### Definition 9U.9: Heat-Kernel Projective RG Ledger `HK-RG-PROJ-LEDGER`

For each fixed finite battery `B_j` and each refinement shell `k>=j`, define
the one-shell operational drift budget

```text
D_{j,k}^{law}
 =
 L_j^{rec}
 (
   eta_{locRG,k}^{B_j}
   + eta_{vol,j,k}
   + eta_{app,j,k}
   + eta_{ct,j,k}
   + eta_{rep,j,k}
   + eta_{prec,j,k}
 ).
```

The terms mean:

1. `eta_{locRG,k}^{B_j}`: Paper-11 local-RG residual on the finite record
   battery `B_j`;
2. `eta_{vol,j,k}`: finite-volume exhaustion defect for the supports in
   `B_j`;
3. `eta_{app,j,k}`: lattice/block loop-approximant drift;
4. `eta_{ct,j,k}`: perimeter, cusp, block, and scheme counterterm drift;
5. `eta_{rep,j,k}`: representation-tail or character-battery truncation
   drift;
6. `eta_{prec,j,k}`: finite-precision readout refinement drift;
7. `L_j^{rec}`: the finite Lipschitz constant of the readout algebra
   `Alg_1(B_j)` with respect to the listed generator drifts.

`HK-RG-PROJ-LEDGER` holds when:

```text
sup_{F in Alg_1(B_j)}
| E_{Gamma_{k+1}^{B_j}}F - E_{Gamma_k^{B_j}}F |
 <= D_{j,k}^{law},

sum_{k>=j} D_{j,k}^{law} < infinity
```

for every fixed `B_j`.

The local-RG term is the part supplied by the Paper-11 AF ledger when its
local-radius and defect-summability hypotheses hold. The other terms are the
explicit operational transports supplied or demanded by Papers 12--15. This
definition removes the circular phrase "projectivity defect" from the input:
projectivity will be the output of summing the named one-shell law drifts.

### Theorem 9U.10: `HK-RG-PROJ-LEDGER` Proves `HK-PROJ-DRIFT`

If `HK-RG-PROJ-LEDGER` holds and the budget admits a split

```text
D_{j,k}^{law}
 <=
 A_proj(j) exp(-mu_proj d(k,j)) + r_proj(j,k)
```

with

```text
sum_{k>=j} A_proj(j) exp(-mu_proj d(k,j)) < infinity,
sum_{k>=j} r_proj(j,k) < infinity,
```

then `HK-PROJ-DRIFT(A_proj,mu_proj,r_proj)` holds.

Proof.

The first displayed inequality in Definition 9U.9 is exactly the one-shell
drift estimate required in Definition 9U.5. The second displayed inequality
splits that one-shell estimate into the exponential drift part and the
named remainder. The two summability assumptions are precisely the
summability clauses of `HK-PROJ-DRIFT`. `square`

### Definition 9U.11: Heat-Kernel Constant Transport Ledger `HK-RG-XLEDGER`

For each fixed finite battery `B_j` and each refinement shell `k>=j`, define
the one-shell `X_15` constant drift budget

```text
D_{j,k}^{X}
 =
 L_j^{X}
 (
   D_{j,k}^{law}
   + eta_{FBE,j,k}
   + eta_{AFRCE,j,k}
   + eta_{KP,j,k}
   + eta_{tail,j,k}
   + eta_{surf,j,k}
   + eta_{Creutz,j,k}
   + eta_{ren,j,k}
 ).
```

Here `L_j^X` is a finite sensitivity constant for the finite list of
`X_15` constants restricted to `B_j`. The remaining terms track the one-shell
drift in the Paper-14/15 constants: finite-block entry, residual envelope,
KP margin, character-tail budget, surface reserve, Creutz reserve, and
renormalization constants.

`HK-RG-XLEDGER` holds when:

```text
max_ell | c_{k+1}^ell restricted to B_j - c_k^ell restricted to B_j |
 <= D_{j,k}^{X},

sum_{k>=j} D_{j,k}^{X} < infinity.
```

This ledger is meaningful only on a margin-preserving branch: the KP,
decoration, surface, and Creutz inequalities must stay away from their
critical boundaries by a positive finite-battery reserve. If a margin tends
to zero, `L_j^X` can blow up and `HK-XDRIFT` is not proved.

### Theorem 9U.12: `HK-RG-XLEDGER` Proves `HK-XDRIFT`

If `HK-RG-XLEDGER` holds, then `HK-XDRIFT` holds with

```text
x_{j,k}=D_{j,k}^{X}.
```

Proof.

The first displayed inequality in Definition 9U.11 is the one-shell
constant drift bound required in Definition 9U.6. The second displayed
inequality is exactly the summability clause. Therefore `HK-XDRIFT` holds.
`square`

### Theorem 9U.13: Projectivity From The Actual Heat-Kernel RG Ledger

Assume the concrete readout scheme of Definition 9U.4. If the actual
heat-kernel RG ledger satisfies `HK-RG-PROJ-LEDGER` and `HK-RG-XLEDGER` with
the summability split of Theorem 9U.10, then:

```text
HK-PROJ-DRIFT + HK-XDRIFT
=> HK-PROJ-CLOSE
=> AYM-PROJ.
```

Proof.

Theorem 9U.10 gives `HK-PROJ-DRIFT`. Theorem 9U.12 gives `HK-XDRIFT`.
Theorem 9U.7 gives `HK-PROJ-CLOSE`. Theorem 9U.2 gives `AYM-PROJ`.
`square`

### Honest Boundary 9U.14: What Has And Has Not Been Proved

The proof above closes the logical projectivity gap:

```text
actual heat-kernel one-shell RG drift ledger
+ actual heat-kernel one-shell X_15 constant ledger
=> projectivity.
```

It does not yet prove those two ledgers unconditionally for four-dimensional
continuum `SU(N)` Yang-Mills. Paper 11's AF summability theorem supplies the
local-RG residual part under its uniformity and defect-summability
hypotheses. Papers 12--15 supply the form of the counterterm, loop,
projection, tail, surface, and Creutz transports. The remaining constructive
work is to verify the displayed summable budgets for the actual heat-kernel
trajectory with margins that do not collapse.

## 9V. Regulator And Gauge-Chart Gate `HK-REG-CLOSE`

The second continuum gate is regulator and chart independence. In Barandes
terms, this is not a claim that unobserved gauge potentials are physically
primitive. It is a claim that different proof coordinates push forward to
the same finite record laws in the continuum limit.

### Definition 9V.1: Heat-Kernel Comparison Certificate `HK-REG-CLOSE`

Let `rho` range over declared comparison descriptions: Wilson plaquette
action, alternative heat-kernel scheme choices, gauge-fixing charts,
blocking choices, and finite collar refinements. For every finite battery
`B_j`, let `C_{k,rho}^{(j)}` be the declared comparison map from the
`rho`-description records to the heat-kernel records on `B_j`.

`HK-REG-CLOSE` holds when, for every fixed `j` and every declared `rho`,
there are nonnegative tail defects `delta_{j,k}^{rho}` and `d_{j,k}^{rho}` such
that:

```text
sup_{F in Alg(B_j), ||F||_infty<=1}
| E_{Gamma_k^{HK}}[F]
  - E_{Gamma_k^{rho}}[F o C_{k,rho}^{(j)}] |
 <= delta_{j,k}^{rho},

max_ell | c_{k,HK}^ell restricted to B_j
          - c_{k,rho}^ell transported to B_j |
 <= d_{j,k}^{rho},

sum_{k>=j} (delta_{j,k}^{rho}+d_{j,k}^{rho}) < infinity.
```

The term `d_{j,k}^{rho}` bounds the drift of the finite list of exported
renormalized constants, including residual, surface, Creutz, loop-shape, and
counterterm-ledger constants. All comparison maps must be record maps on
finite batteries. No comparison may use an undeclared divisible
partial-kernel story.

The heat-kernel coordinate is the primary comparison chart, not an ontology.
For two non-heat-kernel descriptions `rho` and `sigma`, common-refinement
comparison is obtained by transporting both to the heat-kernel records on
`B_j` and using the triangle inequality. Thus `HK-REG-CLOSE` is a
common-refinement statement, not a claim that a Wilson or gauge-fixed field
configuration equals a heat-kernel field configuration pointwise.

### Theorem 9V.2: `HK-REG-CLOSE` Proves `AYM-REG`

If `HK-REG-CLOSE` holds, then the heat-kernel actual trajectory satisfies
the `AYM-REG` subcertificate.

Proof.

For every finite record battery, the displayed finite-record comparison says
that the `rho`-description and the heat-kernel description have the same
continuum finite-record expectations after transport by the declared record
map `C_{k,rho}^{(j)}`. Summability prevents finite comparison errors from
accumulating along the cofinal tower. The `d_{j,k}^{rho}` bounds keep the
renormalized certificate constants in the same equivalence class. Pairwise
comparison between any two declared descriptions follows through the
heat-kernel common refinement. Therefore regulator, gauge-chart, and
blocking choices are proof-coordinate choices, not different primitive laws.
This is exactly `AYM-REG`. `square`

### Definition 9V.4: Concrete Regulator/Chart Comparison Scheme

A concrete regulator/chart comparison scheme consists of:

1. the heat-kernel primary readout maps `R_{k,B_j}^{HK,op}`;
2. for every declared comparison description `rho`, readout maps
   `R_{k,B_j}^{rho,op}` on the same finite labels `B_j`;
3. a finite record comparison map

```text
C_{k,rho}^{(j)}
 :
 image(R_{k,B_j}^{rho,op})
 -> image(R_{k,B_j}^{HK,op})
```

   built only from declared operations: coordinate identification of scalar
   closed-loop records, finite bin refinement/coarsening, counterterm
   reparametrization, blocking/collar re-expression, and gauge-chart
   averaging or gauge-invariant projection;
4. comparison laws

```text
Gamma_k^{rho,B_j}
 =
 (R_{k,B_j}^{rho,op})_* mu_k^{rho}.
```

The comparison map may depend on `k`, `rho`, and `B_j`, but it must be a map
of declared finite records. It may not use a hidden field-level identity as
an unrecorded bridge.

### Definition 9V.5: Regulator/Chart RG Comparison Ledger `HK-RG-REG-LEDGER`

For every fixed finite battery `B_j`, shell `k>=j`, and declared comparison
description `rho`, define

```text
D_{j,k}^{reg,rho}
 =
 L_j^{reg,rho}
 (
   eta_{act,j,k}^{rho}
   + eta_{chart,j,k}^{rho}
   + eta_{block,j,k}^{rho}
   + eta_{ctsch,j,k}^{rho}
   + eta_{vol,j,k}^{rho}
   + eta_{tail,j,k}^{rho}
   + eta_{prec,j,k}^{rho}
 ).
```

The terms mean:

1. `eta_{act,j,k}^{rho}`: action/regulator comparison defect, for example
   heat-kernel versus Wilson plaquette action after the declared finite
   scheme matching;
2. `eta_{chart,j,k}^{rho}`: gauge-chart or gauge-fixing transport defect
   after projection to scalar records;
3. `eta_{block,j,k}^{rho}`: blocking, collar, and finite-cell refinement
   defect;
4. `eta_{ctsch,j,k}^{rho}`: counterterm-scheme reparametrization defect;
5. `eta_{vol,j,k}^{rho}`: finite-volume and boundary defect;
6. `eta_{tail,j,k}^{rho}`: representation-tail or omitted-record defect;
7. `eta_{prec,j,k}^{rho}`: finite-readout precision defect;
8. `L_j^{reg,rho}`: the finite Lipschitz constant of `Alg_1(B_j)` under the
   declared comparison map.

`HK-RG-REG-LEDGER` holds when:

```text
sup_{F in Alg_1(B_j)}
| E_{Gamma_k^{HK,B_j}}F
  - E_{Gamma_k^{rho,B_j}}(F o C_{k,rho}^{(j)}) |
 <= D_{j,k}^{reg,rho},

sum_{k>=j} D_{j,k}^{reg,rho} < infinity.
```

This is where Wilson/heat-kernel universality, gauge-chart independence, and
blocking independence actually enter the proof. They are not assumed by
notation; they are finite-record comparison estimates.

### Theorem 9V.6: `HK-RG-REG-LEDGER` Gives The Law Part Of `HK-REG-CLOSE`

If `HK-RG-REG-LEDGER` holds for every declared `rho`, then the law-comparison
part of `HK-REG-CLOSE` holds with

```text
delta_{j,k}^{rho}=D_{j,k}^{reg,rho}.
```

Proof.

The displayed inequality in Definition 9V.5 is exactly the finite-record
comparison required in Definition 9V.1. The summability clause in Definition
9V.5 is exactly the summability clause for `delta_{j,k}^{rho}`. `square`

### Definition 9V.7: Regulator/Chart Constant Transport Ledger `HK-RG-REGX-LEDGER`

For every fixed finite battery `B_j`, shell `k>=j`, and declared comparison
description `rho`, define

```text
D_{j,k}^{regX,rho}
 =
 L_j^{regX,rho}
 (
   D_{j,k}^{reg,rho}
   + eta_{FBE,j,k}^{rho}
   + eta_{AFRCE,j,k}^{rho}
   + eta_{KP,j,k}^{rho}
   + eta_{tailX,j,k}^{rho}
   + eta_{surf,j,k}^{rho}
   + eta_{Creutz,j,k}^{rho}
   + eta_{renX,j,k}^{rho}
 ).
```

Here `L_j^{regX,rho}` is the finite sensitivity constant for the exported
`X_15` constants under the `rho` comparison. The ledger holds when:

```text
max_ell | c_{k,HK}^ell restricted to B_j
          - c_{k,rho}^ell transported to B_j |
 <= D_{j,k}^{regX,rho},

sum_{k>=j} D_{j,k}^{regX,rho} < infinity.
```

As with `HK-RG-XLEDGER`, this requires margin preservation. If a KP,
decoration, surface, or Creutz margin is transported through a near-critical
denominator, the sensitivity constant can blow up and regulator independence
is not proved.

### Theorem 9V.8: `HK-RG-REGX-LEDGER` Gives The Constant Part Of `HK-REG-CLOSE`

If `HK-RG-REGX-LEDGER` holds for every declared `rho`, then the constant
transport part of `HK-REG-CLOSE` holds with

```text
d_{j,k}^{rho}=D_{j,k}^{regX,rho}.
```

Proof.

The displayed bound in Definition 9V.7 is exactly the finite-list constant
comparison required in Definition 9V.1. Its summability is the required
summability of `d_{j,k}^{rho}`. `square`

### Theorem 9V.9: Regulator Independence From The Actual Heat-Kernel RG Ledger

Assume the concrete comparison scheme of Definition 9V.4. If the actual
trajectory satisfies `HK-RG-REG-LEDGER` and `HK-RG-REGX-LEDGER` for every
declared comparison description, then `HK-REG-CLOSE` holds and hence:

```text
HK-RG-REG-LEDGER + HK-RG-REGX-LEDGER
=> HK-REG-CLOSE
=> AYM-REG.
```

Proof.

Theorem 9V.6 supplies the law-comparison defects. Theorem 9V.8 supplies the
constant-transport defects. Hence all clauses of `HK-REG-CLOSE` hold.
Theorem 9V.2 then gives `AYM-REG`. `square`

### Honest Boundary 9V.10: What Has And Has Not Been Proved

The regulator/chart problem has now been reduced to finite-record comparison
ledgers:

```text
concrete comparison scheme
+ HK-RG-REG-LEDGER
+ HK-RG-REGX-LEDGER
=> HK-REG-CLOSE
=> AYM-REG.
```

This does not prove Wilson/heat-kernel universality, gauge-chart
independence, or blocking independence unconditionally. It states the exact
finite-record estimates needed to make those phrases legitimate in ISP
language. Failure of any summable comparison ledger is a typed obstruction,
not a matter of choosing friendlier continuum notation.

### Corollary 9V.11: First Continuum Export

The current strongest heat-kernel export is:

```text
HK-X15-CLOSE + HK-PROJ-CLOSE + HK-REG-CLOSE
=> regulator-independent projective positive X_15 tower.
```

The remaining `CYC` gates are `AYM-RP-COV`, `AYM-LC`, `AYM-NT`, and the
whole-process compatibility check `AYM-WP` across all the preceding
certificates.

## 9W. Reflection Positivity And Euclidean Covariance Gate

Once projectivity and regulator comparison are stated at the record-law
level, reflection positivity and covariance must also be transported at that
level. They are not extra structure on hidden fields.

### Definition 9W.1: Heat-Kernel RP/Covariance Certificate `HK-RPCOV-CLOSE`

`HK-RPCOV-CLOSE` holds when, for every fixed finite OS battery `B_j`, every
finite OS-positive record polynomial `F in Alg(B_j)`, and every Euclidean
motion `g` preserving the declared admissible loop class, there are
nonnegative defects `r_{j,k}` and `q_{j,k}(g)` such that:

```text
W_k^{HK}(theta F * F)
 >= - r_{j,k} ||F||^2,

| W_k^{HK}(g.F) - W_k^{HK}(F) |
 <= q_{j,k}(g) ||F||,

r_{j,k} -> 0,
q_{j,k}(g) -> 0,
sum_{k>=j} (r_{j,k}+q_{j,k}(g)) < infinity
```

after transport through the projective and regulator comparison maps of
`HK-PROJ-CLOSE` and `HK-REG-CLOSE`.

For lattice reflections exactly represented at cutoff before readout and
transport, the bare RP defect is zero. For
continuum rotations and translations represented only through lattice/block
approximants, `q_{j,k}(g)` includes approximant, boundary, blocking, and
renormalization-counterterm defects.

### Definition 9W.1A: Symmetric-Positive OS Readout

A finite OS battery `B_j` is symmetric-positive for the heat-kernel readout
if:

1. the battery is split into positive-time records and their reflected
   records by a declared lattice reflection `theta`;
2. every scalar counterterm multiplying a record is real, positive, and
   reflection symmetric:

```text
Z_{k,theta alpha}=Z_{k,alpha}>0,
C_{k,theta alpha}=theta C_{k,alpha};
```

3. perimeter and cusp counterterms depend only on unoriented perimeter and
   cusp-angle data, as in the Paper-12 symmetric-positive ledger;
4. finite-precision readout maps commute with reflection up to a declared
   defect `eta_{binRP,j,k}`;
5. the OS-positive test class is generated by finite polynomials `F` in the
   positive-time records.

This is an operational condition on readouts. It does not promote a
gauge-fixed field configuration to ontology.

### Lemma 9W.1B: Exact Heat-Kernel Cutoff RP Before Transport

For a symmetric-positive finite OS battery at cutoff `k`, the heat-kernel
lattice record functional satisfies

```text
W_k^{HK,bare}(theta F * F) >= 0
```

for every positive-time finite record polynomial `F`. After applying
symmetric-positive scalar counterterms and finite readout binning, one has

```text
W_k^{HK,ren}(theta F * F)
 >=
 - eta_{ctRP,j,k} ||F||^2
 - eta_{binRP,j,k} ||F||^2.
```

Proof.

The heat-kernel lattice action is reflection positive at finite cutoff for
the declared reflection, so the bare inequality is the standard finite
lattice OS inequality applied to the finite record polynomial `F`.

Symmetric-positive scalar counterterms multiply the OS Gram matrix by a
positive diagonal matrix and possibly add the declared counterterm-weighted
defect from Paper 12. Positive diagonal conjugation preserves
positive-semidefiniteness. The finite readout map is reflection-compatible up
to `eta_{binRP,j,k}`, so binning can only introduce the displayed defect.
`square`

### Definition 9W.1C: Reflection-Positivity Transport Ledger `HK-RP-LEDGER`

For every fixed finite OS battery `B_j` and shell `k>=j`, define

```text
D_{j,k}^{RP}
 =
 eta_{ctRP,j,k}
 + eta_{binRP,j,k}
 + eta_{projRP,j,k}
 + eta_{regRP,j,k}
 + eta_{volRP,j,k}.
```

The terms are:

1. `eta_{ctRP,j,k}`: Paper-12 counterterm-weighted RP defect;
2. `eta_{binRP,j,k}`: finite readout/binning reflection defect;
3. `eta_{projRP,j,k}`: projective transport loss from `HK-PROJ-CLOSE`;
4. `eta_{regRP,j,k}`: regulator/chart transport loss from `HK-REG-CLOSE`;
5. `eta_{volRP,j,k}`: finite-volume or reflection-plane buffer defect.

`HK-RP-LEDGER` holds when:

```text
W_k^{HK}(theta F * F)
 >= - D_{j,k}^{RP} ||F||^2,

sum_{k>=j} D_{j,k}^{RP} < infinity,
D_{j,k}^{RP} -> 0.
```

The exact heat-kernel cutoff contribution is zero. All nonzero terms are
transport/readout/counterterm losses.

### Theorem 9W.1D: `HK-RP-LEDGER` Gives The RP Half Of `HK-RPCOV-CLOSE`

If the symmetric-positive OS readout condition holds and `HK-RP-LEDGER`
holds, then the reflection-positivity clause of `HK-RPCOV-CLOSE` holds with

```text
r_{j,k}=D_{j,k}^{RP}.
```

Proof.

Lemma 9W.1B gives exact cutoff reflection positivity before declared
transport and bounds the counterterm/readout defects. The projective,
regulator, and finite-volume transports add exactly the remaining terms in
`D_{j,k}^{RP}`. The summability and vanishing tail are part of
`HK-RP-LEDGER`. This is precisely the first displayed inequality in
Definition 9W.1. `square`

### Definition 9W.1E: Admissible Euclidean Motion Ledger `Euc_adm`

For the finite heat-kernel readout tower, an admissible Euclidean motion
`g in Euc_adm` is one of:

1. an exact hypercubic lattice symmetry preserving the finite lattice,
   battery, reflection structure, and volume;
2. a continuum translation or rotation preserving `Loop_adm`, together with
   a declared sequence of lattice/block approximant maps `g_k` such that
   `g_k C_{k}` approximates `(gC)_k` for every loop in the fixed finite
   battery;
3. a finite composition of the preceding motions, with the defect budget
   obtained by summing the component budgets.

The action of `g` on finite record polynomials is the transported action on
declared scalar records:

```text
g.W_rho(C) = W_rho(gC),
```

with representation labels unchanged unless the battery explicitly contains
a declared representation relabeling. Gauge charts are not acted on as
ontology; only scalar records and their readout laws are compared.

### Definition 9W.1F: Euclidean-Invariant Counterterm/Readout Ledger

A finite battery has Euclidean-invariant counterterm/readout data for
`g in Euc_adm` when:

1. perimeter counterterms depend only on unoriented perimeter;
2. cusp counterterms depend only on unoriented cusp angles;
3. block and collar counterterms are transported by the declared block/collar
   comparison maps;
4. finite readout bins satisfy

```text
Q_alpha(T_{k,alpha}) transported by g
 =
 Q_{g alpha}(T_{k,g alpha})
```

   up to a declared defect `eta_{binCov,j,k}(g)`;
5. the loop approximant rule is equivariant up to a declared defect
   `eta_{appCov,j,k}(g)`.

These are exactly the operational conditions needed for the Paper-12
counterterm covariance theorem to apply on finite batteries.

### Definition 9W.1G: Euclidean-Covariance Transport Ledger `HK-COV-LEDGER`

For every fixed finite battery `B_j`, shell `k>=j`, and
`g in Euc_adm`, define

```text
D_{j,k}^{Cov}(g)
 =
 eta_{exactCov,j,k}(g)
 + eta_{appCov,j,k}(g)
 + eta_{binCov,j,k}(g)
 + eta_{ctCov,j,k}(g)
 + eta_{blockCov,j,k}(g)
 + eta_{projCov,j,k}(g)
 + eta_{regCov,j,k}(g)
 + eta_{volCov,j,k}(g).
```

The terms are:

1. `eta_{exactCov,j,k}(g)`: exact lattice symmetry defect, equal to zero for
   exact hypercubic symmetries of the cutoff law and battery;
2. `eta_{appCov,j,k}(g)`: loop/lattice approximant defect for continuum
   motions;
3. `eta_{binCov,j,k}(g)`: finite readout/binning covariance defect;
4. `eta_{ctCov,j,k}(g)`: Paper-12 counterterm-weighted covariance defect;
5. `eta_{blockCov,j,k}(g)`: blocking, collar, and finite-cell transport
   defect;
6. `eta_{projCov,j,k}(g)`: projective transport loss from `HK-PROJ-CLOSE`;
7. `eta_{regCov,j,k}(g)`: regulator/chart transport loss from
   `HK-REG-CLOSE`;
8. `eta_{volCov,j,k}(g)`: finite-volume boundary or motion-buffer defect.

`HK-COV-LEDGER` holds when:

```text
| W_k^{HK}(g.F) - W_k^{HK}(F) |
 <= D_{j,k}^{Cov}(g) ||F||,

sum_{k>=j} D_{j,k}^{Cov}(g) < infinity,
D_{j,k}^{Cov}(g) -> 0.
```

For exact hypercubic symmetries before readout and transport, the exact
cutoff contribution is zero. For genuine continuum rotations, all work is in
the approximant and transport terms.

### Theorem 9W.1H: `HK-COV-LEDGER` Gives The Covariance Half Of `HK-RPCOV-CLOSE`

If `g in Euc_adm`, the Euclidean-invariant counterterm/readout ledger holds,
and `HK-COV-LEDGER` holds, then the Euclidean-covariance clause of
`HK-RPCOV-CLOSE` holds with

```text
q_{j,k}(g)=D_{j,k}^{Cov}(g).
```

Proof.

For exact lattice symmetries, the finite heat-kernel law is invariant before
readout, so `eta_{exactCov,j,k}(g)=0`. For continuum Euclidean motions, the
declared approximant maps replace exact invariance by the approximant defect
`eta_{appCov,j,k}(g)`.

By Definition 9W.1F and the Paper-12 counterterm covariance theorem,
perimeter and cusp counterterms do not create a new covariance anomaly beyond
the counterterm-weighted defect `eta_{ctCov,j,k}(g)`. Binning, block/collar
transport, projectivity, regulator comparison, and finite-volume motion
buffers contribute exactly the remaining terms in `D_{j,k}^{Cov}(g)`.
Thus the displayed covariance bound in `HK-COV-LEDGER` is precisely the
second displayed inequality in Definition 9W.1, with a summable vanishing
tail. `square`

### Theorem 9W.1I: `HK-RP-LEDGER + HK-COV-LEDGER` Prove `HK-RPCOV-CLOSE`

Assume:

1. the symmetric-positive OS readout condition of Definition 9W.1A;
2. `HK-RP-LEDGER`;
3. `g in Euc_adm`;
4. the Euclidean-invariant counterterm/readout ledger of Definition 9W.1F;
5. `HK-COV-LEDGER`.

Then `HK-RPCOV-CLOSE` holds with

```text
r_{j,k}=D_{j,k}^{RP},
q_{j,k}(g)=D_{j,k}^{Cov}(g).
```

Proof.

Theorem 9W.1D proves the reflection-positivity clause of Definition 9W.1.
Theorem 9W.1H proves the Euclidean-covariance clause. The summability and
vanishing conditions for `r_{j,k}` and `q_{j,k}(g)` are exactly the
summability and vanishing conditions in the two ledgers. Hence
`HK-RPCOV-CLOSE` holds. `square`

### Theorem 9W.2: `HK-RPCOV-CLOSE` Proves `AYM-RP-COV`

If `HK-PROJ-CLOSE`, `HK-REG-CLOSE`, and `HK-RPCOV-CLOSE` hold, then the
heat-kernel actual trajectory satisfies `AYM-RP-COV`.

Proof.

For reflection positivity, take a fixed finite OS-positive test `F`. The
first displayed estimate gives a lower bound by `-r_{j,k}||F||^2`; when the
RP subledger is used, Theorem 9W.1D supplies this bound from exact
finite-cutoff RP plus the declared transport defects. Since `r_{j,k}->0`,
the limit functional is nonnegative on `theta F * F`.

For Euclidean covariance, the second displayed estimate gives equality in
the continuum limit for each declared finite motion and finite record test.
The summability condition makes the limit independent of the cofinal
refinement. This is exactly the reflection-positivity and Euclidean
covariance transport clause in `AYM-CLOSE`. `square`

## 9X. Loop-Continuity Gate

The loop-completion gate is where renormalized Wilson loops stop being only
finite battery records and become a controlled continuum test class.

### Definition 9X.1: Paper-12 Loop Metric Imported Into Paper 16

Paper 16 uses the Paper-12 admissible loop metric, with one normalization.
Inside a fixed admissible stratum, loops have the same number of labeled
cusps, the same cyclic order of smooth arcs, and the same representation
label. Let `d_adm` be the Paper-12 metric controlling:

1. uniform position of the constant-speed parametrization;
2. perimeter;
3. tangent variation on smooth arcs;
4. cusp-angle variation.

Set

```text
d_loop(C,C') = min(1,d_adm(C,C'))
```

inside a fixed stratum, and set `d_loop(C,C')=1` for loops in different
admissible strata. For a product or cumulant record

```text
alpha = ((C_1,rho_1),...,(C_m,rho_m))
```

use the tuple metric

```text
d_loop^{(m)}(alpha,alpha')
 =
 sum_{q=1}^m d_loop(C_q,C'_q).
```

The completion `Loop_comp` is only the metric completion of this declared
clean class. It does not add uncontrolled self-intersections, zero-angle
cusps, cusp accumulation, or tangent self-approaches. Those would require new
operational records and new counterterms.

### Definition 9X.1A: Paper-12 Loop-Modulus Package

For each finite Paper-16 battery `B_j`, the Paper-12 loop-modulus package
consists of:

1. calibrated perimeter and cusp counterterm ledgers;
2. product-bounded or cumulant-bounded renormalized loop records up to the
   product degree of `B_j`;
3. product smearing-removal consistency;
4. the AF loop-variation estimate of Paper 12 on the same finite loop
   stratum;
5. a finite-battery modulus

```text
omega_j(delta) = L_j delta + omega_j^tail(delta),
omega_j(delta) -> 0 as delta -> 0.
```

Here `L_j` is the maximum of the Paper-12 finite-battery constants over the
records in `B_j`, and `omega_j^tail` is the maximum of the Paper-12 tail
moduli after the perimeter and cusp singular pieces have been removed.

This is an import of Paper 12, Definition 5.1, Definition 5.4, Lemma 5.5, and
Theorem 5.6. It is not a new microscopic process and it does not compose
partial transition kernels. It is a statement about the pushed-forward
record law on the declared renormalized loop battery.

### Definition 9X.1B: Heat-Kernel Loop Modulus `HK-LOOP-MODULUS`

Fix `j`. For every record `T_alpha` in `B_j`, where `alpha` is either a
single loop or a finite product/cumulant tuple of loops, and for every
same-stratum comparison `alpha,alpha'`, define the level-`i` loop-continuity
defect by

```text
R_{j,i}^{LC}
 =
 sum_{k>=i} D_{j,k}^{LC}.
```

`HK-LOOP-MODULUS` holds when there are nonnegative adjacent-shell defects
`D_{j,k}^{LC}` with

```text
sum_{k>=j} D_{j,k}^{LC} < infinity
```

such that, for every `i>=j`,

```text
| E_{Gamma_i}(T_alpha^{ren})
  - E_{Gamma_i}(T_{alpha'}^{ren}) |
 <=
 omega_j(d_loop^{(m)}(alpha,alpha')) + R_{j,i}^{LC}.
```

For a one-loop record this is the usual Wilson-loop modulus. For products and
cumulants it is the same statement in the tuple metric. The expectations are
always taken against the whole pushed-forward law `Gamma_i`; no unobserved
intermediate kernel is being composed.

### Definition 9X.1C: Loop-Continuity Transport Ledger `HK-LC-TRANSPORT`

For `k>=j`, split the adjacent-shell loop-continuity defect as

```text
D_{j,k}^{LC}
 =
 eta_{P12,j,k}
 + eta_{appLC,j,k}
 + eta_{binLC,j,k}
 + eta_{perLC,j,k}
 + eta_{cuspLC,j,k}
 + eta_{smearLC,j,k}
 + eta_{projLC,j,k}
 + eta_{regLC,j,k}
 + eta_{volLC,j,k}.
```

The terms mean:

1. `eta_{P12,j,k}`: residual Paper-12 AF loop-variation and connected-tail
   loss after the declared finite-battery modulus `omega_j` is extracted;
2. `eta_{appLC,j,k}`: lattice or block approximant loss for replacing a
   continuum loop by its level-`k` representative;
3. `eta_{binLC,j,k}`: finite record binning and battery restriction loss;
4. `eta_{perLC,j,k}`: perimeter-counterterm transport loss;
5. `eta_{cuspLC,j,k}`: cusp or corner-counterterm transport loss;
6. `eta_{smearLC,j,k}`: smeared-to-unsmeared removal loss;
7. `eta_{projLC,j,k}`: projective transport loss from `HK-PROJ-CLOSE`;
8. `eta_{regLC,j,k}`: regulator and gauge-chart comparison loss from
   `HK-REG-CLOSE`;
9. `eta_{volLC,j,k}`: finite-volume and boundary-exhaustion loss.

`HK-LC-TRANSPORT` holds when every term is computed from the same cutoff law
and declared record maps, and

```text
sum_{k>=j} D_{j,k}^{LC} < infinity
```

for every fixed battery `B_j`.

### Definition 9X.1D: Heat-Kernel Loop-Continuity Certificate `HK-LC-CLOSE`

`HK-LC-CLOSE` holds when there is a declared loop metric `d_loop`, a
completion `Loop_comp`, finite-battery moduli `omega_j(delta)->0`, and
summable loop-continuity transport tails `R_{j,i}^{LC}` such that, for every
fixed battery `B_j`, every record tuple `alpha,alpha'` in the same admissible
stratum, and every `i>=j`,

```text
| E_{Gamma_i}(T_alpha^{ren})
  - E_{Gamma_i}(T_{alpha'}^{ren}) |
 <=
 omega_j(d_loop^{(m)}(alpha,alpha')) + R_{j,i}^{LC},

R_{j,i}^{LC} -> 0.
```

The preferred sufficient condition is the explicit `HK-LC-TRANSPORT` tail
above. The loop class excludes uncontrolled self-intersections, cusp
accumulation, and zero-angle degenerations unless new record counterterms are
explicitly added.

### Theorem 9X.1E: Paper-12 Modulus Plus Transport Gives `HK-LC-CLOSE`

Assume, for every fixed `B_j`:

1. the Paper-12 loop-modulus package holds;
2. `HK-LC-TRANSPORT` holds;
3. `HK-PROJ-CLOSE` and `HK-REG-CLOSE` use the same loop approximants,
   counterterm branches, and finite record maps.

Then `HK-LOOP-MODULUS` holds, and hence `HK-LC-CLOSE` holds with modulus
`omega_j` and tail `R_{j,i}^{LC}`.

Proof.

Paper 12 gives the renormalized loop modulus after perimeter/cusp
calibration, product-boundedness, smearing removal, and the AF loop-variation
estimate are imposed on a fixed finite loop battery. Transporting that bound
to the Paper-16 actual heat-kernel tower adds exactly the losses listed in
`HK-LC-TRANSPORT`: loop approximants, finite binning, perimeter and cusp
counterterms, smeared-to-unsmeared removal, projectivity, regulator/chart
comparison, and volume exhaustion.

The triangle inequality gives, at level `i`,

```text
| E_{Gamma_i}(T_alpha^{ren})
  - E_{Gamma_i}(T_{alpha'}^{ren}) |
 <=
 omega_j(d_loop^{(m)}(alpha,alpha'))
 + sum_{k>=i} D_{j,k}^{LC}.
```

The summability condition makes the tail tend to zero. This is exactly
`HK-LOOP-MODULUS`, which is the concrete form of `HK-LC-CLOSE`. `square`

### Theorem 9X.2: `HK-LC-CLOSE` Proves `AYM-LC`

If `HK-PROJ-CLOSE`, `HK-REG-CLOSE`, and `HK-LC-CLOSE` hold, then the
heat-kernel actual trajectory satisfies `AYM-LC`.

Proof.

For fixed `C,C'`, the displayed modulus is uniform on the cofinal tower up
to summable defects. The projective and regulator comparison gates ensure
that the same renormalized loop record is being compared at every node. In
the continuum limit the defect tail vanishes, leaving

```text
| W_infty(T_alpha) - W_infty(T_{alpha'}) |
 <=
 omega_j(d_loop^{(m)}(alpha,alpha')).
```

Therefore the countable admissible loop algebra extends uniquely to
`Loop_comp` by Theorem 7.2. This is exactly `AYM-LC`. `square`

## 9Y. Nontriviality Anchor Gate

Nontriviality must be tied to a record that survives the same transports as
the rest of the tower. A raw finite-lattice Creutz or Wilson-loop gap is not
enough unless every comparison loss is debited.

### Definition 9Y.1: Preferred Anchor Record

The preferred Paper-16 anchor is not a bare Wilson loop. It is a scalar
operational record extracted from a perimeter-canceling block-scale Creutz
battery.

Concretely, an anchor package consists of:

1. a fixed physical block scale `s_0`;
2. a nontrivial representation `rho`;
3. the four-loop Creutz battery

```text
Xi = (A,B,C,D)
```

   from Paper 13;
4. a positive block-scale Creutz margin, transported through the Paper-15
   connected-polymer/surface/decoration ledger;
5. the scalar loop-record extraction of Paper 13, Theorem 7.24 and Theorem
   7.33, producing one admissible scalar record `T_*` in the finite battery
   and a trivial reference value `T_triv(T_*)`.

The scalar extraction is important. `AYM-NT` is a statement about a continuum
Wilson-loop record functional, not about an unobserved sheet variable or a
hidden gauge-field configuration.

### Definition 9Y.1A: Paper-13/15 Anchor Package

The Paper-13/15 anchor package holds for `B_j` when one of the following
equivalent positive-reserve inputs has been verified on the same Creutz
battery and block scale:

1. Paper 13 gives a scale-resolved Creutz margin

```text
|Xi_infty| >= kappa_res c_0
```

   and hence a scalar anchor

```text
c_seed = kappa_res c_0 / (2(B_Xi+1)) > 0;
```

2. Paper 15 gives an explicit transported Creutz reserve

```text
M_15^{bd} > 0
```

   together with the declared scalar-anchor extraction constant
   `K_anc<infinity`, giving

```text
c_seed = K_anc M_15^{bd} > 0.
```

In either form, the output is a fixed finite scalar loop record `T_*`, a
trivial reference value `T_triv(T_*)`, and a positive seed reserve `c_seed`.
All three are finite-battery data.

### Definition 9Y.1B: Nontriviality Transport Ledger `HK-NT-TRANSPORT`

For the fixed anchor record `T_*`, define the total nontriviality transport
loss

```text
R_i^{NT}
 =
 R_{Creutz,i}^{NT}
 + R_{anch,i}^{NT}
 + R_{app,i}^{NT}
 + R_{bin,i}^{NT}
 + R_{ct,i}^{NT}
 + R_{loop,i}^{NT}
 + R_{proj,i}^{NT}
 + R_{reg,i}^{NT}
 + R_{vol,i}^{NT}.
```

The terms mean:

1. `R_{Creutz,i}^{NT}`: remaining Creutz/surface/decoration reserve loss not
   already absorbed into `c_seed`;
2. `R_{anch,i}^{NT}`: scalar-anchor extraction loss from the nonlinear
   Creutz margin to the chosen record `T_*`;
3. `R_{app,i}^{NT}`: loop-shape, lattice-approximant, or block-approximant
   loss;
4. `R_{bin,i}^{NT}`: finite battery and record-binning loss;
5. `R_{ct,i}^{NT}`: perimeter/cusp/counterterm-branch transport loss;
6. `R_{loop,i}^{NT}`: loop-continuity loss from `HK-LC-CLOSE`;
7. `R_{proj,i}^{NT}`: projective transport loss from `HK-PROJ-CLOSE`;
8. `R_{reg,i}^{NT}`: regulator and gauge-chart comparison loss from
   `HK-REG-CLOSE`;
9. `R_{vol,i}^{NT}`: finite-volume and boundary-condition exhaustion loss.

`HK-NT-TRANSPORT` holds when every term is evaluated on the same
pushed-forward cutoff law `Gamma_i`, the same record maps, and the same
counterterm branches, and

```text
R_i^{NT} -> 0.
```

The positive-reserve form of the ledger is the eventual inequality

```text
R_i^{NT} <= c_seed/2.
```

### Definition 9Y.1C: Heat-Kernel Nontriviality Certificate `HK-NT-CLOSE`

`HK-NT-CLOSE` holds when there is a fixed admissible scalar record `T_*`, a
trivial reference value `T_triv(T_*)`, a seed reserve `c_seed>0`, and a
transport loss `R_i^{NT}` satisfying `HK-NT-TRANSPORT` such that, on a
cofinal tail,

```text
| E_{Gamma_i}(T_*^{ren}) - T_triv(T_*) |
 >= c_seed - R_i^{NT},

c_*^{bd}
 =
 c_seed/2
 > 0.
```

Equivalently, after the positive-reserve form of `HK-NT-TRANSPORT` begins to
hold,

```text
| E_{Gamma_i}(T_*^{ren}) - T_triv(T_*) |
 >= c_*^{bd}.
```

The certificate is deliberately scalar. A surviving nonlinear Creutz
combination is admissible only after Paper 13's scalar-extraction step has
chosen at least one scalar Wilson-loop record separated from the trivial
functional.

### Theorem 9Y.1D: Creutz Reserve Plus Transport Gives `HK-NT-CLOSE`

Assume:

1. the Paper-13/15 anchor package holds with seed reserve `c_seed>0`;
2. `HK-NT-TRANSPORT` holds for the extracted scalar record `T_*`;
3. `HK-PROJ-CLOSE`, `HK-REG-CLOSE`, and `HK-LC-CLOSE` use the same anchor
   battery, loop approximants, counterterm branches, and pushed-forward laws.

Then `HK-NT-CLOSE` holds.

Proof.

The Paper-13/15 anchor package supplies a finite scalar loop record `T_*`
whose expected value is separated from the trivial value by `c_seed` before
the final Paper-16 transport losses are debited. The final losses are exactly
the terms in `R_i^{NT}`: residual Creutz/surface/decoration loss, scalar
extraction loss, loop approximant and binning loss, counterterm transport,
loop-continuity transport, projectivity, regulator/chart comparison, and
finite-volume exhaustion.

By the triangle inequality for the finite scalar record,

```text
| E_{Gamma_i}(T_*^{ren}) - T_triv(T_*) |
 >= c_seed - R_i^{NT}.
```

Since `R_i^{NT}->0`, on a cofinal tail `R_i^{NT}<=c_seed/2`. Thus
`HK-NT-CLOSE` holds with `c_*^{bd}=c_seed/2`. `square`

### Theorem 9Y.2: `HK-NT-CLOSE` Proves `AYM-NT`

If `HK-PROJ-CLOSE`, `HK-REG-CLOSE`, `HK-LC-CLOSE`, and `HK-NT-CLOSE` hold,
then the heat-kernel actual trajectory satisfies `AYM-NT`.

Proof.

`HK-NT-CLOSE` gives, on a cofinal tail,

```text
| E_{Gamma_i}(T_*^{ren}) - T_triv(T_*) | >= c_*^{bd}.
```

Projectivity and regulator/chart independence make the scalar anchor value a
Cauchy whole-process record value. Loop continuity makes the chosen
approximant independent of the admissible representative. Passing to the
continuum limit gives

```text
| W_infty(T_*) - T_triv(T_*) | >= c_*^{bd}.
```

The limit functional is therefore not the trivial Wilson-loop functional, by
Theorem 8.1. This is `AYM-NT`. `square`

## 9Z. Whole-Process Compatibility Gate

The final gate is an ontology audit. It prevents the proof from quietly
using mutually incompatible ledgers for different estimates.

### Definition 9Z.1: Common Heat-Kernel Closure Tower

The common heat-kernel closure tower is the data

```text
T_HK =
{
  i=(a_i,L_i,beta_i,B_i,Rep_i,Loop_i),
  Gamma_i,
  Pi_{i->j},
  Phi_i^rho,
  ell_i,
  Z_i,
  X_i,
  C_i
}.
```

Here:

1. `i` ranges over one cofinal directed family;
2. `Gamma_i` is the pushed-forward finite cutoff record law;
3. `Pi_{i->j}` are the declared restriction maps between finite batteries;
4. `Phi_i^rho` are the regulator, chart, blocking, and gauge-fixing
   comparison maps into the heat-kernel primary readout chart;
5. `ell_i` are the declared lattice/block approximants for continuum loops;
6. `Z_i` are the perimeter, cusp, counterterm, and finite-renormalization
   branches;
7. `X_i` denotes the finite `X_15` numerical certificate data;
8. `C_i` denotes all constants, margins, and defect ledgers used by the
   proof.

The tower is common when the following compatibility conditions hold:

1. `B_i`, `Rep_i`, and `Loop_i` are nested and cofinal in the declared
   record algebra;
2. `Pi_{i->j}` restricts records by declared coordinate deletion or by the
   declared finite comparison map, never by an implicit conditional process;
3. the loop approximants `ell_i`, counterterm branches `Z_i`, and comparison
   maps `Phi_i^rho` are the same objects in every certificate that mentions
   them;
4. every constant in `C_i` is computed from `Gamma_i`, the declared maps, and
   finite deterministic readout data.

### Definition 9Z.2: Whole-Process Compatibility Ledger `HK-WP-LEDGER`

`HK-WP-LEDGER` holds when every Paper-16 certificate uses the common tower
`T_HK` as follows:

| Certificate | Required shared data |
| --- | --- |
| `HK-X15-CLOSE` | `B_i`, `Rep_i`, `Loop_i`, `X_i`, and the finite record readouts |
| `HK-PROJ-CLOSE` | the same `Gamma_i`, `B_i`, and restriction maps `Pi_{i->j}` |
| `HK-REG-CLOSE` | the same comparison maps `Phi_i^rho`, counterterms `Z_i`, and readout batteries |
| `HK-RPCOV-CLOSE` | the same OS batteries, Euclidean-motion approximants, counterterms, and record maps |
| `HK-LC-CLOSE` | the same loop approximants `ell_i`, counterterms `Z_i`, and Paper-12 loop metric |
| `HK-NT-CLOSE` | the same Creutz battery, scalar anchor record, loop approximants, counterterms, and comparison maps |

The ledger also requires that a loss appearing in two certificates has one
declared value. It cannot be spent once in a positivity margin and then
silently replaced by a sharper unrelated estimate in a later transport
step.

### Definition 9Z.3: No-Hidden-Divisibility Clause

The no-hidden-divisibility clause holds when every estimate in Paper 16 is a
statement about:

1. expectations under `Gamma_i`;
2. finite pushforwards of `Gamma_i`;
3. deterministic restriction or comparison maps applied to those record laws;
4. limits of such finite record laws.

It forbids proofs that introduce an unrecorded partial kernel
`K_{i->m}` and then compose it as though the whole process were Markovian,
divisible, or conditionally independent. Gauge-fixed fields, small/large
field splits, polymer expansions, charts, and covariance decompositions may
appear only as proof coordinates for inequalities about the same
pushed-forward record laws.

### Definition 9Z.4: Heat-Kernel Whole-Process Certificate `HK-WP-CLOSE`

`HK-WP-CLOSE` holds when:

1. the common heat-kernel closure tower `T_HK` is fixed;
2. `HK-WP-LEDGER` holds for all certificates from `HK-X15-CLOSE` through
   `HK-NT-CLOSE`;
3. the no-hidden-divisibility clause holds;
4. all constants and margins in the compact ledger are attached to `T_HK`;
5. all finite-volume, regulator/chart, projective, loop, counterterm,
   covariance, and nontriviality losses are assigned to exactly one declared
   ledger entry or explicitly shared with the same value.

### Theorem 9Z.5: `HK-WP-CLOSE` Proves `AYM-WP`

If `HK-WP-CLOSE` holds, then the heat-kernel actual trajectory satisfies
`AYM-WP`.

Proof.

Definition 9Z.1 fixes the single cofinal family

```text
i=(a_i,L_i,beta_i,B_i,Rep_i,Loop_i)
```

and the single family of pushed-forward laws `Gamma_i`. Definition 9Z.2
checks that the projectivity, regulator, RP/covariance, loop-continuity, and
nontriviality certificates all use the same batteries, maps, counterterm
branches, loop approximants, and constants. Definition 9Z.3 rules out hidden
composition of unrecorded partial kernels.

Therefore every clause of `AYM-CLOSE` is evaluated on one whole-process
record law and one declared readout ledger. This is exactly the
whole-process compatibility clause `AYM-WP`. `square`

## 9AA. Heat-Kernel Strong `CYC` Assembly

The named heat-kernel gates now assemble into a single closure certificate.

### Definition 9AA.1: Heat-Kernel Continuum Closure `HK-CYC-CLOSE`

`HK-CYC-CLOSE` holds when all of the following hold on one cofinal
heat-kernel tower:

1. `HK-X15-CLOSE`;
2. `HK-PROJ-CLOSE`;
3. `HK-REG-CLOSE`;
4. `HK-RPCOV-CLOSE`;
5. `HK-LC-CLOSE`;
6. `HK-NT-CLOSE`;
7. `HK-WP-CLOSE`.

### Theorem 9AA.2: `HK-CYC-CLOSE` Proves `AYM-CLOSE` And Strong `CYC`

If `HK-CYC-CLOSE` holds, then the heat-kernel actual trajectory satisfies
`AYM-CLOSE` and therefore strong `CYC`.

Proof.

`HK-X15-CLOSE` gives a positive `X_15` tower by Theorem 9T.2.
`HK-PROJ-CLOSE` gives summable projectivity by Theorem 9U.2. The finite
volume part is included in the declared losses of `HK-REG-CLOSE`,
`HK-LC-CLOSE`, and `HK-NT-CLOSE`; if volume exhaustion is handled by a
separate ledger, it is an explicit subrow of those losses. `HK-REG-CLOSE`
gives regulator and chart independence by Theorem 9V.2. `HK-RPCOV-CLOSE`
gives reflection positivity and Euclidean covariance by Theorem 9W.2.
`HK-LC-CLOSE` gives loop continuity by Theorem 9X.2. `HK-NT-CLOSE` gives a
nontriviality anchor by Theorem 9Y.2. `HK-WP-CLOSE` gives whole-process
compatibility by Theorem 9Z.5.

By Definition 9B.1 and Theorem 9B.2, these named subcertificates are exactly
the clauses of `AYM-CLOSE`, evaluated on one common heat-kernel tower. Thus
`AYM-CLOSE` holds. Theorem 9A.5 then gives strong `CYC`. `square`

### Corollary 9AA.3: Heat-Kernel Route To `CYM_WL`

If `HK-CYC-CLOSE` holds, then `CYM_WL` holds.

Proof.

Theorem 9AA.2 gives the chain

```text
HK-CYC-CLOSE
=> AYM-CLOSE
=> strong CYC.
```

Theorem 10.1 gives `CYM_WL`. `square`

## 10. Main Closure Theorems

### Definition 10.0: `CYM_WL`

`CYM_WL` denotes a nontrivial, gauge-invariant, reflection-positive,
Euclidean-covariant, loop-continuous continuum Wilson-loop functional on the
declared pure `SU(N)` loop class.

### Theorem 10.1: Strong Closure

If:

1. Paper 14's `FBE` tower holds;
2. verified positive `nCPSC` holds on the actual continuum trajectory;
3. the resulting `X_15` tower satisfies strong `CYC`;

then `CYM_WL` holds.

Proof.

Theorem 9.2 gives a positive `X_15` tower. Strong `CYC` gives the continuum
functional by Theorem 5.1. Reflection positivity, Euclidean covariance, and
gauge invariance follow from Theorems 6.1--6.3. Loop-continuity gives the
declared completion by Theorem 7.2. Nontriviality follows from Theorem 8.1.
Thus all clauses of `CYM_WL` hold. `square`

### Theorem 10.1A: Actual-Trajectory Closure

If actual `4D SU(N)` Yang-Mills satisfies `AYM-CLOSE`, then `CYM_WL` holds.

Proof.

Corollary 9A.6 gives verified positive `nCPSC`, a positive `X_15` tower, and
strong `CYC`. Theorem 10.1 then gives `CYM_WL`. `square`

### Theorem 10.2: Weak/Subsequential Closure

If the hypotheses of Theorem 10.1 hold only along a cofinal subsequence, then
there is a subsequential `CYM_WL` functional. If two such subsequences give
different values on some Wilson-loop record, then the actual trajectory has
a non-uniqueness obstruction rather than a unique continuum Yang-Mills
functional.

Proof.

Theorem 5.2 constructs subsequential functionals. If two limits disagree on
a record, uniqueness on the declared continuum path fails. `square`

### Corollary 10.3: Conditional Nonperturbative Yang-Mills Reconstruction

The V3 papers 11--16 prove the following conditional reconstruction:

```text
Paper-11/12 AF local-polymer ledgers
+ Paper-14 FBE tower
+ verified positive Paper-15 nCPSC
+ strong CYC
=> CYM_WL.
```

Equivalently, after Section 9A, the same reconstruction can be stated as:

```text
AYM-CLOSE => CYM_WL.
```

This is a rigorous ISP record-law route to a continuum-facing pure
`SU(N)` Yang-Mills Wilson-loop functional, conditional on the named
nonperturbative inputs.

## 11. Obstruction Ledger

If Paper 16 fails, it fails in one of the following typed ways:

1. **Paper-14 entry obstruction:** no compatible `FBE` tower.
2. **`AFRCE` obstruction:** residual connected cumulants fail the
   coefficient-normalized decay envelope.
3. **KP entropy obstruction:** `eta_res^{bd}` does not stay below `1`.
4. **Character-tail obstruction:** non-leading characters consume the
   decoration margin.
5. **Surface obstruction:** `M_SUB^{bd}<=0`.
6. **Creutz obstruction:** `M_15^{bd}<=0`.
7. **Projectivity obstruction:** finite tower nodes do not define a unique
   continuum functional.
8. **RP/covariance obstruction:** reflection positivity or Euclidean
   covariance defects do not vanish.
9. **Loop-completion obstruction:** admissible loop continuity fails.
10. **Triviality obstruction:** every anchor collapses to the trivial
    functional.
11. **Whole-process obstruction:** the constants depend on regulator,
    gauge-chart, or an undeclared partial-kernel decomposition.

Each obstruction is a statement about records and finite-battery functionals.
None is repaired by reinterpreting residuals as virtual particles.

## 12. What Paper 16 Does And Does Not Finish

Paper 16 finishes the V3 reconstruction logic up to the named closure
certificate:

```text
verified positive nCPSC + strong CYC => CYM_WL.
```

It also reduces the actual-trajectory version to one named constructive
certificate:

```text
AYM-CLOSE => CYM_WL.
```

It does not finish:

1. the unconditional proof of verified positive `nCPSC`;
2. mass gap;
3. confinement;
4. QCD with matter;
5. gravity or stress-energy geometry reconstruction.

Those become the next papers only after the `CYM_WL` gate is secured or its
obstruction is identified.

## 13. Paper-17 Export

There are now two clean export levels.

If Theorem 10.1 holds, Paper 17 may import the full continuum package:

```text
CYM_WL,
W_infty,
reflection positivity,
Euclidean covariance,
loop continuity,
nontrivial Wilson-loop anchor,
X_15 tower,
obstruction-free CYC ledger.
```

Paper 17 may not assume a mass gap. It must prove a spectral/decay gate from
the reconstructed Wilson-loop functional and its OS representation.

If only the heat-kernel workbench has been discharged through Corollary
9V.11, Paper 17 may import only the finite/projective regulator-independent
record package:

```text
HK-X15-CLOSE,
HK-PROJ-CLOSE,
HK-REG-CLOSE,
regulator-independent projective positive X_15 tower,
open RP/covariance, loop-continuity, nontriviality, and whole-process gates.
```

In that weaker export mode, Paper 17 is not a mass-gap paper yet. It is a
continuum-completion paper whose first task is to close the remaining `CYC`
gates.

If `HK-CYC-CLOSE` has been discharged but no spectral/decay theorem has been
proved, Paper 17 may import:

```text
CYM_WL from the heat-kernel route,
W_infty,
projective regulator-independent positive X_15 tower,
reflection positivity,
Euclidean covariance,
loop continuity,
nontriviality anchor,
whole-process compatibility.
```

That is the right input for a mass-gap program, but it is still not a mass
gap.

## 13A. Compact Gate Ledger

This ledger is a map of reductions, not a declaration that actual
four-dimensional `SU(N)` Yang-Mills has been constructed. A row marked
`proved` means Paper 16 proves the implication once the named hypotheses are
verified on the common heat-kernel tower `T_HK`. The hard analytic burden is
the final column.

| Stage | Gate | Paper-16 result | Actual-trajectory burden |
| --- | --- | --- | --- |
| finite cutoff | `AYM-LAW` | proved at finite cutoff for standard heat-kernel/Wilson-type RP actions | none at the finite node |
| analytic branch | `HK-LF-SRC => HK-LF-CLOSE => HK-LFS` | proved and closed for standard finite block/collar heat-kernel templates by Theorem 9J.8 | verify the common finite-template ledger `HK-LF-TPL`, common heat-kernel metric, and cofinal AF time cutoff |
| analytic branch | `HK-CT-RATE => HK-CT-SRC => HK-CT-CLOSE => HK-CTS` | proved as same-record counterterm source theorem; clean minimal row gives zero tail amplitudes | adopt the clean minimal row or verify positive exponential rates for any nonempty irrelevant/scheme tails |
| analytic branch | `HK-SF-CLOSE => HK-SF-GCD` | proved as small-field reduction; finite-range covariance source is isolated as `HK-COV-FR-SRC(C_0,R_G)` and imported from Paper 11 under the uniform Dirichlet/collar-template hypotheses | verify `lambda_D>0`, finite `R_blk`, and common-record `HK-SF-YM2` on the chosen row |
| analytic branch | `HK-AN-RES-COMMON` | proved as common residual-constant assembly theorem | supply the audited small-field, large-field, and counterterm constants on the same tower |
| analytic branch | clean minimal KP worksheet | proved as exact scalar reduction; finite-template constants close `theta_clean<1`, `delta_clean(m)>0`, and `eta_clean(m)<1` by Corollary 9N.1Q.2 and Theorem 9N.1Q.3 | verify finite same-row `Delta_B,L_ent,L_KP,lambda_D,R_blk,C_v^{row},r_res^clean,m` |
| analytic branch | `HK-AN-FINTPL-CLOSE(m)` | proved as the compact finite-template analytic export theorem | verify the finite-template row data in Definition 9N.1Q.4 on the actual heat-kernel tower |
| analytic branch | `HK-KP-TEST => AYM-KP` | proved as threshold theorem | supply size-resolved constants with `eta_res^{bd}<1` |
| analytic branch | `HK-AN-CLOSE => AYM-AFRCE + AYM-KP` | proved as assembled analytic branch theorem; clean finite-template branch closes the first five execution steps by Theorem 9N.1Q.3 | verify the finite-template row data on the actual heat-kernel tower |
| numerical positive branch | `HK-DEC-CLOSE => AYM-TAIL` | proved as character-tail/decoration theorem | choose growing `Rep_{R_i}` and prove `C_dec` compatibly with surface/Creutz records |
| numerical positive branch | `HK-SURF-CLOSE => AYM-SURF` | proved as surface-reserve theorem | prove leading sheet coefficient, surface entropy bound, and loss constants |
| numerical positive branch | `HK-CREUTZ-CLOSE => AYM-CREUTZ` | proved as transported Creutz-reserve theorem | bound battery, regulator, volume, and loop-shape losses |
| numerical positive branch | `HK-NCPSC-CLOSE => verified positive nCPSC` | proved as assembled numerical certificate theorem | prove analytic, decoration, surface, Creutz, and compatibility certificates together |
| finite export | `HK-X15-CLOSE => positive X_15 tower` | proved as finite-battery export theorem | prove Paper-14 `FBE` and `HK-NCPSC-CLOSE` on one common tower |
| projectivity | `HK-RG-PROJ-LEDGER => HK-PROJ-DRIFT` | proved as one-shell law-drift summability theorem | verify local-RG, volume, approximant, counterterm, representation-tail, and precision budgets |
| projectivity | `HK-RG-XLEDGER => HK-XDRIFT` | proved as one-shell constant-drift summability theorem | verify finite sensitivity of `X_15` constants and margin preservation |
| projectivity | `HK-PROJ-CLOSE => AYM-PROJ` | proved as projectivity reduction | prove the law-drift and constant-drift ledgers on the actual heat-kernel trajectory |
| regulator/chart | `HK-RG-REG-LEDGER => law part of HK-REG-CLOSE` | proved as finite-record comparison reduction | verify action, chart, blocking, counterterm-scheme, volume, tail, and precision defects |
| regulator/chart | `HK-RG-REGX-LEDGER => constant part of HK-REG-CLOSE` | proved as constant-transport reduction | verify finite sensitivity of transported `X_15` constants and margin preservation |
| regulator/chart | `HK-REG-CLOSE => AYM-REG` | proved as regulator/chart reduction | prove both regulator comparison ledgers on the actual trajectory |
| RP/covariance | `HK-RP-LEDGER => RP half of HK-RPCOV-CLOSE` | proved as exact cutoff RP plus symmetric-positive transport theorem | verify counterterm, binning, projectivity, regulator, and volume RP defects are summable |
| RP/covariance | `HK-COV-LEDGER => covariance half of HK-RPCOV-CLOSE` | proved as Euclidean-invariant counterterm/readout transport theorem | verify approximant, binning, counterterm, block, projective, regulator, and volume covariance defects |
| RP/covariance | `HK-RP-LEDGER + HK-COV-LEDGER => HK-RPCOV-CLOSE` | proved as RP/covariance assembly theorem | prove both ledgers on one common heat-kernel tower |
| RP/covariance | `HK-RPCOV-CLOSE => AYM-RP-COV` | proved as RP/covariance transport reduction | prove the RP and covariance ledgers on the actual trajectory |
| loop continuity | `Paper-12 loop package + HK-LC-TRANSPORT => HK-LC-CLOSE` | proved as loop-modulus transport theorem | verify AF loop-variation, smearing removal, counterterm, projective, regulator, and volume defects on one tower |
| loop continuity | `HK-LC-CLOSE => AYM-LC` | proved as loop-continuity reduction | prove the transported loop-continuity ledger on the actual trajectory |
| nontriviality | `Paper-13/15 anchor package + HK-NT-TRANSPORT => HK-NT-CLOSE` | proved as Creutz-to-scalar-anchor transport theorem | prove the Creutz reserve and final anchor-loss ledger on one tower |
| nontriviality | `HK-NT-CLOSE => AYM-NT` | proved as nontriviality-anchor reduction | prove the transported scalar anchor has positive reserve |
| ontology audit | `HK-WP-CLOSE => AYM-WP` | proved as common-tower/no-hidden-divisibility audit theorem | prove all certificates use one pushed-forward law, one readout ledger, and shared constants |
| final closure | `HK-CYC-CLOSE => AYM-CLOSE => strong CYC => CYM_WL` | proved as heat-kernel closure theorem | prove all heat-kernel subcertificates on the actual trajectory |

In compressed form, the dependency graph is:

```text
HK-LF-CLOSE
+ HK-CT-CLOSE
+ HK-SF-CLOSE
+ HK-KP-TEST
=> HK-AN-CLOSE
=> AYM-AFRCE + AYM-KP

HK-AN-CLOSE
+ HK-DEC-CLOSE
+ HK-SURF-CLOSE
+ HK-CREUTZ-CLOSE
=> HK-NCPSC-CLOSE
=> verified positive nCPSC

FBE
+ HK-NCPSC-CLOSE
=> HK-X15-CLOSE
=> positive X_15 tower

HK-X15-CLOSE
+ HK-PROJ-CLOSE
+ HK-REG-CLOSE
+ HK-RPCOV-CLOSE
+ HK-LC-CLOSE
+ HK-NT-CLOSE
+ HK-WP-CLOSE
=> HK-CYC-CLOSE
=> AYM-CLOSE
=> strong CYC
=> CYM_WL.
```

The common-tower requirement is part of the theorem, not bookkeeping
decoration. All rows must use the same pushed-forward laws `Gamma_i`, the
same record maps, the same loop approximants, the same counterterm branches,
and the same constants ledger. Otherwise the implication stops at a
collection of separate estimates and does not prove `AYM-CLOSE`.

### Actual-Trajectory Burden Checklist

After Section 13A, the remaining mathematical work is not to invent new
closure architecture. It is to verify the listed gates on one common actual
heat-kernel tower `T_HK`:

- [ ] verify the finite-template row data of Definition 9N.1Q.4, hence
  `HK-AN-FINTPL-CLOSE(m)`, `HK-AN-CLOSE(m)`, and `AYM-AFRCE + AYM-KP`;
- [ ] prove `HK-NCPSC-CLOSE`, hence verified positive `nCPSC`;
- [ ] prove `HK-X15-CLOSE`, hence a positive `X_15` tower on the same
  batteries;
- [ ] prove `HK-PROJ-CLOSE`, hence projective finite-battery marginals;
- [ ] prove `HK-REG-CLOSE`, hence regulator and gauge-chart independence;
- [ ] prove `HK-RPCOV-CLOSE`, hence reflection positivity and Euclidean
  covariance after transport;
- [ ] prove `HK-LC-CLOSE`, hence loop continuity on `Loop_adm`;
- [ ] prove `HK-NT-CLOSE`, hence a nontrivial scalar Wilson-loop anchor;
- [ ] prove `HK-WP-CLOSE`, hence the common-tower/no-hidden-divisibility
  audit.

These bullets must be discharged on the same `Gamma_i`, `B_i`, `Rep_i`,
`Loop_i`, comparison maps, loop approximants, counterterm branches, and
constants ledger. Otherwise Paper 16 gives separate conditional estimates,
not `AYM-CLOSE`.

## 14. Honest Status

Paper 16 is broad and complete as a closure theorem and now has a sharper
actual-trajectory reduction. It proves:

```text
AYM-CLOSE
=> verified positive nCPSC
=> positive X_15 tower
=> strong CYC
=> CYM_WL.
```

The finite-cutoff record-law part is unconditional for standard
reflection-positive lattice gauge actions: the pushed-forward laws exist,
are positive, gauge invariant, and lattice-covariant.

The current proof workbench now adds three sharper facts:

1. `AYM-CLOSE` is split into named subcertificates, so every later failure is
   typed.
2. The primary regulator path is `HK-AYM`, the heat-kernel lattice trajectory.
   Wilson action is demoted to an `AYM-REG` comparison chart until a summable
   comparison theorem is proved.
3. The first analytic bottleneck is reduced first to a precise local-cluster
   estimate and then to three constructive subgates:

```text
HK-SF-GCD + HK-LFS + HK-CTS
=> HK-LCB
=> AYM-AFRCE.
```

4. The large-field subgate has been reduced further:

```text
HK-BFE + HK-LF-DOM + sigma_lf>h_poly
=> HK-LFS.
```

5. The block finite-energy part has been reduced to a finite-dimensional
   denominator margin:

```text
compact heat-kernel lower bound
+ finite block geometry
+ m_B(delta)>0
=> HK-BFE,

m_B(delta)=c_H delta^2-a_D.
```

6. The generic margin has been tested, and the sharper collar-adapted route
   has been turned into an explicit source criterion:

```text
generic route passes only if delta^2 > P_b^{loc} a_- / c_H.

q_loc(e_col+L_B alpha^2)<a_ad<c_H
=> HK-CAD
+ m_B^sharp(delta)>0
=> HK-BFE,

m_B^sharp(delta)=(c_H-a_ad)delta^2.
```

7. The large-field coefficient dominance gate has been reduced to finite
   coefficient-extractor bookkeeping:

```text
HK-LF-REP-SRC(N_lab,J_blk,R_blk,E_blk)
=> HK-LF-REP
=> HK-LF-DOM,

M_L=N_lab J_blk R_blk E_blk.
```

8. The large-field branch has been assembled into a single importable
   certificate:

```text
HK-LF-SRC => HK-LF-CLOSE => HK-LFS,

sigma_lf^sharp
 =
 (c_H-a_ad) delta^2/t_L
 - log(C_ad P_b C_H N_lab J_blk R_blk E_blk)
 > h_poly.
```

Theorem 9J.8 now proves the standard finite-template large-field source:
finite collar extension gives `HK-CAD`, finite batteries give
`HK-LF-REP-SRC`, and the entropy margin is forced by a cofinal AF time
cutoff. Thus the remaining large-field burden is only to verify that the
chosen actual trajectory uses that common finite-template ledger, metric, and
cutoff.

The counterterm gate has also been promoted from a placeholder to a
same-record source theorem:

```text
HK-CT-RATE
=> HK-CT-SRC
=> HK-CT-CLOSE
=> HK-CTS.
```

Under the Paper-11 ledger-compatible pure-gauge trajectory, the clean
minimal counterterm branch has zero nonlocal counterterm/scheme tail
amplitudes by Theorem 9K.2G. If the actual branch uses a non-clean
counterterm or scheme convention, the remaining counterterm burden is the
explicit finite rate audit of positive irrelevant and scheme-tail rates on
the same pushed-forward record tower. After those constants are fixed, the
common residual-constant assembly is automatic by Theorem 9N.1I; the only
remaining analytic closure step is the scalar KP test.

9. Counterterm stability has been reduced to a local counterterm ledger:

```text
HK-CT-CLOSE => HK-CTS.
```

10. The small-field gate has been reduced to a block-conditioned covariance
    and tree-activity certificate:

```text
HK-SF-CLOSE => HK-SF-GCD.
```

The tree-activity certificate has now been made explicit. With

```text
S_G(mu_G/2)<=C_E,
HK-SF-YM2 finite vertex ledger,
```

the source bound is

```text
theta_sf <= e C_v^{YM2} C_G C_E g_*^2.
```

Paper 11's block-conditioned covariance supplies finite `C_G,mu_G,C_E` on
the fixed-ratio branch. Hence `theta_sf<1` follows on a sufficiently fine AF
tail once `HK-SF-YM2` is verified on the same pushed-forward record law. The
`SEL_0` one-block verification is supplied in Paper 19 by the common-record
`HK-SF-YM2` import theorem. In
the strict axial-tree, exact-covariance, connected/cumulant, minimal-record
branch,

```text
C_v^{YM2,min}
=24C_4C_cov^2+18C_3^2C_cov^3+C_JC_cov
 + C_rem g_*^{epsilon_v}.
```

11. The residual KP gate now has an explicit threshold:

```text
eta_res^{bd}(m)
 =
 C_KP A_res exp(-(mu_res-h_KP-m) r_*)
 /
 (1-exp(-(mu_res-h_KP-m)))
 < 1.
```

The threshold has also been sharpened to a scalar decision. With

```text
D_0=mu_res-h_KP,
B_res=C_KP A_res,
```

the easiest pass is always `m=0`; some `m>=0` passes if and only if

```text
B_res exp(-D_0 r_*)/(1-exp(-D_0))<1.
```

If a positive weight `m_req` is required, it must lie below the explicit
`m_max` of Theorem 9M.1A. The range-absorption route is valid only when
polymers below the enlarged range are actually absorbed into the declared
local ledger.

12. The analytic branch is now assembled into a single certificate:

```text
HK-AN-SRC
=> HK-AN-CLOSE
=> AYM-AFRCE + AYM-KP.
```

The ordered source certificate is:

```text
HK-SF-SRC with theta_sf<1
+ HK-LF-CLOSE with sigma_lf^sharp>h_poly
+ HK-CT-RATE => HK-CT-CLOSE
+ HK-AN-RES-COMMON common residual constants
+ eta_res^{bd}(m)<1
=> HK-AN-CLOSE(m).
```

The exact scalar KP decision is

```text
D_0=mu_res-h_KP,
B_res=C_KP A_res,
eta_res^{bd}(m)
=B_res exp(-(D_0-m)r_res)/(1-exp(-(D_0-m)))<1.
```

On the clean minimal row this is the three-inequality worksheet:

```text
theta_clean<1,
delta_clean(m)>0,
eta_clean(m)<1.
```

The older compressed import remains:

```text
HK-AN-CLOSE => AYM-AFRCE + AYM-KP.
```

The first execution step is no longer open on batteries with a verified
common-record `HK-SF-YM2` import:

```text
Paper-11 covariance
+ HK-SF-YM2 on the same pushed-forward record law
+ sufficiently fine AF tail
=> HK-SF-SRC with theta_sf<1.
```

Paper 19 supplies this verification for the frozen `SEL_0` one-block
battery. The next analytic source target is therefore `HK-LF-CLOSE` with
`sigma_lf^sharp>h_poly`.

13. The character-tail branch is now assembled into a decoration certificate:

```text
HK-DEC-CLOSE => AYM-TAIL,

eta_dec^{bd}
 =
 eta_res^{bd}(m) + C_dec epsilon_ch
 < 1.
```

14. The surface reserve is packaged as:

```text
HK-SURF-CLOSE => AYM-SURF,

M_SUB^{bd}
 =
 kappa_sheet - h_surf - L_dec eta_dec^{bd} - R_surf
 > 0.
```

15. The transported Creutz reserve is packaged as:

```text
HK-CREUTZ-CLOSE => AYM-CREUTZ,

M_15^{bd}
 =
 M_SUB^{bd} - L_bat - L_reg - L_vol - L_shape
 > 0.
```

16. The whole Paper-15 numerical certificate is now assembled:

```text
HK-NCPSC-CLOSE => verified positive nCPSC.
```

17. The finite-battery export to Paper 15's output tower is now assembled:

```text
HK-X15-CLOSE => positive X_15 tower.
```

18. The projectivity gate has been reduced to summable finite-battery
    marginal defects:

```text
HK-PROJ-CLOSE => AYM-PROJ.
```

18A. The abstract projectivity defect has been made concrete. The restriction
     map is coordinate deletion on declared records, so the exact projection
     part has no defect. All nonzero projectivity burden is now cross-scale
     drift:

```text
concrete readout scheme
+ HK-PROJ-DRIFT
+ HK-XDRIFT
=> HK-PROJ-CLOSE
=> AYM-PROJ.
```

The remaining projectivity proof is therefore not vague projective-limit
language. It is the task of proving the finite-battery drift envelope and the
`X_15` constant drift envelope from the actual heat-kernel RG ledger.

18B. The finite-battery drift envelope has now been reduced to a one-shell
     heat-kernel RG law-drift budget:

```text
HK-RG-PROJ-LEDGER
=> HK-PROJ-DRIFT.
```

18C. The `X_15` constant drift envelope has now been reduced to a one-shell
     constant transport budget:

```text
HK-RG-XLEDGER
=> HK-XDRIFT.
```

18D. Therefore the projectivity route is now:

```text
concrete readout scheme
+ HK-RG-PROJ-LEDGER
+ HK-RG-XLEDGER
=> HK-PROJ-CLOSE
=> AYM-PROJ.
```

The remaining constructive burden is to verify the two RG ledgers for the
actual heat-kernel trajectory with summable local-RG, finite-volume,
loop-approximant, counterterm, representation-tail, precision, and constant
transport budgets. If any Paper-15 margin approaches zero, `HK-RG-XLEDGER`
fails because the finite sensitivity constant for the exported `X_15`
constants can diverge.

19. The regulator and gauge-chart independence gate has been reduced to
    summable finite-record comparison defects:

```text
HK-REG-CLOSE => AYM-REG.
```

19A. The regulator/chart comparison has now been made concrete. The
     comparison maps are finite record maps into the heat-kernel primary
     readout chart, and pairwise regulator independence follows by common
     refinement:

```text
concrete comparison scheme
+ HK-RG-REG-LEDGER
+ HK-RG-REGX-LEDGER
=> HK-REG-CLOSE
=> AYM-REG.
```

The remaining constructive burden is to prove the two regulator comparison
ledgers: finite-record law comparison and finite-list `X_15` constant
transport comparison. This is where Wilson/heat-kernel universality,
gauge-chart independence, blocking independence, and counterterm-scheme
independence must actually be proved as summable operational estimates.

20. Reflection positivity and Euclidean covariance have been reduced to
    summable finite-record OS and Euclidean-motion approximant defects:

```text
HK-RPCOV-CLOSE => AYM-RP-COV.
```

20A. The reflection-positivity half has now been separated and reduced:

```text
symmetric-positive OS readout
+ HK-RP-LEDGER
=> RP half of HK-RPCOV-CLOSE.
```

The heat-kernel bare cutoff RP contribution is exact. The remaining RP
burden is summability of counterterm, binning, projectivity, regulator/chart,
and volume/reflection-plane defects. This is the correct OS foundation for a
later mass-gap paper, but it still must be paired with the Euclidean
covariance half of `HK-RPCOV-CLOSE`.

20B. The Euclidean covariance half has now been separated and reduced:

```text
Euc_adm
+ Euclidean-invariant counterterm/readout ledger
+ HK-COV-LEDGER
=> covariance half of HK-RPCOV-CLOSE.
```

For exact hypercubic lattice symmetries the cutoff covariance defect is zero.
For genuine continuum rotations/translations, the burden is summability of
approximant, binning, counterterm, block/collar, projective, regulator/chart,
and finite-volume motion-buffer defects.

20C. The full RP/covariance gate is now assembled:

```text
symmetric-positive OS readout
+ HK-RP-LEDGER
+ Euc_adm
+ Euclidean-invariant counterterm/readout ledger
+ HK-COV-LEDGER
=> HK-RPCOV-CLOSE
=> AYM-RP-COV.
```

21. Loop continuity is now a concrete transported Paper-12 modulus:

```text
Paper-12 loop package
+ HK-LC-TRANSPORT
=> HK-LC-CLOSE
=> AYM-LC.
```

The defect split is explicit:

```text
AF loop-variation/connective-tail loss,
lattice or block approximant loss,
finite binning loss,
perimeter-counterterm loss,
cusp-counterterm loss,
smeared-to-unsmeared loss,
projective transport loss,
regulator/chart loss,
finite-volume loss.
```

The remaining burden is not conceptual loop completion; it is proving that
these losses are summable on the same actual heat-kernel tower:

```text
HK-LC-CLOSE => AYM-LC.
```

22. Nontriviality is now reduced to a transported scalar anchor extracted
    from the Paper-13/15 Creutz route:

```text
Paper-13/15 anchor package
+ HK-NT-TRANSPORT
=> HK-NT-CLOSE
=> AYM-NT.
```

The nontriviality loss ledger is explicit:

```text
Creutz/surface/decoration reserve loss,
scalar-anchor extraction loss,
loop-shape or block-approximant loss,
finite-battery/binning loss,
perimeter/cusp counterterm loss,
loop-continuity loss,
projective transport loss,
regulator/chart loss,
finite-volume loss.
```

The remaining burden is proving the positive-reserve inequality
`R_i^{NT}<=c_seed/2` on the actual heat-kernel tower:

```text
HK-NT-CLOSE => AYM-NT.
```

23. Whole-process compatibility is now a common-tower audit:

```text
HK-WP-CLOSE => AYM-WP.
```

The audit fixes one cofinal family

```text
i=(a_i,L_i,beta_i,B_i,Rep_i,Loop_i),
```

one pushed-forward law `Gamma_i`, one battery/readout ledger, one family of
restriction and regulator/chart maps, one set of loop approximants, one
counterterm branch ledger, and one constants ledger. The no-hidden-divisibility
clause forbids composing unrecorded partial kernels as if the process were
Markovian or divisible.

24. The heat-kernel route now has a single final closure certificate:

```text
HK-CYC-CLOSE
=> AYM-CLOSE
=> strong CYC
=> CYM_WL.
```

### What Paper 16 Does Not Prove

Paper 16 does not prove any of the following:

1. an unconditional construction of continuum `4D SU(N)` Yang-Mills;
2. the Clay mass-gap theorem;
3. confinement or an arbitrary-loop area law;
4. QCD with dynamical matter;
5. the Standard Model;
6. gravity, stress-energy reconstruction, or geometry from records.

It proves the conditional closure architecture from ISP whole-process record
laws to a nontrivial reflection-positive Euclidean-covariant Wilson-loop
functional, provided the named actual-trajectory ledgers are all proved on
one common tower.

The central remaining mathematical burden is now explicit:

```text
prove AYM-CLOSE for the actual 4D SU(N) asymptotically-free continuum
trajectory.
```

The first concrete sub-burdens are now:

```text
prove HK-CYC-CLOSE, i.e. prove HK-X15-CLOSE, HK-PROJ-CLOSE, HK-REG-CLOSE,
HK-RPCOV-CLOSE, HK-LC-CLOSE, HK-NT-CLOSE, and HK-WP-CLOSE on one common
heat-kernel tower.
```

The remaining hard constructive pieces are the actual proof of the assembled
numerical certificate, Paper-14 common-tower entry, summable projectivity,
regulator/chart independence, RP/covariance transport, loop continuity, and a
nontriviality anchor. If `AYM-CLOSE` is discharged, V3 reaches a nontrivial
reflection-positive Euclidean-covariant continuum Wilson-loop functional. If
not, the failure ledger identifies the exact obstruction to the
ISP-to-Yang-Mills route.
