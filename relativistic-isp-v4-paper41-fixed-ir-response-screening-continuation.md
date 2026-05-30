# Relativistic ISP V4 Paper 41: Fixed-IR Response Screening And Hostile-Collar Continuation

Author: Felix Robles Elvira

Date: 2026-05-30

Status: continuation and proof-audit paper for Paper 40, Sections 52.16-52.19.
This paper does not prove continuum Yang-Mills confinement, does not prove a
mass gap, does not prove continuum survival of a string tension, and does not
modify the Yang-Mills measure. It continues the fixed-physical-`R`
single-collar lower-tail problem isolated in Paper 40 and makes explicit the
assumptions under which Branches I-III can be pursued without leaving
fixed-IR or Barandes alignment. Sections 14-31 (this revision) carry that
program through a chain of exact reductions and clearly-labelled frontier
explorations that progressively *localize* the open kernel; they prove no part
of confinement. Section 32 states the maximally-localized open problem (the
`SO(3)` dressing) self-containedly; Section 33 is the final status ledger.

## Abstract

Paper 40 reduced the localized center-sign certificate to the
single-collar charged-ratio problem. After auditing transport, entropy,
boundary-transfer, capacity, localized Tomboulis-Yaffe, de-tiling, and
reflected-asymmetry routes, the remaining alternatives were:

```math
\boxed{
\begin{array}{ll}
\text{Branch I}
&
\text{fixed-IR charge-sensitive response screening},\\[1mm]
\text{Branch II}
&
\text{finite-rank physical boundary compression or boundary RG},\\[1mm]
\text{Branch III}
&
\text{positive-mass hostile-collar response collapse}.
\end{array}}
```

This paper is the continuation workbench for those three branches. Its first
job is not to broaden the target, but to prevent accidental target drift. The
target remains the original single-collar conditional ratio under the original
finite `SU(2)` law, at fixed physical scale `R`, uniformly as `a -> 0`. Any
reflection-positive, transfer-kernel, boundary-RG, or response-calculus object
used below is an analytic proof device only. It is not a hidden Markov record
dynamics and not an extra ISP stochastic law.

**Abstract addendum (§§14–31, this revision).** The single-collar problem is
developed through a chain of exact reductions and clearly-labelled frontier
explorations that progressively *localize* the open kernel without proving it.
The reflected-asymmetry side is discharged for rectangular loops
(§§14–18: Lemma 41.20/41.21 even–odd reduction; Lemma 41.31 symmetric-sheet
vanishing; Proposition 41.32 / Corollary 41.33 equivariant symmetrization),
leaving the conditional magnitude `m(\eta)=\langle\Xi_S\rangle_\eta` — equivalently
the center-flux area law (§19) — as the sole frontier. A leading-order test rules
out the cheap death of the decimation route (§27); marrying it to Balaban's
small-field RG locates confinement in the *intermediate-field* regime (§28); an
induced-`Z_2` reformulation anchors the target on the exactly-known 4D `Z_2`
self-dual threshold (§29) while §29.7 shows why merely refining the estimate is a
mirage; a gauge-invariant heat-kernel *modular duality* rewrites the center
sector as a vortex gas with an exact fugacity `e^{-\pi^2/t}` (§30); and the bare
gas is then solved completely, its entropy `\log(1+\sqrt2)` also exact (§31). The
net result is a **maximal localization**: the open problem reduces to a single
classical object — the `SO(3)` dressing of the vortex free energy at intermediate
coupling — with the energy (`\pi^2`) and the bare entropy (`\log(1+\sqrt2)`)
already exact and the gauge-projection ambiguity removed. **Section 32 states that
open problem self-containedly.** No part of this paper proves confinement, a mass
gap, or continuum survival of a string tension; the contribution is the reduction,
the negative results, and the localization.

## 0. Continuation From Paper 40

Searchable continuation tag:

`V4P41-FIXED-IR-RESPONSE-SCREENING-CONTINUATION`.

This paper continues:

- Paper 40, Section 51: boundary-stable de-tiling for the single-collar ratio;
- Paper 40, Section 52: reflected-asymmetry estimate for the local charged
  ratio;
- Paper 40, Sections 52.16-52.19: the three remaining branches.

The single-collar ratio is:

```math
r_a(\eta)
=
\frac{
Z^{\mathrm{ch}}_a(\eta)
}{
Z^0_a(\eta)
}.
```

Here:

- `eta` is the fixed physical collar/environment readout;
- `Z_ch` is the charged physical readout weight;
- `Z_0` is the pinned physical readout weight;
- all weights are computed under the original finite `SU(2)` conditional law;
- `R` is fixed before `a -> 0`.

The reflected collar is:

```math
\theta\eta.
```

The reflected-asymmetry object is:

```math
\mathcal A_a(\eta)
=
\log r_a(\eta)
-
\log r_a(\theta\eta).
```

Paper 40 showed that paired reflection-positive estimates de-tile to the
single-collar lower tail if:

```math
\left|
\mathcal A_a(\eta)
\right|
\le
D_R
```

with `D_R` independent of `a`.

## 1. Non-Negotiable Alignment Contract

Searchable assumption tag:

`V4P41-ASSUMPTION-LEDGER-FIXED-IR-BARANDES`.

The following assumptions are part of the contract of this paper. Any argument
that violates one of them is outside the paper.

### 1.1. Fixed-IR Contract

```math
\boxed{
\begin{array}{ll}
\mathrm{IR1}
&
\text{fix the physical scale }R\text{ before taking }a\to0,\\[1mm]
\mathrm{IR2}
&
\text{constants may depend on }R\text{ but not on }a,\\[1mm]
\mathrm{IR3}
&
\text{events and readouts must be physical-resolution objects},\\[1mm]
\mathrm{IR4}
&
\text{microscopic positivity at fixed }a\text{ is not enough},\\[1mm]
\mathrm{IR5}
&
\text{weak-coupling good-sector smallness is not an IR substitute},\\[1mm]
\mathrm{IR6}
&
\text{global or tiled averages do not replace fixed-collar estimates}.
\end{array}}
```

### 1.2. Barandes-Alignment Contract

```math
\boxed{
\begin{array}{ll}
\mathrm{B1}
&
\text{use the original finite SU(2) configuration law},\\[1mm]
\mathrm{B2}
&
\text{use deterministic readouts of the same finite configuration},\\[1mm]
\mathrm{B3}
&
\text{do not add hidden Markov dynamics},\\[1mm]
\mathrm{B4}
&
\text{do not add an ISP center-sector tilt or new prior},\\[1mm]
\mathrm{B5}
&
\text{treat kernels and interpolations as proof devices only},\\[1mm]
\mathrm{B6}
&
\text{do not infer stochastic transition laws from record language},\\[1mm]
\mathrm{B7}
&
\text{separate configuration string tension from RP spectral mass gap}.
\end{array}}
```

### 1.3. Target-No-Drift Contract

The target is not:

```math
\boxed{
\begin{array}{ll}
\mathrm{N1}
&
\text{a global torus twisted-sector ratio},\\[1mm]
\mathrm{N2}
&
\text{a reflected/tiled average over collars},\\[1mm]
\mathrm{N3}
&
\text{a fixed-cutoff nonzero measure statement},\\[1mm]
\mathrm{N4}
&
\text{a statement after sampling from the charged class},\\[1mm]
\mathrm{N5}
&
\text{a theorem for a modified or tilted law},\\[1mm]
\mathrm{N6}
&
\text{a mass-gap theorem before OS/RP reconstruction}.
\end{array}}
```

The target is:

```math
\boxed{
\begin{array}{c}
\text{the single-collar charged-to-pinned ratio under the original}\\[1mm]
\text{finite SU(2) conditional law, at fixed physical }R,\\[1mm]
\text{with constants uniform as }a\to0.
\end{array}}
```

## 2. What Is Assumed And What Is Not

This paper may assume the following setup, inherited from Paper 40:

```math
\boxed{
\begin{array}{ll}
\mathrm{S1}
&
\text{finite-cutoff SU(2) lattice variables and Haar/Wilson weights},\\[1mm]
\mathrm{S2}
&
\text{measurable charged and pinned physical readout classes},\\[1mm]
\mathrm{S3}
&
\text{a fixed physical block and fixed physical collar},\\[1mm]
\mathrm{S4}
&
\text{a reflected collar operation }\eta\mapsto\theta\eta,\\[1mm]
\mathrm{S5}
&
\text{formal differentiability of smooth collar interpolations when stated},\\[1mm]
\mathrm{S6}
&
\text{paired RP/TY estimates only as explicit conditional inputs}.
\end{array}}
```

This paper does not assume:

```math
\boxed{
\begin{array}{ll}
\mathrm{X1}
&
\text{the charged lower-tail theorem},\\[1mm]
\mathrm{X2}
&
\text{the reflected-asymmetry bound},\\[1mm]
\mathrm{X3}
&
\text{boundary-stable de-tiling},\\[1mm]
\mathrm{X4}
&
\text{finite-rank boundary RG},\\[1mm]
\mathrm{X5}
&
\text{positive or negative hostile-collar probability},\\[1mm]
\mathrm{X6}
&
\text{continuum confinement or mass gap}.
\end{array}}
```

The purpose of Paper 41 is to test X2-X5, not to assume them.

## 3. The Three Branches

Searchable branch tag:

`V4P41-BRANCHES-I-II-III`.

Paper 40 left three possible ways forward.

### 3.1. Branch I: Charge-Sensitive Response Screening

Let `eta(t)` be a physical collar interpolation from `theta eta` to `eta`.
Let `dot S_eta(t)` denote the collar action derivative. Branch I asks whether:

```math
\int_0^1
\left|
\left\langle
\dot S_{\eta(t)}
\right\rangle_{\mathrm{ch},t}
-
\left\langle
\dot S_{\eta(t)}
\right\rangle_{0,t}
\right|
dt
\le
D_R
```

with `D_R` independent of `a`.

This is not a bound on the raw collar action. It is a bound on the
charged-minus-pinned response.

### 3.2. Branch II: Finite-Rank Physical Boundary Compression

Branch II asks whether there is a deterministic physical collar readout:

```math
\Pi_R^{\mathrm{eff}}(\eta)
```

with finitely many physical degrees of freedom such that:

```math
\left|
\log r_a(\eta)
-
\log r_a(\eta')
\right|
\le
C_R
```

whenever:

```math
\Pi_R^{\mathrm{eff}}(\eta)
=
\Pi_R^{\mathrm{eff}}(\eta').
```

This is not allowed to contain `r_a(eta)` by definition. If the readout stores
the answer, it is tautological and inadmissible.

### 3.3. Branch III: Positive-Mass Hostile Response

Branch III is the negative route. It asks whether there are physical hostile
collar classes `H_R,a` with:

```math
\nu_{R,a}(H_{R,a})
\ge
p_R
>
0,
```

and:

```math
\log r_a(\eta)
-
\log r_a(\theta\eta)
\le
-L_a,
\qquad
L_a\to\infty,
```

for all `eta` in `H_R,a`.

Here `nu_R,a` is the original collar/environment law induced by the same finite
`SU(2)` measure. Pointwise hostile collars are not enough; the hostile class
must have fixed-IR positive mass.

## 4. Branch I: Response-Screening Program

`V4P41-TARGET-4101-RESPONSE-SCREENING`.

### 4.1. Physical-Cell Decomposition

Partition the physical collar into finitely many physical cells:

```math
C_R
=
\bigcup_{j=1}^{M_R}
C_{R,j},
```

with `M_R` independent of `a`. Decompose:

```math
\dot S_{\eta(t)}
=
\sum_{j=1}^{M_R}
Y_{j,a,t}.
```

Each `Y_j,a,t` may contain cutoff-many plaquette terms. The fixed-IR target is:

```math
\int_0^1
\left|
\left\langle
Y_{j,a,t}
\right\rangle_{\mathrm{ch},t}
-
\left\langle
Y_{j,a,t}
\right\rangle_{0,t}
\right|
dt
\le
D_{R,j}.
```

If:

```math
\sum_{j=1}^{M_R}
D_{R,j}
\le
D_R,
```

then Branch I proves reflected asymmetry.

### 4.2. Assumptions Needed For A Valid Branch I Proof

A Branch I proof must explicitly verify:

```math
\boxed{
\begin{array}{ll}
\mathrm{I1}
&
\text{the interpolation stays inside the same admissible collar class},\\[1mm]
\mathrm{I2}
&
\text{the derivative formula is justified at finite cutoff},\\[1mm]
\mathrm{I3}
&
\text{the physical-cell decomposition has }M_R\text{ independent of }a,\\[1mm]
\mathrm{I4}
&
\text{the divergent collar energy common to both sectors cancels},\\[1mm]
\mathrm{I5}
&
\text{the remaining charged-minus-pinned response is }O_R(1),\\[1mm]
\mathrm{I6}
&
\text{the proof does not use the desired lower-tail denominator circularly}.
\end{array}}
```

### 4.3. Branch I Failure Modes

Branch I fails if:

```math
\boxed{
\begin{array}{ll}
\mathrm{IF1}
&
\text{the interpolation changes the physical readout target},\\[1mm]
\mathrm{IF2}
&
\text{the response bound is proved only term-by-term microscopically},\\[1mm]
\mathrm{IF3}
&
\text{the sector expectation comparison uses the lower-tail theorem},\\[1mm]
\mathrm{IF4}
&
\text{a physical cell has response divergence on positive collar mass}.
\end{array}}
```

Failure mode IF4 should be converted into Branch III.

## 5. Branch II: Boundary Compression And Boundary RG

`V4P41-TARGET-4102-FINITE-RANK-BOUNDARY-RG`.

### 5.1. Admissible Compression

A compression map is admissible only if:

```math
\boxed{
\begin{array}{ll}
\mathrm{C1}
&
\text{it is deterministic from the finite SU(2) collar configuration},\\[1mm]
\mathrm{C2}
&
\text{it has finitely many physical degrees of freedom at fixed }R,\\[1mm]
\mathrm{C3}
&
\text{it does not contain }r_a(\eta)\text{ or sector partition functions},\\[1mm]
\mathrm{C4}
&
\text{its fiber-stability constants are uniform as }a\to0,\\[1mm]
\mathrm{C5}
&
\text{it retains all charge-sensitive collar response data up to }O_R(1).
\end{array}}
```

### 5.2. Non-Admissible Compression

The following are not acceptable:

```math
\boxed{
\begin{array}{ll}
\mathrm{NC1}
&
\text{center-only data, unless coset response is separately controlled},\\[1mm]
\mathrm{NC2}
&
\text{the full boundary transfer functional},\\[1mm]
\mathrm{NC3}
&
\text{any readout that stores charged and pinned weights by definition},\\[1mm]
\mathrm{NC4}
&
\text{a finite readout whose fibers have uncontrolled microscopic response}.
\end{array}}
```

### 5.3. Boundary RG Target

The valid Branch II theorem is:

```math
\boxed{
\begin{array}{c}
\text{there exists a finite-rank physical boundary state}\\[1mm]
\Pi_R^{\mathrm{eff}}(\eta)\\[1mm]
\text{such that all residual charge-sensitive collar response}\\[1mm]
\text{inside each fiber is bounded by }O_R(1).
\end{array}}
```

This is equivalent in spirit to Branch I. Branch I expresses the theorem as
screening of collar-energy response; Branch II expresses it as finite-rank
boundary RG.

## 6. Branch III: Hostile-Collar Program

`V4P41-TARGET-4103-HOSTILE-COLLAR-PROGRAM`.

### 6.1. What Counts As Hostile

A hostile collar class must be:

```math
\boxed{
\begin{array}{ll}
\mathrm{H1}
&
\text{defined by physical-resolution collar data or a stable thick event},\\[1mm]
\mathrm{H2}
&
\text{positive-mass under the original collar law},\\[1mm]
\mathrm{H3}
&
\text{negative for the charged-minus-pinned reflected response},\\[1mm]
\mathrm{H4}
&
\text{not canceled by simultaneous collapse of the reflected partner},\\[1mm]
\mathrm{H5}
&
\text{not an artifact of section choice or gauge representative}.
\end{array}}
```

### 6.2. What Does Not Count As Hostile

The following do not falsify the route:

```math
\boxed{
\begin{array}{ll}
\mathrm{NH1}
&
\text{one bad collar configuration of Haar measure zero},\\[1mm]
\mathrm{NH2}
&
\text{a microscopic event whose probability vanishes as }a\to0,\\[1mm]
\mathrm{NH3}
&
\text{large collar holonomy without sector-response collapse},\\[1mm]
\mathrm{NH4}
&
\text{small capacity without charged target mass collapse},\\[1mm]
\mathrm{NH5}
&
\text{a bad result for a modified or tilted law}.
\end{array}}
```

### 6.3. Character-Expansion Version

In a character or spin-foam representation, Branch III becomes:

```math
\boxed{
\begin{array}{c}
\text{prove that on a positive-mass physical collar class,}\\[1mm]
\text{odd boundary states lose fixed-IR entropy or weight}\\[1mm]
\text{relative to even boundary states.}
\end{array}}
```

This is a clean falsification route. It is also hard: it must prove a
positive-probability lower-tail statement for hostile collar classes.

## 7. Decision Tree For Paper 41

Searchable decision tag:

`V4P41-DECISION-TREE`.

The proof order should be:

1. Try Branch I first.
2. If Branch I fails because of unresolved microscopic collar modes, translate
   the failure into Branch II and test finite-rank boundary RG.
3. If the response divergence is physical and has positive collar mass,
   translate the failure into Branch III.
4. Do not introduce a fourth formal language unless it proves one of these
   three estimates.

The decision tree is:

```math
\boxed{
\begin{array}{c}
\text{response screening}\\[1mm]
\Downarrow\\[1mm]
\text{reflected asymmetry}\\[1mm]
\Downarrow\\[1mm]
\text{boundary-stable de-tiling}\\[1mm]
\Downarrow\\[1mm]
\text{single-collar lower tail}
\end{array}}
```

or:

```math
\boxed{
\begin{array}{c}
\text{positive-mass hostile response}\\[1mm]
\Downarrow\\[1mm]
\text{failure of reflected asymmetry}\\[1mm]
\Downarrow\\[1mm]
\text{failure of boundary-stable de-tiling}\\[1mm]
\Downarrow\\[1mm]
\text{failure of this fixed-IR certificate route}
\end{array}}
```

## 8. The First Concrete Target In Paper 41

The first theorem to attempt is:

`V4P41-TARGET-4104-PHYSICAL-CELL-RESPONSE-SCREENING`.

For each physical collar cell `C_R,j`, prove:

```math
\int_0^1
\left|
\left\langle
Y_{j,a,t}
\right\rangle_{\mathrm{ch},t}
-
\left\langle
Y_{j,a,t}
\right\rangle_{0,t}
\right|
dt
\le
D_{R,j},
```

with:

```math
\sum_{j=1}^{M_R}
D_{R,j}
<
\infty
```

at fixed `R`, uniformly as `a -> 0`.

Any proof of this target must include an assumption audit:

```math
\boxed{
\begin{array}{ll}
\text{same law}
&
\text{original finite SU(2) law only},\\[1mm]
\text{same collar}
&
\text{no replacement by a reflected or averaged collar},\\[1mm]
\text{same target}
&
\text{single-collar charged-to-pinned ratio},\\[1mm]
\text{fixed IR}
&
\text{constants independent of }a,\\[1mm]
\text{Barandes}
&
\text{no hidden stochastic dynamics or measure tilt},\\[1mm]
\text{noncircular}
&
\text{no use of the desired lower tail as input}.
\end{array}}
```

## 9. Paper 41 Boundary

This paper is a continuation of the fixed-IR certificate route. Even if Branch
I or Branch II is proved, the result is still a fixed-physical-`R` certificate
input for Paper 40. It is not, by itself, the full continuum Yang-Mills
confinement theorem and not the Clay mass-gap theorem.

If Branch III is proved, the result is also bounded: it falsifies this
single-collar fixed-IR certificate route, not the physical truth of
confinement.

The value of Paper 41 is that the remaining work is no longer hidden behind a
formal reduction. It is one of three concrete estimates:

```math
\boxed{
\begin{array}{ll}
\text{positive}
&
\text{fixed-IR charge-sensitive response screening},\\[1mm]
\text{positive}
&
\text{finite-rank physical boundary RG},\\[1mm]
\text{negative}
&
\text{positive-mass hostile-collar response collapse}.
\end{array}}
```

## 10. Full Investigation Of Branch I: Response Screening

`V4P41-TARGET-4105-BRANCH-I-RESPONSE-SCREENING-AUDIT`.

Branch I is the most direct positive route. It tries to prove that charged and
pinned conditional laws see the same divergent collar energy, up to a fixed
physical remainder.

The target is:

```math
\int_0^1
\left|
\left\langle
Y_{j,a,t}
\right\rangle_{\mathrm{ch},t}
-
\left\langle
Y_{j,a,t}
\right\rangle_{0,t}
\right|
dt
\le
D_{R,j}
```

for each physical collar cell.

### 10.1. Finite-Cutoff Differentiation Is Legitimate

At finite cutoff, the configuration space is a compact product of finitely many
copies of `SU(2)`. The collar interpolation changes only finitely many action
terms. Therefore:

```math
\frac{d}{dt}
\log Z^s_a(\eta(t))
=
-
\left\langle
\dot S_{\eta(t)}
\right\rangle_{s,t},
\qquad
s\in\{0,\mathrm{ch}\}.
```

**Theorem 41.1 (Finite-Cutoff Response Identity).** For every fixed `a`, smooth
collar interpolation, and sector `s`, the logarithmic derivative of the sector
partition function is the negative conditional expectation of the collar
action derivative.

#### Proof

The finite-cutoff partition function is a finite-dimensional compact integral
with smooth positive density. Differentiation under the integral is justified
by compactness and smooth dependence on the collar parameter. Dividing by
`Z^s_a(eta(t))` gives the expectation formula.

#### Decision

The obstruction is not differentiability. It is uniformity as `a -> 0`.

### 10.2. The Exact Branch I Equivalence

Subtract the pinned derivative from the charged derivative:

```math
\frac{d}{dt}
\log r_a(\eta(t))
=
-
\left\langle
\dot S_{\eta(t)}
\right\rangle_{\mathrm{ch},t}
+
\left\langle
\dot S_{\eta(t)}
\right\rangle_{0,t}.
```

**Theorem 41.2 (Response Screening Is Equivalent To Asymmetry Control Along
The Path).** If the integrated charged-minus-pinned response is bounded by
`D_R`, then:

```math
\left|
\log r_a(\eta)
-
\log r_a(\theta\eta)
\right|
\le
D_R.
```

Conversely, if the reflected-asymmetry bound holds for all collar endpoints
and for all subpaths of the interpolation family, then the total variation of
the response along those paths is bounded in the same physical scale.

#### Proof

The first direction is the fundamental theorem of calculus. The converse is a
standard bounded-variation reading: apply the endpoint asymmetry bound to
subintervals and refine partitions. It controls the total variation only for
the chosen admissible path class, not for arbitrary microscopic paths.

#### Decision

Branch I is not a merely sufficient trick. It is the differential form of the
reflected-asymmetry theorem, once the interpolation class is fixed.

### 10.3. Attempt A: Bound The Two Sector Expectations Separately

The crude estimate is:

```math
\left|
\left\langle
Y_{j,a,t}
\right\rangle_{\mathrm{ch},t}
-
\left\langle
Y_{j,a,t}
\right\rangle_{0,t}
\right|
\le
2
\left\|
Y_{j,a,t}
\right\|_{\infty}.
```

**Theorem 41.3 (Separate Expectation Bounds Fail Fixed-IR).** Separate
absolute bounds on charged and pinned collar energies do not prove Branch I.

#### Proof

The physical cell contains cutoff-many microscopic plaquette terms. The norm
of `Y_j,a,t` grows with the number of plaquettes in the cell. This is exactly
the divergent common collar energy that Branch I was designed to cancel.

#### Decision

Attempt A fails. It violates fixed-IR alignment.

### 10.4. Attempt B: Gauge Or Ward Cancellation

Gauge invariance removes dependence on representatives. It does not force a
charged physical sector and a pinned physical sector to have the same response
to a fixed physical collar.

**Theorem 41.4 (Gauge Invariance Does Not Prove Response Screening).** Gauge
invariance alone does not imply Branch I.

#### Proof

Both sectors are gauge-invariant readout classes. The charged/pinned
difference is not a gauge artifact; it is the physical center pairing under
the fixed collar. Gauge invariance can simplify variables but cannot identify
the two conditional sector measures.

#### Decision

Attempt B fails as a standalone proof.

### 10.5. Attempt C: Reflection Positivity

Reflection positivity can pair `eta` and `theta eta`, but Branch I compares
charged and pinned responses under the same collar.

**Theorem 41.5 (RP Does Not Directly Bound The Response Difference).** RP can
support paired estimates and package compatibility, but it does not supply the
single-collar charged-minus-pinned response bound.

#### Proof

RP gives positivity of reflected products. It controls sums or geometric means
over reflected collars. Branch I asks for the magnitude of a logarithmic
derivative difference at one fixed collar. That is a scale estimate, not a
positivity statement.

#### Decision

Attempt C is partial only. It must be combined with Branch I or Branch II.

### 10.6. Attempt D: Covariance Formula

Let `E_ch` and `E_0` be the charged and pinned readout events inside a common
conditional ensemble. For a collar cell observable `Y`, sector expectation
differences can be written in covariance form:

```math
\left\langle
Y
\right\rangle_{\mathrm{ch}}
-
\left\langle
Y
\right\rangle_{0}
=
\frac{\mathrm{Cov}(Y,1_{E_{\mathrm{ch}}})}{\mu(E_{\mathrm{ch}})}
-
\frac{\mathrm{Cov}(Y,1_{E_0})}{\mu(E_0)}.
```

**Theorem 41.6 (Covariance Control Is Non-Circular Only With Denominator
Control).** Covariance estimates prove Branch I if the sector denominators are
already bounded below by non-circular inputs. Without denominator control, the
covariance formula can be circular.

#### Proof

The formula is the identity for conditional expectations. To bound the right
side, one must divide by the sector probabilities. But lower bounds on those
probabilities are close to the charged lower-tail theorem. Thus this route is
valid only if paired RP or another independent statement supplies the
denominator scale.

#### Decision

Attempt D gives a useful representation, but it does not close Branch I by
itself.

### 10.7. Attempt E: Physical-Cell Screening

The right positive theorem is a physical-cell screening estimate:

```math
\left|
\left\langle
Y_{j,a,t}
\right\rangle_{\mathrm{ch},t}
-
\left\langle
Y_{j,a,t}
\right\rangle_{0,t}
\right|
\le
D_{R,j}(t),
```

where:

```math
\int_0^1
D_{R,j}(t)dt
\le
D_{R,j}.
```

**Criterion 41.7 (Physical-Cell Screening Criterion).** If Criterion 41.7
holds for every physical collar cell, then Branch I proves reflected
asymmetry, de-tiling, and the single-collar lower-tail theorem, assuming the
paired RP input from Paper 40.

#### Proof

Sum the physical-cell bounds over `j` and integrate in `t`. The number of
cells is fixed by `R`, so the resulting constant is independent of `a`.
Theorem 41.2 gives reflected asymmetry, and Paper 40 Section 51 de-tiles the
paired RP estimate.

#### Decision

This is the surviving positive Branch I target.

### 10.8. Attempt F: Strong-Coupling Calibration

In strong coupling, a character expansion may make charged/pinned response
screening provable because local defects have summable weights.

**Theorem 41.8 (Strong Coupling Calibrates But Does Not Close The Fixed-IR
Continuum Branch).** Strong-coupling screening, if proved, validates the
definitions but does not prove the continuum fixed-IR branch.

#### Proof

The continuum limit for four-dimensional asymptotically free `SU(2)` is reached
at weak bare coupling. Strong-coupling expansions do not automatically survive
along that scaling trajectory.

#### Decision

Attempt F is useful for checking signs and constants, not for closing the
paper.

### 10.9. Branch I Verdict

Branch I is fully investigated. It does not close by formal symmetry,
separate energy bounds, gauge invariance, or RP alone. It remains alive as the
specific estimate:

```math
\boxed{
\begin{array}{c}
\text{physical-cell charged-minus-pinned response screening}\\[1mm]
\text{with constants independent of }a.
\end{array}}
```

If that estimate fails on a positive-mass physical collar class, the failure
feeds directly into Branch III.

## 11. Full Investigation Of Branch II: Boundary Compression

`V4P41-TARGET-4106-BRANCH-II-BOUNDARY-COMPRESSION-AUDIT`.

Branch II asks whether a finite physical boundary state can retain all
charge-sensitive collar information relevant to the local ratio.

### 11.1. Exact Compression Would Prove Branch I

Assume there is a finite physical readout `Pi_eff` such that:

```math
\Pi_R^{\mathrm{eff}}(\eta)
=
\Pi_R^{\mathrm{eff}}(\eta')
```

implies:

```math
\left|
\log r_a(\eta)
-
\log r_a(\eta')
\right|
\le
C_R.
```

**Theorem 41.9 (Finite Compression Proves Response Screening In Quotient
Form).** A complete finite physical boundary compression proves the
reflected-asymmetry estimate after a finite comparison of reflected effective
states.

#### Proof

Compare `eta` to its effective boundary state, compare that state to its
reflection inside a finite-dimensional physical state space, then compare back
to `theta eta`. The constants depend only on `R` if fiber stability is
uniform.

#### Decision

Branch II is a valid positive route if the compression is non-tautological and
fiber-stable.

### 11.2. Center-Only Compression Fails

Center data alone do not determine the Wilson action response.

**Theorem 41.10 (Center-Only Compression Is Too Coarse).** Retaining only
center signs or center pairings is not enough to control `r_a(eta)` under the
ordinary finite `SU(2)` law.

#### Proof

Two collars can have identical center data and different coset or adjoint
holonomies. The Wilson action and the charged/pinned conditional weights
depend on those coset variables. Unless their charged-minus-pinned effect is
separately screened, center-only compression misses relevant data.

#### Decision

Center-only compression reduces to Branch I for the missing coset response.

### 11.3. Finite Wilson-Net Compression

A finite Wilson-net readout retains finitely many physical loops, holonomies,
and center pairings around the collar.

**Theorem 41.11 (Finite Wilson-Net Compression Is Equivalent To Residual
Screening).** A finite Wilson-net readout proves Branch II exactly when the
microscopic modes not retained by the net have uniformly bounded
charge-sensitive response.

#### Proof

The retained net controls only finitely many observables. The fiber over a net
value still contains cutoff-many microscopic modes. If their effect on
`log r_a` is bounded, the net is complete up to fixed-IR constants. If not,
two collars in the same fiber can have different ratios, so compression fails.

#### Decision

Finite Wilson-net compression is not independent of Branch I; it is Branch I
applied inside readout fibers.

### 11.4. Full Boundary Transfer State Is Tautological

Let `Pi_full(eta)` store the full charged and pinned transfer functionals.
Then it determines `r_a(eta)`.

**Theorem 41.12 (Full Boundary Transfer Compression Is Tautological).** A
compression that stores the sector partition weights or complete transfer
functional does not prove the theorem.

#### Proof

If the readout contains the answer, fiber stability is automatic. But the
proof has merely renamed the target ratio. This violates the
target-no-drift and noncircularity contract.

#### Decision

Full transfer compression is inadmissible unless it is reduced to a finite
physical state with an independent stability proof.

### 11.5. Boundary RG Version

The admissible positive version is a finite-rank boundary RG theorem:

```math
\eta
\longmapsto
\Pi_R^{\mathrm{eff}}(\eta),
```

where the residual microscopic collar modes have only `O_R(1)` effect on the
charged/pinned ratio.

**Criterion 41.13 (Finite-Rank Boundary RG Criterion).** Branch II succeeds if
there exists a deterministic finite-rank physical boundary RG map whose fiber
residual response is uniformly bounded as `a -> 0`.

#### Proof

A finite-rank map gives a finite physical comparison problem, and the residual
bound controls everything left inside each fiber. Combining both gives exact
compression with fixed-IR constants.

#### Decision

This is the surviving Branch II target.

### 11.6. Attempted Proof By Compactness Of Effective State Space

If the effective state space is compact and finite-dimensional, one might hope
uniform bounds are automatic.

**Theorem 41.14 (Effective Compactness Does Not Prove Fiber Stability).** A
compact finite effective state space is not enough. One must prove that the
pushforward captures the charge-sensitive response.

#### Proof

Compactness bounds continuous functions of the effective variables. It says
nothing about variation of `log r_a(eta)` inside a fiber unless the function
factors through the effective state. Fiber stability is exactly the missing
factorization theorem.

#### Decision

No compactness shortcut.

### 11.7. Branch II Verdict

Branch II is fully investigated. It does not close by center-only data,
finite Wilson nets without residual control, full transfer states, or compact
effective-state notation. It survives exactly as:

```math
\boxed{
\begin{array}{c}
\text{finite-rank physical boundary RG}\\[1mm]
\text{plus cutoff-uniform residual response screening.}
\end{array}}
```

Thus Branch II is equivalent in mathematical content to Branch I, but it may
be the cleaner implementation if one can construct the boundary RG map.

## 12. Full Investigation Of Branch III: Hostile Collars

`V4P41-TARGET-4107-BRANCH-III-HOSTILE-COLLAR-AUDIT`.

Branch III is the negative route. It tries to prove that response screening
fails on a physical collar class with positive environment mass.

### 12.1. Exact Negative Statement

The required hostile statement is:

```math
\nu_{R,a}(H_{R,a})
\ge
p_R
>
0
```

and:

```math
\log r_a(\eta)
-
\log r_a(\theta\eta)
\le
-L_a,
\qquad
L_a\to\infty,
```

for all `eta` in `H_R,a`.

**Theorem 41.15 (Positive-Mass Hostile Collars Falsify This Route).** If the
hostile statement holds, the boundary-stable de-tiling route of Paper 40
fails.

#### Proof

The reflected-asymmetry estimate requires the left side to be bounded below
by a fixed `-D_R`. On `H_R,a`, it tends to `-infinity`. Since the event has
mass bounded below, the failure is physical for this conditional route.

#### Decision

This is the exact negative theorem.

### 12.2. Pointwise Hostile Collars Are Insufficient

One can often write a collar that favors pinned response over charged response.

**Theorem 41.16 (Pointwise Hostility Is Not Enough).** A sequence of individual
hostile collars does not falsify the route unless it thickens to a
positive-mass physical event.

#### Proof

Individual collar configurations have zero Haar probability. A shrinking
microscopic neighborhood can also have probability tending to zero. Fixed-IR
falsification requires a physical event or a separate probability lower bound.

#### Decision

The negative route needs probability, not just construction.

### 12.3. Large Holonomy Hostility

Large physical collar holonomy is a natural candidate hostile class.

**Theorem 41.17 (Large Holonomy Is Only A Diagnostic).** Large collar holonomy
does not prove hostile response unless it is shown to suppress the charged
sector relative to the pinned sector.

#### Proof

Large holonomy may raise or lower both charged and pinned sector weights
together. Hostility is a difference-of-differences statement. Therefore
large holonomy must be paired with an odd/even or charged/pinned comparison.

#### Decision

Large holonomy can guide examples, but it is not itself the Branch III
theorem.

### 12.4. Character-Expansion Hostility

In a positive character expansion, hostile response would be odd/even boundary
entropy collapse on a positive-mass physical collar class.

**Criterion 41.18 (Odd/Even Entropy-Collapse Criterion).** Branch III succeeds
if one proves a physical collar event of positive mass on which odd constrained
boundary states have total weight smaller than even constrained states by
`e^{-L_a}` with `L_a -> infinity`, and the reflected partner does not collapse
simultaneously.

#### Proof

The charged/pinned ratio is represented by the odd/even constrained boundary
weight ratio. Collapse of that ratio gives collapse of `r_a(eta)`. If the
reflected ratio supplies paired compensation, the reflected asymmetry diverges
negatively.

#### Decision

This is the strongest negative representation.

### 12.5. Strong-Coupling Check Points Against Generic Hostility

In strong coupling, odd surfaces can proliferate rather than disappear.

**Theorem 41.19 (Strong Coupling Does Not Support A Generic Hostile-Collar
Claim).** Strong-coupling intuition does not suggest that positive-mass
hostile collars are automatic.

#### Proof

Confining strong-coupling expansions typically give abundant disorder-sector
surfaces. A generic collapse of odd boundary sectors would conflict with that
calibration. This is not a proof in the continuum scaling regime, but it warns
against assuming Branch III is easy.

#### Decision

Branch III is a serious falsification route, not a default expectation.

### 12.6. Branch III Verdict

Branch III is fully investigated. It does not close by pointwise examples,
large holonomy alone, or capacity diagnostics. It survives exactly as:

```math
\boxed{
\begin{array}{c}
\text{positive-mass physical collar class}\\[1mm]
\text{with charged-minus-pinned response collapse,}\\[1mm]
\text{equivalently odd/even boundary entropy collapse.}
\end{array}}
```

If this is proved, the Paper 40 single-collar fixed-IR certificate route fails.
If it cannot be proved and Branch I screening succeeds, the route remains
positive.

## 13. Final Decision After Branches I-III

`V4P41-FINAL-BRANCH-DECISION`.

The three branches have now been investigated one by one.

```math
\boxed{
\begin{array}{ll}
\text{Branch I}
&
\text{survives as physical-cell response screening},\\[1mm]
\text{Branch II}
&
\text{survives as finite-rank boundary RG plus residual screening},\\[1mm]
\text{Branch III}
&
\text{survives as positive-mass odd/even entropy collapse}.
\end{array}}
```

No branch closes by formal symmetry, finite-cutoff compactness, gauge
invariance, reflection positivity alone, center-only data, or pointwise bad
collar examples.

The least indirect positive theorem is:

```math
\boxed{
\begin{array}{c}
\text{for every physical collar cell, charged and pinned}\\[1mm]
\text{expectations of the collar-energy response differ by }O_R(1),\\[1mm]
\text{uniformly as }a\to0.
\end{array}}
```

The equivalent boundary-RG theorem is:

```math
\boxed{
\begin{array}{c}
\text{there is a finite-rank physical boundary state whose fibers}\\[1mm]
\text{have uniformly bounded charge-sensitive residual response.}
\end{array}}
```

The clean negative theorem is:

```math
\boxed{
\begin{array}{c}
\text{there is a positive-mass physical collar class where}\\[1mm]
\text{odd/even boundary entropy collapses as }a\to0.
\end{array}}
```

This is the honest endpoint of the branch-by-branch survey. The next actual
proof should try the physical-cell response-screening theorem first, because it
is the shortest path back to Paper 40's single-collar lower-tail certificate.
Sections 14-15 carry out that next step.

## 14. Continuation Program: Four Routes To The Single-Collar Asymmetry

`V4P41-CONTINUATION-PROGRAM-FOUR-ROUTES`.

Sections 10-13 left one target: the reflected-asymmetry bound

```math
\left|
\mathcal A_a(\eta)
\right|
=
\left|
\log r_a(\eta)-\log r_a(\theta\eta)
\right|
\le
D_R,
\qquad
D_R\text{ independent of }a.
```

This section records four concrete continuation routes to that bound, and §15
develops the first to the fullest. None of the four closes the estimate. Each
reorganizes it and attaches it to a usable tool; together they fix exactly what
is rigorous and what is the one remaining fixed-IR input.

### 14.1. Route R1: Reflection Even/Odd Reduction (Developed In §15)

The asymmetry is, by the trivial decomposition under the reflection involution
`θ`, exactly twice the reflection-odd part of the log-ratio:

```math
\mathcal A_a(\eta)
=
2\,(\log r_a)^{\mathrm{odd}_\theta}(\eta).
```

Consequence: de-tiling needs **only** the reflection-odd part of `log r_a`
bounded; the reflection-even part — which carries any reflection-symmetric
collar self-energy and any reflection-symmetric divergence — drops out
identically. This is exactly why Attempt A (§10.3) was too strong: a crude
bound on the full charged-minus-pinned response mixes the (irrelevant) even part
with the (relevant) odd part. R1 recasts reflection positivity (Attempt C, §10.5)
in its correct role here: not as a positivity bound on the ratio, but as the
**symmetry** that lets the even, divergent part cancel. Most promising; shortest
path to the certificate.

### 14.2. Route R2: Relative-Entropy Screening Bound

Bound the per-cell response by the closeness of the two sector collar marginals:

```math
\left|
\left\langle\dot S\right\rangle_{\mathrm{ch}}
-
\left\langle\dot S\right\rangle_{0}
\right|
\le
\underbrace{\left\|\dot S\right\|_{\mathrm{osc}}}_{\sim (R/a)^{d}}
\cdot
\underbrace{\left\|\mu^{\mathrm{col}}_{\mathrm{ch}}-\mu^{\mathrm{col}}_{0}\right\|_{\mathrm{TV}}}_{\text{sector closeness at the collar}}.
```

The product is `O_R(1)` iff conditioning on the deep center charge perturbs the
collar marginal by only an `a`-uniform amount — the quantitative form of "center
screening." This converts Attempt D's circular covariance identity into a
one-sided bound and connects to Pinsker, log-Sobolev, and the Paper-40 entropy
bridge. It is the analytic engine for R1's residual.

### 14.3. Route R3: Explicit Finite-Rank Boundary State

The minimal non-tautological `Π^{eff}_R` is forced: the charged/pinned
distinction is a single `Z_2` center pairing (rank one) plus finitely many low
transfer/coset modes (Theorem 41.10 rules out center-only). So

```math
\Pi^{\mathrm{eff}}_R
=
(\text{center pairing})
\;\oplus\;
(\text{finitely many low transfer/coset modes}),
```

and the residual is the **high-coset-mode** charged-minus-pinned response — i.e.
Branch I restricted to high modes. An optional lever is boundary-RG irrelevance
of the high modes; honest caveat: irrelevance is a near-fixed-point notion and is
forbidden as a weak-coupling substitute by IR5 unless promoted to a genuine
confined-phase boundary fixed-point statement.

### 14.4. Route R4: Asymmetric-Collapse Requirement (Sharpening Branch III)

Because the target is the asymmetry `𝒜_a = log r_a(η) − log r_a(θη)`, a
**reflection-symmetric** collapse `log r_a(η) ≈ log r_a(θη) → −∞` leaves `𝒜_a`
bounded and does not defeat de-tiling. The negative route therefore requires a
positive-mass class on which the collapse is **reflection-asymmetric**:

```math
(\log r_a)^{\mathrm{odd}_\theta}(\eta)\to-\infty
\quad\text{on a class of mass}\ \ge p_R>0.
```

This is strictly more specific than Branch III as stated in §12, and it is the
exact matched falsifier of R1. It is checkable (e.g. on large-coset-holonomy
collars).

### 14.5. Ranking And Choice

Route R1 is the most promising: the reduction is exact, the surviving residual is
symmetry-protected, it explains the failure of Attempt A, and it is the shortest
path to the de-tiling certificate. Routes R2 and R3 are the analytic engines for
R1's residual; R4 is its matched falsifier. We develop R1.

## 15. Full Development: The Reflection Even/Odd Reduction

`V4P41-TARGET-4108-REFLECTION-EVEN-ODD-REDUCTION`.

This section develops Route R1 to the point where exactly one fixed-IR estimate
remains, with everything else proved unconditionally.

### 15.1. The Reflection Involution On Collar Readouts

`θ` is an involution on collar readouts: `θ²=id`. It is induced by reflection of
the finite `SU(2)` configuration across the collar's reflection hyperplane, under
which the Wilson measure `μ_a` is invariant (the reflection-positivity hyperplane
of Paper 40 §18). The charged and pinned readout classes carry an induced action
`c\mapsto\theta c` on sector labels.

### 15.2. Exact Even/Odd Decomposition

For any function `f` of the collar readout, define

```math
f^{\mathrm{even}}(\eta)
=
\tfrac12\!\left(f(\eta)+f(\theta\eta)\right),
\qquad
f^{\mathrm{odd}}(\eta)
=
\tfrac12\!\left(f(\eta)-f(\theta\eta)\right).
```

Since `θ²=id`, this is an exact orthogonal decomposition `f=f^{even}+f^{odd}`
with `f^{even}(\theta\eta)=f^{even}(\eta)` and `f^{odd}(\theta\eta)=-f^{odd}(\eta)`.

**Lemma 41.20 (Asymmetry Is The Odd Part).** *For every fixed cutoff and every
collar readout,*

```math
\mathcal A_a(\eta)
=
\log r_a(\eta)-\log r_a(\theta\eta)
=
2\,(\log r_a)^{\mathrm{odd}}(\eta).
```

#### Proof

Immediate from the definition of `f^{odd}` with `f=\log r_a`. `∎`

#### Decision

The de-tiling target is therefore equivalent to an `a`-uniform bound on the
reflection-odd part alone:

```math
\boxed{
\left|\mathcal A_a(\eta)\right|\le D_R
\iff
\left|(\log r_a)^{\mathrm{odd}}(\eta)\right|\le \tfrac12 D_R.
}
```

### 15.3. The Reflection-Even Part Carries The Dangerous Divergence

The point of Lemma 41.20 is that the part of `log r_a` that defeated Attempt A is
reflection-even, hence absent from the target.

**Theorem 41.21 (Even Part Absorbs Reflection-Symmetric Divergences).** *Suppose
`log r_a` admits a decomposition `log r_a = L^{sym}_a + L^{res}_a` in which
`L^{sym}_a` is reflection-symmetric, `L^{sym}_a(\theta\eta)=L^{sym}_a(\eta)`.
Then `L^{sym}_a` contributes nothing to `\mathcal A_a`:*

```math
\mathcal A_a(\eta)
=
L^{\mathrm{res}}_a(\eta)-L^{\mathrm{res}}_a(\theta\eta)
=
2\,(L^{\mathrm{res}}_a)^{\mathrm{odd}}(\eta).
```

*In particular any reflection-symmetric divergent collar self-energy — exactly
the `\sim (R/a)^{d}` term that makes Attempt A fail — is irrelevant to the
asymmetry.*

#### Proof

A reflection-symmetric function is its own even part, so
`(L^{sym}_a)^{odd}=0`. Apply Lemma 41.20 to `log r_a = L^{sym}_a+L^{res}_a` and
use linearity of `f\mapsto f^{odd}`. `∎`

#### Decision

Attempt A bounded `|\langle\dot S\rangle_{ch}-\langle\dot S\rangle_0|`, which
contains both even and odd parts; its divergence lives entirely in the even part
that Theorem 41.21 discards. The honest residual question is therefore reduced
to: **is the divergent part of `log r_a` reflection-symmetric?**

### 15.4. Response Form Of The Odd Part

Use the finite-cutoff response identity (Theorem 41.2): along any smooth collar
path `eta(t)` from `θη` to `η`,

```math
\log r_a(\eta)-\log r_a(\theta\eta)
=
\int_0^1
\left(
\left\langle\dot S_{\eta(t)}\right\rangle_{0,t}
-
\left\langle\dot S_{\eta(t)}\right\rangle_{\mathrm{ch},t}
\right)
dt.
```

Choose the path **reflection-odd**: a path with `eta(1-t)=\theta\,eta(t)` and a
reflection-symmetric midpoint `eta(1/2)=\theta\,eta(1/2)`. Then the integrand at
`t` and at `1-t` are reflected partners, and the reflection-symmetric component
of the response cancels pairwise inside the integral, leaving

```math
(\log r_a)^{\mathrm{odd}}(\eta)
=
\int_0^{1/2}
\Big(
\Delta^{\mathrm{resp}}_a(t)
-
\Delta^{\mathrm{resp}}_a(t)\big|_{\theta}
\Big)
dt,
\qquad
\Delta^{\mathrm{resp}}_a(t)
:=
\left\langle\dot S\right\rangle_{0,t}-\left\langle\dot S\right\rangle_{\mathrm{ch},t}.
```

So the surviving quantity is the **reflection-odd part of the charged-minus-
pinned response** — a double difference (charge, then reflection) of the collar
response. Both the charge-blind collar self-energy and its reflection-symmetric
part are removed before any estimate is attempted.

### 15.5. The Residual Estimate As A Connected Correlation

`Δ^{resp}_a(t)` is, by the covariance identity (Attempt D, §10.6), a connected
correlation between the collar action derivative and the deep center charge:

```math
\Delta^{\mathrm{resp}}_a(t)
=
\frac{\mathrm{Cov}\!\left(\dot S_{\eta(t)},\,\mathbf 1_{\mathrm{ch}}\right)}{\mu(\mathrm{ch}\mid \eta(t))}
-
(\text{pinned analogue}),
```

between two regions at fixed physical separation `\rho_R` (collar to deep sheet).
Its reflection-odd part is supported where the collar `η` **breaks** reflection
symmetry. The residual target is then

```math
\boxed{
\left|
\int_0^{1/2}\!\!
\Big(\Delta^{\mathrm{resp}}_a(t)-\Delta^{\mathrm{resp}}_a(t)\big|_\theta\Big)dt
\right|
\le \tfrac12 D_R,
\qquad
D_R\ \text{independent of}\ a.
}
```

Reflection positivity enters here in its **structural** role: it supplies the
transfer representation in which this connected correlation between separated
regions is organized, and the reflection symmetry that makes the residual purely
odd. It does **not**, by itself, supply the magnitude bound (consistent with
Theorem 41.5).

### 15.6. What Is Proved And What Remains Open

```math
\boxed{
\begin{array}{ll}
\mathrm{PROVED}_{\mathrm{exact}}
&
\mathcal A_a=2(\log r_a)^{\mathrm{odd}}\ \text{(Lemma 41.20), unconditional},\\[1mm]
\mathrm{PROVED}_{\mathrm{cancel}}
&
\text{reflection-symmetric divergences drop out (Theorem 41.21)},\\[1mm]
\mathrm{PROVED}_{\mathrm{form}}
&
\text{the odd part is a reflection-odd charged-minus-pinned response (§15.4)},\\[1mm]
\mathrm{OPEN}_{\mathrm{IR}}
&
\text{the odd response is }O_R(1)\text{ uniformly as }a\to0\ (\S15.5).
\end{array}}
```

Three honest qualifications:

1. **This is weaker than the lower-tail.** The bound is on a *relative*,
   reflection-odd quantity; both `log r_a(η)` and `log r_a(θη)` may be large, only
   their difference must be controlled. So `OPEN_IR` is strictly weaker than the
   single-collar lower-tail theorem it feeds (via Paper-40 de-tiling).
2. **It is symmetry-protected and vanishes in the symmetric case.** If the
   collar's coupling to the deep center charge is reflection-symmetric, the odd
   response is zero and `𝒜_a=0`. The estimate measures only reflection-symmetry
   breaking of that coupling.
3. **No weak-coupling escape.** `OPEN_IR` is still a fixed-IR connected-
   correlation bound uniform as `a→0`; small-`g_eff` good-sector control does not
   prove it (IR5). The reduction relocates and shrinks the target; it does not
   remove the one genuine estimate.

### 15.7. Matched Falsifier And Branch III

By Lemma 41.20, the negative route is exactly the failure of `OPEN_IR`:

```math
\boxed{
\begin{array}{c}
\text{R1 fails}\iff (\log r_a)^{\mathrm{odd}}(\eta)\to-\infty
\ \text{on a collar class of mass}\ \ge p_R>0,\\[1mm]
\text{i.e. reflection-asymmetric collapse — the sharpened Branch III (§14.4).}
\end{array}}
```

A reflection-symmetric collapse does not falsify R1. This is the precise sense in
which the de-tiling route is robust to symmetric hostility and vulnerable only to
asymmetric hostility, and it is the concrete object to test on large-coset-
holonomy collars.

### 15.8. Status Of The Development

```math
\boxed{
\begin{array}{c}
\text{The single-collar asymmetry is reduced, exactly and unconditionally,}\\[1mm]
\text{to an }a\text{-uniform bound on one reflection-odd charged response.}\\[1mm]
\text{That bound is the sole remaining fixed-IR input; it is open,}\\[1mm]
\text{strictly weaker than the lower-tail, and symmetry-protected.}
\end{array}}
```

This is the fullest honest development of Route R1. It does not prove confinement
or the lower-tail; it isolates the minimal reflection-odd estimate whose proof
would, with Paper-40 de-tiling, deliver the single-collar fixed-IR certificate —
and whose positive-mass failure would falsify the route. The next concrete work
is the residual bound of §15.5, attacked through Route R2 (relative-entropy
screening) or Route R3 (finite-rank boundary state). Section 16 carries out R2.

## 16. Relative-Entropy Route: Mandatory Cancellation And The Residual Center-Decorrelation

`V4P41-TARGET-4109-RELATIVE-ENTROPY-ROUTE`.

This section attacks the §15.5 residual through Route R2. The outcome is not a
proof. It is one rigorous structural result — the even/odd cancellation of §15 is
**mandatory**, not optional — together with a sharp reduction of the residual to a
center-decorrelation estimate plus a sector-probability lower bound. A scaling
argument (flagged as such) shows distance-clustering alone, even a full mass gap,
is insufficient.

### 16.1. Covariance Form Of The Response (Exact)

Let `μ` be the finite-cutoff conditional law at the path collar `η(t)`, with
charged/pinned deep-sheet sector events `E_ch, E_0`, and let `Ṡ_p` be the collar
action derivative on plaquette `p`.

**Lemma 41.22 (Covariance Form).** *For every fixed cutoff and every collar
plaquette,*

```math
\Delta^{\mathrm{resp}}_p
:=
\left\langle\dot S_p\right\rangle_0
-
\left\langle\dot S_p\right\rangle_{\mathrm{ch}}
=
\frac{\mathrm{Cov}\!\left(\dot S_p,\mathbf 1_{E_0}\right)}{\mu(E_0)}
-
\frac{\mathrm{Cov}\!\left(\dot S_p,\mathbf 1_{E_{\mathrm{ch}}}\right)}{\mu(E_{\mathrm{ch}})}.
```

*When the sector probabilities are comparable, `μ(E_ch) ≈ μ(E_0) =: p`, this is*

```math
\Delta^{\mathrm{resp}}_p
\approx
-\frac{1}{p}\,\mathrm{Cov}\!\left(\dot S_p,\,Q\right),
\qquad
Q:=\mathbf 1_{E_{\mathrm{ch}}}-\mathbf 1_{E_0},
```

*a connected correlation between local collar energy and the deep center-charge
contrast `Q`.*

#### Proof

`⟨Y⟩_c − 𝔼[Y] = Cov(Y,𝟙_{E_c})/μ(E_c)` is the conditional-expectation identity;
the unconditional `𝔼[Ṡ_p]` cancels in the difference. `∎`

#### Decision

The naive bound on the *full* measures fails: `μ_ch` and `μ_0` are conditioned on
disjoint deep events, so `‖μ_ch − μ_0‖_TV ≈ 1`. Lemma 41.22 replaces it by a
collar-marginal connected correlation, which is the correct object.

### 16.2. The Raw Response Diverges Under Distance-Clustering (Scaling)

**Proposition 41.23 (Distance-Clustering Is Insufficient; Scaling Argument).**
*Assume the strongest distance estimate, exponential clustering with a fixed
physical mass `m`,*

```math
\left|\mathrm{Cov}\!\left(\dot S_p,\mathbf 1_{E_c}\right)\right|
\le
C\,\beta\,e^{-m\,d(p)},
\qquad
\mu(E_c)\ge p_R,
```

*where `d(p)` is the physical collar-to-charge distance and `‖Ṡ_p‖=O(β)` with
`β∼\log(1/a)` along the 4D asymptotically free trajectory. Then the summed raw
response is extensive and divergent:*

```math
\left|\sum_{p\in\mathrm{collar}}\Delta^{\mathrm{resp}}_p\right|
\;\lesssim\;
\frac{C\beta}{p_R\,a^{4}}
\int_{\mathrm{collar}}e^{-m\,d(x)}\,d^4x
\;=\;
O\!\left(\frac{\beta\,V_{\mathrm{eff}}(R)}{p_R\,a^{4}}\right)
\xrightarrow[a\to0]{}\infty.
```

#### Proof (scaling)

The collar holds `∼ V_col/a^4` microscopic plaquettes; each contributes
`O(β e^{-m d(p)})` by hypothesis. Converting the sum to a fixed physical integral
gives the `1/a^4` density times the convergent physical integral
`V_eff(R)=∫ e^{-m d}`. The exponents are schematic and geometry-dependent; the
robust content is that the bound grows as a positive power of `1/a`. `∎`

#### Decision

```math
\boxed{
\begin{array}{c}
\text{Distance-clustering — even a full mass gap — does not bound the raw}\\[1mm]
\text{Branch-I response, because it is an extensive sum over }\sim 1/a^4\text{ plaquettes.}\\[1mm]
\text{Therefore a cancellation, not an absolute bound, is required:}\\[1mm]
\text{the §15 even/odd reduction is mandatory, not merely convenient.}
\end{array}}
```

This is the genuine positive result of the route, and it quantitatively explains
the failure of Attempt A (§10.3).

### 16.3. The Odd Residual Reduces To Center-Charge Decorrelation

By Lemma 41.20 the survivor is the reflection-odd part, in which the
reflection-symmetric (distance-only) piece responsible for the divergence of
Proposition 41.23 cancels:

```math
(\log r_a)^{\mathrm{odd}}(\eta)
=
\sum_{p\in\mathrm{collar}}
\big[\Delta^{\mathrm{resp}}_p\big]^{\mathrm{odd}_\theta},
\qquad
\big|\Delta^{\mathrm{resp}}_p\big|\le\operatorname{osc}(\dot S_p)=O(\beta)
\ \text{(see §16.4).}
```

The remaining sum is still over `∼1/a^4` plaquettes, so it is `O_R(1)` only if the
collar-energy/center-charge correlation is suppressed by **more than distance** —
namely by center symmetry, which makes local energy observables decorrelate from
the deep center sector. Define this as the closing criterion.

**Criterion 41.24 (Center-Decorrelation Closes The Odd Residual).** *If, at fixed
physical `R` and uniformly as `a→0`,*

```math
\left|
\sum_{p\in\mathrm{collar}}
\big[\Delta^{\mathrm{resp}}_p\big]^{\mathrm{odd}_\theta}
\right|
\le
\tfrac12 D_R,
```

*then `|𝒜_a(η)| ≤ D_R` and, with Paper-40 de-tiling, the single-collar fixed-IR
certificate follows.*

#### Decision

The hypothesis of Criterion 41.24 is exactly a center-charge decorrelation
(disorder) estimate — the confinement content itself — not a generic clustering
or weak-coupling input. R2 reduces the residual to it; it does not supply it.

### 16.4. The Denominator Is Auto-Compensated (T1 Is Not An Obstruction)

A correction to the natural first guess — and to the first draft of this
section. One might fear that the `1/μ(E_c)` in the covariance form of Lemma 41.22
blows up the response when a sector is rare, forcing a separate sector-
probability floor. It does not.

**Lemma 41.25 (Conditional Response Is Bounded Independently Of Sector Mass).**
*For every fixed cutoff, every collar plaquette, and every sector of positive
probability,*

```math
\left|\Delta^{\mathrm{resp}}_p\right|
=
\left|\left\langle\dot S_p\right\rangle_0-\left\langle\dot S_p\right\rangle_{\mathrm{ch}}\right|
\le
\operatorname{osc}(\dot S_p),
\qquad
\left|\mathrm{Cov}\!\left(\dot S_p,\mathbf 1_{E_c}\right)\right|
\le
\operatorname{osc}(\dot S_p)\,\mu(E_c).
```

*Hence the factor `1/μ(E_c)` in Lemma 41.22 is always compensated, and no
sector-probability floor is needed to control the response.*

#### Proof

A conditional expectation of `\dot S_p` lies between its own extrema, so the
difference of two conditional expectations is at most `osc(\dot S_p)`. The
covariance bound is the same statement:
`|Cov(\dot S_p,\mathbf 1_{E_c})| = |\langle\dot S_p\rangle_c-\langle\dot S_p\rangle|\,\mu(E_c) \le osc(\dot S_p)\,\mu(E_c)`. `∎`

#### Decision

The sub-target "T1" of the first draft — a collar-local two-sidedness floor
`μ(E_c|η)≥p_R` — is therefore **spurious**: it is not required to bound the
asymmetry residual. The genuine question of whether `μ(E_{ch}|η)` is exponentially
small is the single-collar lower tail itself, produced by the asymmetry bound
together with the Paper-40 paired-RP de-tiling (which supplies the
reflection-symmetric magnitude), not by a separate input to the residual. The
sole residual of Route R2 is the extensive odd sum of §16.3.

### 16.5. Status Of The Relative-Entropy Route

```math
\boxed{
\begin{array}{ll}
\mathrm{PROVED}_{\mathrm{mandatory}}
&
\text{the raw response is extensive-divergent under distance-clustering;}\\
&
\text{the §15 even/odd cancellation is mandatory (Prop. 41.23)},\\[1mm]
\mathrm{PROVED}_{\mathrm{nofloor}}
&
\text{the conditional response is bounded by osc; the denominator is}\\
&
\text{auto-compensated, so the first-draft floor "T1" is spurious (Lemma 41.25)},\\[1mm]
\mathrm{REDUCED}_{\mathrm{sole}}
&
\text{the sole residual is the summed reflection-odd center-charge}\\
&
\text{decorrelation (Criterion 41.24)},\\[1mm]
\mathrm{OPEN}_{\mathrm{IR}}
&
\text{that residual is the fixed-IR disorder estimate at the frontier}.
\end{array}}
```

Honest verdict: Route R2 removes exactly the parts that were always going to
cancel, proves that distance-clustering and (by IR5) weak-coupling cannot
substitute, shows the sector-probability denominator is not an obstruction
(Lemma 41.25), and deposits everything on a single residual:

```math
\boxed{
\text{(T2) odd center-decorrelation:}\quad
\textstyle\sum_p[\Delta^{\mathrm{resp}}_p]^{\mathrm{odd}_\theta}=O_R(1)\ \text{(the disorder frontier)}.
}
```

The reflection-symmetric magnitude of `log r_a` is supplied separately by the
Paper-40 paired-RP de-tiling; the asymmetry route adds only T2. T2 is the genuine
center-disorder content and coincides with the vortex/'t Hooft free-energy
frontier identified in Paper 40. R2 is therefore a faithful reduction, not a
closure: it does not prove T2, and the scaling argument of §16.2 is
order-of-magnitude, not a rigorous theorem. The attempt to "crack T1" instead
**dissolved** it — a deflationary advance: a false obstruction is removed and the
open content is concentrated on the single frontier estimate T2.

## 17. Attack On T2: Strong-Coupling Result And The Equivalence To Confinement

`V4P41-TARGET-4110-T2-ATTACK`.

This section records a direct attack on T2 (the sole residual of §16). The honest
outcome is that T2 does not close: it is not a tractable sub-lemma but is
**equivalent**, at fixed physical `R`, to disorder-side confinement itself. Four
angles were tried; one yields a rigorous strong-coupling result, and the rest
converge on a single conserved obstruction.

### 17.1. Two Angles That Do Not Reach T2

**Finite-mode / path decomposition.** Interpolate `η→θη` in steps and bound each
susceptibility `∂log r_a/∂(mode)`. This fails by a conservation law: a localized
physical mode touches `O_R(1)` plaquettes but requires `O(1/a^4)` moves to reach
`θη`; a smooth mode requires `O_R(1)` moves but each carries an extensive
`O(β/a^4)` response. Extensivity is invariant under repartitioning of the path.

**Reflection positivity / Tomboulis-Yaffe.** RP submultiplicativity controls the
*reflected-pair*, i.e. the **symmetric** combination `log r_a(η)+log r_a(θη)` —
which is the magnitude already supplied by the Paper-40 de-tiling. T2 is the
**odd** part, exactly the combination RP cancels. So RP and the T-Y vortex-free-
energy bounds are structurally aimed at the complement of T2, not at T2.

### 17.2. Strong-Coupling Result (Rigorous, IR5-Bounded)

**Proposition 41.26 (T2 Holds At Fixed Strong Coupling).** *There is `β_c>0` such
that for every fixed `β<β_c`, T2 holds: `|𝒜_a(η)|≤D_R(β)` uniformly as `a→0`.*

#### Proof (cluster expansion)

At fixed `β<β_c` the character/polymer expansion of the `SU(2)` lattice measure
converges, and connected correlations decay as `ζ(β)^{d_{\mathrm{lat}}}` with
`ζ(β)<1` and `d_lat` the lattice distance (Osterwalder-Seiler). The per-plaquette
response obeys `|\Delta^{resp}_p|\le C(β)\,ζ(β)^{d_{\mathrm{lat}}(p,\mathrm{sheet})}`.
Summing, with the number of plaquettes at lattice distance `d` growing
polynomially,

```math
\Big|\sum_{p}[\Delta^{\mathrm{resp}}_p]^{\mathrm{odd}}\Big|
\le
C(β)\sum_{d\ge \rho_R/a} d^{3}\,ζ(β)^{d}
=
O_R(1).
```

The lattice correlation length is `O(1)` lattice spacings `=O(a)` physical, so
only an `O(1)`-plaquette neighborhood of the sheet contributes as `a→0`. `∎`

#### Decision (IR5 boundary)

Proposition 41.26 validates the route and the definitions, but it does **not**
reach the continuum. The continuum trajectory is `β→∞` (asymptotic freedom);
there `ζ(β)→1`, the lattice correlation length grows without bound, the `O(a)`-
physical localization is lost, and the `β/a^4` extensivity returns uncured. This
is exactly the IR5 boundary: strong-coupling control does not survive the
scaling limit. Proposition 41.26 is therefore recovered known territory, not the
continuum statement.

### 17.3. T2 Is Equivalent To Fixed-IR Confinement

**Proposition 41.27 (T2 ⇔ Fixed-IR Disorder-Side Confinement, Modulo The
Paper-40 RP Magnitude).** *At fixed physical `R`:*

- *(⇐) if the theory confines on the disorder side — the conditional center-vortex
  free energy `log r_a(η)` is perimeter-bounded uniformly in `a` (equivalently
  center symmetry is unbroken) — then `log r_a` and its reflection-odd part are
  `O_R(1)`, so T2 holds;*
- *(⇒) if T2 holds, then with the Paper-40 paired-RP de-tiling (which supplies the
  reflection-symmetric magnitude `log r_a(η)+log r_a(θη)`) the single-collar lower
  tail follows, which is the disorder-side confinement certificate.*

#### Proof

(⇐) is the standard 't Hooft order/disorder dictionary: a perimeter-law vortex
free energy is bounded, hence so is its odd part. (⇒) is the Paper-40 de-tiling:
T2 bounds the ratio `log r_a(η)−log r_a(θη)`, the RP input bounds the sum, and
together they bound `log r_a(η)` below — the lower tail. `∎`

#### Decision

T2 is therefore **not a side-estimate that helps prove confinement**; it is, modulo
a separately-supplied RP magnitude, **equivalent** to fixed-IR disorder-side
confinement. This explains structurally why every reduction in §§14-16 left T2
standing: there is nothing smaller beneath it. The physical content of the
equivalence is center-symmetry: T2 holds iff local energy decorrelates from the
global center charge, i.e. iff center symmetry is unbroken.

### 17.4. The Conserved Obstruction And The Named Frontier Input

Every angle meets one obstruction: the response is an extensive sum over `~1/a^4`
plaquettes, cured only by **center-charge decorrelation** (the per-plaquette
responses summing to `O_R(1)` by genuine cancellation). Distance-clustering
cannot do it (§16.2); RP targets the symmetric complement (§17.1); center-
decorrelation *is* confinement (§17.3); energy-entropy delivers it at strong
coupling only (§17.2). The single input that would close T2 is:

```math
\boxed{
\begin{array}{c}
\text{a uniform-in-}a\text{ bound on the summed reflection-odd}\\[1mm]
\text{center-charge / collar-energy connected correlation —}\\[1mm]
\text{the conditional, local analogue of a Tomboulis-Yaffe weak-coupling}\\[1mm]
\text{vortex-free-energy perimeter law, open in }4D.
\end{array}}
```

### 17.5. Honest Status Of The T2 Attack

```math
\boxed{
\begin{array}{ll}
\mathrm{PROVED}_{\mathrm{strong}}
&
\text{T2 holds at fixed strong coupling (Prop. 41.26); IR5-bounded, known territory},\\[1mm]
\mathrm{PROVED}_{\mathrm{equiv}}
&
\text{T2}\Leftrightarrow\text{fixed-IR disorder-side confinement, modulo Paper-40 RP (Prop. 41.27)},\\[1mm]
\mathrm{OBSTRUCTION}
&
\text{conserved extensivity, cured only by center-decorrelation},\\[1mm]
\mathrm{OPEN}_{\mathrm{frontier}}
&
\text{the named weak-coupling vortex-free-energy input; this is the open problem}.
\end{array}}
```

T2 does not crack. The reduction chain of this paper (R1 → even/odd → T2) lands
**exactly** on the known hard problem: the strong-coupling case is done, and the
weak-coupling continuum case is the 4D 't Hooft vortex-free-energy frontier. This
is the honest terminus of the rigorous reduction chain; further progress
requires genuine weak-coupling vortex-free-energy analysis, not another formal
reduction. Section 18 records exploratory, partly-conjectural directions toward
that frontier.

## 18. Exploratory Directions: Analyticity, Spectral Asymmetry, And Solvable Calibration

`V4P41-TARGET-4111-EXPLORATORY-DIRECTIONS`.

This section is explicitly speculative. Each direction is tagged by rigor level.
None closes T2; together they reframe it and propose a new sub-target. They are
recorded because they change the *status* of T2 and supply a concrete object to
compute, not because they constitute a proof.

### 18.1. Direction A: No-Bulk-Transition Continuation

**Rigor: conditional on the (believed, numerically robust, not rigorously proven)
absence of a bulk phase transition in 4D SU(2) Wilson theory.**

The strong-coupling series for `𝒜_a(β)` converges and is bounded for `β<β_c`
(Proposition 41.26); the series then fails at its radius `β_c`. But `β_c` is the
radius of convergence — a complex/roughening singularity — not necessarily a
singularity of the function. Since 4D SU(2) has no bulk phase transition (one
analytic phase from strong to weak coupling), `𝒜_a(β)` continues analytically
along the whole trajectory `β:0\to\infty`.

**Observation 41.28 (Status Reclassification).** *Under no bulk transition, T2's
failure at weak coupling is a failure of the strong-coupling **method** (series
radius), not evidence that T2 is false: `𝒜_a(β)` does not blow up at `β_c`.
Hence T2 is reclassified from "prove or falsify" to "resum": the task is the
analytic continuation / Borel-Padé resummation of the vortex-free-energy series
past `β_c`.*

This is a status change, not a bound: analytic functions can still grow, so
analyticity alone does not give `|𝒜_a|≤D_R`. But it removes the worry that T2 is
false (the Branch III fear), consistent with confinement being a single phase.

**Logical relation (sharpened).** A *proof* of no bulk transition would extend
confinement from strong coupling to all fixed lattice couplings (one analytic
phase) — a major step — but T2 is the `a→0` statement at fixed physical `R`,
which additionally needs asymptotic scaling (`σ_{phys}>0` in the continuum);
analyticity does not supply that. Conversely a proof of T2 to the continuum would
establish that confinement persists, i.e. no *deconfinement* transition along the
trajectory. The two are deeply linked but not identical: no-transition is broader
(any non-analyticity), T2 is the continuum-scaling statement. So this is a
near-link, not a biconditional.

### 18.2. Direction B: The Reflection-Commutator / Spectral-Asymmetry Localization

**Rigor: conjectural framework; proposes a new sub-target T2′.**

Reflection positivity gives a plane Hilbert space, a reflection `Θ` (`Θ²=1`), and
charged/neutral transfer operators `T_{ch},T_0`. Schematically
`log r_a(η)=log[⟨η|T_{ch}|η⟩/⟨η|T_0|η⟩]`, so

```math
\mathcal A_a(\eta)=\log r_a(\eta)-\log r_a(\Theta\eta).
```

If `[T_{ch},Θ]=[T_0,Θ]=0` then `𝒜_a≡0`. Therefore the entire asymmetry is
sourced by the **non-commutation of the charged transfer with reflection**,
`[T_{ch},Θ]`, which is supported only where the center defect crosses the
reflection plane — a fixed-physical, codimension-≥1 set, not the bulk collar.
This is the structural reason the `1/a^4` extensivity should be absent from
`𝒜_a`: the reflection-symmetric bulk commutes with `Θ` and drops, leaving a
commutator localized to a lower-dimensional fixed set. It is the discrete
analogue of the fact that the odd-under-involution part of a determinant is a
finite spectral asymmetry (eta-invariant) supported on the fixed-point locus.

**Conjecture 41.29 (Commutator Localization Sub-Target T2′).** *The asymmetry is
controlled by the reflection-commutator of the charged transfer,*

```math
\left|\mathcal A_a(\eta)\right|
\le
C_R\,\big\|[T_{\mathrm{ch}},\Theta]\big\|_{\,\mathrm{defect}\cap\mathrm{plane}},
```

*and this commutator, localized to the defect–plane intersection, is `O_R(1)`
uniformly as `a→0`.*

T2′ is **not** the open RP3 charged-gap of Paper 40 §40: RP3 wants a spectral
*gap* of `T_{ch}`; T2′ wants a *commutator* `[T_{ch},Θ]`, a different and
plausibly weaker object (a commutator can be small with no gap). Routing T2 to a
lower-dimensional commutator rather than a bulk gap is the freshest reduction
available. Open: the nonperturbative construction of `T_{ch}` and the proof that
the commutator is bounded.

#### 18.2.1. Second Pass: The Commutator Is The Vortex Twist's Reflection-Defect

Write the charged transfer as the neutral transfer dressed by the center-vortex
insertion `V` — the 't Hooft twist multiplying links crossing the spanning defect
surface by `z=-1`: `T_{ch}=V\,T_0` in the transfer representation. Since
`[T_0,Θ]=0` (RP),

```math
[T_{\mathrm{ch}},\Theta]=[V,\Theta]\,T_0,
\qquad
[V,\Theta]=\big(V-\Theta V\Theta\big)\Theta=\big(V-V_{\theta(\mathrm{defect})}\big)\Theta .
```

The difference `V-V_{θ(defect)}` is supported only on the symmetric difference
`defect △ θ(defect)` — the reflection-asymmetric part of the 2D spanning surface,
a fixed-physical **codimension-2** (`~1/a^2`) region, not codim-1 and not the
bulk collar.

**Observation 41.30 (Symmetric-Defect Vanishing; transfer representation).** *In
the transfer representation, assume RP (`Θ` unitary, `Θ²=1`, `[T_0,Θ]=0`),
`r_a(η)=⟨η|T_{ch}|η⟩/⟨η|T_0|η⟩` with `|θη⟩=Θ|η⟩`, and a reflection-symmetric
spanning defect (`θ(defect)=defect`, hence `[T_{ch},Θ]=0`). Then `𝒜_a(η)=0` for
every collar `η`.*

#### Proof

```math
r_a(\theta\eta)
=\frac{\langle\Theta\eta|T_{\mathrm{ch}}|\Theta\eta\rangle}{\langle\Theta\eta|T_0|\Theta\eta\rangle}
=\frac{\langle\eta|\Theta T_{\mathrm{ch}}\Theta|\eta\rangle}{\langle\eta|\Theta T_0\Theta|\eta\rangle}
=\frac{\langle\eta|T_{\mathrm{ch}}|\eta\rangle}{\langle\eta|T_0|\eta\rangle}
=r_a(\eta),
```

using `[T_{ch},Θ]=[T_0,Θ]=0` and `Θ²=1`. Hence `𝒜_a=0`. `∎`

#### Decision

This reorganizes T2. **The collar's own asymmetry is irrelevant**; only the
charged-sector operator's reflection symmetry matters. T2 reduces to two precise,
non-frontier-looking sub-questions:

```math
\boxed{
\begin{array}{ll}
\mathrm{(i)} & \text{justify the transfer representation of the conditional sector}\\
& E_{\mathrm{ch}}\text{ as the operator insertion }V\text{ (conditioning vs operator)},\\[1mm]
\mathrm{(ii)} & \text{determine when the spanning defect admits a reflection-symmetric choice;}\\
& \text{where it does, }\mathcal A_a\equiv0\text{ and T2 holds.}
\end{array}}
```

The residual is only loops/collars whose geometry forbids a reflection-symmetric
spanning surface; there the open object is the codim-2 commutator `[V,Θ]` on
`defect △ θ(defect)` — a `1/a^2` (not `1/a^4`) object, a genuine reduction in the
divergence degree. **Honest caveats:** (a) `T_{ch}=V T_0` and the matrix-element
form of `r_a` are the transfer *representation*; the exact identification of
conditioning on `E_{ch}` with inserting `V` must be established and may carry
corrections — this conditioning-vs-operator subtlety is now load-bearing. (b)
Whether the symmetric tiling that pairs `η↔θη` always admits a symmetric local
defect is a geometric claim to prove, not assert.

#### 18.2.2. Resolution Of Caveat (a): The Conditional Center-Flux Form

Caveat (a) — "is conditioning on `E_{ch}` the same as inserting `V`?" — is
answered, and in the favorable direction. The charged/pinned sectors are the two
`Z_2` center sectors of the sheet `S`. Let `Ξ_S=\prod_{p\in S}b_p\in\{\pm1\}` be
the center flux through `S` and `m(η):=\mathbb E_\mu[Ξ_S\mid\text{collar}=η]` the
conditional center-flux order parameter. Conditioning on a sector is the
**projector** `P_\pm=(1\pm Ξ_S)/2`, **not** the operator insertion `V`:

```math
\mu(E_\pm\mid\eta)=\frac{1\pm m(\eta)}{2},
\qquad
r_a(\eta)=\frac{\mu(E_-\mid\eta)}{\mu(E_+\mid\eta)}=\frac{1-m(\eta)}{1+m(\eta)}.
```

So the rigorous object is a Möbius transform of `m`; the `V`-insertion picture of
§18.2.1 was a heuristic, now replaced.

**Lemma 41.31 (Symmetric-Sheet Vanishing — rigorous).** *If `μ` is reflection-
invariant under `θ` (standard for the Wilson action across the RP hyperplane) and
the sheet is reflection-symmetric (`θS=S`), then `m(θη)=m(η)` for every collar,
hence `𝒜_a(η)\equiv0`.*

#### Proof

By `θ`-invariance of `μ` and `θ(\{\text{collar}=θη\})=\{\text{collar}=η\}`,

```math
m(θη)=\mathbb E_\mu[Ξ_S\mid θη]=\mathbb E_\mu[Ξ_S\circ θ\mid η]=\mathbb E_\mu[Ξ_{θS}\mid η],
```

using `Ξ_S\circ θ=Ξ_{θS}` (the center variable is reflection-covariant). Since
`θS=S`, `Ξ_{θS}=Ξ_S`, so `m(θη)=m(η)`, giving `r_a(θη)=r_a(η)` and `𝒜_a=0`. `∎`

No transfer matrix and no operator-insertion assumption are used — only reflection
covariance of a conditional expectation. Observation 41.30 is thereby upgraded to
a lemma, and (a) is resolved.

#### 18.2.3. The Clarifying Catch: The Magnitude, Not The Asymmetry, Is The Frontier

Lemma 41.31 does **not** close confinement, and seeing why sharpens the whole
chain. With `𝒜_a\equiv0` (symmetric sheet), the de-tiling's asymmetry input is
rigorously satisfied, so the single-collar lower tail rests entirely on the
remaining input — the **magnitude**: `m(η)` bounded away from `\pm1` uniformly as
`a\to0` (equivalently `log r_a(η)` bounded), the conditional **vortex free
energy**. This is **not** supplied by reflection positivity: Paper 40 §40 gives
RP2 (domination/upper bound), not the strict lower bound the magnitude needs.

```math
\boxed{
\begin{array}{c}
\text{The asymmetry (T2) is the tractable half — rigorously }0\text{ for symmetric sheets.}\\[1mm]
\text{The magnitude }m(η)\not\to\pm1\text{ (vortex free energy) is the hard half: the frontier.}\\[1mm]
\text{RP-domination does not give it.}
\end{array}}
```

This **refines §17**: the framing "T2 ⇔ confinement (modulo RP magnitude)" put the
weight on T2, but the honest correction is that the asymmetry is the easy part and
the magnitude carries the confinement content. The reduction chain R1 → even/odd →
T2, fully cashed out, shows the difficulty was never the asymmetry — it is the
conditional center-flux order parameter staying off `\pm1` into the continuum,
which is exactly the vortex-free-energy frontier. Caveat (b) (symmetric defects in
de-tiling) now matters only for trivializing the asymmetry, which was the easy
half regardless.

#### 18.2.4. Resolution Of Caveat (b): Equivariant Symmetrization For Rectangular Loops

Caveat (b) — "can the de-tiling use reflection-symmetric spanning sheets?" — is
resolved for the physically relevant (axis-aligned rectangular) Wilson loop, up to
perimeter-order corner terms, by an explicit `Z_2`-chain symmetrization.

Work with `Z_2` 2-chains. Let `Π` be the collar reflection plane, `θ` the
reflection, and `S=S^++S^-` the split of a spanning sheet across `Π`. Define

```math
S^\ast:=S^++\theta S^+\pmod 2.
```

**Proposition 41.32 (Equivariant Symmetrization).** *If `∂S` is `θ`-symmetric
(`θ(∂S)=∂S`), then `θS^\ast=S^\ast` and `∂S^\ast=∂S`.*

#### Proof

`∂S^\ast=∂S^++θ(∂S^+)`, and `∂S^+=(∂S\cap+)+(S\cap\Pi)`. Since `θ` fixes `Π`
pointwise, `θ(S\cap\Pi)=S\cap\Pi`, so the two cut terms cancel mod 2:
`(S\cap\Pi)+(S\cap\Pi)=0`. With `∂S` symmetric, `θ(∂S\cap+)=(∂S\cap-)`, hence
`∂S^\ast=(∂S\cap+)+(∂S\cap-)=∂S`. Invariance `θS^\ast=θS^++S^+=S^\ast` is immediate.
`∎`

The mod-2 cancellation of the cut along the fixed plane is the mechanism: a single
reflected half-sheet, glued along `Π`, returns to the original boundary with no
seam. So a `θ`-symmetric spanning sheet exists whenever the boundary is
`θ`-symmetric, and Lemma 41.31 then gives `𝒜_a≡0`.

**Corollary 41.33 (Rectangular Loops: Asymmetry Vanishes Off Corners).** *Tile each
straight side of an axis-aligned rectangular Wilson loop with collars whose RP
reflection planes are the coordinate hyperplanes perpendicular to that side
through lattice midpoints. Then the local loop segment and the flat sheet's
boundary are `θ`-symmetric, so by Proposition 41.32 a `θ`-symmetric spanning sheet
exists and by Lemma 41.31 `𝒜_a≡0` on every straight-side collar. The `O_R(1)`
corner collars contribute `O_R(1)`.*

The corners are L-shaped, symmetric only about a `45°` diagonal — not a lattice RP
plane — so they are not forced to `𝒜_a=0`; but there are four of them, each a
fixed physical region, so their total is `O_R(1)` and **perimeter-order**, absorbed
into the constant `κ` of `⟨W⟩\le e^{-σA+κL}` where it cannot affect the area term.

```math
\boxed{
\begin{array}{c}
\text{For rectangular loops the de-tiling asymmetry input holds:}\\[1mm]
\mathcal A_a\equiv0\text{ on straight-side collars (Prop. 41.32 + Lemma 41.31),}\\[1mm]
O_R(1)\text{ on the four corners (perimeter-order).}
\end{array}}
```

**Honest caveats.** (i) Proposition 41.32 requires the full boundary `∂S` —
including the sheet's exit curves on the collar walls — to be `θ`-symmetric, not
only the loop segment; for a flat/minimal sheet and perpendicular bisecting planes
this is natural but is a geometric detail to verify. (ii) Corners give `O_R(1)`,
not `0` (perimeter, harmless for the area law, but the asymmetry is not *exactly*
zero everywhere).

**What it resolves and what it does not.** This finishes the **asymmetry side** of
the de-tiling for rectangular loops. It does **not** prove confinement: with the
asymmetry handled, the single-collar lower tail rests entirely on the **magnitude**
(`m(η)` off `\pm1`, i.e. `⟨Ξ_S⟩` area-law decay), which is the vortex-free-energy
frontier and is not supplied by RP (§18.2.3). Caveat (b) cracked thus completes the
tractable half and isolates the magnitude as the sole open frontier.

### 18.3. Direction C: Solvable Calibration

**Rigor: exact in the stated limits; calibration, not the 4D continuum.**

- **2D Yang-Mills** is exactly solvable (heat-kernel / Migdal): `log r_a(η)` is
  closed-form, T2 holds exactly (exact area law), and one can check whether `𝒜_a`
  is the finite localized object Conjecture 41.29 predicts. A clean test.
- **Large-N SU(N)**: center-vortex free energies have definite scaling (`k`-string
  sine/Casimir), disorder is `1/N^2`-organized; T2 is plausibly clean and tests
  the commutator-localization picture.

### 18.4. Long Shots

**Rigor: speculative.**

- **Kramers-Wannier on the center sector**: a `Z_2` self-duality relating
  `r_a(η)↔r_a(θη)` could pin the asymmetry. Caveat: SU(2) is not self-dual and
  center-only data are too coarse (Theorem 41.10).
- **Migdal-Makeenko loop equations**: the conditional vortex free energy obeys an
  exact nonperturbative functional equation; its reflection structure might close
  into a bounded fixed point. Caveat: loop equations are hard to close in 4D.

### 18.5. Honest Status Of The Exploratory Directions

```math
\boxed{
\begin{array}{ll}
\mathrm{A\ (analyticity)}
&
\text{reclassifies T2 as true-needs-resummation; conditional on no bulk transition; not a bound},\\[1mm]
\mathrm{B\ (commutator)}
&
\text{conjectural; new sub-target T2}'=\|[T_{\mathrm{ch}},\Theta]\|\text{, lower-dim, } \ne\text{ RP3 gap},\\[1mm]
\mathrm{C\ (solvable)}
&
\text{exact calibration in 2D / large-}N,\text{ consistent with T2},\\[1mm]
\mathrm{long\ shots}
&
\text{KW center duality, loop equations — speculative}.
\end{array}}
```

None of these is a proof, and B is a conjecture, not a theorem. Their value is to
change the status of T2 (Direction A: almost certainly true), to supply a fresh
lower-dimensional target (Direction B: the reflection-commutator T2′), and to give
checkable calibrations (Direction C). The frontier itself — a uniform weak-coupling
bound — remains open.

## 19. The Open Problem, Stated Self-Containedly

`V4P41-OPEN-PROBLEM-EXACT-STATEMENT`.

**This section is self-contained and may be read in isolation.** It defines, from
nothing, the single open problem on which the entire reduction of this paper
rests. No symbol or claim here depends on §§0-18; everything used is redefined.
The aim is zero ambiguity: a reader of only this section should be able to state
the problem precisely and recognize a purported solution.

### 19.1. The lattice gauge theory

Fix a lattice spacing `a>0` and a finite four-dimensional hypercubic lattice
`Λ={0,a,2a,…,(L-1)a}^4`, with boundary conditions for which reflection across each
coordinate hyperplane is a symmetry (periodic, or the reflection-symmetric
boundary conditions of Osterwalder–Seiler).

```math
\boxed{
\begin{array}{ll}
\text{links}
&
ℓ=(x,μ),\ x∈Λ,\ μ∈\{1,2,3,4\}\ \text{(from }x\text{ to }x+a\hat e_\mu\text{); reversal}\to U_ℓ^{-1},\\[1mm]
\text{link field}
&
U_ℓ\in SU(2)\ \text{for every link},\\[1mm]
\text{plaquette}
&
U_p=U_{x,μ}\,U_{x+a\hat e_μ,ν}\,U_{x+a\hat e_ν,μ}^{-1}\,U_{x,ν}^{-1}\ \text{for the }(μ,ν)\text{ square at }x,\\[1mm]
\text{action}
&
S_β(U)=β\sum_p\big(1-\tfrac12\operatorname{tr}U_p\big),\qquad β=4/g_0^2,\\[1mm]
\text{measure}
&
d\mu_{a,β}(U)=Z_{a,β}^{-1}\,e^{-S_β(U)}\prod_ℓ dU_ℓ,\quad dU_ℓ=\text{normalized Haar on }SU(2),\\[1mm]
\text{expectation}
&
\langle\,\cdot\,\rangle_{a,β}=\int(\cdot)\,d\mu_{a,β}.
\end{array}}
```

Here `\operatorname{tr}` is the `2×2` fundamental trace and `g_0` the bare
coupling. This is ordinary 4D `SU(2)` Wilson lattice gauge theory; no further
structure is assumed.

### 19.2. The gauge-invariant Wilson loop and the string tension

For a rectangular contour `C_{R,T}` of physical side lengths `R,T` built from
lattice links, the **fundamental Wilson loop** is the gauge-invariant observable

```math
W(C)=\tfrac12\operatorname{tr}\prod_{ℓ∈C}U_ℓ .
```

The **lattice string tension** at coupling `β` and the **continuum string
tension** along the trajectory of §19.5 are

```math
σ_{\mathrm{lat}}(β)=-\lim_{R,T\to\infty}\frac{a^2}{RT}\,\log\big|\langle W(C_{R,T})\rangle_{a,β}\big|,
\qquad
σ_{\mathrm{phys}}=\lim_{a\to0}\frac{σ_{\mathrm{lat}}(β(a))}{a^2}.
```

Confinement at coupling `β` means `σ_lat(β)>0` (the Wilson loop has an area law).
`σ_lat` is dimensionless (lattice units); `σ_phys` has dimension (length)`^{-2}`.

### 19.3. The center-flux reformulation `Ξ_S`

`SU(2)` has center `\{+\mathbf 1,-\mathbf 1\}\cong\mathbb Z_2`. Fix a **center
projection**: a measurable map `U_ℓ\mapsto z_ℓ\in\{\pm1\}` assigning a `Z_2`
center value to each link (e.g. the center component in maximal center gauge, or
the section-relative center part of the `SU(2)\to SO(3)` lift). Define the `Z_2`
plaquette and, for a set of plaquettes `S` (a "sheet"), the **center flux**:

```math
b_p=\prod_{ℓ∈∂p}z_ℓ\in\{\pm1\},\qquad Ξ_S=\prod_{p∈S}b_p .
```

By `Z_2` Stokes (each interior link occurs in two plaquettes and cancels), if
`∂S=C` then

```math
Ξ_S=\prod_{ℓ∈C}z_ℓ ,
```

so `Ξ_S` is **surface-independent** — it depends only on the boundary loop `C` —
and equals the **center-projected Wilson loop**. Its area-law content defines the
**center string tension** `σ_c(β)`, `σ_{c,\mathrm{phys}}`, exactly as in §19.2
with `W` replaced by `Ξ`.

**Status of `Ξ_S` (read carefully).** The projection `z_ℓ` depends on the
center-projection choice, so `Ξ_S` is gauge/section-dependent; only its area-law
content is physics. **Center dominance** — the equality
`σ_{c,\mathrm{phys}}=σ_{\mathrm{phys}}` — is expected and numerically robust but
**not rigorously proven**. Hence the gauge-invariant statement of §19.2 (via `W`)
is the canonical, ambiguity-free form of the problem; the `Ξ_S` form is the
center reformulation, equal to it under center dominance.

### 19.4. The conditional single-collar magnitude (the form this paper reduces to)

Fix a physical scale `R` and a **collar**: a fixed physical region near a segment
of the contour `C`. Let `η` denote a fixed **collar readout** — a deterministic
function of the configuration restricted to the collar (the conditioning datum).
Define the **conditional center-flux order parameter** and the **charged/pinned
ratio**

```math
m(η)=\big\langle Ξ_S\big\rangle_{a,β}\big(\,\cdot\mid\text{collar readout}=η\,\big)\in[-1,1],
\qquad
r_a(η)=\frac{1-m(η)}{1+m(η)} ,
```

where `r_a(η)=\mu(Ξ_S=-1\mid η)/\mu(Ξ_S=+1\mid η)` is the ratio of the two `Z_2`
center-sector conditional probabilities. The **single-collar magnitude** is the
requirement that `m(η)` be bounded away from `\pm1` uniformly in `a`, equivalently
that `|\log r_a(η)|` be bounded. This is the object to which the present paper
reduces continuum confinement after its asymmetry side is discharged (§§14-18);
it is connected to the full area law of §19.2-19.3 by the de-tiling of those
sections.

### 19.5. The continuum (weak-coupling) trajectory

Weak coupling is `g_0^2=4/β\to0`, i.e. `β\to\infty`. The **continuum limit** is
`a\to0` taken jointly with `β=β(a)\to\infty` along the renormalization trajectory
that holds a physical reference scale fixed (equivalently, holds a renormalized
coupling at a fixed physical distance constant). Asymptotic freedom (positive
one-loop coefficient) gives `a(β)\to0` as `β\to\infty`, so a region of fixed
physical size `R` contains `\sim(R/a)^4\to\infty` plaquettes.

```math
\boxed{
\text{"uniformly as }a\to0\text{ at fixed physical }R\text{": constants may depend on }R,\ \text{never on }a.}
```

### 19.6. The open problem (exact)

**Open Problem (continuum confinement / string-tension positivity).** *For 4D
`SU(2)` Wilson lattice gauge theory (§19.1), prove or disprove that, along the
continuum trajectory (§19.5),*

```math
\boxed{
σ_{\mathrm{phys}}=\lim_{a\to0}\frac{σ_{\mathrm{lat}}(β(a))}{a^2}\ \ \text{exists, is finite, and satisfies}\ \ σ_{\mathrm{phys}}>0 .
}
```

*Equivalently in the center form (under center dominance): the center-projected
Wilson loop obeys an area law with a positive continuum center string tension,*

```math
\big|\langle Ξ_S\rangle_{a,β(a)}\big|\le K\,\exp\!\big(-σ_{c,\mathrm{phys}}\,\mathrm{Area}_{\mathrm{phys}}(S)+κ\,\mathrm{Perim}_{\mathrm{phys}}(∂S)\big),
\qquad σ_{c,\mathrm{phys}}>0 .
```

*Equivalently in the single-collar magnitude form (§19.4), to which this paper
reduces: there is `δ_R>0`, independent of `a`, such that for the relevant fixed
physical `R` and all admissible collar readouts `η`,*

```math
\boxed{
\liminf_{a\to0}\ \inf_{η}\ \big(1-|m(η)|\big)\ \ge\ δ_R\ >\ 0 .
}
```

These three are the same confinement statement (the second modulo center
dominance, the third modulo the §§14-18 de-tiling).

### 19.7. What is known and what is open

```math
\boxed{
\begin{array}{ll}
\textbf{Known}
&
\text{at each fixed small }β\ (\text{strong coupling}):\ σ_{\mathrm{lat}}(β)=\log(4/β)+O(β)>0,\\
&
\text{by a convergent character/cluster expansion (Wilson 1974; Osterwalder–Seiler).}\\
&
\text{This is at fixed lattice spacing; it does not reach the continuum.}\\[2mm]
\textbf{Open}
&
\text{whether }σ_{\mathrm{lat}}(β)>0\text{ persists as }β\to\infty,\ \text{and whether}\\
&
σ_{\mathrm{phys}}>0\ (\text{asymptotic scaling}),\ \text{as }a\to0.\ \textbf{This is the open problem.}
\end{array}}
```

It is the lattice form of the 4D Yang–Mills confinement/mass-gap question of the
Clay Millennium Problem.

### 19.8. What counts as a solution

A solution is a proof or disproof of §19.6 by estimates **uniform along the
continuum trajectory** that do not assume the conclusion in disguise. In
particular a valid proof may **not** assume, as an input, any of:

```math
\boxed{
\begin{array}{l}
\text{a mass gap; exponential clustering; a finite correlation length;}\\
\text{a positive string tension; center-charge decorrelation;}\\
\text{a strong-coupling estimate as a substitute for the continuum statement;}\\
\text{a weak-coupling perturbative/good-sector bound as a substitute.}
\end{array}}
```

Each of these is equivalent to, or stronger than, or methodologically forbidden
for, the conclusion. Concretely, the open content is a bound on the
center-disorder (vortex) free energy that is uniform as `a\to0` at fixed physical
`R` — the 4D weak-coupling 't Hooft vortex-free-energy estimate. After the
asymmetry side of this paper is discharged (§§14-18, Lemmas 41.20/41.31,
Propositions 41.23/41.32, Corollary 41.33), the single-collar magnitude of §19.4
is the sole remaining input, and no formal reduction in this paper closes it.

## 20. External Audit: The Kernel Is The Clay Kernel, Not A Closed Proof

`V4P41-AUDIT-CLAY-KERNEL-NONABELIAN-FORK`.

This section records the external audit that should govern how the rest of this
paper is read. Its purpose is not to weaken the reductions above. It is to keep
their status exact: the paper has isolated a sharp fixed-IR center-disorder
kernel, but it has not proved the continuum Yang-Mills confinement problem.

### 20.1. No-Overclaim Rule

The open problem of §19 is the lattice form of the four-dimensional Yang-Mills
confinement/mass-gap problem. Any statement in this paper that would imply a
positive continuum string tension must therefore be treated as a candidate
solution to a Millennium problem unless it is explicitly conditional.

Accordingly, every downstream claim is governed by the following rule.

```math
\boxed{
\begin{array}{l}
\text{A reduction may be called closed only if its remaining input is not}\\
\text{equivalent to confinement, a mass gap, center disorder, or a}\\
\text{uniform weak-coupling vortex-free-energy bound.}
\end{array}}
```

This is not rhetorical caution. It is a mathematical guardrail against assuming
the missing scale. The continuum effect is non-perturbative in the bare coupling;
perturbative small-field estimates and fixed-cutoff strong-coupling estimates do
not by themselves control it.

### 20.2. The SU(2) Versus U(1) Fork

Any proof strategy for four-dimensional `SU(2)` confinement must distinguish it
from compact four-dimensional `U(1)` lattice gauge theory. The latter has a
weak-coupling Coulomb phase, so a method that uses only abelian-compatible
ingredients cannot be a proof of the `SU(2)` continuum area law.

The forbidden class includes:

- purely local energy estimates that ignore non-commutativity;
- dimension-counting or entropy-counting estimates insensitive to the group;
- positivity arguments that would apply unchanged to compact `U(1)`;
- fixed-plaquette small-field estimates without a non-abelian mechanism that
  survives the continuum trajectory.

The allowed mechanisms must use something genuinely non-abelian, such as
asymptotic freedom, `SO(3) x Z_2` frustration, non-commuting holonomies, or a
center-vortex free-energy flow that differs from the compact-abelian case.

Migdal-Kadanoff type recursions are useful as diagnostics here: on hierarchical
lattices they exhibit the desired `SU(2)` flow toward strong coupling, while the
compact `U(1)` case has a weak-coupling Coulomb behavior. On the hypercubic
lattice this is not a proof, because the required inequalities do not close in
the needed direction. Its lesson is only directional: the relevant phenomenon is
a non-abelian flow, not a fixed-coupling small-field estimate.

### 20.3. The Vortex-Free-Energy Dictionary

On a periodic four-torus, let `Z_+` be the untwisted partition function and let
`Z_-` be the partition function with a nontrivial `Z_2` center twist inserted on
a coclosed stack of plaquettes winding two periodic directions. Define the
magnetic-vortex free energy by

```math
F_{\mathrm{mg}}(a,L)=-\log\frac{Z_-}{Z_+}.
```

The Tomboulis-Yaffe route gives a rigorous bridge from center-vortex disorder to
Wilson-loop area law: if the appropriate vortex free energy has the confining
large-volume behavior, then the Wilson loop is bounded by an area-law expression.
For `SU(2)`, the electric and magnetic center sectors are related by the finite
`Z_2` Fourier transform, so the magnetic vortex free energy is the natural dual
quantity for bounding electric flux and Wilson loops.
Conversely, thick center vortices are known to be necessary in the standard
vortex picture: if the relevant thick vortices linking the loop are constrained
away, the Wilson loop loses the area law at weak coupling.

For this paper the important point is the dictionary, not a new theorem:

```math
\boxed{
\begin{array}{c}
\text{single-collar magnitude}\\
\Updownarrow\\
\text{conditional non-collapse of the center sector}\\
\Updownarrow\\
\text{fixed-IR version of a center-vortex free-energy lower/upper balance}\\
\Updownarrow\\
\text{the residual confinement kernel.}
\end{array}}
```

The fixed-IR single-collar problem of §19.4 is the local conditional analogue of
the vortex-free-energy estimate. It is sharper than the global twist statement
because it asks for sector non-collapse after conditioning on an admissible
physical collar readout.

### 20.4. Thin Vortices, Thick Vortices, And The Circle

The physical mechanism expected to save center disorder at weak bare coupling is
vortex thickening. Thin vortices are efficient at strong coupling but their
action cost is too large at weak coupling; they are suppressed as `beta` grows.
The expected continuum disorder comes instead from vortices with finite physical
thickness. Their action cost and positional entropy are then both physical-scale
quantities.

This is also the circle. To prove that thick vortices have the right fixed
physical cost is to prove that the theory dynamically generates the relevant
physical scale. That is exactly what a continuum confinement proof must do.
Therefore the phrase "thick vortices percolate" is a mechanism unless backed by
a cutoff-uniform free-energy estimate; as an assumption, it is the conclusion in
physical language.

### 20.5. Alignment Ledger For The Audit

The audit does not modify the ontology or target.

```math
\boxed{
\begin{array}{ll}
\text{Fixed IR} &
\text{all constants may depend on the physical collar scale }R
\text{ but not on }a.\\
\text{Barandes alignment} &
\text{all readouts are deterministic functions of one finite }SU(2)
\text{ configuration.}\\
\text{No hidden Markov law} &
\text{transfer operators, RG maps, and kernels are proof devices, not new}\\
&
\text{dynamics postulated by the ontology.}\\
\text{No broadening} &
\text{global twist, tiled, and entropy statements are used only if they}\\
&
\text{return to the original single-collar conditional ratio.}
\end{array}}
```

## 21. Three Proposal Audits

`V4P41-AUDIT-THREE-PROPOSALS`.

The three natural proposals are: an entropy formulation, a `Z_2` comparison
formulation, and a reflection-positivity/decimation formulation. Each has a
rigorous part. Each stops at the same fixed-IR center-disorder estimate.

### 21.1. Proposal I: Conditional Entropy

Let

```math
p_a(\eta)=\mu_{a,\beta(a)}(\Xi_S=+1\mid\eta),
\qquad
m_a(\eta)=2p_a(\eta)-1.
```

The binary entropy of the conditional center sector is

```math
H_2(p)=-p\log p-(1-p)\log(1-p).
```

The single-collar magnitude is exactly equivalent to non-collapse of this
conditional binary entropy.

**Lemma 41.34 (entropy equivalence).** For fixed `R`, the following two
statements are equivalent, with constants depending only on each other:

```math
\liminf_{a\to0}\inf_{\eta}\big(1-|m_a(\eta)|\big)>0,
```

and

```math
\liminf_{a\to0}\inf_{\eta}H_2(p_a(\eta))>0.
```

**Proof.** Since

```math
1-|m_a(\eta)|=2\min(p_a(\eta),1-p_a(\eta)),
```

both quantities vanish exactly when the conditional law of `\Xi_S` becomes a
point mass. On any closed subinterval of `(0,1)`, `H_2` is bounded below; near
`0` or `1`, both `H_2(p)` and `\min(p,1-p)` vanish monotonically. This gives the
two-sided conversion of constants.

The entropy view also gives a real monotonicity, but only in expectation. Suppose
collar readouts are nested so that a finer readout determines the coarser one:

```math
\eta_n=f_n(\eta_{n+1}).
```

Then the data-processing inequality gives

```math
H(\Xi_S\mid\eta_{n+1})\le H(\Xi_S\mid\eta_n).
```

Thus refining the collar cannot raise the average unresolved center entropy. The
continuum limit is therefore the hard limit. However, this does **not** prove the
worst-collar lower bound of §19.4, because an average entropy statement can hide
a small set of hostile readouts.

The first tempting entropy target is summability of the cross-scale information
loss. That target is vacuous. Since `\Xi_S` is binary,

```math
0\le I(\Xi_S;\eta_n)\le H(\Xi_S)\le \log 2,
```

so the total information budget is automatically finite. The real target is not
summability. It is non-saturation:

```math
\boxed{
\inf_{\eta}H(\Xi_S\mid\eta)\ge h_R>0
\quad\text{uniformly as }a\to0.
}
```

In words: deconfinement is the possibility that a continuum-resolution physical
collar learns the center flux completely. Fixed-IR confinement on this route is
the statement that a positive amount of center-sector uncertainty survives every
admissible collar readout.

**Audit verdict.** Entropy gives the cleanest language for the target. It does
not manufacture the missing lower bound.

### 21.2. Proposal II: A `Z_2` Comparison Sandwich

The natural comparison idea is to rewrite the `SU(2)` theory in center and coset
variables:

```math
SU(2)\longrightarrow SO(3)\times Z_2
```

up to the usual section and compatibility bookkeeping. One then asks whether the
induced center sector can be sandwiched between ferromagnetic `Z_2` gauge
systems whose disordered phase is known.

The rigorous obstruction is frustration. After the `SO(3)` variables are
integrated or conditioned away, the effective `Z_2` theory is not a
ferromagnetic single-plaquette model. It contains fluctuating monopole and
hybrid-vortex constraints. Equivalently, the effective couplings are not
sign-definite and not purely local in the FKG/Griffiths sense.

Therefore the standard monotone comparison tools do not apply:

```math
\boxed{
\text{no FKG/GKS sandwich is available for the true induced }Z_2
\text{ center measure.}
}
```

This is not merely a technical nuisance. The same non-abelian frustration that
distinguishes `SU(2)` from compact `U(1)` is what destroys the easy comparison
proof. Engineered `Z_2` models can be made confining by enforcing positivity or
damping assumptions, but that proves the engineered model, not the induced
center sector of `SU(2)` Wilson theory.

The comparison route still yields a useful negative statement:

```math
F_{\mathrm{mg}}(a,L)\ge0
```

is the easy side, expressing that inserting a twist cannot create a negative
vortex free-energy cost in the relevant normalized setting. The confining input
needed here is the opposite type of estimate: a uniform fixed-IR sector
comparability or disorder lower bound.

**Audit verdict.** The `Z_2` comparison route identifies the correct
non-abelian obstruction, but the available correlation inequalities have the
wrong hypotheses for the true induced center measure.

### 21.3. Proposal III: Reflection Positivity And Decimation

Reflection positivity is the strongest rigorous positive structure available in
this paper. It gives a transfer matrix, chessboard estimates, and the
Tomboulis-Yaffe type route from a local/tiled disorder input to an area-law
output. The obstruction is not that reflection positivity is false. The
obstruction is that reflection positivity supplies upper-bound technology, while
the missing fixed-IR input is a lower-bound or minorization statement.

In schematic form, a decimation route compares twisted and untwisted partition
functions across scales:

```math
\frac{Z_n^-}{Z_n}
\quad\longrightarrow\quad
\frac{Z_{n+1}^-}{Z_{n+1}}.
```

The contested step in the Tomboulis-style program is a per-decimation
inequality controlling this ratio uniformly along the weak-coupling trajectory.
In the present paper's language, that per-step ratio control is another form of
the single-collar non-collapse estimate. It must stop the odd/charged center
sector from being lost under repeated coarse-graining.

This is the location of the Ito-Seiler objection to the Tomboulis program: the
unresolved item is not reflection positivity itself, but the uniform per-step
control of the twisted/untwisted ratio under approximate decimation.

Reflection positivity proves:

- existence of a positive transfer matrix;
- even/odd center grading when the center transformation is represented;
- chessboard upper bounds;
- fixed-cutoff positivity statements.

Reflection positivity does not by itself prove:

- a lower bound on the charged/odd sector;
- uniform fixed-physical tile minorization as `a\to0`;
- a strict positive continuum string tension.

**Audit verdict.** RP and decimation are the serious analytic route, but the
remaining inequality is exactly the fixed-IR center-disorder kernel, not a
formal consequence of RP.

## 22. Unified Kernel: Entropy, Decimation, And Minorization

`V4P41-UNIFIED-KERNEL-ENTROPY-DECIMATION-MINORIZATION`.

The three audits above are not three unrelated failures. They expose the same
residual estimate in three languages.

### 22.1. Transfer Operator And Center Grading

In a temporal-gauge transfer-matrix representation, reflection positivity gives
a positive self-adjoint transfer operator `T` on the physical Hilbert space. Let
`P` denote the global center transformation when represented on this space. Then

```math
P^2=1,
\qquad
PT=TP.
```

Consequently `T` decomposes into center-even and center-odd blocks:

```math
T=T_+\oplus T_-.
```

Let

```math
\lambda_+(a)=\|T_+\|,
\qquad
\lambda_-(a)=\|T_-\|,
\qquad
\Delta_c(a)=\log\frac{\lambda_+(a)}{\lambda_-(a)}.
```

Perron-Frobenius positivity puts the vacuum in the even block, so

```math
\Delta_c(a)\ge0.
```

This inequality is rigorous but too weak. A continuum proof cannot require
`\Delta_c(a)` to be bounded below by a positive lattice-unit constant, because a
fixed physical length contains `O(1/a)` transfer steps and elementary lattice
gaps vanish in a continuum limit.

The fixed-IR object is the physical block operator

```math
T_R(a)=T^{N_R(a)},
\qquad
N_R(a)=\left\lfloor\frac{R}{a}\right\rfloor.
```

The needed scale statement is instead

```math
\boxed{
\liminf_{a\to0}N_R(a)\Delta_c(a)>0
}
```

in the charged center channel relevant to the collar/tile under consideration.
Equivalently, the center distinction must accumulate to a positive physical
amount across a fixed physical block, while each microscopic step becomes
near-identity.

### 22.2. Minorization Form Of The Same Target

Normalize the positive kernel of `T_R(a)` to a Markov kernel on boundary
configurations:

```math
P_R^a(\omega,d\zeta)
=
\frac{K_R^a(\omega,\zeta)\,d\zeta}
{\int K_R^a(\omega,u)\,du}.
```

Write its density as `p_R^a(\omega,\zeta)`, so that
`P_R^a(\omega,d\zeta)=p_R^a(\omega,\zeta)d\zeta`. Define the Dobrushin overlap
coefficient by

```math
\alpha_R(a)
=
\inf_{\omega,\omega'}
\int \min\{p_R^a(\omega,\zeta),p_R^a(\omega',\zeta)\}\,d\zeta.
```

The fixed-physical block minorization target is

```math
\boxed{
\liminf_{a\to0}\alpha_R(a)\ge\alpha_R^*>0.
}
```

This is not asserted here as an automatic theorem equivalent to confinement in
full generality. It is the correct lower-bound shape: a fixed physical transfer
block must retain a uniformly positive amount of mixing/overlap in the charged
center sector after the microscopic cutoff is removed. In standard Markov-kernel
settings, such a minorization is precisely the kind of floor that prevents a
conditional binary sector from collapsing to a point mass.

For this paper it should be read as a candidate sufficient bridge:

```math
\boxed{
\text{fixed-physical charged-sector minorization}
\quad\Longrightarrow\quad
\text{single-collar entropy floor}
\quad\Longrightarrow\quad
\text{the fixed-IR certificate of Sections 14--19.}
}
```

The hard part is the first arrow. At fixed cutoff it is easy because the state
space is compact and the kernel is strictly positive after a finite block. Along
the continuum trajectory the block is an infinite product of near-identity
operators, and minorization is not stable under such products without a
quantitative non-perturbative input.

### 22.3. Relative-Entropy Form Of The Same Obstruction

For two finite-volume Gibbs measures `mu` and `nu` with actions `S_mu` and
`S_nu` over the same reference measure, the Gibbs variational identity gives

```math
-\log\frac{Z_\nu}{Z_\mu}
=
\mathbb E_\mu[S_\nu-S_\mu]
-
D_{\mathrm{KL}}(\mu\|\nu).
```

Thus a twisted/untwisted free-energy comparison can be read as a mean-action
term minus a relative-entropy term. Under a decimation or coarse-graining map,
the information about the binary center flux is a contraction of the full
configuration information by data processing. Schematically,

```math
I(\Xi_S;\text{coarse detail})
\le
D_{\mathrm{KL}}(\text{exact block law}\|\text{approximating block law}).
```

This explains why the entropy and decimation views point to the same residual:
relative-entropy control can keep the bookkeeping distortion finite, but it
does not by itself prove the non-saturation gap. The missing step remains a
lower bound saying that the limiting conditional center law is not a point mass.

### 22.4. The Shared Residual Estimate

The same missing statement has four equivalent faces inside this paper's
reduction:

```math
\boxed{
\begin{array}{cl}
\text{entropy face} &
\inf_{\eta}H(\Xi_S\mid\eta)\ge h_R>0,\\[1mm]
\text{center face} &
\text{the induced frustrated }Z_2\text{ sector remains disordered},\\[1mm]
\text{decimation face} &
\text{twisted/untwisted ratios are controlled at every RG step},\\[1mm]
\text{operator face} &
\text{fixed-physical charged blocks satisfy a minorization floor.}
\end{array}}
```

This shared estimate is the rigorous dimensional-transmutation kernel. It is
where the physical scale must enter. It cannot be replaced by:

- a fixed-cutoff strong-coupling expansion;
- a weak-coupling perturbative good-sector estimate;
- reflection positivity alone;
- an abelian-compatible comparison theorem;
- an assumed mass gap or assumed center disorder.

### 22.5. Why Reflection Positivity Cannot Close The Floor By Itself

Reflection positivity is a Schwarz-type positivity:

```math
\langle \theta(A)A\rangle\ge0.
```

Iterating this positivity gives chessboard inequalities and upper bounds on
correlators. The missing estimate is a lower bound: the charged center channel
must retain enough weight after conditioning or coarse-graining. Upper-bound
technology cannot by itself produce this floor.

This explains why the lower side of decimation is the delicate side. The upper
bracket is naturally RP-compatible. The lower bracket asks for a positive
amount of center disorder to survive the continuum product, and this is exactly
the input that would distinguish confining `SU(2)` from weak-coupling compact
`U(1)`.

### 22.6. The Honest Next Target

The most precise next target is not another global criterion. It is the
fixed-physical charged-block lower-tail problem:

```math
\boxed{
\text{prove or falsify a uniform lower bound on the charged-sector overlap}
\text{ of }T_R(a)\text{ as }a\to0\text{ at fixed physical }R.
}
```

Two concrete, non-broadening tests follow.

1. **Decimation test.** Rewrite the contested twisted/untwisted decimation step
   as a transfer-operator inequality for `T_R(a)`. Determine exactly which lower
   bound on the odd/charged block would make the step valid.

2. **Functional-inequality test.** Estimate the spectral-gap, log-Sobolev, or
   hypercontractive constants of the elementary `SU(2)` plaquette transfer
   operator and track their degradation under the product of `N_R(a)` steps.
   The test passes only if the accumulated fixed-physical block retains a
   cutoff-uniform charged-sector floor. If the constants degrade as in an
   abelian near-identity diffusion with no non-perturbative scale, the route
   fails.

Both tests are proof devices internal to ordinary `SU(2)` Wilson theory. They do
not add a Markov ontology, do not change the readout law, and do not broaden the
target beyond the single-collar conditional ratio. They merely locate the last
estimate with maximal precision.

### 22.7. Bottom-Line Status

The paper's current status after the audit is:

```math
\boxed{
\begin{array}{l}
\text{All formal response/asymmetry/de-tiling reductions have been pushed to}\\
\text{one fixed-IR kernel: conditional center-sector non-collapse.}\\[1mm]
\text{The entropy, }Z_2\text{ comparison, RP/decimation, and operator}\\
\text{minorization languages all identify the same missing estimate.}\\[1mm]
\text{No section of this paper proves that estimate. Proving it would be a}\\
\text{genuine continuum confinement result, not a bookkeeping lemma.}
\end{array}}
```

The value of the reduction is therefore not that it solves the Clay problem. Its
value is that it names the exact lower-bound estimate any fixed-IR center route
must prove, and it rules out several tempting ways of mistaking a conditional
criterion for that proof.

## 23. Numerical Decimation Diagnostic: The Block Flow Sees More Than One Plaquette

`V4P41-NUMERICAL-MK-DECIMATION-DIAGNOSTIC`.

Section 22.6 proposed a concrete diagnostic: replace the elementary
single-plaquette object by a block-decimation object and check whether the
effective lightest-channel coefficient begins to distinguish `SU(2)` from
compact `U(1)`. This section records that computation.

The computation is a diagnostic only. It uses the standard character-coefficient
Migdal-Kadanoff style recursion with scale factor `b=2` in dimension `d=4`. It is
not a proof for the hypercubic lattice, and it is not a substitute for the
single-collar lower-tail estimate.

### 23.1. Recursion Used

Write the normalized central plaquette weight in character form. For `SU(2)`:

```math
f_n(U)=1+\sum_{j>0}(2j+1)c_j(n)\chi_j(U).
```

For compact `U(1)`:

```math
f_n(\theta)=1+2\sum_{k\ge1}c_k(n)\cos(k\theta).
```

The MK-style step used in the script is:

```math
\zeta=b^{d-2}=4,
\qquad
r=b^2=4,
```

and

```math
F_j(n)=\int [f_n(U)]^\zeta\,\frac{\chi_j(U)}{2j+1}\,dU,
\qquad
c_j(n+1)=\left(\frac{F_j(n)}{F_0(n)}\right)^r
```

for `SU(2)`, with the analogous Fourier projection for `U(1)`.

The lightest-channel gap proxies are:

```math
m_{1/2}^{SU(2)}(n)=-\log c_{1/2}(n),
\qquad
m_1^{U(1)}(n)=-\log c_1(n).
```

The effective beta is inferred from the tree weak-coupling relations:

```math
m_{1/2}^{SU(2)}\sim \frac{3}{2\beta_{\mathrm{eff}}},
\qquad
m_1^{U(1)}\sim \frac{1}{2\beta_{\mathrm{eff}}}.
```

For `SU(2)`, the one-loop continuum prediction for the beta decrement under a
scale-two block is

```math
\Delta\beta_{\mathrm{1loop}}
=8b_0\log2,
\qquad
b_0=\frac{11}{24\pi^2},
\qquad
\Delta\beta_{\mathrm{1loop}}=0.257511807\ldots .
```

The script is:

```text
mk_decimation_diagnostic.py
```

It uses only Python's standard library: midpoint quadrature on the group class
angle and finite character/Fourier cutoffs.

### 23.2. Run Result

The stable convergence check used:

```text
python3 mk_decimation_diagnostic.py \
  --beta 50 100 200 \
  --steps 6 \
  --grid-su2 8192 --grid-u1 8192 \
  --j2-max 120 --n-max 120
```

For initial `beta=100`, the output was:

```text
SU(2), beta_eff inferred from m_{1/2}
step    beta_eff       beta decrement from previous step
0       99.501288      -
1       99.875079      -0.373790
2       99.663778       0.211301
3       99.416044       0.247734
4       99.166028       0.250016
5       98.915869       0.250159
6       98.665700       0.250169

U(1), beta_eff inferred from m_1
step    beta_eff       beta decrement from previous step
0       99.497887      -
1       99.874869      -0.376982
2       99.898335      -0.023465
3       99.899801      -0.001466
4       99.899893      -0.000092
5       99.899898      -0.000006
6       99.899899      -0.000000
```

The same pattern was stable at `beta=50` and `beta=200`:

```text
SU(2): after the first transient, the step decrement stabilizes near 0.250.
U(1):  after the first transient, the step decrement tends to 0.
```

The `SU(2)` diagnostic decrement is close to, but not identical with, the
one-loop value `0.257511807...`. That level of agreement should not be
overinterpreted: the MK recursion is an approximate/hierarchical diagnostic, not
the exact hypercubic RG. The important feature is qualitative and stable:

```math
\boxed{
\text{the block recursion sees a non-abelian }SU(2)\text{ flow signal,}
\qquad
\text{while }U(1)\text{ remains approximately marginal.}
}
```

### 23.3. Interpretation

The earlier single-plaquette computation gave only the tree-level gaps:

```math
m_{1/2}^{SU(2)}\sim\frac{3}{2\beta},
\qquad
m_1^{U(1)}\sim\frac{1}{2\beta}.
```

That object cannot see the one-loop coefficient. It distinguishes the two
groups only by the geometric Casimir factor `3:1`, and both gaps scale like
`1/beta`.

The decimation diagnostic changes the picture. After blocking, the inferred
`SU(2)` beta begins to decrease by an approximately constant amount per scale,
while the `U(1)` beta stops running. This is precisely the kind of
abelian/non-abelian fork that the elementary plaquette object lacked.

The honest reading is:

```math
\boxed{
\begin{array}{l}
\text{single plaquette: tree stiffness only; no }b_0\text{ signal;}\\
\text{MK block diagnostic: visible }SU(2)\text{ running signal;}\\
\text{true hypercubic proof: still requires uniform control of the}\\
\text{twisted/untwisted block ratio, i.e. the Claim-2.1-type lower bound.}
\end{array}}
```

Thus the diagnostic supports the decision made in §22.6: the right object is not
the elementary transfer operator but the block-renormalized charged-sector
operator. It also explains why the Tomboulis-style decimation program is the
right neighborhood of the problem: the block recursion is the first place where
the non-abelian flow can appear.

### 23.4. What This Does And Does Not Establish

It establishes:

- the numerical setup can be run without broadening the target;
- the elementary single-plaquette obstruction is real but not the end of the
  story;
- the block diagnostic separates `SU(2)` from compact `U(1)`;
- the `SU(2)` block decrement is close to the expected one-loop scale-two
  decrement in this MK scheme.

It does not establish:

- a proof of confinement;
- a proof of center-sector minorization;
- a proof of the Tomboulis/Ito-Seiler per-step inequality;
- a proof that the hypercubic lattice has the same controlled block flow.

The correct next analytic target is therefore sharpened, not solved:

```math
\boxed{
\text{prove a fixed-IR lower bound for the exact hypercubic block ratio,}
\quad
\text{or prove that the MK-visible flow cannot be controlled exactly.}
}
```

This remains Barandes aligned: the decimation is only a proof/diagnostic device
applied to ordinary finite `SU(2)` Wilson measures. It adds no hidden Markov
law, no ontology-level transition rule, and no new probabilistic premise.

## 24. The U(1) Side Of The Diagnostic: Why The Decrement Dies

`V4P41-U1-MK-MARGINALITY-DIAGNOSTIC`.

Section 23 found numerically that the `U(1)` effective-beta decrement dies to
zero under the MK-style coefficient flow. This section records the mathematical
reason. The statement is only about the diagnostic recursion, not about the full
hypercubic proof problem.

### 24.1. The Exact Transform Behind The Coefficients

For `U(1)`, write a normalized even class function as

```math
f(\theta)=1+2\sum_{k\ge1}c_k\cos(k\theta).
```

Let `b=2`, `d=4`, so

```math
\zeta=b^{d-2}=4,
\qquad
r=b^2=4.
```

The unstrengthened part of the MK diagnostic forms

```math
q(\theta)=\frac{f(\theta)^4}{\int f(\phi)^4\,d\phi}.
```

If `\widehat q_k` is the `k`-th Fourier coefficient of `q`, the strengthening
step sets

```math
c_k'=(\widehat q_k)^4.
```

But raising Fourier coefficients to the fourth power is exactly fourfold
convolution on `U(1)`. Thus the diagnostic transform can be read as:

```math
\boxed{
f
\quad\longmapsto\quad
q=\frac{f^4}{\int f^4}
\quad\longmapsto\quad
q*q*q*q.
}
```

This identity is the whole reason the `U(1)` decrement dies.

### 24.2. Heat-Kernel Line Is Marginal

Let the `U(1)` heat-kernel line be represented in Fourier coefficients by

```math
c_k(s)=\exp(-s k^2),
\qquad
s>0.
```

The lightest-channel mass is then

```math
m_1(s)=-\log c_1(s)=s,
\qquad
\beta_{\mathrm{eff}}=\frac{1}{2s}.
```

For small `s`, the heat kernel is locally Gaussian on the principal branch:

```math
H_s(\theta)
=
\sum_{k\in\mathbb Z}e^{-sk^2}e^{ik\theta}
\approx
\left(\frac{\pi}{s}\right)^{1/2}\exp\left(-\frac{\theta^2}{4s}\right),
```

with only exponentially small wrap-around corrections. Therefore:

```math
H_s(\theta)^4
\approx
\text{constant}\cdot
\exp\left(-\frac{\theta^2}{s}\right)
\approx
\text{constant}\cdot H_{s/4}(\theta).
```

After normalization, the first half of the transform sends `s` to `s/4`. The
second half is fourfold convolution, which adds heat-kernel times:

```math
H_{s/4}*H_{s/4}*H_{s/4}*H_{s/4}=H_s.
```

Thus in the weak-coupling heat-kernel regime,

```math
\boxed{
M_{U(1)}(H_s)=H_s+\text{exponentially small periodic corrections}.
}
```

Equivalently,

```math
\boxed{
\beta_{\mathrm{eff}}(n+1)-\beta_{\mathrm{eff}}(n)\longrightarrow0.
}
```

This is the analytic explanation of the numerical observation that the `U(1)`
decrement dies.

### 24.3. Why Wilson Initial Data Falls Onto This Marginal Line

The Wilson one-plaquette `U(1)` coefficients are

```math
c_k(0)=\frac{I_k(\beta)}{I_0(\beta)}.
```

For fixed `k` and large `beta`,

```math
\frac{I_k(\beta)}{I_0(\beta)}
=
\exp\left(-\frac{k^2}{2\beta}+O\left(\frac{k^4}{\beta^3}\right)\right).
```

So the initial Wilson weight is already a heat kernel to leading order, with

```math
s=\frac{1}{2\beta}+O(\beta^{-2}).
```

The first few MK diagnostic steps remove the non-Gaussian Wilson corrections.
Once the flow is close to the heat-kernel line, the power/convolution cancellation
above makes the effective beta stop running. This is what the script sees:

```text
U(1), beta=100
step 2 decrement: 0.023465
step 3 decrement: 0.001466
step 4 decrement: 0.000092
step 5 decrement: 0.000006
step 6 decrement: 0.000000
```

### 24.4. Theorem Inside The Diagnostic

**Proposition 41.35 (U(1) diagnostic marginality).** In the weak-coupling
`U(1)` MK-style coefficient diagnostic with `b=2`, `d=4`, and `r=\zeta=4`, the
heat-kernel line is asymptotically fixed. For Wilson initial data at large
`beta`, the effective-beta decrement tends to zero after the transient projection
onto that line.

**Proof.** The transform is exactly "raise the density to the fourth power,
renormalize, then take fourfold convolution." On the heat-kernel line, raising to
the fourth power divides the local Gaussian heat time by four, while fourfold
convolution multiplies it by four. Hence the heat time, and therefore
`beta_eff`, is unchanged up to exponentially small periodic wrap corrections.
The Bessel asymptotic for `I_k(beta)/I_0(beta)` places the Wilson initial data on
this heat-kernel line to leading order as `beta` tends to infinity. The remaining
non-Gaussian corrections are the transient seen numerically.

### 24.5. Why This Matters For The SU(2) Question

The `U(1)` proof is useful because it says the diagnostic is not automatically
creating fake running. In the abelian weak-coupling case, the Gaussian line is
marginal and the decrement dies. Therefore a persistent decrement in the
`SU(2)` block diagnostic is a genuinely non-abelian signal of the diagnostic
flow, not a universal artifact of the MK recipe.

The contrast is:

```math
\boxed{
\begin{array}{ll}
U(1) & \text{power/convolution cancellation leaves the Gaussian line marginal;}\\
SU(2) & \text{block flow shows a persistent decrement in the diagnostic.}
\end{array}}
```

This still does not prove confinement. It only justifies the next target more
sharply: prove that the exact hypercubic `SU(2)` block operator has a controlled
non-abelian lower-bound analogue of the MK-visible decrement, or prove that this
diagnostic signal cannot be promoted to the exact theory.

## 25. The SU(2) Side Of The Diagnostic: Positivity Of The Decrement

`V4P41-SU2-MK-POSITIVE-DECREMENT-DIAGNOSTIC`.

Section 24 proved that the `U(1)` decrement dies because the Gaussian
heat-kernel line is marginal under the diagnostic. This section proves the
corresponding `SU(2)` statement in the same diagnostic: in weak coupling, the
effective beta decrement is positive and tends to `1/4`.

This is again a theorem about the MK-style character-flow diagnostic, not about
the exact hypercubic block ratio.

### 25.1. Heat-Kernel Coordinates

Let `K_t` be the central `SU(2)` heat kernel with respect to normalized Haar
measure, with character coefficients

```math
c_j(t)=\exp(-\lambda_j t),
\qquad
\lambda_j=4j(j+1)=(2j+1)^2-1.
```

The lightest center-charged channel is `j=1/2`, so

```math
\lambda_{1/2}=3.
```

The effective beta used in the diagnostic is

```math
\beta_{\mathrm{eff}}=\frac{3}{2m_{1/2}},
\qquad
m_{1/2}=-\log c_{1/2}.
```

On the heat-kernel line this is simply

```math
\beta_{\mathrm{eff}}=\frac{1}{2t}.
```

### 25.2. The Curvature Factor That U(1) Does Not Have

For small `t` and small class angle `alpha`, the `SU(2)` heat kernel has the
local form

```math
K_t(\alpha)
=
C_t\,\frac{\alpha}{\sin\alpha}
\exp\left(-\frac{\alpha^2}{4t}\right)
+\text{image terms},
```

where the image terms are exponentially small as `t` tends to zero. The factor

```math
\frac{\alpha}{\sin\alpha}
=
1+\frac{\alpha^2}{6}+O(\alpha^4)
```

is the local curvature/Jacobian correction absent from the flat `U(1)` Gaussian
calculation.

The first half of the diagnostic sends

```math
K_t
\quad\longmapsto\quad
q_t=\frac{K_t^4}{\int K_t^4\,dU}.
```

With the `SU(2)` class-angle Haar density

```math
dU=\frac{2}{\pi}\sin^2\alpha\,d\alpha,
```

the measure `q_t dU` has local density proportional to

```math
\sin^2\alpha
\left(\frac{\alpha}{\sin\alpha}\right)^4
\exp\left(-\frac{\alpha^2}{t}\right)d\alpha
=
\alpha^2
\left(1+\frac{\alpha^2}{3}+O(\alpha^4)\right)
\exp\left(-\frac{\alpha^2}{t}\right)d\alpha.
```

For comparison, a heat kernel at time `t/4` would have density

```math
\alpha^2
\left(1-\frac{\alpha^2}{6}+O(\alpha^4)\right)
\exp\left(-\frac{\alpha^2}{t}\right)d\alpha.
```

Thus `q_t` is not exactly `K_{t/4}`. Relative to `K_{t/4}`, it carries the extra
factor

```math
\left(\frac{\alpha}{\sin\alpha}\right)^3
=
1+\frac{\alpha^2}{2}+O(\alpha^4).
```

This is the source of the positive decrement.

### 25.3. Character-Coefficient Expansion

Let

```math
\varphi_j(\alpha)=\frac{\chi_j(\alpha)}{2j+1}.
```

Its small-angle expansion is

```math
\varphi_j(\alpha)
=
1-\frac{\lambda_j}{6}\alpha^2
+\frac{\lambda_j(3\lambda_j-4)}{360}\alpha^4
+O(\alpha^6).
```

Under the normalized `q_t` measure above, the Gaussian radial moments are

```math
\mathbb E_{q_t}[\alpha^2]
=
\frac{3t}{2}+\frac{t^2}{2}+O(t^3),
```

and

```math
\mathbb E_{q_t}[\alpha^4]
=
\frac{15t^2}{4}+O(t^3).
```

Therefore the normalized `j`-channel coefficient after the first half-step is

```math
a_j(t)
=
\mathbb E_{q_t}[\varphi_j]
=
1-\frac{\lambda_j t}{4}
+\frac{\lambda_j(\lambda_j-4)t^2}{32}
+O_j(t^3).
```

Equivalently,

```math
\log a_j(t)
=
-\lambda_j\left(\frac{t}{4}+\frac{t^2}{8}\right)
+O_j(t^3).
```

### 25.4. Strengthening And The Positive Decrement

The second half of the diagnostic raises each coefficient to the fourth power:

```math
c_j'(t)=a_j(t)^4.
```

Hence

```math
-\log c_j'(t)
=
\lambda_j\left(t+\frac{t^2}{2}\right)+O_j(t^3).
```

For the `j=1/2` channel, the new effective heat time is therefore

```math
t'=t+\frac{t^2}{2}+O(t^3).
```

Since `beta_eff=1/(2t)`, the transformed effective beta is

```math
\beta_{\mathrm{eff}}'
=
\frac{1}{2t'}
=
\frac{1}{2t}-\frac{1}{4}+O(t).
```

Thus

```math
\boxed{
\beta_{\mathrm{eff}}-\beta_{\mathrm{eff}}'
=
\frac{1}{4}+O(\beta_{\mathrm{eff}}^{-1}).
}
```

In particular, the decrement is strictly positive for sufficiently weak coupling.

### 25.5. Proposition

**Proposition 41.36 (SU(2) diagnostic positive decrement).** In the weak-coupling
`SU(2)` MK-style coefficient diagnostic with `b=2`, `d=4`, and `r=\zeta=4`,
the heat-kernel line satisfies

```math
\beta_{\mathrm{eff}}(n)-\beta_{\mathrm{eff}}(n+1)
\longrightarrow
\frac{1}{4}
```

as `\beta_{\mathrm{eff}}(n)` tends to infinity. For Wilson initial data at large
`beta`, the same asymptotic holds after the initial projection onto the
heat-kernel regime.

**Proof.** The local heat-kernel expansion gives the first-half coefficient
asymptotic of §25.3. The coefficient-strengthening step raises this coefficient
to the fourth power, giving the new lightest-channel mass in §25.4. Converting
that mass back to `beta_eff` yields the displayed decrement. Wilson initial data
has the same heat-kernel asymptotic at large `beta`, so the same conclusion
holds after the transient non-Gaussian correction is removed.

### 25.6. What Was Actually Proved

The `U(1)` and `SU(2)` diagnostic sides are now both understood:

```math
\boxed{
\begin{array}{ll}
U(1) &
\text{flat Gaussian power/convolution cancellation, decrement }\to0,\\[1mm]
SU(2) &
\text{curvature/Jacobian correction, decrement }\to1/4.
\end{array}}
```

This is the clean mathematical version of the numerical fork. It is still not
the exact hypercubic proof: the MK diagnostic sees a non-abelian block-flow
signal, but the open theorem remains the fixed-IR lower bound for the exact
twisted/untwisted hypercubic block ratio.

## 26. Attempted Transfer To The Exact Hypercubic Twisted Ratio

`V4P41-ATTEMPTED-TRANSFER-TO-EXACT-HYPERCUBIC-RATIO`.

We now try to transfer the `SU(2)` decrement proved in §25 from the MK diagnostic
to the exact hypercubic twisted/untwisted block ratio. This section is the
honest endpoint of that attempt. It gives a precise conditional transfer lemma,
then identifies the unconditional missing input.

### 26.1. The Exact Object To Transfer To

Let `B` be a scale-two hypercubic block. Let `Z_B^+` be the exact fine-lattice
block partition function with fixed coarse boundary data and no center twist,
and let `Z_B^-` be the same block partition function with a `Z_2` center twist
through the corresponding coclosed plaquette stack. The exact block ratio is

```math
R_B^{\mathrm{ex}}=\frac{Z_B^-}{Z_B^+}.
```

Equivalently, after exact blocking, one may write the coarse block weight as an
effective action containing a plaquette character part plus all generated
extended-loop and multi-plaquette terms:

```math
S_{\mathrm{eff}}
=
S_{\mathrm{plaq}}
+
S_{\mathrm{ext}}.
```

The MK diagnostic keeps only a special positive central plaquette recursion. The
exact hypercubic block does not: `S_ext` is generated immediately.

The desired transfer is therefore not merely

```math
\beta_{\mathrm{eff}}^{MK}(n)-\beta_{\mathrm{eff}}^{MK}(n+1)>0.
```

It is the stronger statement that the exact ratio obeys a corresponding
lower-bound flow:

```math
\boxed{
R_B^{\mathrm{ex}}
\text{ is bounded below by the MK-predicted charged/twisted block weight,}
\text{ up to a summable fixed-IR error.}
}
```

This is the local form of the Tomboulis/Ito-Seiler lower-bound problem.

### 26.2. Why The Signal Is Delicate

The MK theorem of §25 says, in effective-beta variables,

```math
\beta_{\mathrm{eff}}(n)-\beta_{\mathrm{eff}}(n+1)
=
\frac14+O(\beta_{\mathrm{eff}}^{-1}).
```

But the lightest-channel mass is

```math
m_{1/2}=\frac{3}{2\beta_{\mathrm{eff}}}+O(\beta_{\mathrm{eff}}^{-2}).
```

Thus a decrement of `1/4` in `beta_eff` corresponds to only

```math
m_{1/2}(n+1)-m_{1/2}(n)
=
\frac{3}{8\beta_{\mathrm{eff}}(n)^2}
+O(\beta_{\mathrm{eff}}^{-3}).
```

This is the key scale. Any exact hypercubic comparison must control the
difference between the exact block and the MK block at `O(beta^{-2})` in the
lightest charged channel, with the correct sign. An `O(beta^{-1})` or merely
bounded error is far too large.

### 26.3. Conditional Transfer Lemma

Let

```math
m_n^{MK}=-\log c_{1/2}^{MK}(n),
\qquad
m_n^{ex}=-\log c_{1/2}^{ex}(n),
```

where `c_{1/2}^{ex}` denotes the exact blocked lightest charged coefficient
extracted from the hypercubic block weight after the same normalization. Suppose
that, for all sufficiently weak-coupling steps in the fixed-IR blocking range,

```math
\left|
\big(m_{n+1}^{ex}-m_n^{ex}\big)
-
\big(m_{n+1}^{MK}-m_n^{MK}\big)
\right|
\le
\frac{\varepsilon}{\beta_n^2},
```

with some `\varepsilon<3/8`. Then the exact charged channel has positive
effective-beta decrement for all sufficiently large `beta_n`.

**Proof.** By §25,

```math
m_{n+1}^{MK}-m_n^{MK}
=
\frac{3}{8\beta_n^2}+O(\beta_n^{-3}).
```

The assumed comparison leaves a positive mass increment

```math
m_{n+1}^{ex}-m_n^{ex}
\ge
\frac{3/8-\varepsilon+o(1)}{\beta_n^2}>0.
```

Since `beta_eff=3/(2m)` in the weak-coupling normalization, a positive mass
increment is a positive effective-beta decrement.

This proves the transfer only under the displayed comparison estimate.

### 26.4. What The Lemma Does Not Give

The lemma does not prove the comparison estimate. Proving it is the hard part.
There are three natural attempts.

**Attempt A: reflection positivity.** RP controls chessboard repetitions and
upper bounds. It does not supply the needed lower comparison

```math
R_B^{\mathrm{ex}}\ge e^{-E_B}R_B^{MK}
```

with `E_B=O(beta^{-2})` or summable over the fixed-IR blocking range. This is the
same ceiling-versus-floor obstruction already isolated in §22.5.

**Attempt B: small-field stationary phase.** On a fixed weak-coupling block,
one can formally expand the exact hypercubic block action around the trivial
connection. This is where the usual one-loop non-abelian running appears. In
principle it gives a formal decrement close to

```math
8b_0\log2,
\qquad
b_0=\frac{11}{24\pi^2}.
```

But this is a small-field statement. The twisted/untwisted ratio is a sector
comparison, and the lower bound must control the complement of the small-field
region without assuming vortex disorder. The formal perturbative decrement does
not by itself give the required charged-sector lower tail.

This is the neighborhood of Balaban-style rigorous lattice RG: small-field
effective actions and coupling renormalization can be controlled with great
precision. The present target asks for the additional lower control of the
twisted sector and its generated extended interactions. That extra lower bound
is not supplied merely by the small-field coupling flow.

**Attempt C: large-field suppression.** One might hope to show that all
large-field corrections to the MK block are exponentially small in `beta`, hence
smaller than `beta^{-2}`. This is plausible for one isolated perturbative block,
but not enough for the fixed-IR theorem. Along the continuum trajectory a fixed
physical block contains a growing sequence of RG steps, and the exact effective
action generates extended interactions at every step. The needed estimate is a
uniform product lower bound on the twisted ratio, not just a one-block
large-deviation estimate.

### 26.5. The Exact Missing Statement

The attempted transfer reduces the problem to the following statement.

**Target 41.37 (O(beta^-2) exact twisted-ratio block lower comparison).** Prove
or falsify the following exact hypercubic block comparison.

```math
\boxed{
\begin{array}{l}
\textbf{Exact hypercubic block comparison.}\\
\text{For each weak-coupling block step in the fixed-IR range,}\\
\text{the exact twisted/untwisted hypercubic block ratio is bounded}\\
\text{below by the MK/heat-kernel charged block prediction with an}\\
\text{error smaller than the }O(\beta^{-2})\text{ decrement signal,}\\
\text{and the accumulated error remains summable up to the fixed}\\
\text{physical scale }R.
\end{array}}
```

This is a precise Claim-2.1-type lower-bound statement. It is not a formal
consequence of the MK decrement. It is exactly the bridge from diagnostic flow
to the true hypercubic theory.

**Equivalence note (no reduction is achieved here).** Target 41.37 must not be
mistaken for a sub-lemma that is *easier* than the open problem of §19. It is
not. Controlling the exact twisted/untwisted hypercubic block ratio below the
`O(\beta^{-2})` decrement signal, with the correct sign, *uniformly across the*
`O(1/a)` *blocking steps up to a fixed physical scale*, is precisely the
weak-coupling continuum confinement statement of §19.6 restated at maximal
resolution:

```math
\boxed{
\text{Target 41.37}
\;\Longleftrightarrow\;
\text{the §19.6 open problem (weak-coupling center area law), sharpest form.}
}
```

The arrow "⟸" is the content of the conditional transfer lemma §26.3 plus the
fixed-IR accumulation of §22.1; the arrow "⟹" holds because a proof of §19.6 at
weak coupling would in particular supply a uniform charged-sector floor for the
blocked transfer operator, hence the block comparison. Thus 41.37 is a *faithful
restatement*, not a weakening: any honest attempt on 41.37 is an attempt on the
Clay-level problem itself, and no amount of diagnostic flow (MK or otherwise)
discharges it.

### 26.6. Verdict Of The Transfer Attempt

The attempted transfer partially succeeds:

```math
\boxed{
\text{MK decrement}
+
\text{exact }O(\beta^{-2})\text{ lower comparison}
\quad\Longrightarrow\quad
\text{positive exact block decrement.}
}
```

But the unconditional transfer fails at the lower comparison:

```math
\boxed{
\text{the exact hypercubic twisted-ratio floor is still open.}
}
```

This is not a failure of fixed-IR alignment. It is the fixed-IR target in its
sharpest form. To continue, one must either prove the exact hypercubic block
comparison above, or show by counterexample/estimate that the MK-visible
`SU(2)` decrement is destroyed by the generated extended interactions in the
true hypercubic block action.

## 27. Leading-Order Test: Does The Generated `S_ext` Preserve Or Destroy The Decrement?

`V4P41-LEADING-ORDER-SEXT-SIGN-AND-ORDER-TEST`.

Section 26.6 named the cheap, decisive branch: *show by estimate whether the
MK-visible decrement is preserved or destroyed by the generated extended
interactions*. This section executes that branch at leading weak-coupling order.
It is **not** a proof of Target 41.37 (which §26.5 shows is the open problem
itself). It is the bounded, falsifiable test of whether the transfer route is
even alive: it measures the **sign** and the **order in `\beta^{-1}`** of the
first generated correction in the lightest charged channel, and asks whether
either kills the route.

Rigor level of this section: the **order count** and the **sign** are robust
(they rest on the proven MK result of §25, the verified `O(\beta^{-2})` scaling
below, and the established one-loop lattice coefficient `b_0=11/24\pi^2>0`). The
identification of the *precise magnitude* of the generated term with the
one-loop/MK scheme difference is flagged as heuristic.

### 27.1. The Order At Which The Signal Lives (Verified)

By Proposition 41.36 the MK block decrement is `\tfrac14` in `\beta_{\rm eff}`.
In the physical observable — the lightest charged-channel mass — this is

```math
m_{1/2}=\frac{3}{2\beta_{\mathrm{eff}}}
\;\Longrightarrow\;
m_{1/2}(n{+}1)-m_{1/2}(n)
=\frac{3}{8\beta_{\mathrm{eff}}(n)^2}+O(\beta^{-3}).
```

This `\tfrac{3}{8}\beta^{-2}` law is confirmed by direct run of
`mk_decimation_diagnostic.py` on the late, heat-kernel-line steps:

```text
beta   measured Delta m_{1/2} (step 2->3)   predicted 3/(8 beta^2)
100         3.751e-5                            3.750e-5
200         9.330e-6                            9.375e-6
400         2.350e-6                            2.344e-6
```

Consequence: the charged-channel signal is an `O(\beta^{-2})` mass increment.
This fixes the measuring stick for any generated term:

```math
\boxed{
\begin{array}{ll}
\text{a generated mass shift of order }\beta^{-1} & \text{would swamp the signal (route falsified);}\\
\text{a generated mass shift of order }o(\beta^{-2}) & \text{would be invisible (no effect);}\\
\text{a generated mass shift of order }\beta^{-2} & \text{is the only order that can matter.}
\end{array}}
```

### 27.2. What MK Keeps, What The Exact Block Generates

MK retains only the single central-plaquette character recursion (the bond-move
power `\zeta` and the decimation power `r`). The exact hypercubic block, formed
by integrating the interior fine links at fixed coarse boundary data, does not
factorize this way. An interior link `\ell` is shared by `2(d-1)=6` plaquettes
(at `d=4`) lying in different planes; integrating it out couples those
plaquettes. The leading **genuinely non-abelian** generated interaction is the
transverse-vertex contribution — the `[A,A]` part of the lattice field strength
`F=dA+[A,A]` connecting the fluctuation of `\ell` across the planes that share
it. These transverse `[A,A]` couplings are exactly what bond-moving discards;
they are the seed of `S_{\mathrm{ext}}`.

### 27.3. Order Of The Leading Generated Term

Write `U_\ell=\exp(i\,g\,a\,A_\ell)`, `g^2=4/\beta`. The tree plaquette stiffness
sets `m_{1/2}^{\rm tree}=3/(2\beta)=O(g^2)`. Splitting the interior-link integral
into Gaussian fluctuation plus interaction:

- the **quadratic** (Gaussian) part reproduces the abelian-like heat-kernel flow
  — this is precisely the MK-captured `\tfrac14` decrement of §25;
- the leading **non-abelian** generated term is one insertion of the cubic/quartic
  `[A,A]` vertex, i.e. relative order `g^2=4/\beta` to the Gaussian result.

Hence its contribution to the charged-channel mass is

```math
\delta m_{1/2}^{\,S_{\rm ext}}
\;\sim\;
m_{1/2}^{\rm tree}\times O(g^2)
\;=\;
O(\beta^{-1})\times O(\beta^{-1})
\;=\;
O(\beta^{-2}).
```

This is the *same order* as the MK signal of §27.1 — not larger, not smaller.

```math
\boxed{\textbf{Order test: PASSED.}\quad
\delta m_{1/2}^{\,S_{\rm ext}}=O(\beta^{-2})
\text{ — same order as the decrement, neither swamping nor invisible.}}
```

This also explains, retroactively, *why* Target 41.37 demands `O(\beta^{-2})`
control: the entire physical effect sits at that order, so any coarser estimate
literally cannot see the route, favorable or not.

### 27.4. Sign Of The Leading Generated Term

The leading transverse `[A,A]` vertex is the one-loop self-interaction that
renders the coupling running. For `SU(2)` (and every asymptotically free
Yang-Mills theory) it carries the asymptotic-freedom sign: integrating out the
short-distance fluctuations *decreases* the effective coupling, equivalently
*increases* the confining-direction block decrement, by the one-loop amount

```math
\Delta\beta_{\rm 1loop}=8b_0\log 2=0.257511\ldots,
\qquad
b_0=\frac{11}{24\pi^2}>0.
```

The decisive comparison is that this **exceeds** the MK decrement:

```math
\underbrace{0.257511}_{\text{exact one-loop}}
\;>\;
\underbrace{0.250000}_{\text{MK (Prop. 41.36)}},
\qquad
\text{difference}=+0.007512>0.
```

In mass variables the net leading contribution of the generated tower is

```math
\delta m_{1/2}^{\,S_{\rm ext}}
\;\approx\;
\frac{3}{2}\,\frac{(0.257511-0.250000)}{\beta^2}
\;\approx\;
\frac{+0.0113}{\beta^2}
\;>\;0,
```

i.e. it **reinforces** the MK decrement rather than cancelling it.

```math
\boxed{\textbf{Sign test: PASSED.}\quad
\text{the leading generated }S_{\rm ext}\text{ adds confining-direction decrement.}}
```

*Heuristic flag.* The identification "discarded `S_{\rm ext}` supplies exactly the
`+0.0075` one-loop/MK difference" is scheme-dependent and is not claimed as a
theorem; MK and the exact block are different coarse-grainings. What is robust,
and all that the test needs, is (i) `b_0>0`, an established lattice one-loop
fact, and (ii) the exact one-loop decrement exceeds the MK decrement — so the
leading generated correction has the *same sign* as the signal, not the opposite.

### 27.5. Verdict Of The Leading-Order Test

```math
\boxed{
\begin{array}{l}
\textbf{Leading-order falsification test: PASSED (route not dead).}\\[1mm]
\text{To leading weak-coupling order the generated extended interactions enter}\\
\text{the charged-channel mass increment at the same }O(\beta^{-2})\text{ order as the}\\
\text{MK decrement, and with the same (asymptotic-freedom) sign. The MK-visible}\\
\text{}SU(2)\text{ decrement is therefore not destroyed by the first generated term —}\\
\text{it is reinforced.}
\end{array}}
```

But "passed at leading order" is emphatically **not** a proof, and seeing the gap
precisely is the point of the test:

```math
\boxed{
\begin{array}{l}
\text{What remains open is neither the sign nor the order (both favorable). It is}\\
\text{the }\textit{uniform, all-orders, summable lower bound}\text{ on the }\textit{full}\text{ generated}\\
\text{tower across all }O(1/a)\text{ steps — controlling the large-field/twisted}\\
\text{complement, not merely the leading vertex. That is Target 41.37, i.e. by}\\
\text{§26.5 the §19.6 open problem itself (Balaban-type constructive RG).}
\end{array}}
```

So the test does exactly what a good diagnostic should: it **rules out the cheap
death of the route** (a wrong-sign or `O(\beta^{-1})` first correction would have
killed it, and neither occurs), and it **relocates the open content with maximal
precision** onto the one estimate — uniform all-orders summable control — that
§§19, 22, 26 already identified as the irreducible kernel. It manufactures no
progress on the kernel; it certifies only that the leading obstruction one might
have feared is absent.

## 28. Marrying The §27 Signal To Balaban's Small-Field RG: A Located Terminus

`V4P41-BALABAN-SMALLFIELD-MARRIAGE-LOCATED-TERMINUS`.

This section attempts the one join that could in principle turn §27's per-step
signal into a rigorous statement: combine it with the only rigorous weak-coupling
4D non-abelian RG control that exists, Balaban's small-field renormalization
group. It is **not** a proof. The attempt terminates, and the entire value of the
section is that the terminus is *located precisely* and is *sharper* than "this is
the open problem": it shows the obstruction is not a missing bound but a
**domain complementarity** — §27 and Balaban both live in the regime where the
theory is *ordered*, and confinement lives in the complementary regime neither
tool reaches.

### 28.1. What Balaban Rigorously Provides (And What It Does Not)

Balaban's lattice gauge RG (Balaban, Commun. Math. Phys. **102** (1985), **109**
(1987), **116** (1988); and the SU(2) construction with an infrared cutoff of
Magnen–Rivasseau–Séneor, Commun. Math. Phys. **155** (1993)) establishes, for
`SU(2)`/`SU(3)` in `d=4` at weak bare coupling:

- a gauge-covariant block-spin transformation and a **small-field / large-field
  decomposition** of configurations;
- **exponential suppression of large-field regions** (the action cost of a
  large-field block is `\gtrsim 1/g^2` per unit volume);
- in the small-field region, the one-step effective action equals the classical
  (background-field) action plus **controlled** quantum corrections, with the
  coupling renormalizing by the rigorous **one-loop** law;
- **UV stability**: partition functions and effective actions stay bounded
  uniformly as `a\to0`, over the range of scales for which the running coupling
  remains small.

What Balaban's small-field program does **not** provide, and does not claim:

- the **deep infrared**, where the running coupling `g_k` reaches `O(1)`;
- any **area law / string tension / vortex free-energy lower bound**;
- the **mass gap** or full Osterwalder–Schrader reconstruction.

The IR cutoff in Magnen–Rivasseau–Séneor is exactly the boundary that is *not*
removed; removing it is the open problem.

### 28.2. Where The §27 Signal Sits In Balaban's Flow

The per-block decrement of §§25, 27,

```math
\Delta\beta=8b_0\log 2=0.2575\ldots,
\qquad
b_0=\frac{11}{24\pi^2},
```

**is** the one-loop running. (The MK value `\tfrac14` of Prop. 41.36 is its
uncontrolled-scheme approximation.) Its reinforcing sign is asymptotic freedom:
`\beta` decreases — equivalently `g_k` grows — toward the IR. This is *precisely*
the quantity Balaban controls rigorously in the small-field window. So in that
window the join is almost tautological:

```math
\boxed{
\text{§27's charged-sector decrement }=\text{ the one-loop running, which Balaban}
\text{ makes rigorous wherever }g_k\text{ is small.}
}
```

The charged-channel mass there is `m_{1/2}=3/(2\beta_k)=3g_k^2/8`, which is *small*
in the window — a light perturbative stiffness, not a string tension.

### 28.3. The Accumulation, And What It Actually Builds

Summing the rigorous decrement over the window, `\beta` runs from `\beta_0` down
across

```math
K_{\max}\;\sim\;\frac{\beta_0}{\Delta\beta}\;\sim\;3.9\,\beta_0
```

scale-two steps before `g_k` leaves the small-field regime. By dimensional
transmutation the physical scale at the window's end,
`a\,2^{K_{\max}}\sim\Lambda^{-1}`, is the confinement scale itself. So the
marriage rigorously carries the flow *down to the neighborhood of the confinement
scale*. But the object it accumulates is the **running coupling**, not a string
tension:

```math
\boxed{
\sum_{k<K_{\max}}\Delta\beta
\;=\;\beta_0-\beta_{K_{\max}}
\;=\;\text{the asymptotic-freedom flow, not }\sigma.
}
```

Reaching `g_k\sim O(1)` is **not** confinement. A flow that reaches strong
coupling may confine *or* may reach a conformal IR fixed point with no area law
(this is exactly what happens inside the conformal window for gauge theories with
enough matter). Pure `SU(2)` is believed to confine, but the perturbative flow to
`g\sim O(1)` does not by itself distinguish a confining IR from a conformal one.
That distinction is the nonperturbative disorder content — and it is invisible to
both §27 (leading order) and Balaban (small field).

### 28.4. Two-Sided Check: The Window Is The Ordered Regime

The decisive observation is that confinement is not merely *unproven* in the
small-field window — it is *absent* there, and two independent computations agree:

- **Charged-channel side.** With `g_k` small the Wilson loop is governed by the
  Gaussian/Coulomb behavior of the small-field effective action: perimeter law and
  a Coulomb potential, **no area term**. The light mass `3g_k^2/8` is a stiffness,
  not a tension.
- **Vortex side.** A thin center vortex on a coclosed sheet costs free energy
  `\sim\beta_k` per sheet plaquette in the small-field regime, so vortices are
  **suppressed**; the center symmetry is **ordered**, `\langle\Xi_S\rangle\approx1`,
  and `m(\eta)\to1`, `r_a\to0` — the *opposite* of the §19.6 disorder one needs.

```math
\boxed{
\text{In the Balaban window the center sector is ORDERED}
\text{ (vortices heavy, no area law). Confinement = vortex condensation =}
\text{ center disorder occurs only as }g_k\to O(1),\text{ at the window's IR edge.}
}
```

The two sides are the 't Hooft order/disorder pair, and they place the area law
unambiguously *outside* the small-field window.

### 28.5. The Located Terminus

The marriage does not fail for lack of a clever inequality. It terminates because
of where its two ingredients live:

```math
\boxed{
\begin{array}{l}
\textbf{Domain complementarity.}\\[1mm]
\text{§27's leading-order signal and Balaban's small-field control both hold in}\\
\text{the weak-effective-coupling (}g_k\text{ small) window, where the center is}\\
\text{ordered and there is no area law. The string tension is generated entirely}\\
\text{in the complementary regime }g_k\sim O(1)\text{ — the }\textit{end of the small-field}\\
\textit{window}\text{, where large-field/vortex configurations begin to dominate —}\\
\text{which neither tool reaches.}
\end{array}}
```

Honest ledger of the attempt:

- **Established (modulo citation of Balaban):** §27's per-step charged-sector
  decrement is the rigorous one-loop running throughout the small-field window;
  the accumulated flow rigorously reaches the neighborhood of the confinement
  scale.
- **Newly sharpened (the genuine output):** the open content is not "a lower bound
  on the twisted ratio at weak coupling" in the naive sense — at small `g_k` that
  ratio is *favorable but ordered* (no confinement to find there). The open object
  is the **rigorous continuation of the controlled flow through the onset of
  large-field/vortex dominance**, `g_k:\text{small}\to O(1)`, and the proof that
  the center sector *disorders* there.
- **Unchanged:** that continuation — the **intermediate-field problem** — is the
  open problem. It is a *third* object, distinct from both asymptotic freedom
  (Balaban, controlled) and the strong-coupling expansion (Osterwalder–Seiler,
  controlled): it is the bridge between them, and it is empty of rigorous results
  in `d=4`.

### 28.6. What This Reframes The Target To

The cleanest restatement the marriage produces:

```math
\boxed{
\begin{array}{l}
\text{Continue Balaban's small-field RG past the window: control the regime}\\
\text{where }g_k\text{ grows from small to }O(1)\text{ and large-field (vortex) sectors}\\
\text{turn on, and show the center flux }\Xi_S\text{ decorrelates (condenses) there.}
\end{array}}
```

This is strictly more informative than Target 41.37 as previously phrased,
because it says *where* the estimate must be proved (the intermediate-field
bridge), *why* the weak-coupling-favorable §27 signal does not already give it
(that signal is in the ordered window), and *what new control is required*
(matching the small-field flow to the onset of large-field dominance — neither an
asymptotic-freedom nor a strong-coupling statement). Naming this object precisely
is the section's output; constructing it is the open problem, and nothing here
constructs it.

### 28.7. Status Of The Marriage

```math
\boxed{
\begin{array}{l}
\text{Marriage attempt: TERMINATES at a located boundary, not a proof.}\\[1mm]
\text{Output: confinement is structurally localized to the intermediate-field}\\
\text{bridge }(g_k:\text{small}\to O(1))\text{, outside the domain of both §27 and}\\
\text{Balaban's small-field control. The §27 signal is the (ordered-regime) running,}\\
\text{not the (disordered-regime) tension. No breach of the wall; a sharper map of it.}
\end{array}}
```

## 29. Frontier Exploration: Confinement As An Induced-`Z_2` Threshold Crossing

`V4P41-FRONTIER-INDUCED-Z2-THRESHOLD-CROSSING`.

**This section is explicitly frontier exploration, not a reduction and not a
proof.** It develops an original angle on the intermediate-field regime that §28
located as the home of confinement, carries it to a concrete leading-order
computation, and stops at a precisely-identified boundary. The deliverable is a
*new, rigorously-anchored coordinate system* for the crossing, plus one honest
quantitative finding about where the nonperturbative content must sit. It closes
nothing.

### 29.1. The Idea

Every previous route tracks the `SU(2)` vortex free energy (equivalently the
twisted/untwisted ratio of §26, equivalently `1-m(\eta)`) directly, and bottoms
out because that object is uncontrolled at `g_k\sim O(1)`. The new angle:

```math
\boxed{
\begin{array}{l}
\text{Integrate out the }SO(3)\text{ coset to induce an effective }Z_2\text{ \emph{gauge} coupling}\\
\beta_{Z_2}^{\rm eff}\text{ for the center-flux variables, and compare it to the}\\
\textbf{exactly known}\text{ 4D }Z_2\text{ gauge transition. The center disorders}\\
\text{(}SU(2)\text{ confines) iff }\beta_{Z_2}^{\rm eff}\text{ flows below that threshold.}
\end{array}}
```

This trades the *unknown* `SU(2)` disorder threshold for a *known* `Z_2` one. Two
features make it more than a relabeling, and they are the section's point:

1. the `Z_2` target threshold is **exact** and both `Z_2` phases are
   **rigorously controlled** (convergent expansions away from criticality);
2. it exposes **two** drivers pushing `\beta_{Z_2}^{\rm eff}` down toward the
   threshold — the asymptotic-freedom running of `\beta_k` (the §27 signal) *and*
   an `SO(3)`-coset **screening factor** — whereas the standard confinement
   narrative emphasizes only the running.

### 29.2. The Exact Decomposition

`SU(2)` bundles split as an `SO(3)=SU(2)/Z_2` bundle carrying a `Z_2` obstruction
`w_2` (the second Stiefel–Whitney class). The center vortices are exactly the
`w_2` flux, and `\Xi_S` is the `w_2` flux through `S`:

```math
Z_{SU(2)}=\sum_{\text{center sectors}}Z_{SO(3)}[w_2],
\qquad
m(\eta)=\langle\Xi_S\rangle_\eta=\text{response to flipping }w_2\text{ through }S.
```

At the level of the single-plaquette weight, this is the center even/odd split
already used in §24–25: writing `w(U_p)=e^{\beta(\frac12\operatorname{tr}U_p-1)}`,

```math
w(U)=w_+(U)+w_-(U),
\qquad
w_\pm(U)=e^{-\beta}\big[\tfrac12 e^{\beta\frac12\operatorname{tr}U}\pm\tfrac12 e^{-\beta\frac12\operatorname{tr}U}\big],
```

with `w_+` center-even (integer spins, the `SO(3)` content) and `w_-` center-odd
(half-integer spins, the `Z_2` content). Integrating the `SO(3)` coset fluctuations
at fixed center flux produces an effective action `S_{Z_2}^{\rm eff}[z]` for the
plaquette center variables `z_p=\pm1`, whose leading term is a `Z_2` gauge action
with coupling `\beta_{Z_2}^{\rm eff}`.

### 29.3. The Rigorously Known Target Threshold

4D `Z_2` gauge theory is Wegner-self-dual, with self-dual point fixed by
`\tanh\beta^\ast=e^{-2\beta^\ast}`, i.e.

```math
\boxed{
\beta^\ast=\tfrac12\log(1+\sqrt2)=0.440687\ldots
}
```

Away from it both phases are controlled: a convergent strong-coupling (high-`T`)
expansion gives the **disordered/confining** phase (`Z_2` vortices condensed,
center-flux area law) for `\beta_{Z_2}<\beta^\ast`, and self-duality maps it to
the ordered phase for `\beta_{Z_2}>\beta^\ast`. (The true transition is weakly
first order near `\beta_c\approx0.443`; `\beta^\ast` is the exact anchor.) This is
the leverage the `SU(2)` problem lacks and the `Z_2` reformulation borrows:

```math
\boxed{
\beta_{Z_2}^{\rm eff}<\beta^\ast
\quad\Longrightarrow\quad
\text{center flux obeys an area law}
\quad\Longrightarrow\quad
SU(2)\text{ center confinement.}
}
```

### 29.4. Leading Induced Coupling, And A Quantitative Finding

At tree level the cost of forcing one plaquette into the center-flipped sector
(`\tfrac12\operatorname{tr}U_p:+1\to-1`) is `2\beta`, matching a `Z_2` gauge cost
`2\beta_{Z_2}`, so the **tree** induced coupling is `\beta_{Z_2}^{\rm eff}=\beta`.
The `SO(3)` fluctuations renormalize this by a **screening factor**
`Z_{\rm scr}(g_k)\le1` — the coset can spread the center flux (thicken the
vortex), lowering its cost:

```math
\beta_{Z_2}^{\rm eff}(k)=\beta_k\,Z_{\rm scr}(g_k),
\qquad
Z_{\rm scr}=1-O(g_k^2)\ \text{(leading)},\ \ \text{decreasing as }g_k\uparrow.
```

Both factors push downward: `\beta_k` falls by the §27 running, `Z_{\rm scr}`
falls by `SO(3)` decorrelation. The crossing condition is
`\beta_K\,Z_{\rm scr}(g_K)<\beta^\ast=0.4407`.

Now the honest quantitative finding. The `SU(2)` bulk crossover sits near
`\beta\approx2.2`. To cross `\beta^\ast` there one needs

```math
Z_{\rm scr}(g)<\frac{\beta^\ast}{\beta}\approx\frac{0.441}{2.2}\approx0.20.
```

But the **leading** (single-plaquette) screening proxy
`Z_{\rm scr}\approx\langle\tfrac12\operatorname{tr}U_p\rangle\approx0.66` at
`\beta=2.2` gives only

```math
\beta_{Z_2}^{\rm eff}\approx2.2\times0.66\approx1.45\ \gg\ \beta^\ast .
```

```math
\boxed{
\begin{array}{l}
\textbf{Finding.}\ \text{The running plus \emph{leading} (single-plaquette) screening does}\\
\text{NOT cross the }Z_2\text{ threshold at the crossover: it overshoots by a factor }\sim3\text{--}5.\\[1mm]
\text{Crossing requires }Z_{\rm scr}\lesssim0.2\text{, i.e. a genuinely nonperturbative}\\
\text{(thick-vortex / multi-plaquette) screening enhancement, not the leading flow.}
\end{array}}
```

This is informative precisely because it is negative in a sharp way: it certifies
that the center disorder is **not** an artifact one could reach by combining the
rigorous §27 running with leading screening — the missing factor of `\sim5` is
exactly the nonperturbative thick-vortex content, now pinned to a number rather
than left qualitative.

### 29.5. The Located Stop

What the angle establishes (modulo standard inputs):

- the `Z_2` side is rigorous — exact threshold `\beta^\ast`, both phases
  controlled — so "center disorders iff `\beta_{Z_2}^{\rm eff}<\beta^\ast`" is a
  clean, rigorously-anchored *criterion*;
- two independent downward drivers are identified and the running one is the
  rigorous §27 signal;
- a concrete numerical gap (the factor `\sim5` of §29.4) localizes the
  nonperturbative content.

Where it stops, honestly:

- `Z_{\rm scr}` at `g\sim O(1)` is uncontrolled — it *is* the intermediate-field
  problem of §28, now wearing screening coordinates;
- the induced `S_{Z_2}^{\rm eff}[z]` is **not** a pure nearest-neighbor `Z_2`
  gauge action: integrating out `SO(3)` generates multi-plaquette and extended
  `Z_2` couplings (the §26 `S_{\rm ext}` tower in `Z_2` clothing), and the exact
  threshold `\beta^\ast` is the nearest-neighbor value; controlling the deviation
  is open;
- the `SU(2)\to SO(3)\times Z_2` split carries gauge-fixing/center-projection
  ambiguities (Gribov copies, choice of section), so `\beta_{Z_2}^{\rm eff}` is
  defined only up to the same scheme dependence flagged for `\Xi_S` in §19.3.

### 29.6. Status Of The Exploration

```math
\boxed{
\begin{array}{l}
\textbf{Frontier exploration: a new coordinate, not a breach.}\\[1mm]
\text{Reframes intermediate-field center disorder as an induced }Z_2\text{ coupling}\\
\text{crossing the \emph{exactly known} 4D }Z_2\text{ self-dual threshold }\beta^\ast=\tfrac12\log(1+\sqrt2).\\[1mm]
\text{Genuine gains: rigorous target threshold; two drivers (running + }SO(3)\text{ screening);}\\
\text{a pinned numerical gap (}\sim5\times\text{) showing the crossing is thick-vortex driven.}\\[1mm]
\text{Open exactly as §28: the screening }Z_{\rm scr}\text{ at }g\sim O(1)\text{, plus the induced}\\
\text{multi-plaquette }Z_2\text{ tower and the projection scheme. No part of this is a proof.}
\end{array}}
```

### 29.7. Why Refining The Estimate Is A Mirage

The §29.4 finding — running plus *leading* screening overshoots `\beta^\ast` by a
factor `\sim5` at the bare crossover — invites the optimistic reading "we are
close; a better estimate will cross." This subsection records why that reading is
a trap, because the trap is instructive.

Do the natural refinement "along the line": evaluate the criterion not at the
bare crossover scale but at the **RG-flowed** scale where the thick vortex
actually lives, so `\beta_k` is the run-down coupling. Then the criterion **does**
cross:

```math
\beta_k\,Z_{\rm scr}<\beta^\ast
\quad\Longleftrightarrow\quad
\beta_k<\frac{\beta^\ast}{Z_{\rm scr}}\approx\frac{0.441}{0.66}\approx0.67 .
```

So a refined estimate crosses the threshold. But two facts make the crossing
empty as a step toward a proof:

1. **It crosses in the already-solved regime.** `\beta_k\approx0.67`
   (`g^2\approx6`) is *strong* effective coupling — at or inside the convergent
   strong-coupling / Osterwalder–Seiler regime (`\beta\lesssim1`) where the area
   law is **already rigorous**. Refining until the number crosses merely
   reproduces the known strong-coupling result; it never enters the
   weak-coupling/continuum regime where the difficulty lives.

2. **The dimensional-transmutation match is built in.** The crossing sits at a
   fixed physical scale (`\approx0.17/\Lambda`, constant in `\beta_0` across
   `\beta_0=4\text{--}12`). This looks like a success but is tautological: the
   per-step decrement `\Delta\beta=8b_0\log2` *encodes* the same `b_0` that
   defines `\Lambda`, so the flowed crossing scale matching the confinement scale
   is guaranteed by construction, not earned.

```math
\boxed{
\begin{array}{l}
\textbf{The obstruction was never the value of the number.}\\[1mm]
\text{Refining an uncontrolled heuristic until it crosses a threshold is not}\\
\text{convergence to a proof: "distance to }\beta^\ast\text{" is not a rigorous quantity}\\
\text{when the estimate is uncontrolled at the crossing coupling. The factor-}5\\
\text{at the crossover and the crossing at }\beta_k\approx0.67\text{ are equally heuristic.}\\[1mm]
\text{Progress requires rigorous control of }Z_{\rm scr}\text{ (and the induced tower) at}\\
g\sim O(1)\text{ — the §28 intermediate-field problem — which no refinement of}\\
\text{the estimate supplies, because the line itself is the heuristic.}
\end{array}}
```

What the screening picture *does* establish is genuine and worth keeping: it is
**self-consistent and dimensionally correct**, it reproduces strong-coupling
confinement, and it locates the crossing precisely (strong effective coupling,
fixed physical scale). It does not approach the weak-coupling problem. As a route
to rigor, this line is closed; as a confirmation that the confinement scenario
hangs together quantitatively, it succeeds.

## 30. Frontier Exploration: A Gauge-Invariant Center-Vortex Gas By Heat-Kernel Modular Duality

`V4P41-FRONTIER-MODULAR-CENTER-VORTEX-GAS`.

**Frontier exploration, not a proof.** This section proposes the best new idea I
have for `Z_{\rm scr}`: stop *estimating* the screening and instead change
representation by an *exact* transformation, so that the strong-coupling center
sector — which has no small parameter on the spectral side and is gauge-ambiguous
under center projection — is rewritten as a **center-vortex gas with an exact
fugacity**, obtained without any gauge fixing. The transformation is the
Poisson/modular identity for the `SU(2)` heat kernel. The single-object version is
exact and verified; the coupled `4D` version is conjectural, and the section is
honest about the residual being the open problem — but in coordinates where the
energy of a vortex is an *exact constant* and the only open competitor is a
*classical entropy*.

### 30.1. The Idea, And Why It Is Not The §29 Heuristic

The standard center-vortex route (Greensite, Engelhardt, …) extracts vortices by
**maximal-center gauge + projection**, which is exactly the gauge-dependent step
flagged in §19.3 and §29.5. The new element:

```math
\boxed{
\begin{array}{l}
\text{Reach the center-vortex representation by the \emph{exact, gauge-invariant}}\\
\text{Poisson resummation of the heat kernel over its center, not by projection.}\\
\text{Poisson summation introduces no scheme choice; the vortex content it}\\
\text{exposes is therefore an honest invariant, and its energy is computed, not fit.}
\end{array}}
```

This is *not* the §29 mirage: §29 refined an uncontrolled estimate of a number;
here we apply an exact identity that *replaces* the object by an equal one in a
different basis. No estimate is being pushed toward a threshold.

### 30.2. The Exact Modular Identity (Verified)

Write the `SU(2)` heat kernel in the class angle `\theta` (`\tfrac12\operatorname{tr}U=\cos\theta`)
via `n=2j+1`, and reduce it to the center theta function

```math
\Theta(t,\theta)=\sum_{n\in\mathbb Z}e^{-tn^2/4}\,e^{in\theta}.
```

Poisson summation gives the **exact** modular transformation

```math
\boxed{
\Theta(t,\theta)=\sqrt{\tfrac{4\pi}{t}}\sum_{m\in\mathbb Z}e^{-(\theta-2\pi m)^2/t}.
}
```

(Verified numerically to machine precision, `|{\rm LHS}-{\rm RHS}|\sim10^{-16}`,
at `(t,\theta)=(0.1,0.4),(0.3,0.7),(1,1.2),(3,2),(6,2.5)`.) The **spectral** side
(sum over representations `n`) converges fast at large `t` (strong coupling); the
**geometric** side (sum over images `m`) converges fast at small `t` (weak
coupling). The center flip `U\to-U` is `\theta\to\theta+\pi`, so the image lattice
splits:

```math
\underbrace{\theta=2\pi m}_{\text{center-even (identity images)}}
\qquad\text{vs}\qquad
\underbrace{\theta=\pi(2m+1)}_{\text{center-odd (vortex images)}}.
```

### 30.3. The Exact Vortex Fugacity

On the geometric side the center-odd (vortex) sector is carried by the
half-shifted lattice. The nearest vortex image sits at `\theta=\pi`, the nearest
identity image at `\theta=0`, so the **vortex fugacity** — the weight of one
elementary center defect relative to none — is exactly

```math
\boxed{
y(t)=\exp\!\Big(-\frac{\pi^2}{t}\Big),
\qquad
\text{energy coefficient }=\pi^2=\big(\text{geodesic distance to the center element}\big)^2 .
}
```

The energy of a center vortex is therefore **not a fitted coupling** but the
*exact* modular constant `\pi^2` (the squared class-angle distance from `1` to
`-1`), divided by the heat time. Numerically `y(t)=e^{-\pi^2/t}` runs from
`2.7\times10^{-9}` at `t=0.5` (vortices dilute, weak coupling) to `0.29` at
`t=8` (vortices proliferating, strong coupling) — monotone in coupling, as a
fugacity must be.

### 30.4. What This Buys: Screening As A Classical Energy–Entropy Crossing

In this representation the center sector is a **gas of vortex sheets** with
fugacity `y(t)=e^{-\pi^2/t}` per plaquette of sheet. The screening `Z_{\rm scr}`
of §29 — the cost reduction that lets vortices condense — is now the *response of
this gas*, and condensation (center disorder, `SU(2)` confinement) is the
classical energy–entropy crossing

```math
\boxed{
s_{\rm sheet}\;>\;\frac{\pi^2}{t}
\quad\Longleftrightarrow\quad
\text{center-vortex condensation}
\quad\Longleftrightarrow\quad
\text{area law,}
}
```

where `s_{\rm sheet}` is the entropy per unit area of coclosed vortex sheets in
`4D`. The decisive shift relative to §29:

- the **energy** side is now an *exact* constant, `\pi^2/t` — no screening
  estimate, no scheme;
- the only open competitor is `s_{\rm sheet}`, a **classical combinatorial
  entropy** of surfaces, plus the interaction the `SO(3)` bulk induces between
  sheets;
- the representation is **gauge-invariant** (Poisson, not projection), so unlike
  the standard center-vortex program it carries no projection ambiguity.

So the open quantity has changed character: from "an uncontrolled quantum
expectation `Z_{\rm scr}(g)`" to "the entropy and self-interaction of a gas of
surfaces with a known fugacity." That is a more classical, more tractable-looking
object — the kind of place where energy–entropy (Peierls/Pirogov–Sinai) methods
have teeth.

### 30.5. The Honest Wall

This does not close the problem, and the wall is precise:

- **Single-object exactness vs. coupled `4D`.** The modular identity is exact for
  the *decoupled* heat kernel (one plaquette / `2D`). In `4D` the plaquettes are
  coupled (Bianchi constraint + `SO(3)` dynamics), and the clean self-duality is
  broken — the vortex gas becomes *interacting*, the interactions being the
  `SO(3)` dressing. Those interactions are the §26 `S_{\rm ext}` tower once more,
  now as forces between center defects.
- **Diluteness fails exactly at condensation.** The fugacity-controlled dilute-gas
  expansion converges only while `y(t)` is small (weak coupling, ordered). At the
  condensation point `s_{\rm sheet}=\pi^2/t` the gas is *dense*, and the dilute
  expansion breaks down precisely where the answer is decided — the same dense-gas
  wall as every prior route, now in modular coordinates.
- **Entropy is not yet a theorem.** `s_{\rm sheet}` (the connective constant of
  `SO(3)`-dressed coclosed surfaces in `4D`) is a well-posed combinatorial
  quantity but is not computed here; the bare-surface entropy is a geometric
  constant, the dressed one needs the bulk.

### 30.6. Why It Is Nonetheless The Best Candidate

```math
\boxed{
\begin{array}{l}
\textbf{Best new idea, honestly bounded.}\\[1mm]
\text{Exact, gauge-invariant Poisson/modular rewriting of the }SU(2)\text{ center}\\
\text{sector as a vortex gas with \emph{exact} fugacity }e^{-\pi^2/t}\text{ (energy }=\pi^2\text{,}\\
\text{the squared distance to the center element). It converts }Z_{\rm scr}\text{ from an}\\
\text{uncontrolled quantum estimate into a classical surface energy–entropy}\\
\text{crossing }s_{\rm sheet}\gtrless\pi^2/t\text{, removing the projection ambiguity and}\\
\text{fixing the energy exactly.}\\[1mm]
\text{Open (the wall, relocated to its most classical form): the }4D\text{ dressed-}\\
\text{sheet entropy/interaction at the dense (condensation) point. Not a proof;}\\
\text{the best-posed version of the kernel this program has produced.}
\end{array}}
```

The advance, such as it is, is one of *form*: it is the first representation in
which the vortex energy is an exact number and the entire remaining unknown is a
classical combinatorial entropy — the cleanest target to hand to a genuine
energy–entropy (Pirogov–Sinai-type) attack, and the first center-vortex framing
here that is free of gauge-projection ambiguity. It is offered in that spirit:
not a breach, but the sharpest and most classical statement of what must be
estimated, with the energy side finished exactly.

## 31. The Bare Gas Is Exactly Solved; The Open Kernel Is Exactly The `SO(3)` Dressing

`V4P41-BARE-GAS-SOLVED-OPEN-KERNEL-IS-SO3-DRESSING`.

This is the capstone of the §§27–30 frontier arc. It records that the *second*
ingredient of the §30 vortex gas — the entropy — is also an exact constant, so
the bare gas is completely solved, and the entire open content collapses onto a
single, physically identified object. It is not a proof; it is the maximal
localization the program reaches.

### 31.1. Both Ingredients Of The Bare Gas Are Exact

The §30 modular representation fixed the vortex **energy** exactly: `\pi^2/t` per
sheet plaquette, `\pi^2` being the squared class-angle distance to the center
element. The **entropy** of the bare (undressed) gas is *also* exact, because the
bare gas is nothing but 4D `Z_2` gauge theory, whose disorder transition is the
Wegner self-dual point:

```math
\boxed{
\begin{array}{ll}
\text{energy coefficient} & \pi^2 \quad(\text{heat-kernel modular duality, §30});\\[1mm]
\text{bare sheet entropy} & s_0=\log(1+\sqrt2)=0.88137\ldots\\
& \big(\text{connective constant }\mu=1/\tanh\beta^\ast=1+\sqrt2,\ \beta^\ast=\tfrac12\log(1+\sqrt2),\ \text{§29}\big).
\end{array}}
```

(The high-temperature surface expansion of 4D `Z_2` gauge has weight
`(\tanh\beta)^{\rm area}`, convergent while `\tanh\beta\cdot\mu<1`; at the
self-dual point `\tanh\beta^\ast=\sqrt2-1`, giving `\mu=1+\sqrt2` and
`s_0=\log(1+\sqrt2)`.) Hence the bare energy–entropy crossing is at an exact
`O(1)` value,

```math
\frac{\pi^2}{t_c^{\,0}}=s_0
\quad\Longrightarrow\quad
t_c^{\,0}=\frac{\pi^2}{\log(1+\sqrt2)}=11.20\ldots,
```

a strong-coupling point, as expected. **The bare center-vortex gas is completely
solved: both its energy and its entropy are exact constants.**

### 31.2. Therefore The Entire Open Content Is The Dressing

Subtracting the solved bare gas from the true theory leaves *exactly one* object:

```math
\boxed{
\text{open kernel}=\text{the }SO(3)\text{ dressing}
=\Big(\text{true induced vortex gas}\Big)-\Big(\text{bare }Z_2\text{ gauge gas}\Big).
}
```

This is the same residual that every earlier route isolated — the §26
`S_{\rm ext}` tower, the §28 intermediate-field regime, the §29 deviation of the
induced `Z_2` theory from nearest-neighbour, the §30 inter-sheet interaction — now
seen as the modification of an *exactly solved* free vortex gas by the `SO(3)`
coset. The localization is maximal: two of the three ingredients (energy, bare
entropy) are finished as exact numbers; only the dressing remains.

### 31.3. What The Dressing Physically Is

The dressing has a clean topological identity, and naming it is the section's one
genuinely new physical statement. In `SU(2)` the center-vortex sheets are
**closed** (`\pi_1(SU(2))=0`). In the coset `SO(3)=SU(2)/Z_2` they need not be:
`\pi_1(SO(3))=Z_2` permits the sheets to bound on `Z_2`-monopole worldlines
(codimension three in 4D). The `SU(2)` measure is the sum over `SO(3)`
configurations with the closure constraint, and the dressing is precisely how the
`SO(3)` coset fluctuations — carrying that monopole structure — renormalize the
sheet tension `\pi^2/t` and the sheet entropy `s_0`:

```math
\boxed{
\begin{array}{l}
\text{Dressing} = SO(3)\text{-coset renormalization of (vortex tension, vortex entropy),}\\
\text{tied to the }SO(3)\ Z_2\text{-monopole content (sheets closed in }SU(2)\text{,}\\
\text{boundable by monopoles in }SO(3)\text{). Confinement } \Leftrightarrow \text{ the dressed}\\
\text{crossing }s_{\rm dressed}>\pi^2_{\rm dressed}/t\text{ is reached at a fixed physical scale.}
\end{array}}
```

This matches the long-standing `SO(3)`–`Z_2` monopole/vortex picture
(Datta–Mathur; Halliday–Schwimmer) of why the `SU(2)` continuum limit confines
where naive weak coupling would not: the `SO(3)` sector's own disorder
(light `Z_2` monopoles at intermediate coupling) is what dresses the vortices into
condensation.

### 31.4. Why This Is The Terminus (Honest)

The dressing is open for the reason it has always been open: it lives at
intermediate-to-strong `SO(3)` coupling, where neither a convergent expansion nor
Balaban small-field control applies, and where the dilute-gas expansion that
*would* compute it breaks down precisely at the dense condensation point. No
representation removes this; §§27–31 have only made the surrounding structure
exact so that the dressing stands alone.

```math
\boxed{
\begin{array}{l}
\textbf{Maximal localization reached.}\\[1mm]
\text{Energy }\pi^2\text{ exact; bare entropy }\log(1+\sqrt2)\text{ exact; gauge-ambiguity removed.}\\
\text{Sole open object: the }SO(3)\text{ dressing (= }Z_2\text{-monopole renormalization of}\\
\text{the vortex tension and entropy) at intermediate coupling. This is the §19.6}\\
\text{problem in its most reduced and most classical form. Not proved here, and}\\
\text{not provable by further change of representation — only by a genuine}\\
\text{estimate of the dressed surface free energy.}
\end{array}}
```

The §§27–31 arc is, honestly, a single sustained act of *localization*: it carried
the open problem from "prove a weak-coupling lower bound" (§§14–26) to "estimate
one classical surface free energy, with the energy and the bare entropy already
exact, and no gauge ambiguity" (§§30–31). That is the most this line of thought
produces. Closing it requires the dressed-surface estimate itself — expert,
non-perturbative, and not a reframing — and absent that, the honest action is to
record the localization and stop, not to re-derive the same kernel a further way.

## 32. The Open Problem (The `SO(3)` Dressing), Stated Self-Containedly

`V4P41-OPEN-PROBLEM-SO3-DRESSING-SELF-CONTAINED`.

**This section is self-contained.** A reader who reads only this section should
understand the open problem this paper localizes, what is already solved, what
remains, and exactly which requirements a solution must respect. Every symbol is
defined here; nothing outside this section is needed.

### 32.1. The theory, from scratch

Work on the 4-dimensional hypercubic lattice `\Lambda=(a\mathbb Z)^4` with spacing
`a>0`. Each oriented nearest-neighbour link `\ell` carries a group element
`U_\ell\in SU(2)`; reversing orientation inverts it. For an elementary square
(plaquette) `p` with boundary links `\ell_1\ell_2\ell_3\ell_4`, set
`U_p=U_{\ell_1}U_{\ell_2}U_{\ell_3}U_{\ell_4}`. The Wilson action and Gibbs
measure are

```math
S_\beta=\beta\sum_p\Big(1-\tfrac12\operatorname{tr}U_p\Big),
\quad
\beta=\frac{4}{g_0^2},
\quad
d\mu=\frac1Z\,e^{-S_\beta}\prod_\ell dU_\ell,
```

with `dU_\ell` normalized Haar measure and `Z` the normalizing partition
function. `\langle\cdot\rangle` denotes the `\mu`-expectation.

### 32.2. The continuum trajectory, and what "fixed-IR / uniform in `a`" means

The continuum limit is the joint limit `g_0^2=4/\beta\to0` and `a\to0` tied by
asymptotic freedom (`a\Lambda_{SU(2)}\sim\exp(-{\rm const}/g_0^2)`, so weak bare
coupling forces small spacing). Fix a **physical** length `R` (e.g. a Wilson-loop
size) in physical units and hold it fixed while `a\to0`, so `R/a\to\infty`
lattice spacings span it. Then:

```math
\boxed{
\begin{array}{l}
\textbf{Fixed-IR / uniform in }a:\ \text{a bound whose constants depend only on }R\\
\text{(and the theory), never on }a\text{ — equivalently, a bound that survives }a\to0\\
\text{at fixed physical }R.\ \textbf{This is the decisive requirement:}\text{ estimates that}\\
\text{hold only in lattice units, or only at fixed cutoff, are continuum-empty}\\
\text{because elementary lattice gaps vanish as }a\to0.
\end{array}}
```

### 32.3. The confinement quantity the problem reduces to

Let `z_\ell\in\{\pm1\}` be the `\mathbb Z_2`-center projection of `U_\ell` (the
nearest center element; this carries a section/gauge choice, flagged in §32.7),
and `b_p=\prod_{\ell\in\partial p}z_\ell\in\{\pm1\}` the center flux of plaquette
`p`. For a surface `S` of physical size `R` spanning a closed loop `C=\partial S`,
the **center flux** is

```math
\Xi_S=\prod_{p\in S}b_p=\prod_{\ell\in C}z_\ell\qquad(\mathbb Z_2\text{-Stokes: surface-independent}).
```

Let `m(\eta)=\langle\Xi_S\rangle_\eta` be its expectation conditioned on a fixed
physical collar `\eta`, and `r_a=(1-m)/(1+m)`. Center confinement is the area-law
decay `\langle\Xi_S\rangle\sim e^{-\sigma_{\rm phys}\,{\rm Area}}` with
`\sigma_{\rm phys}>0`, equivalently

```math
\boxed{
\liminf_{a\to0}\ \inf_{\eta}\big(1-|m(\eta)|\big)\ \ge\ \delta_R>0 .
}
```

(That center confinement equals fundamental confinement is *center dominance*,
expected and numerically robust but not proven; see §32.7.)

### 32.4. What is already solved: the exact bare vortex gas

Two exact facts reduce the difficulty to a single object.

- **Exact energy (heat-kernel modular duality, §30).** Poisson-resumming the
  plaquette weight over its center rewrites the center sector, *gauge-invariantly
  and with no center projection*, as a gas of center-vortex sheets (coclosed
  2-surfaces). Each sheet plaquette carries the **exact** energy `\pi^2/t`, where
  `\pi^2` is the squared class-angle distance from `1` to the center element `-1`
  and `t` is the effective heat-kernel time of the scale-appropriate plaquette
  weight (`t` grows monotonically as the effective coupling grows toward the IR;
  the precise `t\!\leftrightarrow\!\beta` map is scheme-dependent, but `\pi^2` is
  exact and scheme-independent).
- **Exact bare entropy (`Z_2` self-duality, §31).** With the `SO(3)=SU(2)/Z_2`
  coset frozen, the vortex gas *is* 4D `Z_2` gauge theory, whose disorder
  transition is the Wegner self-dual point `\beta^\ast=\tfrac12\log(1+\sqrt2)`.
  Its surface connective constant and entropy are therefore exact:

```math
\mu=\frac1{\tanh\beta^\ast}=1+\sqrt2,
\qquad
s_0=\log(1+\sqrt2)=0.88137\ldots,
\qquad
t_c^{0}=\frac{\pi^2}{s_0}=11.20\ldots .
```

So the **bare** gas is completely solved: both its energy (`\pi^2`) and its
entropy (`\log(1+\sqrt2)`) are exact constants, and it condenses at the exact
`O(1)` heat-time `t_c^0`.

### 32.5. The open object: the `SO(3)` dressing (defined precisely)

Integrate out the `SO(3)=SU(2)/Z_2` coset degrees of freedom at fixed center-flux
configuration `\{z\}`. The result is an effective `\mathbb Z_2` gauge action
`S^{\rm eff}_{Z_2}[z]`. The **dressing** is its deviation from the bare
nearest-neighbour `Z_2` gauge action:

```math
\boxed{
\mathcal D[z]\ :=\ S^{\rm eff}_{Z_2}[z]-S^{\rm bare}_{Z_2}[z].
}
```

Equivalently, `\mathcal D` is the `SO(3)`-coset renormalization of the two exact
bare quantities — the vortex tension `\pi^2/t\to\tau(t)` and the sheet entropy
`s_0\to s(t)` — equivalently the tower of induced multi-plaquette / extended
`Z_2` couplings (the "`S_{\rm ext}` tower"). Its physical content: in `SU(2)` the
vortex sheets are **closed** (`\pi_1(SU(2))=0`); in `SO(3)` they may bound on
`Z_2`-monopole worldlines (`\pi_1(SO(3))=Z_2`, codimension three in 4D), and
`\mathcal D` is exactly how the coset's monopole-carrying fluctuations soften the
sheets.

### 32.6. The open problem (exact statement, three equivalent forms)

```math
\boxed{
\begin{array}{l}
\textbf{Open problem.}\ \text{Prove or disprove that the }SO(3)\text{-dressed center-vortex gas}\\
\text{condenses at a fixed physical scale, uniformly as }a\to0.\ \text{Equivalently, any of:}\\[2mm]
\text{(i)}\ \ s(t)>\tau(t)\ \text{(dressed entropy beats dressed energy) at the scale}\\
\qquad\text{corresponding to fixed physical }R,\ \text{uniformly as }a\to0;\\[1mm]
\text{(ii)}\ \ \text{the induced }Z_2\text{ theory }S^{\rm eff}_{Z_2}\text{ is in its disordered (confining) phase}\\
\qquad\text{(effective coupling below }\beta^\ast\text{) at fixed physical }R,\ \text{uniformly as }a\to0;\\[1mm]
\text{(iii)}\ \ \liminf_{a\to0}\inf_\eta(1-|m(\eta)|)\ge\delta_R>0\ \ (\text{= §32.3}).
\end{array}}
```

The three are equivalent. Form (iii) is the bare confinement statement; (i)–(ii)
expose that the *only* unknown is `\mathcal D` (the energy `\pi^2` and bare
entropy `\log(1+\sqrt2)` being already exact).

### 32.7. Requirements and limitations a solution must respect

```math
\boxed{
\begin{array}{l}
\textbf{R1 (fixed-IR).}\ \text{The estimate is at a fixed physical scale }R,\text{ not asymptotic in }R.\\[1mm]
\textbf{R2 (uniform in }a\textbf{).}\ \text{Constants depend on }R\text{ only, never on }a.\ \text{This is the crux:}\\
\qquad\text{a fixed physical block contains }O(1/a)\text{ steps and microscopic gaps vanish.}\\[1mm]
\textbf{R3 (intermediate coupling).}\ \mathcal D\text{ must be controlled where the effective}\\
\qquad\text{coupling is }O(1)\ \text{(the dense / condensation regime), NOT at weak coupling}\\
\qquad\text{(gas dilute, center ordered, no confinement) and NOT only at strong bare}\\
\qquad\text{coupling (already solved, does not reach the continuum).}\\[1mm]
\textbf{R4 (no dilute-gas shortcut).}\ \text{The fugacity expansion converges only on the}\\
\qquad\text{ordered side and breaks down exactly at condensation; a genuine dense-regime}\\
\qquad\text{method is required (Pirogov–Sinai for the disordered phase, RP/chessboard}\\
\qquad\text{lower bounds, or constructive-RG continuation past the small-field window).}\\[1mm]
\textbf{R5 (non-circularity).}\ \text{A solution may NOT assume: a mass gap; clustering or a}\\
\qquad\text{finite correlation length; }\sigma_{\rm phys}>0;\text{ center decorrelation; the strong-coupling}\\
\qquad\text{expansion as a continuum substitute; weak-coupling / Balaban small-field control}\\
\qquad\text{as a substitute for R3; center dominance; nor the bare-gas solution as the dressed one.}\\[1mm]
\textbf{R6 (gauge).}\ \text{The modular vortex-gas representation is gauge-invariant; the explicit}\\
\qquad\text{computation of }\mathcal D\text{ via coset integration carries section-choice subtleties that}\\
\qquad\text{a solution must either avoid (stay manifestly invariant) or control.}
\end{array}}
```

### 32.8. What counts as a solution

A proof of any one equivalent form in §32.6, respecting R1–R6, establishes
continuum `SU(2)` center confinement (`\sigma_{\rm phys}>0`); a disproof shows the
center route fails (and any `SU(2)` string tension is not center-dominated).
Honest partial credit: a rigorous bound on the dressing `\mathcal D` at
intermediate coupling that is uniform in `a` — even short of closing the crossing
— would be a genuine advance, since it is the single missing ingredient onto which
every reduction in this paper converges.

## 33. Final Status Ledger

`V4P41-FINAL-STATUS-LEDGER`.

```math
\boxed{
\begin{array}{ll}
\textbf{Proved (unconditional, this paper):}\\
\quad\bullet\ \text{exact even–odd reduction of the reflected asymmetry} & (\text{Lem. 41.20/41.21});\\
\quad\bullet\ \text{asymmetry vanishes for reflection-symmetric sheets} & (\text{Lem. 41.31});\\
\quad\bullet\ \text{symmetric sheets exist for rectangular loops, }\mathcal A_a\equiv0\text{ off corners} & (\text{Prop. 41.32 / Cor. 41.33});\\
\quad\bullet\ \text{exact heat-kernel modular identity; vortex fugacity }e^{-\pi^2/t} & (\text{§30});\\
\quad\bullet\ \text{bare vortex gas solved: entropy }\log(1+\sqrt2) & (\text{§31}).\\[2mm]
\textbf{Established modulo cited inputs:}\\
\quad\bullet\ \text{leading-order generated }S_{\rm ext}\text{ is }O(\beta^{-2})\text{, reinforcing sign} & (\text{§27, one-loop }b_0);\\
\quad\bullet\ \text{§27 signal = one-loop running, rigorous in the small-field window} & (\text{§28, Balaban}).\\[2mm]
\textbf{Located, not proved:}\\
\quad\bullet\ \text{the magnitude frontier }=\text{ the }SO(3)\text{ dressing at intermediate coupling} & (\text{§32}).\\[2mm]
\textbf{NOT proved (open):}\\
\quad\bullet\ \text{confinement, mass gap, }\sigma_{\rm phys}>0,\text{ center dominance.}
\end{array}}
```

**Contribution.** This paper does not solve Yang–Mills confinement. It provides
(a) a faithful chain of exact reductions from the single-collar certificate to one
kernel; (b) a set of negative results closing tempting shortcuts (No-Free-Lunch
Thm 40.5; the spurious-`T1` correction; the §29.7 estimate-refinement mirage; the
RP ceiling-vs-floor obstruction §22.5); and (c) a *maximal localization* in which
the kernel's energy (`\pi^2`) and bare entropy (`\log(1+\sqrt2)`) are exact, the
gauge-projection ambiguity is removed, and the sole remaining unknown — the
`SO(3)` dressing — is stated self-containedly in §32 with its exact requirements.
Whether that dressing drives condensation at a fixed physical scale, uniformly in
`a`, is the open problem, and it is Clay-level. Nothing here should be read as a
proof of it.
