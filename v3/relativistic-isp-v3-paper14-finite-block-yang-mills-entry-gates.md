# Relativistic ISP V3 Paper 14: Finite-Block Entry Gates For Actual Continuum SU(N) Yang-Mills

Author: Felix Robles Elvira

## Abstract

Paper 13 reduced the nonperturbative Yang-Mills problem to a finite list of
record-level gates. This paper begins the next step: it tries to prove that
the actual four-dimensional continuum `SU(N)` trajectory enters the
finite-block operational record domain required by that reduction.

The paper does not assume a mass gap, particles, a Wightman representation, or
a Hilbert-space spectrum. Those are later representation outputs. The objects
here are finite batteries of gauge-invariant Wilson-loop and block-plaquette
records, their exact cutoff laws, and the whole-process defects relating those
laws under volume, regulator, chart, and counterterm changes.

The main target is the finite-block entry package

```text
FBE(s_0,L,rho) := BLU(s_0,L) + CE(s_0,rho,L) + WP(s_0,L).
```

Here `BLU` is block-limit uniqueness, `CE` is central character extraction,
and `WP` is whole-process certificate independence. Paper 15 will attack the
remaining residual and surface gates `RPF`, `KP_dec`, and `SUB`.

### Post-Paper-20 Source Boundary

This paper can export finite-block entry gates, character-window ledgers, and
whole-process certificate data. It does not export the later Paper-20
`SEL2` tree-rate source. In particular, it does not prove

```text
P20-SEL2-TREE-RATE-GATE:
q_rho gamma_rho > Theta_esc^tree,
T_-^{SEL2} > Theta_T^tree(rho).
```

Those inequalities remain same-record block-plaquette coefficient estimates
for Paper 20 or a later source paper, not consequences of finite-block entry
alone.

## 1. Ontological Discipline

The declared ontology is operational and finite at every stage.

1. A record is a declared finite gauge-invariant scalar, such as a normalized
   Wilson loop or a central block-plaquette character.
2. A finite battery is a finite list of such records, together with the
   sigma-algebra they generate.
3. A cutoff Yang-Mills model supplies one whole-process probability law on
   each battery.
4. Refinement, gauge chart changes, counterterm changes, and volume changes
   are compared by pushing forward whole laws to common batteries.
5. No statement in this paper composes unrecorded partial kernels as if the
   microscopic process were Markovian or divisible.

This is the Barandes-aligned point: the laws of the records are primary.
Fields, Hilbert spaces, particles, and local nets may appear only as
reconstructed representation layers after positivity, covariance, and
continuity gates are closed.

## 2. Imports From Paper 13

Paper 13 exports the following finite gate language.

```text
ACSB(s_0,rho,L)
=> SB(s_0,rho,L)
=> surface-polymer entry
=> exact RG entry
=> RSB(s_0,rho,L)
=> block-scale sheet expansion
=> scalar Creutz anchor
```

The actual-continuum strong-block entry package `ACSB(s_0,rho,L)` consists of
six gates:

1. `BC(s_0,L)`: finite-block continuum convergence;
2. `CE(s_0,rho,L)`: central one-plaquette character extraction;
3. `RPF(s_0,L)`: local residual factorization;
4. `KP_dec(s_0,rho,L)`: residual decoration KP smallness;
5. `SUB(s_0,rho,L)`: surface subcriticality;
6. `WP(s_0,L)`: whole-process covariance of the certificate.

Paper 13 also reduces `BC` to block-limit uniqueness `BLU(s_0,L)`. This paper
therefore focuses on:

```text
BLU(s_0,L), CE(s_0,rho,L), WP(s_0,L).
```

## 3. The Finite-Block Battery

Fix:

- a compact connected gauge group `G=SU(N)`;
- a physical block scale `s_0>0`;
- an integer block width `L>=2`;
- a finite set of block plaquettes and rectangular block loops inside a
  bounded Euclidean test region;
- a nontrivial irreducible representation `rho` of `G`;
- a sequence of cutoff models indexed by lattice spacing `a`, finite volume
  `V`, bare coupling `g(a)`, gauge-chart choice `q`, and counterterm ledger
  `ct`.

For each cutoff tuple

```text
eta=(a,V,q,ct)
```

let `mu_eta` be the exact cutoff Yang-Mills law pushed forward to the finite
record battery

```text
B_{s_0,L}.
```

The battery contains:

1. normalized scalar Wilson-loop records `W_C`;
2. central block plaquette records `Phi_lambda(P)`;
3. products of finitely many such records needed for the Creutz, coefficient,
   and identity tests.

For non-self-conjugate representations, the scalar central record is the real
paired character

```text
Phi_lambda(U) = (chi_lambda(U) + chi_bar_lambda(U)) / 2.
```

When no ambiguity is possible, `chi_lambda` denotes this declared real central
record.

## 4. Finite-Block Entry Package

### Definition 4.1: Finite-Block Entry

The actual trajectory satisfies `FBE(s_0,rho,L)` if the following three
statements hold.

1. `BLU(s_0,L)`: every cutoff subnet has the same weak limit on
   `B_{s_0,L}`.
2. `CE(s_0,rho,L)`: the limiting block plaquette marginal is central and has
   a positive, subcritical `rho`-coefficient window:

   ```text
   0 < u_- <= u_rho <= u_+ < u_crit,
   ```

   with all non-declared leading coefficients controlled by an explicit
   finite tail bound.
3. `WP(s_0,L)`: the certificates proving the first two statements are
   invariant, up to summable defects, under volume exhaustion, regulator
   refinement, gauge-chart transition, and counterterm reparametrization.

### Theorem 4.2: Paper-14 Entry Reduces The First Half Of ACSB

Assume `FBE(s_0,rho,L)`. Then the gates `BC(s_0,L)`, `CE(s_0,rho,L)`, and
`WP(s_0,L)` of Paper 13 hold.

Proof.

`BLU` gives unique subsequential block limits. Paper 13 proves that finite
compactness plus `BLU` is equivalent to `BC`. The coefficient statement in
Definition 4.1 is exactly `CE`. The whole-process statement is exactly `WP`.
Thus the first, second, and sixth gates of `ACSB` hold. `square`

### Corollary 4.3: Paper 15 Only Needs The Residual Gates

If `FBE(s_0,rho,L)` holds, then Paper 15 can complete `ACSB(s_0,rho,L)` by
proving `RPF(s_0,L)`, `KP_dec(s_0,rho,L)`, and `SUB(s_0,rho,L)`.

Proof.

This is Theorem 4.2 plus Paper 13's six-gate theorem for `ACSB`. `square`

## 5. Gate BLU: Determining Finite-Block Identities

### Definition 5.1: Finite-Block Identity Ledger

A finite-block identity ledger at `(s_0,L)` is a finite or countable family
of identities

```text
I_j(nu)=0,       j in J,
```

on probability laws `nu` over the compact record space generated by
`B_{s_0,L}`.

The ledger is admissible if every identity is expressed only in terms of
declared record moments, finite difference operators on compact group
variables, or pushforward comparisons between whole cutoff laws.

The ledger may include:

1. normalization and positivity;
2. centrality and conjugation invariance;
3. finite-volume Schwinger-Dyson identities for Wilson-loop records;
4. finite Makeenko-Migdal loop identities with explicit cutoff defects;
5. reflection-positivity inequalities on the battery;
6. Euclidean covariance identities up to boundary defects;
7. Bianchi-type plaquette constraints written as identities among
   gauge-invariant records;
8. counterterm transport identities on common refinement batteries.

### Definition 5.2: Determining Ledger

The ledger is determining for `B_{s_0,L}` if there is at most one probability
law `nu` on the finite battery record space satisfying all limiting identities.

Equivalently, if `nu` and `nu'` satisfy every limiting identity, then

```text
int F dnu = int F dnu'
```

for every continuous function `F` of the finite battery records.

### Theorem 5.3: Determining Identities Prove BLU

Assume:

1. every cutoff law `mu_eta` is a probability law on the compact finite
   battery record space;
2. every cutoff subnet has at least one weak limit;
3. the identity defects satisfy

   ```text
   sup_j |I_j(mu_eta)| -> 0
   ```

   along the continuum trajectory, after pushing all laws to the same battery;
4. the limiting ledger is determining.

Then `BLU(s_0,L)` holds.

Proof.

Compactness gives subsequential limits. Let `nu` and `nu'` be two such limits.
By the vanishing-defect assumption and continuity of the ledger functionals,
both satisfy every limiting identity. Since the ledger is determining, `nu`
and `nu'` agree on every continuous finite-battery test function. Hence all
subsequential limits are the same law. This is `BLU(s_0,L)`. `square`

### Lemma 5.4: Moment Determinacy On A Compact Battery

Let `X` be the compact finite battery record space. If two probability laws
on `X` agree on a subalgebra `A subset C(X)` that contains constants,
separates points, and is closed under complex conjugation, then the laws are
equal.

Proof.

By Stone-Weierstrass, `A` is uniformly dense in `C(X)`. Agreement on `A`
therefore implies agreement on all continuous functions. Probability laws on
a compact Hausdorff space are determined by their continuous integrals.
`square`

### Corollary 5.5: Recursive Moment Closure Proves Determinacy

Suppose the identity ledger recursively determines the integral of every
monomial in a point-separating algebra of finite battery records. Then the
ledger is determining, hence Theorem 5.3 proves `BLU(s_0,L)`.

This is the first concrete Paper-14 route: prove that the finite
Schwinger-Dyson, loop, covariance, and positivity identities close a
point-separating record algebra.

## 6. Gate CE: Central Character Extraction

### Definition 6.1: Block Plaquette Marginal

Let `P` be a declared block plaquette. A subsequential block limit `nu`
induces a central probability law

```text
nu_P
```

on `SU(N)` if the distribution of the block holonomy around `P` is invariant
under conjugation.

When `nu_P` is absolutely continuous with respect to Haar measure, write

```text
d nu_P(U) = k_P(U) dU.
```

### Definition 6.2: Haar-Projected Coefficients

For each irreducible representation `lambda`, define the normalized central
coefficient

```text
u_lambda(P) = (1 / d_lambda) int overline{chi_lambda(U)} k_P(U) dU.
```

For non-self-conjugate `lambda`, the operational scalar coefficient used in
the real battery is the corresponding paired coefficient for the record
`Phi_lambda=(chi_lambda+chi_bar_lambda)/2`.

### Definition 6.3: Coefficient Window

The block plaquette marginal satisfies the `rho` coefficient window if there
are constants

```text
0 < u_- <= u_+ < u_crit,
epsilon_tail >= 0
```

such that:

1. `u_- <= u_rho(P) <= u_+`;
2. all non-declared leading coefficients have total controlled weight at most
   `epsilon_tail`;
3. the surface-subcritical reserve exported to Paper 15 is positive:

   ```text
   Margin_CE := u_rho(P)^{N_0}(1-u_rho(P)^{Q_sigma}) - Tail_CE > 0.
   ```

Here `N_0`, `Q_sigma`, and `Tail_CE` are the finite constants appearing in
the Paper-13 surface-subcriticality inequality.

### Proposition 6.4: Coefficient Window Proves CE

If the unique block limit from `BLU` has central block plaquette marginals
and satisfies the coefficient window of Definition 6.3 on every plaquette in
the battery, then `CE(s_0,rho,L)` holds.

Proof.

This is the Paper-13 definition of `CE`: centrality, absolute continuity or
declared coefficient extraction, positive `rho` window, and controlled
off-channel tail. `square`

### Proposition 6.5: Heat-Kernel Reference Calculation

For the heat-kernel class function on `SU(N)`

```text
K_t(U) = sum_lambda d_lambda exp(-t C_2(lambda)/2) chi_lambda(U),
```

with `t>0`, the normalized Haar-projected coefficient is

```text
u_lambda(t) = exp(-t C_2(lambda)/2).
```

In particular, every nontrivial representation has a strictly positive
coefficient smaller than one.

Proof.

The Peter-Weyl orthogonality relation gives

```text
int overline{chi_lambda(U)} chi_sigma(U) dU = delta_{lambda,sigma}
```

with the paired real-character convention when the operational battery stores
real paired characters. Projecting `K_t` therefore extracts the coefficient
multiplying `d_lambda chi_lambda`, and normalization by `d_lambda` gives
`exp(-t C_2(lambda)/2)`. Since
`C_2(lambda)>0` for nontrivial irreducible representations and `t>0`, the
coefficient lies in `(0,1)`. `square`

### Corollary 6.6: Stability Of CE Around A Heat-Kernel Reference

Suppose the actual block plaquette marginal `nu_P` is within total variation
distance `delta_CE` of a heat-kernel reference `K_t dU` on the finite
coefficient battery. Then

```text
|u_lambda(P) - exp(-t C_2(lambda)/2)| <= delta_CE
```

for every tested `lambda`. Hence `CE` holds whenever this error is smaller
than the declared coefficient reserve.

Proof.

The normalized character functional `chi_lambda/d_lambda` has absolute value
at most one. Total variation therefore gives the displayed bound. The final
statement is Definition 6.3. `square`

This does not say actual continuum Yang-Mills is a heat-kernel one-plaquette
model. It supplies a computable reference domain: if the block RG ledger
shows the actual block plaquette marginal is close enough to such a reference,
then the `CE` gate closes with explicit constants.

## 7. Gate WP: Whole-Process Certificate Independence

### Definition 7.1: Certificate

A Paper-14 certificate for a cutoff tuple `eta` consists of:

1. the pushed-forward law on `B_{s_0,L}`;
2. the finite identity defects `Def_ID(eta)`;
3. the coefficient errors `Def_CE(eta)`;
4. the chart and regulator comparison defects `Def_chart(eta,eta')`;
5. the counterterm transport defects `Def_ct(eta,eta')`;
6. the boundary and finite-volume defects `Def_vol(eta)`.

All defects are measured after pushing the compared whole-process laws to a
common finite battery.

### Definition 7.2: Summable Certificate Ledger

The certificate ledger is summable if every admissible chain

```text
eta_0 -> eta_1 -> eta_2 -> ...
```

has a common-refinement defect bound

```text
sum_m [
  Def_chart(eta_m,eta_{m+1})
  + Def_ct(eta_m,eta_{m+1})
  + Def_vol(eta_m)
  + Def_ID(eta_m)
  + Def_CE(eta_m)
] < infinity.
```

### Theorem 7.3: Summable Certificate Ledger Proves WP

If the certificate ledger is summable and the limiting entry gates do not
depend on the chosen admissible chain, then `WP(s_0,L)` holds.

Proof.

Every chart, regulator, counterterm, and volume comparison is performed by
pushing whole laws to a common finite battery. The summable bound makes the
total discrepancy along any admissible chain finite and vanishing at the
continuum endpoint. Thus two admissible certificates differ by a defect that
goes to zero on every declared record in `B_{s_0,L}`. Therefore the entry
certificate is independent of the path used to reach the continuum limit.
This is `WP(s_0,L)`. `square`

### Proposition 7.4: WP Is Not A Gauge Fixing Claim

The gate `WP` does not assert that a particular gauge chart is physically
preferred. It asserts that chart-dependent constructions yield the same
finite-block record law after whole-process pushforward to the gauge-invariant
battery.

Proof.

The certificate space contains charts only as auxiliary coordinates for
estimates. The output battery contains gauge-invariant scalar records. If two
charts give the same pushed-forward law on that battery up to summable
defects, the certificate is chart-independent at the operational level.
`square`

## 8. Combined Entry Theorem

### Definition 8.1: Paper-14 Entry Data

Paper-14 entry data consist of:

1. a determining finite-block identity ledger;
2. vanishing identity defects along the actual continuum trajectory;
3. central block plaquette marginals;
4. a certified `rho` coefficient window;
5. a summable whole-process certificate ledger.

### Theorem 8.2: Paper-14 Entry Data Prove FBE

If the Paper-14 entry data of Definition 8.1 hold at `(s_0,L,rho)`, then
`FBE(s_0,rho,L)` holds.

Proof.

The determining identity ledger and vanishing defects prove `BLU` by Theorem
5.3. The central coefficient window proves `CE` by Proposition 6.4. The
summable certificate ledger proves `WP` by Theorem 7.3. Hence all three
clauses of `FBE` hold. `square`

### Corollary 8.3: Export To Paper 15

Under the assumptions of Theorem 8.2, Paper 15 may assume:

1. a unique finite-block continuum law on `B_{s_0,L}`;
2. explicit character coefficients `u_rho`, tail bounds, and coefficient
   reserves;
3. a whole-process defect budget for changing regulator, chart, counterterm,
   and volume.

It may not assume residual polymer locality, surface subcriticality, a mass
gap, confinement, or a Hilbert-space spectrum.

## 9. First Concrete Work Program

The fastest rigorous route through Paper 14 is:

1. Choose a minimal determining battery:
   - the four Creutz loops from Paper 13;
   - all block plaquette character records needed for `rho`;
   - products up to a declared degree `D_ID`;
   - reflection pairs needed for positivity tests.
2. Write the finite-cutoff identities exactly on that battery:
   - finite Schwinger-Dyson identities;
   - finite loop equations with boundary terms;
   - reflection-positivity inequalities;
   - Euclidean covariance identities up to finite-volume defects.
3. Prove the identity ledger is determining on the chosen battery, or name
   the missing finite determinacy condition.
4. Compute the Haar-projected coefficient window for the block plaquette
   marginal.
5. Compare the actual block marginal to a heat-kernel or character-domain
   reference with an explicit total-variation or cumulant bound.
6. Prove the common-refinement chart/counterterm ledger is summable.
7. Export all constants to Paper 15.

## 10. Exact Finite-Cutoff Identity Source

The identity ledger should not be introduced as an abstract wish. At finite
cutoff it has a concrete compact-group source.

### Definition 10.1: Finite-Cutoff Gauge Measure

On a finite lattice region `Lambda`, let the link variables be

```text
U_e in SU(N).
```

Let the cutoff action be a local gauge-invariant action

```text
S_eta(U) = S_plaq,eta(U) + S_ct,eta(U) + S_boundary,eta(U),
```

where `eta=(a,V,q,ct)` records the regulator, finite volume, chart, and
counterterm choices. The cutoff law is

```text
d mu_eta(U) = Z_eta^{-1} exp(-S_eta(U)) prod_e dU_e,
```

with Haar measure on every link.

This definition is not an ontology claim about microscopic link variables. It
is a regulator chart used to compute the pushed-forward law of the declared
records.

### Theorem 10.2: Exact Compact-Group Schwinger-Dyson Identity

Let `L_e^A` be a left-invariant vector field on the link `e`, associated with
a Lie algebra basis element `A`. For every smooth cylindrical function `F` of
the link variables,

```text
E_eta[L_e^A F] = E_eta[F L_e^A S_eta].
```

Proof.

Haar measure is invariant under the left flow generated by `L_e^A`, and the
finite group manifold is compact, so integration by parts gives

```text
0 = int L_e^A(F exp(-S_eta)) prod_e dU_e.
```

Expanding the derivative yields

```text
0 = E_eta[L_e^A F] - E_eta[F L_e^A S_eta].
```

Rearranging gives the identity. `square`

### Corollary 10.3: Exact Finite Loop Identities

If `F` is a product of Wilson-loop and block-plaquette records, Theorem 10.2
gives an exact finite-cutoff identity among expectations of differentiated
loop products and local action insertions.

In a Wilson plaquette action, `L_e^A S_eta` is a finite sum over plaquettes
touching `e`; therefore the identity is local at finite cutoff before the
projection to a finite battery.

Proof.

Wilson-loop records are smooth cylindrical functions of finitely many link
variables. Applying Theorem 10.2 gives the first statement. Locality of
`L_e^A S_eta` follows from locality of the action. `square`

### Definition 10.4: Finite-Battery Projection Defect

The exact identity in Corollary 10.3 may contain differentiated loop products
or local action insertions outside the chosen battery `B_{s_0,L}`. Let

```text
Pi_D
```

be a declared projection onto the degree-`D` point-separating record algebra
generated by the battery. The finite-battery projection defect is

```text
Def_proj(eta,D)
  = sup | E_eta[G] - E_eta[Pi_D G] |,
```

where the supremum is over every off-battery expression `G` produced by the
finite list of Schwinger-Dyson and loop identities used in the ledger.

### Theorem 10.5: Exact Identities Plus Projection Control Feed BLU

Assume:

1. the exact finite-cutoff identities of Corollary 10.3 are imposed on a
   finite list of record products;
2. `Def_proj(eta,D)->0` along the continuum trajectory for a sequence of
   degrees `D`;
3. the projected limiting identities determine the finite battery law.

Then the hypotheses of Theorem 5.3 hold, and hence `BLU(s_0,L)` holds.

Proof.

The exact identities have zero finite-cutoff defect before projection.
Projection introduces only `Def_proj(eta,D)`, which vanishes by assumption.
Thus every subsequential limit satisfies the projected limiting identities.
If those identities determine the finite battery law, Theorem 5.3 applies.
`square`

### Honest Boundary 10.6: The Real BLU Difficulty

The exact finite-cutoff Schwinger-Dyson identity is easy. The hard part is not
the integration by parts. The hard part is proving that, after restricting to
a finite operational battery:

1. the off-battery projection defects vanish or are summable;
2. the projected identities still determine the finite-block law;
3. the limiting identities are stable under volume, regulator, chart, and
   counterterm transport.

That is the concrete `BLU` problem for Paper 14.

## 11. Step 1: Minimal Determining Battery

The word "minimal" is dangerous unless it is made explicit. The finite
battery below is minimal only relative to the Paper-13 entry route: it keeps
exactly the records needed to test the Creutz anchor, the leading character
coefficient, reflection positivity on the battery, and the finite identities
used for block-limit uniqueness.

### Definition 11.1: Creutz-Character Battery

Fix a block scale `s_0`, block width `L`, representation `rho`, and a finite
physical test box `O`. The Creutz-character battery

```text
B_CC(s_0,L,rho,D,Lambda_*)
```

contains the following records.

1. Four rectangular Wilson-loop records around a fixed block rectangle:

   ```text
   W(R,T), W(R+1,T), W(R,T+1), W(R+1,T+1).
   ```

   These are the scalar records entering the block Creutz combination.
2. For every block plaquette `P` in the rectangle sheet and every
   representation `lambda in Lambda_*`, the central character record

   ```text
   Phi_lambda(P).
   ```

3. Every product of records from items 1 and 2 of total degree at most `D`.
4. Reflection-paired copies of those products whenever the reflected support
   remains inside `O`.
5. The finite list of off-battery expressions generated by one application of
   the compact-group Schwinger-Dyson identity, projected back to the degree
   `D` algebra.

Here `Lambda_*` is a finite representation set containing the trivial
representation, `rho`, `bar rho`, and every representation produced by the
finite tensor products needed by the degree-`D` identities.

### Lemma 11.2: Compactness Of The Battery State Space

The record space of `B_CC(s_0,L,rho,D,Lambda_*)` is compact.

Proof.

Each Wilson-loop and normalized character record is bounded because it is a
continuous class function on compact `SU(N)`. A finite product of bounded
records is bounded. The battery record map therefore lands in a closed
bounded subset of a finite-dimensional Euclidean space after taking the
closure of its image. This closure is compact. `square`

### Definition 11.3: Determining Completion Of The Battery

The finite battery `B_CC(s_0,L,rho,D,Lambda_*)` tests finitely many records.
Its determining completion is the countable increasing family

```text
B_CC^inf = union_D union_Lambda_* B_CC(s_0,L,rho,D,Lambda_*),
```

where `D` increases through positive integers and `Lambda_*` exhausts the
irreducible representations by nondecreasing Casimir.

The completion is still operational: every test uses a finite sub-battery, and
limits are taken only after finite whole-process laws have been compared.

### Proposition 11.4: No Finite-Degree Miracle

For a continuous compact battery with at least one nontrivial interval of
record values, no fixed finite-degree moment list generically determines the
probability law.

Proof.

On a compact interval, distinct probability measures can share finitely many
moments. Pushing those examples through any nonconstant record coordinate
gives distinct laws on the battery with the same finite moment list. Thus a
finite-degree ledger can certify a finite approximation or a finite-parametric
ansatz, but it cannot by itself determine the full law without an additional
finite-dimensional closure theorem. `square`

### Theorem 11.5: Countable Battery Determinacy

If two subsequential block limits agree on all moments of
`B_CC^inf`, then they agree on every continuous function of every finite
Creutz-character battery.

Proof.

For any fixed finite battery, polynomials in the coordinate records form a
unital algebra that separates points on the compact record space. Agreement
on all moments means agreement on that algebra. Stone-Weierstrass and the
Riesz representation theorem imply equality of the two laws on the finite
battery. Since the finite battery was arbitrary, the statement follows.
`square`

## 12. Steps 2-3: Projected Identities And The BLU Route

### Definition 12.1: Projected Schwinger-Dyson Ledger

For each finite battery `B_CC(s_0,L,rho,D,Lambda_*)`, define the projected
Schwinger-Dyson ledger as follows.

1. Choose a finite list of links `e`, Lie algebra basis elements `A`, and
   record polynomials `F` of degree at most `D`.
2. Apply the exact identity

   ```text
   E_eta[L_e^A F] = E_eta[F L_e^A S_eta].
   ```

3. Rewrite every produced term as a finite linear combination of battery
   records plus an off-battery remainder.
4. Record the projected identity

   ```text
   I_{e,A,F}^{D,Lambda_*}(mu_eta)
     = E_eta[Pi_{D,Lambda_*}(L_e^A F - F L_e^A S_eta)].
   ```

5. Put the unprojected remainder into

   ```text
   Def_proj(eta,D,Lambda_*).
   ```

The ledger is whole-process: the expectation is always taken in the full
cutoff measure before pushforward to the finite battery.

### Lemma 12.2: Projected Identity Defect Bound

For every projected identity in Definition 12.1,

```text
|I_{e,A,F}^{D,Lambda_*}(mu_eta)|
  <= Def_proj(eta,D,Lambda_*).
```

Proof.

The exact unprojected Schwinger-Dyson expression has expectation zero by
Theorem 10.2. The projected expression differs from it by the off-battery
remainder. The expectation of that remainder is bounded by the definition of
`Def_proj`. `square`

### Definition 12.3: BLU Closing Sequence

A BLU closing sequence is a pair of increasing sequences

```text
D_n -> infinity,       Lambda_n -> Irrep(SU(N)),
```

such that:

1. the projected ledgers for `(D_n,Lambda_n)` are compatible under inclusion;
2. the projection defects vanish:

   ```text
   Def_proj(eta_n,D_n,Lambda_n) -> 0;
   ```

3. the limiting projected identities determine the moments of
   `B_CC^inf`.

### Theorem 12.4: BLU From The Closing Sequence

If there exists a BLU closing sequence for the actual continuum trajectory,
then `BLU(s_0,L)` holds.

Proof.

Let `nu` and `nu'` be two subsequential finite-block limits. Lemma 12.2 and
the vanishing projection defects imply that both limits satisfy the same
limiting projected identities at every level `n`. The closing sequence says
these identities determine all moments of `B_CC^inf`. Theorem 11.5 then
implies that `nu` and `nu'` agree on every finite battery. Hence the
finite-block limit is unique. This is `BLU(s_0,L)`. `square`

### Honest Boundary 12.5: What Remains For BLU

The exact compact-group identity is proved. The BLU theorem is therefore
reduced to three concrete constructive estimates:

1. off-battery projection defects vanish as the battery is enlarged;
2. the projected identities are compatible across enlargements;
3. the limiting identities determine the countable battery moments.

If any of these fail, Paper 14 must enlarge the record set rather than hide
the failure inside a fictitious Markovian local dynamics.

## 13. Step 4: Hardened CE Coefficient Window

### Definition 13.1: Finite Character Tail

Let `Lambda_*` be the finite representation set used by the coefficient
battery. For a central density `k` on `SU(N)`, define the untested character
tail by

```text
Tail_Lambda_*(k)
  = sum_{lambda notin Lambda_*} d_lambda |u_lambda(k)|.
```

Any stronger norm may be used if it dominates the tested coefficient
functionals and is stable under the whole-process comparison ledger.

### Lemma 13.2: Heat-Kernel Tail Is Finite At Positive Time

For the heat-kernel reference `K_t` with `t>0`,

```text
Tail_Lambda_*(K_t)
  = sum_{lambda notin Lambda_*} d_lambda exp(-t C_2(lambda)/2)
```

is finite after choosing `Lambda_*` with sufficiently large Casimir cutoff,
and tends to zero as `Lambda_*` exhausts the irreducibles.

Proof.

For compact `SU(N)`, representation dimensions grow polynomially in the
highest weight, while the quadratic Casimir grows quadratically. The
exponential factor therefore dominates the polynomial dimension growth for
every `t>0`. The tail is summable and vanishes under exhaustion. `square`

### Definition 13.3: CE Reserve

Choose `t>0`, a finite representation set `Lambda_*`, and an error
`delta_CE`. Define

```text
u_ref = exp(-t C_2(rho)/2),
u_- = u_ref - delta_CE,
u_+ = u_ref + delta_CE,
Tail_CE = Tail_Lambda_*(K_t) + delta_tail.
```

The CE reserve is positive if

```text
0 < u_- <= u_+ < u_crit
```

and

```text
M_CE
  = u_-^{N_0}(1-u_+^{Q_sigma}) - Tail_CE > 0.
```

### Theorem 13.4: Heat-Kernel Neighborhood Proves CE With Reserve

Assume the actual block plaquette marginal is central and satisfies:

```text
||nu_P - K_t dU||_TV <= delta_CE,
Tail_actual <= Tail_Lambda_*(K_t) + delta_tail.
```

If the CE reserve `M_CE` of Definition 13.3 is positive, then
`CE(s_0,rho,L)` holds with exported margin at least `M_CE`.

Proof.

Corollary 6.6 gives `u_- <= u_rho(P) <= u_+`. The tail assumption gives the
off-channel coefficient bound. The two displayed inequalities in Definition
13.3 are exactly the positive subcritical coefficient window required by
Definition 6.3. Therefore Proposition 6.4 proves `CE`, and the margin bound
is `M_CE`. `square`

### Honest Boundary 13.5: CE Is A Real Dynamical Estimate

The heat-kernel calculation is not a claim that continuum Yang-Mills is a
one-plaquette heat-kernel theory. It supplies a reference domain with explicit
constants. The actual missing estimate is the RG comparison:

```text
actual block plaquette marginal
  is within (delta_CE, delta_tail)
  of a positive-time central character domain.
```

If this cannot be proved, the `CE` gate is not closed.

## 14. Step 5: Whole-Process Certificate Ledger

### Definition 14.1: Paper-14 Defect Vector

For a cutoff tuple `eta`, define the Paper-14 defect vector

```text
E_14(eta)
  = (
      E_ID(eta),
      E_proj(eta),
      E_CE(eta),
      E_tail(eta),
      E_chart(eta),
      E_ct(eta),
      E_vol(eta),
      E_cov(eta),
      E_RP(eta)
    ).
```

The entries mean, respectively:

1. raw identity defect;
2. finite-battery projection defect;
3. coefficient-window error;
4. untested representation-tail error;
5. gauge-chart transition defect;
6. counterterm reparametrization defect;
7. finite-volume boundary defect;
8. Euclidean covariance defect;
9. reflection-positivity defect on the finite battery.

All entries are defined by comparing pushed-forward whole-process laws on a
common finite battery.

### Definition 14.2: Transport Norm

Fix nonnegative weights `alpha_i` and define

```text
||E_14(eta)||_tr
  = alpha_ID E_ID
  + alpha_proj E_proj
  + alpha_CE E_CE
  + alpha_tail E_tail
  + alpha_chart E_chart
  + alpha_ct E_ct
  + alpha_vol E_vol
  + alpha_cov E_cov
  + alpha_RP E_RP.
```

The weights are chosen large enough to dominate the Lipschitz constants of
the finite record functionals used in `BLU`, `CE`, and `WP`.

### Theorem 14.3: Summable Transport Proves WP And Preserves Entry

Assume there is an admissible continuum chain `eta_n` such that

```text
sum_n ||E_14(eta_n)||_tr < infinity
```

and the tail of this series from scale `n` onward tends to zero. Then the
Paper-14 certificate is path independent on the declared battery. If, in
addition, the limiting CE reserve is larger than the total coefficient and
transport loss, then `FBE(s_0,rho,L)` is preserved along the chain.

Proof.

The summable bound makes the sequence of pushed-forward whole-process laws
Cauchy on every declared record functional controlled by the transport norm.
Common-refinement comparisons show that two admissible chains have the same
limit whenever their merged chain has summable defect. This is `WP`.

The BLU identities and CE coefficient inequalities are stable under
perturbations bounded by the same transport norm because the weights dominate
their Lipschitz constants. If the positive CE reserve exceeds the accumulated
loss, the inequalities remain strict at the limit. Therefore `FBE` is
preserved. `square`

### Proposition 14.4: Reflection Positivity Is A Ledger Entry, Not A Bonus

If reflection positivity is proved only before gauge-chart or counterterm
transport, it cannot be used later unless its transport defect `E_RP` is
included in the summable ledger.

Proof.

Reflection positivity is an inequality for a finite list of reflected record
polynomials. A chart or counterterm transition changes the pushed-forward law
on which the inequality is evaluated. The inequality survives only if that
change is bounded by a defect smaller than the positivity margin, or if the
transition preserves the inequality exactly. This is precisely the role of
`E_RP`. `square`

## 15. Step 6: Export Constants To Paper 15

### Definition 15.1: Paper-15 Export Package

If Paper 14 closes, it exports the finite tuple

```text
X_14(s_0,L,rho)
  = (
      nu_{s_0,L},
      u_-,
      u_+,
      M_CE,
      Tail_CE,
      E_14^*,
      Lambda_*,
      D_*,
      L_tr
    ).
```

Here:

1. `nu_{s_0,L}` is the unique finite-block continuum law;
2. `u_-` and `u_+` are the leading character coefficient bounds;
3. `M_CE` is the positive CE reserve;
4. `Tail_CE` is the untested coefficient tail;
5. `E_14^*` is the total remaining whole-process transport budget;
6. `Lambda_*` and `D_*` are the representation and degree cutoffs used in the
   certificate;
7. `L_tr` is the finite list of Lipschitz constants for the record
   functionals exported to Paper 15.

### Theorem 15.2: Export Package Is Sufficient For Paper 15 Inputs

The tuple `X_14(s_0,L,rho)` supplies exactly the Paper-15 inputs needed to
attack `RPF`, `KP_dec`, and `SUB`: a unique finite-block law, a leading sheet
coefficient window, a coefficient tail, and a residual transport budget.

Proof.

`RPF` and `KP_dec` require a fixed limiting law to factor into local residual
pieces; this is `nu_{s_0,L}`. `SUB` requires a positive leading coefficient
and explicit tail/transport losses; these are `u_-`, `u_+`, `M_CE`,
`Tail_CE`, and `E_14^*`. The finite cutoffs and Lipschitz constants specify
the exact record class on which Paper 15 may operate. `square`

### Export Boundary 15.3

Paper 15 may use the package `X_14`. It may not assume:

1. a mass gap;
2. confinement;
3. residual polymer locality;
4. surface subcriticality beyond the coefficient reserve;
5. a Hilbert-space particle interpretation;
6. any chart-dependent microscopic field as part of the ontology.

Those must be proved later, or not claimed.

## 16. Identity Basis For The BLU Ledger

The projected ledger becomes useful only after we name the identities that
are allowed to determine the battery law.

### Definition 16.1: Basic Record Monomials

Let `M_{D,Lambda_*}` be the finite set of monomials generated by:

1. Creutz loop records in Definition 11.1;
2. block plaquette character records `Phi_lambda(P)` with
   `lambda in Lambda_*`;
3. reflected copies of those records;
4. products of total degree at most `D`.

Write

```text
m_alpha,       alpha in A_{D,Lambda_*},
```

for an enumeration of `M_{D,Lambda_*}`. The moment coordinates are

```text
x_alpha(nu) = int m_alpha dnu.
```

### Definition 16.2: Identity Basis

The identity basis `ID_{D,Lambda_*}` consists of:

1. normalization:

   ```text
   x_1 = 1;
   ```

2. conjugation/centrality identities for block plaquette records;
3. reflected positivity inequalities

   ```text
   int F theta(F) dnu >= 0
   ```

   for every reflected battery polynomial `F` of degree at most `D/2`;
4. Euclidean covariance identities between translated and rotated battery
   records whose supports remain inside the test box;
5. projected Schwinger-Dyson identities from Definition 12.1;
6. projected finite loop identities obtained by summing the Schwinger-Dyson
   identities over links along a loop deformation.

The basis is ordered by the complexity rank

```text
rank(m_alpha)
  = (degree, total Casimir, support diameter, reflection depth),
```

with lexicographic order.

### Definition 16.3: Closure Matrix

Fix the ordered moment vector

```text
x = (x_alpha)_{alpha in A_{D,Lambda_*}}.
```

After projection, the equalities in `ID_{D,Lambda_*}` can be written as

```text
M_{D,Lambda_*} x = b_{D,Lambda_*} + R_{D,Lambda_*}(x),
```

where:

1. `M_{D,Lambda_*}` is the linear part in the chosen ordered moments;
2. `b_{D,Lambda_*}` contains known constants and lower-rank boundary terms;
3. `R_{D,Lambda_*}` contains nonlinear or off-rank terms whose Lipschitz
   constant is measured on the compact battery state space.

This is not a microscopic dynamical equation. It is a relation among
expectations of declared records in one whole pushed-forward law.

## 17. Triangular Closure For BLU

### Definition 17.1: Triangular Moment Closure

The identity basis has triangular moment closure at `(D,Lambda_*)` if there
is a subset of equalities in `ID_{D,Lambda_*}` and an ordering of the moment
coordinates such that:

1. each new equation solves one highest-rank moment in terms of lower-rank
   moments and already solved same-rank moments;
2. every diagonal coefficient is bounded below:

   ```text
   |diag_alpha| >= kappa_D > 0;
   ```

3. the nonlinear remainder has triangular Lipschitz norm

   ```text
   Lip_tri(R_{D,Lambda_*}) <= r_D < kappa_D;
   ```

4. the unsolved moment coordinates are fixed by normalization, centrality,
   covariance, reflection positivity extremality, or are declared as
   additional records in the next enlarged battery.

### Theorem 17.2: Triangular Closure Determines The Finite Battery Law

Assume triangular moment closure holds at every level of a closing sequence
`(D_n,Lambda_n)`, with

```text
inf_n (kappa_{D_n} - r_{D_n}) > 0,
```

and with projection defects tending to zero. Then the limiting projected
identities determine all moments of `B_CC^inf`, and hence `BLU(s_0,L)` holds.

Proof.

At each finite level, triangular closure solves the ordered moments
recursively. The lower bound on the diagonal and the strict Lipschitz gap make
each recursive step unique: if two candidate moment vectors agree on lower
rank moments, their difference at the next solved coordinate is bounded by
`r_D/kappa_D` times already solved differences, hence is zero. Normalization,
centrality, covariance, and reflected positivity fix the seed coordinates
specified in Definition 17.1.

Compatibility of the closing sequence carries the solved moments to the
countable completion. Projection defects vanish, so every subsequential block
limit satisfies the same limiting triangular system. Thus two subsequential
limits agree on all moments of `B_CC^inf`. Theorem 11.5 implies equality on
every finite battery, and Theorem 12.4 gives `BLU(s_0,L)`. `square`

### Proposition 17.3: What Triangular Closure Cannot Hide

If a same-rank block of the closure matrix has a nontrivial kernel not fixed
by positivity, covariance, centrality, or declared seed moments, then the
identity basis does not determine the finite battery law.

Proof.

A nontrivial kernel direction gives two infinitesimally distinct moment
vectors satisfying the same linearized identities. If the direction is not
removed by positivity, covariance, centrality, or a declared seed value, the
identities leave at least one moment undetermined. Therefore the ledger is
not determining at that level. `square`

### Honest Boundary 17.4

Theorem 17.2 is a real advance, but it is conditional on a structural fact
about the finite loop identity system. Paper 14 must either prove triangular
closure for the declared battery or identify the kernel directions that force
additional records.

## 18. Battery Enlargement If Closure Fails

### Definition 18.1: Forced Record

A forced record is an off-battery expression `G` or unresolved moment
direction that appears in the projected identities and cannot be controlled
by:

1. a vanishing projection defect;
2. triangular closure;
3. positivity/covariance/centrality;
4. the existing coefficient and transport ledgers.

### Definition 18.2: Closure-Enriched Battery

Given a battery `B`, define its one-step closure enrichment `E(B)` by adding:

1. every forced record generated by the projected Schwinger-Dyson and loop
   identities up to the current degree;
2. its reflected partner, if reflection is defined in the test box;
3. all products with existing records up to the declared degree;
4. all representations produced by tensoring the newly added character
   records with `rho`, `bar rho`, and the current `Lambda_*`.

Iterating gives

```text
B subset E(B) subset E^2(B) subset ...
```

### Theorem 18.3: Enrichment Restores Determinacy Or Exposes An Obstruction

Assume that at each enrichment step all newly forced records are bounded
continuous functions on the cutoff configuration space and that the enlarged
battery remains finite at each finite stage. Then exactly one of the
following holds:

1. after finitely or countably many enrichments, the identity basis admits a
   closing sequence and proves `BLU`;
2. the enrichment produces an infinite non-summable tower of forced records;
3. the identities leave a genuine continuum family of finite-block laws.

Proof.

At each finite stage, compactness of the battery state space is preserved.
If the triangular closure criterion eventually holds along a compatible
closing sequence, Theorem 17.2 proves `BLU`. If not, then either the forced
records form a non-summable tower, so no finite operational battery closes
the identities with controlled defects, or some unresolved kernel direction
persists at every stage. The latter yields a continuum family of laws
compatible with all declared identities, by compactness and Proposition 17.3.
These alternatives exhaust the failure modes. `square`

### Barandes Alignment 18.4

Enrichment is not a retreat from ISP. It is the disciplined Barandes-aligned
move: when the record laws are not determined by the declared records, one
declares the additional operational records needed to state the law. The
forbidden move would be to pretend an undeclared microscopic field or a
composed partial kernel has already supplied the missing information.

## 19. Actual-RG Estimate For CE

### Definition 19.1: RG Character-Domain Certificate

The actual continuum trajectory satisfies `RGCE(s_0,rho,L)` if there exist:

1. a positive heat-kernel time `t_0>0`;
2. a representation cutoff `Lambda_*`;
3. errors `delta_CE`, `delta_tail`;
4. a central reference density `K_{t_0}`;
5. a block plaquette marginal `nu_P` of the unique finite-block law;

such that:

```text
||nu_P - K_{t_0} dU||_TV <= delta_CE,
Tail_actual <= Tail_Lambda_*(K_{t_0}) + delta_tail,
M_CE(t_0,delta_CE,delta_tail,Lambda_*) > 0.
```

The certificate is allowed to use constructive RG estimates, but the output
must be a statement about the pushed-forward block plaquette record law.

### Theorem 19.2: RGCE Closes CE

If `BLU(s_0,L)` holds and `RGCE(s_0,rho,L)` holds, then
`CE(s_0,rho,L)` holds with positive exported reserve `M_CE`.

Proof.

`BLU` gives the unique finite-block law and hence a well-defined block
plaquette marginal. `RGCE` supplies the exact hypotheses of Theorem 13.4.
Therefore `CE` holds with the stated reserve. `square`

### Proposition 19.3: Perturbative AF Is Not Enough For RGCE

Asymptotic freedom at arbitrarily small lattice spacing does not by itself
imply `RGCE(s_0,rho,L)` at a fixed physical block scale.

Proof.

Asymptotic freedom controls the ultraviolet running of the bare coupling and
local perturbative expansions at sufficiently short distances. `RGCE`
requires a nonperturbative statement about the full pushed-forward block
plaquette law at physical scale `s_0`: centrality, total-variation proximity
to a positive-time character domain, tail control, and positive coefficient
reserve. These are stronger than the perturbative beta-function statement.
`square`

### Work Target 19.4

The concrete CE task is now:

```text
constructive RG at block scale s_0
=> total-variation or stronger character-domain control
=> RGCE
=> CE.
```

If total variation is too strong, Paper 14 may replace it by any norm that
dominates the tested character coefficients and the Paper-15 tail estimates.

## 20. Concrete WP Chain

### Definition 20.1: Standard Continuum Chain

A standard Paper-14 continuum chain is a sequence

```text
eta_n = (a_n,V_n,q_n,ct_n)
```

with:

1. `a_n -> 0`;
2. `V_n` exhausting Euclidean space while containing the fixed physical test
   box with buffer distance `b_n -> infinity`;
3. `q_n` chosen from a finite atlas of gauge charts on the battery
   certificate region;
4. `ct_n` chosen from the running local action ledger of Paper 11;
5. all laws pushed forward to the same finite battery
   `B_CC(s_0,L,rho,D_n,Lambda_n)`.

### Definition 20.2: Rate Certificate

The standard chain has a rate certificate if there are nonnegative sequences

```text
eps_ID,n, eps_proj,n, eps_CE,n, eps_tail,n,
eps_chart,n, eps_ct,n, eps_vol,n, eps_cov,n, eps_RP,n
```

such that each corresponding defect in `E_14(eta_n)` is bounded by the
matching `eps` sequence and

```text
sum_n (
 eps_ID,n + eps_proj,n + eps_CE,n + eps_tail,n
 + eps_chart,n + eps_ct,n + eps_vol,n + eps_cov,n + eps_RP,n
) < infinity.
```

### Theorem 20.3: Rate Certificate Gives WP

If a standard continuum chain has a rate certificate, then the
whole-process gate `WP(s_0,L)` holds along that chain. If any two standard
chains admit a common refinement chain with a rate certificate, then `WP`
is independent of the standard chain.

Proof.

The rate certificate is a concrete instance of the summable transport norm in
Theorem 14.3. Summability gives Cauchy convergence of all finite record
expectations and vanishing comparison defect between common refinements.
Therefore the entry certificate is chain independent. `square`

### Proposition 20.4: Polynomial Rates Suffice With Scale Separation

Suppose the defects obey

```text
eps_*,n <= C_* n^{-1-p_*}
```

for some `p_*>0`, or obey exponential decay in the buffer distance or
representation cutoff. Then the rate certificate is summable.

Proof.

The series `sum_n n^{-1-p_*}` converges, and exponential tails are summable.
Finite sums of summable sequences are summable. `square`

## 21. Updated Paper-14 Closure Theorem

### Theorem 21.1: Paper 14 Gate Closure

Assume:

1. a BLU closing sequence exists, or equivalently the triangular/enriched
   identity program of Sections 17--18 closes;
2. `RGCE(s_0,rho,L)` holds with positive reserve;
3. a standard continuum chain has a rate certificate, and common refinements
   do also.

Then `FBE(s_0,rho,L)` holds. Consequently Paper 13 gives `BC`, `CE`, and
`WP`, and Paper 15 may begin with the export package `X_14`.

Proof.

The first assumption proves `BLU` by Theorem 12.4 or Theorem 17.2. The second
assumption proves `CE` by Theorem 19.2. The third proves `WP` by Theorem
20.3. Thus every clause of `FBE` holds by Definition 4.1. The export
statement is Theorem 15.2. `square`

### Honest Boundary 21.2

Paper 14 has now reduced its problem to three exact certificates:

```text
BLU closing sequence
+ RGCE character-domain certificate
+ WP rate certificate
=> FBE.
```

This is as far as Paper 14 should go without importing new constructive
four-dimensional Yang-Mills estimates. It is a sharp theorem-level reduction,
not an unconditional construction of continuum Yang-Mills.

## 22. Test: First Nontrivial Creutz-Character Battery

We now test the triangular closure criterion on the first nontrivial battery.
This is a diagnostic step, not a claim of closure.

### Definition 22.1: The First Creutz Battery `B_0`

Take `G=SU(N)` in four Euclidean dimensions, fix a nontrivial representation
`rho`, and take the smallest planar Creutz rectangle:

```text
R=T=1.
```

Let `S_{2x2}` be the planar `2 by 2` block plaquette sheet. The first
Creutz-character battery `B_0` contains:

1. the four scalar loop records

   ```text
   W(1,1), W(2,1), W(1,2), W(2,2);
   ```

2. the central records `Phi_rho(P)` and `Phi_bar_rho(P)` for the plaquettes
   `P subset S_{2x2}`;
3. the reflected copies needed for the first reflection-positivity tests;
4. degree-one products only.

It does not contain loops deformed out of the `2 by 2` sheet, nonplanar
staple loops, or products generated by differentiating higher-degree
monomials.

This is the smallest battery that can even state the block Creutz ratio and
the leading character coefficient.

### Definition 22.2: One-Staple Deformation Records

Let `C` be one of the four Creutz loops and let `e` be an oriented link on
`C`. Let `p` be a plaquette sharing `e` but not contained in the planar sheet
`S_{2x2}`. The one-staple deformation

```text
C triangleleft_e p
```

is the closed loop obtained by replacing the segment `e` of `C` by the other
three sides of `p`. The corresponding scalar record is

```text
W(C triangleleft_e p).
```

If the action contains plaquette characters in representations
`lambda in Lambda_action`, the differentiated identity may also generate
the representation channels appearing in `rho tensor lambda` and
`rho tensor bar lambda`.

### Lemma 22.3: The Finite Loop Identity Produces Exterior Staples

Assume the finite-cutoff local action contains a nonzero plaquette term on
every plaquette adjacent to the support of the Creutz loops. Then applying
the compact-group Schwinger-Dyson identity to any nontrivial Creutz loop
record `W(C)` produces, among its action-insertion terms, exterior
one-staple deformation records `W(C triangleleft_e p)` for plaquettes
`p` sharing a boundary link of `C`.

Proof.

For a link `e` on `C`, the derivative `L_e^A S_eta` is a sum of derivatives
of local action terms involving plaquettes that contain `e`. In a plaquette
action this is exactly the finite staple sum; in a local improved action it
contains the plaquette staple terms plus longer local terms. Multiplying by
`L_e^A W(C)` and summing over the Lie algebra index contracts the generator
insertions by the standard completeness relation. The resulting
gauge-invariant scalar terms are closed loops obtained by replacing the link
segment of `C` with the complementary path around each adjacent plaquette.
For adjacent plaquettes outside `S_{2x2}`, these are precisely the exterior
one-staple deformation records. The coefficients are nonzero whenever the
corresponding plaquette action coefficient is nonzero. `square`

### Lemma 22.4: Exterior Staples Are Not `B_0`-Measurable

For four-dimensional `SU(N)` with the battery `B_0`, an exterior one-staple
deformation record is not a function of the records in `B_0`.

Proof.

Fix the link variables in the planar sheet `S_{2x2}` so that every record in
`B_0` is fixed. Choose an exterior plaquette `p` sharing exactly one boundary
link with the sheet, and vary an exterior link of `p` that is not used by any
loop or plaquette record in `B_0`. This variation leaves every record in
`B_0` unchanged, but it changes the holonomy of the deformed loop
`C triangleleft_e p` for a generic choice of the remaining links. Therefore
`W(C triangleleft_e p)` is not measurable with respect to the sigma-algebra
generated by `B_0`. `square`

### Theorem 22.5: The First Creutz Battery Does Not Close

For a four-dimensional local `SU(N)` plaquette-containing action with
nonzero adjacent plaquette coefficients, the identity basis on `B_0` does
not have exact triangular moment closure.

More precisely, the first projected Schwinger-Dyson/loop identities produce
exterior one-staple deformation records that are not functions of `B_0`.
Thus the exact closure matrix for `B_0` has off-battery terms. Triangular
closure can hold only after either:

1. those terms are proved to have vanishing projection defect along the
   actual continuum trajectory; or
2. the corresponding one-staple deformation records are added to the
   declared battery.

Proof.

Lemma 22.3 shows that the exact finite loop identity contains exterior
one-staple deformation records with nonzero coefficients. Lemma 22.4 shows
that those records are not functions of `B_0`; hence they cannot be rewritten
as exact linear or nonlinear functions of the `B_0` moment coordinates. The
identity therefore cannot be triangularly closed inside `B_0` as an exact
record identity. The only legitimate alternatives are to prove the
projection defects vanish as dynamical estimates or to declare the missing
records and enlarge the battery. `square`

### Definition 22.6: First Forced Enlargement `B_1`

The first forced enlargement `B_1=E(B_0)` is obtained by adding:

1. all exterior one-staple deformations `W(C triangleleft_e p)` for the four
   Creutz loops, every boundary link `e`, and every adjacent plaquette `p`;
2. the nonplanar staple loops generated by transverse plaquettes in the two
   directions orthogonal to the original Creutz plane;
3. the same-plane exterior extension loops generated by plaquettes adjacent
   to the `2 by 2` sheet;
4. all representation channels generated by the action representation set
   under tensoring with `rho` and `bar rho`;
5. reflected copies of the new records;
6. products with the original battery records up to the declared degree.

### Corollary 22.7: First Test Outcome

The first nontrivial Creutz-character battery fails exact triangular closure.
The forced-record output of the test is the one-staple enlarged battery
`B_1`.

This is a positive diagnostic result: it tells Paper 14 exactly what must be
added before the next closure test. It is not a failure of the ISP program.
It is the Barandes-aligned discipline of letting the declared operational
records grow when the record laws demand more information.

### Next Test 22.8

The next triangular closure test should be run on `B_1`. There are two
possible outcomes.

1. The one-staple identities close up to summable projection defects. Then
   `B_1` is a plausible finite seed for the BLU closing sequence.
2. Differentiating the one-staple records forces two-staple, corner,
   larger-rectangle, or local action-density records. Then the enrichment
   continues:

   ```text
   B_0 subset B_1 subset B_2 subset ...
   ```

The key question is not whether forced records appear. They do. The key
question is whether the forced-record tower is summable/local enough to
support the Paper-14 `BLU` closing sequence.

## 23. Test: One-Staple Battery And Forced-Record Growth

We now run the next test. The goal is not to pretend that `B_1` magically
closes. The goal is to learn whether the new failures are still local and
whether their growth has a plausible summability criterion.

### Definition 23.1: One-Staple Battery `B_1`

Let `B_1` be the first forced enlargement of Definition 22.6. Its new
primitive loop records are the one-staple deformations

```text
W(C triangleleft_e p),
```

where `C` is one of the four Creutz loops, `e` is a boundary link of `C`, and
`p` is an adjacent plaquette not already represented in the planar
`2 by 2` sheet.

The battery also contains the reflected copies, the representation channels
generated by the local action, and finite products up to the declared degree.

### Definition 23.2: Forced Record Types At The Next Step

Differentiating a one-staple loop record can force the following record
types.

1. **Retraction records.** The new plaquette cancels the previous staple and
   returns to a loop already in `B_0`.
2. **Two-staple records.** A second adjacent plaquette is attached to a link
   of the one-staple loop.
3. **Corner records.** The second staple shares a corner with the first
   staple, producing a bent nonplanar local detour.
4. **Rectangle-extension records.** The second plaquette lies in the original
   Creutz plane and enlarges the rectangle by one plaquette along one side.
5. **Transverse-sheet records.** The second plaquette lies in one of the two
   transverse directions in four dimensions.
6. **Local action-density records.** If the local action contains improved
   loops or higher-character terms, the derivative of the action produces the
   corresponding finite local loop insertion records.

Every item is a gauge-invariant scalar record after the Lie algebra indices
are contracted in the Schwinger-Dyson identity.

### Lemma 23.3: Differentiating `B_1` Produces `B_2`-Type Records

For a four-dimensional local plaquette-containing `SU(N)` action,
Schwinger-Dyson identities applied to primitive one-staple records in `B_1`
produce records of the six types in Definition 23.2. In general, at least one
two-staple, corner, rectangle-extension, or transverse-sheet record is not a
function of `B_1`.

Proof.

Choose a link on the one-staple loop. The derivative of the action again
sums over local action terms containing that link. For a plaquette action,
these are the plaquette staples adjacent to the chosen link. Contracting the
generator insertion in the differentiated loop with the generator insertion
from the differentiated action replaces the chosen link segment by the
complementary path in the adjacent plaquette. If the adjacent plaquette is the
inverse of the first staple, the record retracts to `B_0`. If it is distinct,
the result is a second local plaquette detour. Depending on its position, this
is a two-staple, corner, rectangle-extension, or transverse-sheet record.
Improved local action terms give the same conclusion with the plaquette
replaced by the finite local loop appearing in the action.

To see that new records are not functions of `B_1`, fix all link variables
appearing in `B_1` and vary an exterior link used only by the second added
plaquette. For a generic configuration, this changes the new deformed loop
while leaving all `B_1` records fixed. Hence the new record is not
`B_1`-measurable. `square`

### Definition 23.4: The Second Forced Enlargement `B_2`

The second forced enlargement `B_2=E(B_1)` is obtained by adding:

1. all two-staple loop records generated by differentiating one-staple
   records;
2. all corner and bent nonplanar loop records generated at this step;
3. all one-plaquette rectangle-extension records;
4. all transverse-sheet records with two local plaquette detours;
5. all local action-density insertion records generated by improved action
   terms of the cutoff action;
6. all representation channels produced by tensoring the previous channels
   with the action channels;
7. reflected copies and finite products up to the declared degree.

### Theorem 23.5: `B_1` Does Not Close Exactly

For a four-dimensional local plaquette-containing `SU(N)` action with
nonzero adjacent plaquette coefficients, the one-staple enlarged battery
`B_1` does not have exact triangular closure. The next forced battery is
`B_2`.

Proof.

Lemma 23.3 shows that the exact Schwinger-Dyson identities for primitive
records in `B_1` produce records not measurable with respect to `B_1`.
Therefore the identities cannot be rewritten as a closed triangular system on
`B_1` moments alone. The missing records are precisely the forced additions
listed in Definition 23.4. `square`

### Definition 23.6: Collar Depth And Complexity

For a forced loop record `W(C')`, define:

1. `depth(C')`: the minimal plaquette-collar distance from `C'` to the
   original `2 by 2` Creutz sheet;
2. `staple_number(C')`: the number of local detours added after `B_0`;
3. `length(C')`: the number of oriented links in a reduced representative of
   the loop;
4. `rep_weight(C')`: the total Casimir of representation channels appearing
   in the record.

Define the total complexity

```text
K(C') = length(C') + depth(C') + staple_number(C') + rep_weight(C').
```

### Theorem 23.7: One-Step Locality-Growth Bound

Assume the cutoff action is local with interaction range `r_A` in plaquette
collar distance and contains finitely many representation channels at each
cutoff. Then one Schwinger-Dyson differentiation step sends a forced loop
record of complexity `K` to a finite linear combination of records with:

```text
depth <= depth_old + r_A,
length <= length_old + 2 r_A + c_A,
staple_number <= staple_number_old + r_A,
rep_weight <= rep_weight_old + C_A,
```

where `c_A` and `C_A` depend only on the finite local action stencil and its
representation channels. The number of new primitive records generated at
one step is bounded by

```text
N_step <= C_geom(d,r_A,A_stencil),
```

with `d=4`.

Proof.

The derivative of the local action at a link only sees action terms whose
support intersects that link and lies within range `r_A`. Replacing a link
segment by the complementary path around such a local action term can enlarge
the loop support only by that local collar. The path length increases by at
most the maximum boundary length of the local action stencil minus the
replaced segment; this is `2 r_A + c_A` after absorbing stencil constants.
The number of added detours is bounded by the number of plaquette-collar
steps in the local term, hence by `r_A`. Tensoring with the finite action
representation channels increases total Casimir by at most `C_A` for one
step. Finally, a finite-dimensional hypercubic lattice has only finitely many
local action stencils adjacent to a link, giving the displayed branching
bound. `square`

### Definition 23.8: Forced-Tower Summability Criterion

Let `B_k=E^k(B_0)` be the forced-record tower. Let `A_k` be the maximal
absolute coefficient, transport weight, or connected-cumulant weight attached
to primitive records first appearing at depth `k`. The tower is summable if

```text
sum_{k>=0} N_k A_k < infinity,
```

where `N_k` is the number of primitive record types first appearing at depth
`k`.

A sufficient exponential criterion is:

```text
N_k <= C_0 C_geom^k,
A_k <= A_0 exp(-m k),
m > log C_geom.
```

More generally, any KP-style polymer norm that dominates
`sum_k N_k A_k` is sufficient.

### Theorem 23.9: Summable Forced Tower Gives A Candidate BLU Closing Sequence

Assume:

1. the forced tower `B_k` satisfies the locality-growth bound of Theorem
   23.7;
2. the forced-tower summability criterion of Definition 23.8 holds;
3. the projected identities are compatible under the inclusions
   `B_k subset B_{k+1}`;
4. the remaining projected identity defects vanish along the continuum chain.

Then the tower `B_0 subset B_1 subset B_2 subset ...` gives a candidate
`BLU` closing sequence in the sense of Definition 12.3.

Proof.

The locality-growth bound keeps every finite stage finite and operational.
Summability makes the total contribution of newly forced records Cauchy in
the record norm used for the identity ledger. Compatibility under inclusion
prevents contradictions between finite stages, and vanishing projected
defects ensures that limiting subsequential laws satisfy the same tower of
identities. Therefore the tower supplies the closing-sequence data, except
for the remaining determinacy check of the limiting countable identity
system. This is exactly a candidate `BLU` closing sequence. `square`

### Fork 23.10: Outcome Of The `B_1` Test

The `B_1` test has the following outcome.

1. Exact finite closure fails again: `B_1` forces `B_2`.
2. The failure is local: one identity step expands support by a bounded
   collar and has finite branching.
3. The remaining nontrivial issue is summability of the forced tower.

Thus Paper 14 has not proved `BLU`, but it has sharpened the problem:

```text
prove forced-tower summability + limiting determinacy
or report a finite-block obstruction.
```

This is the right ontology. The theory is asking for more operational
records; we declare them and then test whether their tower is controlled.

## 24. Full Forced-Tower Theorem

The first two tests show that finite exact closure is the wrong expectation.
The right finite-block question is whether the forced tower is still a
controlled operational object.

### Definition 24.1: Full Forced-Record Tower

Starting from the first Creutz battery `B_0`, define recursively

```text
B_{k+1}=E(B_k),
```

where `E` is the closure-enrichment operation of Definition 18.2, including
all records forced by one projected Schwinger-Dyson/loop-identity step,
their reflected copies, necessary representation channels, and finite
products up to the declared degree.

The full forced battery is the countable union

```text
B_infty = union_{k>=0} B_k.
```

`B_infty` is not treated as one completed microscopic state space. It is a
countable operational ledger: every actual test is performed on some finite
`B_k`, and only then are compatible finite-battery limits compared.

### Lemma 24.2: Finite-Stage Operational Legitimacy

For every finite `k`, the battery `B_k` is finite, gauge-invariant, reflected
on its declared reflected subregion, and compact as a record space.

Proof.

`B_0` is finite and compact by Lemma 11.2. If `B_k` is finite, then one
application of the local finite-stencil Schwinger-Dyson/loop identities
generates only finitely many forced records: finitely many primitive records,
finitely many adjacent action stencils, finitely many representation channels
at the cutoff, finitely many reflected copies, and finitely many products up
to the declared degree. Each generated record is a bounded continuous
gauge-invariant scalar function of compact link variables. Therefore
`B_{k+1}` is finite and compact. Induction proves the claim. `square`

### Theorem 24.3: All-Depth Locality And Branching Bound

Assume the cutoff action has finite plaquette-collar range `r_A`, finite local
stencil branching `C_geom`, path-length increment constant `c_A`, and
representation-weight increment `C_A`. If a primitive record first appears at
tower depth `k`, then its complexity satisfies:

```text
depth <= depth_0 + k r_A,
length <= length_0 + k(2 r_A + c_A),
staple_number <= staple_number_0 + k r_A,
rep_weight <= rep_weight_0 + k C_A.
```

Moreover the number `N_k` of primitive record types first appearing at depth
`k` obeys

```text
N_k <= N_0 C_geom^k.
```

Proof.

The one-step estimates are Theorem 23.7. Iterating the depth, length,
staple-number, and representation-weight inequalities gives the four linear
growth bounds. At each step, every primitive record produces at most
`C_geom` new primitive records, so induction gives the branching estimate
`N_k <= N_0 C_geom^k`. `square`

### Definition 24.4: Forced-Tower Summability `FTS(s_0,L)`

Let `A_k` be a bound on the total identity, projection, transport, or
connected-cumulant weight of primitive records first appearing at depth `k`,
measured in a norm dominating the finite record functionals used by the BLU
ledger. The forced tower satisfies `FTS(s_0,L)` if

```text
sum_{k>=0} N_k A_k < infinity.
```

It satisfies exponential `FTS` if there are constants `A_0>0`, `m>0`, and
`C_geom>=1` such that

```text
A_k <= A_0 exp(-m k),
N_k <= N_0 C_geom^k,
m > log C_geom.
```

The condition may be replaced by any KP-style polymer norm that implies the
same absolute convergence of forced-record tails.

### Lemma 24.5: `FTS` Gives Vanishing Tower Tails

If `FTS(s_0,L)` holds, then the tail contribution of records first appearing
after depth `K` vanishes:

```text
Tail_K := sum_{k>K} N_k A_k -> 0.
```

Proof.

The series in Definition 24.4 is convergent. Tails of a convergent series
vanish. `square`

### Definition 24.6: Limiting Tower Determinacy `LTD(s_0,L)`

The forced tower satisfies limiting tower determinacy if any two
subsequential continuum laws on the finite batteries that:

1. are compatible under the inclusions `B_k subset B_{k+1}`;
2. satisfy every limiting projected identity on every finite `B_k`;
3. have vanishing forced-tower tails in the `FTS` norm;

agree on every finite battery `B_k`.

Equivalently, the countable identity system on `B_infty` determines the
finite-dimensional distributions of the whole forced record ledger.

### Theorem 24.7: `FTS + LTD` Prove `BLU`

Assume:

1. finite-stage compactness holds for the forced tower;
2. the all-depth locality and branching bounds of Theorem 24.3 hold;
3. `FTS(s_0,L)` holds;
4. limiting tower determinacy `LTD(s_0,L)` holds;
5. the projected finite-identity defects vanish on every finite `B_k` along
   the continuum chain.

Then `BLU(s_0,L)` holds.

Proof.

Finite-stage compactness gives subsequential limits on every finite battery.
By a diagonal subsequence argument, every cutoff subnet has a further subnet
whose finite-battery laws converge compatibly on the countable tower. The
vanishing projected identity defects imply that any such limit satisfies the
limiting projected identities on each finite `B_k`. The `FTS` condition gives
vanishing tower tails by Lemma 24.5, so no unsummed forced-record remainder is
left outside the countable identity ledger. By `LTD`, any two such
subsequential limits agree on every finite `B_k`, in particular on the
original finite-block battery used for `FBE`. Thus all subsequential limits
agree, which is `BLU(s_0,L)`. `square`

### Corollary 24.8: Exponential Forced-Tower Decay Is Enough

If the all-depth branching bound holds with `N_k <= N_0 C_geom^k` and the
forced-record weights obey `A_k <= A_0 exp(-m k)` with
`m>log C_geom`, and if `LTD(s_0,L)` and finite identity-defect convergence
hold, then `BLU(s_0,L)` holds.

Proof.

The exponential estimates imply `FTS` by comparison with the geometric
series `sum_k exp(-(m-log C_geom)k)`. Theorem 24.7 applies. `square`

### Proposition 24.9: Meaning Of Failure Of `FTS`

If `FTS(s_0,L)` fails and no stronger norm, cancellation identity, or
additional declared coarse record restores summability, then the Paper-14
finite-block entry route cannot prove `BLU` from the forced-record tower.

This is not a proof that Yang-Mills does not exist. It is a precise
obstruction to this ISP finite-block entry strategy: the declared record law
requires infinitely many unsuppressed operational records before the
finite-block limit is determined.

Proof.

Without summability, tails of the forced tower need not vanish. Then a finite
identity ledger cannot control the contribution of records beyond any finite
depth `K`, and the diagonal limiting argument in Theorem 24.7 loses
closedness. If no replacement norm, cancellation identity, or declared
coarse record controls those tails, the forced-tower proof of `BLU` is
unavailable. `square`

### Theorem 24.10: Paper-14 BLU Reduction

For local finite-stencil cutoff actions, Paper 14 reduces `BLU(s_0,L)` to
the following two nonperturbative statements:

```text
FTS(s_0,L) + LTD(s_0,L).
```

Together with vanishing finite identity defects, these imply `BLU`.

Proof.

Local finite-stencil actions give finite-stage compactness and all-depth
locality/branching by Lemma 24.2 and Theorem 24.3. Adding `FTS`, `LTD`, and
vanishing identity defects gives the hypotheses of Theorem 24.7. `square`

### Section Boundary 24.11: Independent CE And WP Tasks

After the BLU route has been reduced to `FTS + LTD`, the remaining Paper-14
tasks split cleanly:

1. prove `RGCE(s_0,rho,L)`, the actual-RG character-domain estimate for the
   leading block plaquette coefficient;
2. prove the `WP` rate certificate along a standard continuum chain and its
   common refinements.

Thus the full Paper-14 gate can now be stated as:

```text
FTS + LTD + RGCE + WP-rate
=> BLU + CE + WP
=> FBE.
```

## 25. Canonical Forced-Record Weights

The symbol `A_k` in `FTS` must be a precise operational norm. This section
fixes one canonical choice. Other norms may be used only if they dominate the
same finite record functionals.

### Definition 25.1: Forced Shells

Let

```text
F_k = B_k \ B_{k-1}
```

be the primitive forced records first appearing at tower depth `k`, with
`F_0=B_0`. Let `Alg_k` be the unital algebra generated by `B_k`, with the
supremum norm on the compact record space.

### Definition 25.2: Projection Tail Norm

For a primitive forced record `f in F_k`, define its projection tail relative
to the previous battery by

```text
Tail_proj(f)
  = inf_{g in Alg_{k-1}, ||g||_infty <= ||f||_infty}
      sup_{nu in C_14} | int (f-g) dnu |.
```

Here `C_14` is the class of cutoff and subsequential continuum laws admitted
by the Paper-14 certificate. The infimum asks how well the new record can be
predicted by previously declared records, uniformly over the certified law
class.

### Definition 25.3: Connected-Cumulant Tail Norm

For `f in F_k`, define

```text
Tail_conn(f)
  = sup | kappa_nu(f; G_1,...,G_r) |,
```

where the supremum ranges over:

1. `nu in C_14`;
2. `1 <= r <= r_*`, with `r_*` the maximal order used in the projected
   identity ledger;
3. `G_i in Alg_{k-1}` with `||G_i||_infty <= 1`;
4. choices whose supports are those appearing in the finite identity and
   transport ledgers.

This is the record-level version of a connected-polymer norm. It does not
refer to virtual particles or hidden fields.

### Definition 25.4: Transport Tail Norm

Let `Lip_14(f)` be the Lipschitz constant of the record functional `f` with
respect to the finite whole-process transport metric used in the `WP` ledger.
Let `Def_14(k)` be the total unresolved transport defect for shell `F_k`.
Define

```text
Tail_tr(f) = Lip_14(f) Def_14(k).
```

### Definition 25.5: Canonical Forced Weight

For `f in F_k`, set

```text
a(f) = max {
  Tail_proj(f),
  Tail_conn(f),
  Tail_tr(f)
}.
```

The canonical shell weight is

```text
A_k = sup_{f in F_k} |c_f| a(f),
```

where `c_f` is the largest absolute coefficient with which `f` appears in
the projected Schwinger-Dyson, loop, or transport identity at the shell where
it is first forced.

### Lemma 25.6: The Canonical Weight Dominates The BLU Tails

If the finite identity ledger is evaluated on `B_K`, then the unresolved
contribution of forced records beyond depth `K` is bounded by

```text
sum_{k>K} N_k A_k.
```

Proof.

Every off-`B_K` term in the projected identities is a finite linear
combination of primitive forced records in shells `F_k`, `k>K`, multiplied by
coefficients bounded by `|c_f|`. Its expectation, connected contribution, or
transport error is bounded by the corresponding component of `a(f)`. Taking
the maximum and summing over at most `N_k` primitive records in each shell
gives the displayed bound. `square`

### Corollary 25.7: Canonical `FTS`

If

```text
sum_{k>=0} N_k A_k < infinity
```

for the canonical shell weights of Definition 25.5, then
`FTS(s_0,L)` holds.

Proof.

This is Definition 24.4 with the canonical dominating weights of Lemma 25.6.
`square`

## 26. Routes To `FTS`: KP, Clustering, And Area-Law Bounds

The previous section makes `FTS` a concrete estimate. This section gives
three sufficient routes. They are conditional estimates, not claims that
actual four-dimensional Yang-Mills already satisfies them.

### Definition 26.1: Forced-Collar Decay

The certified law class `C_14` satisfies forced-collar decay with constants
`C_F,m_F>0` if every primitive forced record `f in F_k` obeys

```text
a(f) <= C_F exp(-m_F k),
```

where `a(f)` is the canonical tail norm of Definition 25.5 before multiplying
by the finite identity coefficient.

If the coefficients also obey

```text
|c_f| <= C_c exp(g_c k),
```

then

```text
A_k <= C_F C_c exp(-(m_F-g_c)k).
```

### Theorem 26.2: Forced-Collar Decay Proves `FTS`

Assume the all-depth branching bound `N_k <= N_0 C_geom^k`. If forced-collar
decay holds and

```text
m_F - g_c > log C_geom,
```

then `FTS(s_0,L)` holds.

Proof.

The hypotheses give

```text
N_k A_k <= N_0 C_F C_c
  exp(-(m_F-g_c-log C_geom)k).
```

The exponent is negative by assumption, so the series over `k` converges.
Corollary 25.7 gives `FTS`. `square`

### Definition 26.3: KP Forced-Polymer Bound

A KP forced-polymer bound holds if each forced record `f in F_k` has a
polymer expansion with activities `z_gamma` such that:

```text
sum_{gamma touching f} |z_gamma| exp(alpha |gamma|)
  <= C_KP exp(-mu_KP k),
```

and this bound dominates `a(f)`.

### Corollary 26.4: KP Bound Proves `FTS`

If the KP forced-polymer bound holds with `mu_KP-g_c>log C_geom`, then
`FTS(s_0,L)` holds.

Proof.

The KP norm dominates the canonical forced-record tail norm by Definition
26.3, so forced-collar decay holds with `m_F=mu_KP`. Theorem 26.2 applies.
`square`

### Definition 26.5: Collar-Factorizing Exponential Clustering

Ordinary two-point clustering is not enough for long loop records attached to
the original Creutz sheet. The needed condition is collar-factorizing
exponential clustering: for every forced record `f in F_k`, there is a
decomposition

```text
f = f_near f_far + r_f
```

where:

1. `f_near in Alg_{k-1}`;
2. `f_far` is supported in the newly forced collar at distance at least
   `c_d k` from the original sheet, after removing the shared path;
3. `||r_f||_{tail} <= C_r exp(-m_r k)`;
4. connected cumulants between `f_far` and `Alg_{k-1}` are bounded by

   ```text
   C_cl exp(-M c_d k).
   ```

### Theorem 26.6: Collar-Clustering Proves Forced-Collar Decay

If collar-factorizing exponential clustering holds, then forced-collar decay
holds with

```text
m_F = min(m_r, M c_d),
```

up to changing the prefactor `C_F`.

Proof.

The `f_near` factor lies in the previous algebra and is removed by the
projection tail. The remainder `r_f` contributes at most
`C_r exp(-m_r k)`. The connected effect of `f_far` on previous records is
bounded by `C_cl exp(-M c_d k)`. Transport tails are included in the same
certificate norm. Taking the maximum of the three components in
Definition 25.5 gives forced-collar decay with the stated exponent. `square`

### Definition 26.7: Area-Law Forced-Detour Bound

An area-law forced-detour bound holds if the renormalized expectation or
connected contribution of a forced record first appearing at depth `k` is
bounded by

```text
C_Area exp(-sigma a_F k + p_F k),
```

where `sigma>0` is the area coefficient, `a_F>0` is the minimal new area per
tower depth, and `p_F` is the perimeter/cusp counterterm growth per depth
after renormalization.

### Corollary 26.8: Area-Law Bound Proves `FTS`

If

```text
sigma a_F - p_F - g_c > log C_geom,
```

then the area-law forced-detour bound implies `FTS(s_0,L)`.

Proof.

The area-law bound gives forced-collar decay with
`m_F=sigma a_F-p_F`. Theorem 26.2 applies. `square`

### Honest Boundary 26.9

Paper 14 has not proved KP smallness, collar-factorizing clustering, or an
area law for actual continuum Yang-Mills. It has proved the implication from
any one of those estimates to `FTS`, with the needed exponent margin visible.
This is the correct division of labor: Paper 14 names the finite-block entry
condition; later mass-gap, confinement, or constructive-RG papers may try to
prove the decay input.

## 27. A First Route To `LTD`

After `FTS`, the remaining BLU issue is determinacy of the countable identity
system. This section records a sufficient route.

### Definition 27.1: Loop-Identity Determinacy `LID(s_0,L)`

The forced tower satisfies loop-identity determinacy if:

1. the countable algebra generated by `B_infty` separates points on every
   finite `B_k`;
2. the limiting projected Schwinger-Dyson and loop identities recursively
   determine every moment of every primitive forced record, modulo tails
   controlled by `FTS`;
3. reflection positivity and Euclidean covariance fix any homogeneous
   kernel directions left by the linearized identities;
4. the resulting moment functional is positive and normalized on the
   countable tower algebra.

### Theorem 27.2: `LID` Proves `LTD`

If `LID(s_0,L)` holds, then `LTD(s_0,L)` holds.

Proof.

Let `nu` and `nu'` be two compatible subsequential laws satisfying the
limiting projected identities and the `FTS` tail condition. By item 2 of
`LID`, the identities determine the moments of every primitive forced record,
with all tail ambiguities vanishing by `FTS`. Item 3 removes homogeneous
kernel directions. Therefore `nu` and `nu'` agree on the countable record
algebra. Item 1 and Stone-Weierstrass imply agreement on every continuous
function of every finite `B_k`; positivity and normalization ensure these
moments define probability laws rather than signed functionals. Thus `LTD`
holds. `square`

### Proposition 27.3: Failure Modes For `LTD`

`LTD` can fail in exactly the ways relevant to Paper 14:

1. the loop identities leave a nontrivial homogeneous kernel;
2. reflection positivity and covariance do not remove that kernel;
3. the recursive moment solution is not positive;
4. the countable tower algebra fails to separate the finite battery record
   space;
5. `FTS` tails do not vanish, so recursive moment determination is not
   closed.

These are not philosophical problems. They are finite or countable record-law
defects that can be tested at the level of the declared batteries.

## 28. Shell-By-Shell Loop-Identity Invertibility

The condition `LID` is still too global unless it is reduced to shell
certificates. This section gives the shell-level test.

### Definition 28.1: Shell Moment Vector

Let `F_k` be the primitive forced shell from Definition 25.1. Fix a degree
cutoff `D` and a representation cutoff `Lambda_*`. The shell moment vector
is

```text
x_k = ( int m dnu )_{m in Mon(F_k; B_{<k}, D, Lambda_*)},
```

where `Mon(F_k; B_{<k}, D, Lambda_*)` is the finite list of monomials that:

1. contain at least one primitive record from `F_k`;
2. contain any number of records from earlier shells `B_{<k}`;
3. have total degree at most `D`;
4. use representation channels in `Lambda_*`.

The earlier-shell data are denoted

```text
x_{<k}.
```

### Definition 28.2: Shell Linearized Identity System

Project the Schwinger-Dyson, loop, centrality, covariance, and reflection
identity ledger to the shell `F_k`. After moving all earlier-shell and tail
terms to the right-hand side, write the shell system as

```text
M_k x_k = b_k(x_{<k}) + R_k(x_k,x_{<k}) + tau_k.
```

Here:

1. `M_k` is the finite shell identity matrix;
2. `b_k(x_{<k})` is determined by earlier shells;
3. `R_k` is the same-shell nonlinear remainder;
4. `tau_k` is the forced-tail and projection error controlled by `FTS`.

All entries are identities among expectations of declared records in one
whole-process law.

### Definition 28.3: Shell Kernel

The raw shell kernel is

```text
Ker(M_k).
```

The physical shell kernel `Ker_phys(M_k)` is the quotient of `Ker(M_k)` by
directions fixed by:

1. centrality and conjugation symmetry;
2. Euclidean covariance inside the test box;
3. reflection-positivity inequalities saturated or extremal on the shell;
4. positivity and normalization constraints inherited from earlier shells;
5. declared sector labels or newly forced records.

If `Ker_phys(M_k)` is nonzero, the shell identities do not determine the
shell moments.

### Definition 28.4: Shell Invertibility Certificate `SIC(k)`

The shell `F_k` satisfies `SIC(k)` if:

1. `Ker_phys(M_k)=0`;
2. there is a right inverse `Q_k` on the constrained shell range such that

   ```text
   M_k Q_k y = y;
   ```

3. the inverse norm obeys

   ```text
   ||Q_k|| <= q_k;
   ```

4. the same-shell nonlinear remainder is Lipschitz with

   ```text
   Lip(R_k) <= r_k;
   ```

5. the shell gap is positive:

   ```text
   q_k r_k < 1.
   ```

### Theorem 28.5: Shell Invertibility Determines One Shell

Assume `SIC(k)`. If two compatible candidate laws agree on all earlier-shell
moments `x_{<k}` and have the same tail limit `tau_k`, then they agree on the
shell moments `x_k`.

Proof.

Let `x_k` and `x'_k` be two shell moment vectors satisfying the same shell
system. Subtracting gives

```text
M_k (x_k-x'_k)
  = R_k(x_k,x_{<k}) - R_k(x'_k,x_{<k}).
```

Apply the right inverse `Q_k` on the constrained range:

```text
||x_k-x'_k||
  <= q_k r_k ||x_k-x'_k||.
```

Since `q_k r_k < 1`, the difference is zero. Thus the shell moments are
uniquely determined by earlier shells and the tail limit. `square`

### Definition 28.6: Summable Shell Invertibility `SSI(s_0,L)`

The forced tower satisfies summable shell invertibility if every shell
satisfies `SIC(k)` and the amplification of tail errors is summable:

```text
sum_{k>=0} q_k Tail_k < infinity,
```

where `Tail_k` is the forced-tower tail from Lemma 24.5 or any stronger
certified tail norm.

### Theorem 28.7: `SSI + FTS` Prove `LID`

Assume:

1. `FTS(s_0,L)` holds;
2. `SSI(s_0,L)` holds;
3. the countable tower algebra separates points on every finite `B_k`;
4. the recursively determined shell moment functional is positive and
   normalized.

Then `LID(s_0,L)` holds. Consequently `LTD(s_0,L)` holds by Theorem 27.2.

Proof.

Proceed by induction over shell depth. The shell `F_0` is fixed by the seed
records, normalization, centrality, and the finite identity ledger. Assume
all moments up to shell `k-1` are determined. By `SIC(k)` and Theorem 28.5,
the shell moments in `F_k` are uniquely determined up to the certified tail
limit. `FTS` makes the tails vanish, and `SSI` ensures that inverse
amplification of those tails is summable. Thus every shell moment is
recursively determined. The tower algebra separates finite battery points,
and the resulting functional is positive and normalized by assumption.
These are exactly the clauses of `LID`. The final implication is Theorem
27.2. `square`

### Proposition 28.8: Shell Failure Ledger

If `SIC(k)` fails, the failure is classified as one of:

1. **kernel failure:** `Ker_phys(M_k)` is nonzero;
2. **range failure:** the shell right-hand side is not in the constrained
   range of `M_k`;
3. **inverse-growth failure:** `q_k` grows faster than the forced-tail decay;
4. **nonlinear failure:** `q_k r_k >= 1`;
5. **positivity failure:** the recursively determined moments do not define a
   positive shell functional;
6. **record failure:** a kernel direction is not fixed by existing records and
   must be declared as a new sector label or forced record.

The correct response is not to compose partial kernels or invoke hidden
fields. It is to enlarge the declared record/sector ledger, prove a stronger
tail estimate, or report the obstruction.

## 29. Updated Paper-14 Gate

Combining the preceding sections, Paper 14 now has the following sharp
conditional theorem:

```text
forced-collar decay with exponent margin
+ SSI + positivity/separation
+ RGCE
+ WP-rate
=> FTS + LID + LTD + RGCE + WP-rate
=> BLU + CE + WP
=> FBE.
```

The remaining independent constructive estimates are:

1. one of the `FTS` routes: KP forced-polymer decay, collar-factorizing
   clustering, or area-law forced-detour decay;
2. `SSI`, the shell-invertibility certificate, plus positivity and separation
   for the recursively determined tower moments;
3. `RGCE`, the block plaquette character-domain estimate;
4. the `WP` standard-chain rate certificate.

## 30. Finite-Character RGCE

The total-variation version of `RGCE` is strong and clean, but it is probably
stronger than Paper 14 needs. The `CE` gate only requires finitely many
character coefficients, a finite tail estimate, and a positive reserve. This
section replaces total-variation closeness by a finite-character seminorm.

### Definition 30.1: Finite-Character Seminorm

Let `Lambda_*` be a finite representation set containing `rho`, `bar rho`,
the trivial representation, and every coefficient channel exported to Paper
15. For two central block plaquette laws `nu` and `nu_ref`, define

```text
||nu-nu_ref||_{Char,Lambda_*}
  = max_{lambda in Lambda_*}
      |u_lambda(nu)-u_lambda(nu_ref)|
    + Tail_Lambda_*(nu).
```

If the reference is a heat-kernel law `K_t dU`, set

```text
Tail_ref(Lambda_*,t)=Tail_Lambda_*(K_t).
```

The seminorm is operational: it tests only declared central character records
and the declared finite tail bound.

### Definition 30.2: Character-RGCE Certificate `cRGCE`

The actual continuum trajectory satisfies

```text
cRGCE(s_0,rho,L)
```

if there exist `t_0>0`, `Lambda_*`, and constants
`delta_char, delta_tail >= 0` such that the unique block plaquette marginal
`nu_P` is central and:

```text
max_{lambda in Lambda_*}
  |u_lambda(nu_P)-exp(-t_0 C_2(lambda)/2)|
  <= delta_char,
Tail_Lambda_*(nu_P) <= Tail_ref(Lambda_*,t_0)+delta_tail,
```

and the reserve

```text
M_cRGCE
  = (u_ref-delta_char)^{N_0}
    (1-(u_ref+delta_char)^{Q_sigma})
    - Tail_ref(Lambda_*,t_0)
    - delta_tail
```

is positive, where

```text
u_ref=exp(-t_0 C_2(rho)/2).
```

### Theorem 30.3: `cRGCE` Proves `CE`

Assume `BLU(s_0,L)` and `cRGCE(s_0,rho,L)`. Then
`CE(s_0,rho,L)` holds with exported reserve at least `M_cRGCE`.

Proof.

`BLU` gives a unique finite-block law and hence a unique block plaquette
marginal `nu_P`. The `rho` coefficient bound in `cRGCE` gives

```text
u_ref-delta_char <= u_rho(nu_P) <= u_ref+delta_char.
```

The tail bound in `cRGCE` gives the off-channel coefficient control required
by Definition 6.3. Positivity of `M_cRGCE` gives the positive
surface-subcritical reserve. Therefore Proposition 6.4 proves `CE`, and the
exported margin is at least `M_cRGCE`. `square`

### Proposition 30.4: Total-Variation RGCE Implies `cRGCE`

If the total-variation `RGCE` certificate of Definition 19.1 holds, then
`cRGCE` holds with `delta_char <= delta_CE` and the same declared tail bound.

Proof.

For every normalized character coefficient, the tested functional has
supremum norm at most one. Total variation closeness therefore bounds every
tested coefficient error by `delta_CE`. The tail clause is already part of
Definition 19.1. `square`

### Honest Boundary 30.5

`cRGCE` is the right Paper-14 target. It does not ask for a full density
estimate; it asks only for the character coefficients and tails that later
surface and Creutz estimates use. It is still a genuine nonperturbative RG
input about the actual pushed-forward block plaquette law.

## 31. Expanded `WP` Rate Classes

The `WP` certificate also needs a concrete rate ledger. This section breaks
the single summability condition into named sources.

### Definition 31.1: Rate Classes

For the standard continuum chain `eta_n=(a_n,V_n,q_n,ct_n)`, define:

```text
eps_ID,n      <= C_ID n^{-1-p_ID},
eps_proj,n    <= C_proj exp(-m_proj D_n),
eps_CE,n      <= C_CE n^{-1-p_CE},
eps_tail,n    <= C_tail exp(-m_tail C_2(Lambda_n)),
eps_chart,n   <= C_chart n^{-1-p_chart},
eps_ct,n      <= C_ct n^{-1-p_ct},
eps_vol,n     <= C_vol exp(-m_vol b_n),
eps_cov,n     <= C_cov n^{-1-p_cov},
eps_RP,n      <= C_RP n^{-1-p_RP}.
```

Here `D_n` is the finite product-degree cutoff, `Lambda_n` is the
representation cutoff, and `b_n` is the finite-volume buffer distance.

The rate class is admissible if every exponent `p_*` is positive and every
exponential rate constant is positive.

### Theorem 31.2: Admissible Rate Classes Give `WP`

If the standard continuum chain satisfies the admissible rate bounds of
Definition 31.1, and if any two standard chains have a common refinement
chain satisfying the same kind of bounds, then `WP(s_0,L)` holds.

Proof.

Every polynomial sequence `n^{-1-p_*}` with `p_*>0` is summable, and every
exponential sequence in `D_n`, `C_2(Lambda_n)`, or `b_n` is summable after
choosing the cutoffs and buffer to increase. Hence the total rate certificate
of Definition 20.2 is summable. Theorem 20.3 gives `WP` along one chain and
common-refinement independence across chains. `square`

### Proposition 31.3: Reflection Positivity Reserve

Suppose the finite reflected battery has a positivity margin

```text
RP_margin,n >= r_RP > 0
```

on the tested reflected polynomials. If

```text
sum_n eps_RP,n < r_RP/2,
```

then reflection positivity survives the standard-chain transport on the
tested battery.

Proof.

For each reflected polynomial `F`, the transported expectation changes by at
most the accumulated `eps_RP` defect times the declared Lipschitz constant,
absorbed into the definition of `eps_RP`. If the total loss is less than half
the positivity margin, the transported reflected expectation remains
nonnegative with positive reserve. `square`

### Honest Boundary 31.4

The admissible rates are not automatic. Paper 14 has now made the `WP`
target explicit: identity, projection, coefficient, tail, chart,
counterterm, volume, covariance, and reflection-positivity defects must all
be summable as whole-process pushed-forward law comparisons.

## 32. Final Paper-14 Closure Theorem

### Theorem 32.1: Finite-Block Entry Closure

Assume:

1. forced-collar decay with exponent margin, so `FTS(s_0,L)` holds;
2. `SSI(s_0,L)` plus positivity and separation, so `LID` and `LTD` hold;
3. finite projected identity defects vanish on every finite tower battery;
4. `cRGCE(s_0,rho,L)` holds with positive reserve;
5. the admissible `WP` rate classes hold on standard chains and common
   refinements.

Then

```text
FBE(s_0,rho,L)
```

holds. Consequently the Paper-13 gates `BC`, `CE`, and `WP` hold, and Paper
15 may use the export package `X_14(s_0,L,rho)`.

Proof.

Forced-collar decay proves `FTS` by Theorem 26.2, or by the KP, clustering,
or area-law corollaries of Section 26. `SSI` plus positivity and separation
prove `LID` by Theorem 28.7, and `LID` proves `LTD` by Theorem 27.2. With
vanishing finite identity defects, Theorem 24.7 proves `BLU`.

Given `BLU`, `cRGCE` proves `CE` by Theorem 30.3. The admissible rate classes
prove `WP` by Theorem 31.2. Therefore `BLU`, `CE`, and `WP` all hold, which
is exactly `FBE` by Definition 4.1. The export statement is Theorem 15.2.
`square`

### Corollary 32.2: Paper 14 Is Complete As A Reduction Paper

Paper 14 is complete as a reduction paper once Theorem 32.1 is stated with
all certificates explicit. It is not complete as an unconditional
four-dimensional Yang-Mills construction unless the five assumptions of
Theorem 32.1 are proved for actual continuum `SU(N)` Yang-Mills.

## 33. Final Certificate Package For Paper 15

Paper 14 exports to Paper 15:

1. the finite-block law `nu_{s_0,L}`, conditional on the closure theorem;
2. the leading character window `u_- <= u_rho <= u_+`;
3. the positive reserve `M_cRGCE`;
4. the finite character tail bound;
5. the forced-tower constants `C_geom`, `m_F`, `g_c`, and the `FTS` margin;
6. the shell-invertibility constants `q_k`, `r_k`, and inverse-tail budget;
7. the full `WP` defect budget;
8. the exact statement of which constructive estimates remain imported.

Paper 15 may use these only as declared operational record-law data. It may
not reinterpret them as microscopic fields, particles, or a Markovian
subprocess.

## 34. Honest Status

This first pass proves the formal Paper-14 reduction:

```text
determining finite-block identities
+ coefficient window
+ whole-process certificate ledger
=> FBE(s_0,rho,L)
=> BC + CE + WP.
```

It also gives a concrete computable model for the `CE` coefficient window via
the heat-kernel character expansion, and it derives the exact finite-cutoff
compact-group Schwinger-Dyson identities that should feed the `BLU` ledger.
Sections 11--33 now execute the immediate steps: they define the concrete
Creutz-character battery, prove the countable determining-battery theorem,
project the finite Schwinger-Dyson identities onto that battery, state the
closing-sequence theorem for `BLU`, sharpen it into a triangular closure
criterion, add the closure-enrichment fallback when identities force new
records, harden `CE` with a positive heat-kernel neighborhood and an
actual-RG character-domain certificate, define the whole-process transport
norm and a concrete standard-chain rate certificate for `WP`, package the
constants exported to Paper 15, test the first Creutz battery `B_0`, test the
one-staple enlarged battery `B_1`, define the second forced battery `B_2`,
prove a one-step locality-growth bound, define the full forced tower
`B_infty`, prove finite-stage compactness, prove all-depth locality and
branching, define `FTS` and `LTD`, and prove
`FTS + LTD => BLU`. They then make the forced-record weight `A_k` canonical,
prove that KP forced-polymer decay, collar-factorizing clustering, or
area-law forced-detour bounds imply `FTS`, and give the loop-identity
determinacy route `LID => LTD`. They now further reduce `LID` to
shell-by-shell loop-identity invertibility: shell matrices `M_k`, physical
kernel quotients, right inverses `Q_k`, nonlinear Lipschitz gaps, summable
inverse-tail amplification, and positivity/separation of the recursively
determined moment functional. Finally, they replace total-variation `RGCE`
by the weaker finite-character certificate `cRGCE`, expand the `WP` rate
classes, and prove the final closure theorem

```text
forced-collar decay + SSI/positivity/separation
+ cRGCE + WP-rate
=> FBE.
```

It does not yet prove actual four-dimensional continuum `SU(N)` Yang-Mills
satisfies forced-collar decay, `SSI` plus positivity/separation, the `cRGCE`
character-domain certificate, or the `WP` rate certificate. Those are now the
explicit hard tasks. This is progress, but not a hidden solution of the Clay
Yang-Mills problem, not a mass gap proof, and not a confinement theorem.

The first two triangular closure tests have now been run. The first
nontrivial Creutz-character battery `B_0` does not close exactly: the finite
loop identities force exterior one-staple deformation records. The
one-staple enlarged battery `B_1` also does not close exactly: differentiating
one-staple records forces two-staple, corner, rectangle-extension,
transverse-sheet, and local action-density records. This is not a conceptual
failure. It is the expected operational lesson: the declared record battery
must grow into a forced tower

```text
B_0 subset B_1 subset B_2 subset ...
```

The good news is that the forced tower is local at all depths for finite local
action stencils: support and representation complexity grow at most linearly
with tower depth, and branching grows at most exponentially. The open
dynamical question is whether the canonical weights of new forced records
decay fast enough for `FTS`, and whether the shell identity matrices are
invertible in the constrained sense strongly enough for `SSI`. If `FTS`
fails without a replacement norm or cancellation identity, or if `SSI` fails
because an unresolved physical shell kernel remains, Paper 14 must report a
finite-block obstruction or declare the missing sector/record. If
forced-collar decay and `SSI` with positivity/separation hold, they prove
`LID`, hence `LTD`, hence `BLU`; with `cRGCE` and the `WP` rate certificate,
Paper 14 then proves `FBE` and exports a clean package to Paper 15.
