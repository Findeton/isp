# Relativistic ISP V3 Paper 17: Mass Gap Gates For Relativistic ISP Yang-Mills

Author: Felix Robles Elvira

## Abstract

Paper 16 gives the conditional continuum-facing pure `SU(N)` Yang-Mills
Wilson-loop functional:

```text
HK-CYC-CLOSE
=> AYM-CLOSE
=> strong CYC
=> CYM_WL.
```

Paper 17 asks the next question:

```text
Does the resulting gauge-invariant continuum record theory have a positive
spectral gap?
```

The answer of this paper is again conditional but sharper than a slogan. We
define operational gauge-invariant mass-gap probes, formulate an exponential
clustering certificate with a positive continuum mass scale, prove the
reflection-positivity-to-spectral-gap reduction, and isolate the exact
artifact-removal gates needed to distinguish a real continuum mass gap from
finite-volume, smearing, cutoff, block-scale, or finite-battery effects.

The paper does not prove the Clay Yang-Mills mass-gap theorem. It proves the
ISP-aligned gate:

```text
CYM_WL
+ operational gauge-invariant OS probe density
+ positive continuum exponential clustering
+ artifact-removal ledger
+ whole-process compatibility
=> mass gap in the declared gauge-invariant OS sector.
```

### Post-Paper-20 Source Boundary

Paper 17 is downstream of continuum Wilson-loop and clustering inputs. It
does not supply Paper 20's `SEL2` block-plaquette tree-rate source and cannot
be used to infer

```text
P20-SEL2-TREE-RATE-GATE,
T_-^{SEL2} > Theta_T^tree(rho),
q_rho gamma_rho > Theta_esc^tree.
```

Those estimates are prior source gates for the confinement route, not
consequences of the conditional mass-gap reduction.

## 0. Compact Theorem Summary

The target closure chain is:

```text
CYM_WL
+ MG-OBS
+ Paper-13--15 marked connected-polymer import
+ positive debited mass ledger
+ MG-ART
+ MG-WP
=> MG-CLOSE
=> MGAP.
```

Here:

1. `CYM_WL` is the Paper-16 continuum Wilson-loop record functional.
2. `MG-OBS` says the chosen gauge-invariant mass-gap probes are operational
   records and are dense enough in the declared OS sector.
3. the Paper-13--15 import supplies a marked connected-polymer estimate for
   the chosen probe batteries, not merely a finite Creutz reserve.
4. the debited mass ledger proves that the connected-polymer rate survives
   cutoff, volume, smearing, block, battery, regulator, and projective losses.
5. `MG-ART` removes finite-volume, smearing, cutoff, block-scale, and
   finite-battery artifacts.
6. `MG-WP` is the same whole-process compatibility audit as Paper 16,
   specialized to correlation and spectral estimates.
7. `MGAP` means a positive lower spectral gap in a declared gauge-invariant
   OS Hilbert sector.

The core mathematical theorem is:

```text
reflection positivity
+ Euclidean time covariance
+ dense gauge-invariant OS probes
+ connected Euclidean clustering with rate m_gap
=> spectrum(H) on the non-vacuum gauge-invariant sector is contained in
   [m_gap,infinity).
```

## 0A. Barandes-Aligned Ontology

The primitive object remains the whole-process law of records. Paper 17 does
not introduce glueballs, particles, gauge-fixed fields, or a Hilbert-space
spectrum as primitive ontology.

The order is:

```text
finite record laws
-> continuum Wilson-loop functional
-> OS reconstruction from reflection positivity
-> spectral statement.
```

Gauge-fixed fields and local curvature symbols are allowed only as proof
coordinates or shorthand for operational records built from closed
gauge-invariant loops. The mass gap is a property of the reconstructed
OS sector, not a new hidden state variable.

## 0B. Honest Boundary

Paper 17 does not prove:

1. unconditional `4D SU(N)` Yang-Mills existence;
2. Paper 16's `AYM-CLOSE`;
3. confinement or arbitrary large-loop area law;
4. QCD with matter;
5. scattering theory;
6. gravity or stress-energy geometry reconstruction.

It proves that if Paper 16 supplies `CYM_WL` and the new mass-gap gates hold,
then the declared gauge-invariant OS sector has a positive spectral gap.

### Continuum-floor pointer (external review, 2026-05)

This conditional reduction is the *easy* OS direction: exponential clustering
with a positive rate `m_gap` implies a spectral gap. The load-bearing input is
the rate itself — the positive continuum clustering rate / string-tension floor
fed in as `G_j-2PT-KP` and `MG-UNIF(m_*)`. That floor is **not** established
here; it is reduced downstream (Papers 18-21) to a strict source inequality
(sheet rate vs. surface-polymer entropy), which the v3 corpus left **undecided**,
and which the v4 consolidation (paper 39, Section 11, `TOK-BESSEL`) proves only
at *fixed* heat-kernel collar time `t_- > 0`. Uniform survival as `t_- → 0` is
the open infrared step and coincides with the open part of the Clay problem.

Note (non-circular): the ISP suppositions here are existence/reconstruction/
probe-density/whole-process conditions only; none assumes clustering, a
correlation length, or a mass scale. So the gap is genuinely *reduced* to the
floor, not assumed — the circularity risk does not arise. The single missing
piece is the continuum survival of the floor.

## 0C. What This Paper Proves And Does Not Prove

**Proves, conditionally.** Paper 17 proves the following ISP-aligned
conditional theorem:

```text
CYM_WL
+ MG-OS-CLOSE
+ cofinal MG-OBS
+ G_j-2PT-KP for every j
+ MG-UNIF(m_*)
+ MG-WP
=> MG-EXP-CLOSE(m_*)
=> MGAP(m_*).
```

Equivalently: if the continuum Wilson-loop record functional exists with the
Paper-16 structural properties, if the operational loop batteries are dense,
if the Paper-13--15 marked connected-polymer estimates extend to those
batteries, and if the debited rates have a positive common lower bound, then
the declared gauge-invariant OS sector has a positive mass gap.

**Does not prove, unconditionally.** Paper 17 does not prove that actual
four-dimensional `SU(N)` Yang-Mills satisfies `G_j-2PT-KP` for every `j`, nor
that the uniform reserve `MG-UNIF(m_*)` holds. Those are the remaining
dynamical estimates.

**Ontology.** The theorem is still stated in terms of whole-process record
laws, Wilson-loop records, OS reconstruction, and correlation estimates. It
does not add particles, gauge-fixed fields, or hidden microscopic states as
primitive objects.

## 1. Imports

### 1.1 Paper 16

Paper 16 supplies the conditional continuum functional:

```text
CYM_WL.
```

For Paper 17 this means:

1. a normalized continuum Wilson-loop record functional `W_infty`;
2. reflection positivity on the declared OS subalgebra;
3. Euclidean covariance;
4. gauge invariance of closed scalar records;
5. loop continuity on the declared admissible loop class;
6. nontriviality of at least one scalar Wilson-loop record;
7. whole-process compatibility through the common tower `T_HK`.

Paper 17 may use only those outputs. It may not assume a mass gap, a particle
interpretation, or confinement.

### 1.2 Paper 12

Paper 12 supplies the renormalized unsmeared Wilson-loop record technology:

```text
perimeter/cusp renormalization,
smeared-to-unsmeared consistency,
loop-continuity modulus,
counterterm-weighted RP/covariance compatibility.
```

Paper 17 uses this only to define admissible localized loop probes and to
separate genuine mass scales from smearing/counterterm artifacts.

### 1.3 Papers 13--15

Papers 13--15 supply the nontriviality and connected-polymer machinery:

```text
Creutz/scalar anchor,
connected-polymer KP bounds,
surface/decoration reserves,
positive X_15 tower.
```

Paper 17 may use those estimates as candidate sources of exponential
clustering, but it must not confuse a finite Creutz reserve with a spectral
gap. The gap requires decay of two-point connected correlations in Euclidean
time after all artifact losses are removed.

The exact imports used below are:

1. Paper 13, Definition 7.30AR and Theorem 7.30AS: connected-cumulant KP
   control of the residual block law proves `RPF` and `KP_dec`.
2. Paper 13, Definition 7.30AT: the mass-gap/area-law bridge identifies
   exponential connected-cumulant decay as the relevant input for the
   remaining gates.
3. Paper 14, Theorem 4.2 and Theorem 32.1: `FBE(s_0,rho,L)` exports
   `BC`, `CE`, `WP`, and the finite-block package `X_14`.
4. Paper 15, Theorem 7.2A, Theorem 8A.2, Theorem 12.1B, and Definition
   12.5: positive `nCPSC` exports `RCE(A_AF,mu_AF,r_*)`,
   `RKP(A_AF,mu_AF,m_KP)`, `eta_dec^{bd}<1`, and `X_15`.

Paper 15's `X_15` is finite-battery and Creutz-oriented. To use it for a
mass-gap theorem, Paper 17 must add the marked two-point and cofinal-battery
extension stated in Definition 5.4. That is the precise place where the
mass-gap burden enters.

## 2. Operational Mass-Gap Probes

### Definition 2.1: Gauge-Invariant Local Record Probe

A gauge-invariant local record probe at physical scale `r>0` is a bounded
renormalized scalar record `O_{r,rho}(x)` constructed from finitely many
closed Wilson loops contained in a ball or rectangular block of radius `r`
around `x`, with representation labels in a finite battery `Rep_j`.

The allowed generators are:

1. small rectangular Wilson loops;
2. finite linear combinations that cancel the trivial constant component;
3. calibrated field-strength proxies built from closed-loop plaquette or
   clover combinations;
4. finite products and real linear combinations of such records.

The phrase "field-strength proxy" is operational. It means a declared limit
of closed-loop records. It is not a gauge-fixed field inserted as primitive
ontology.

### Definition 2.2: Centered Probe

Given the continuum functional `W_infty`, the centered version of an
observable `O` is

```math
O^0 = O - W_\infty(O)\,\mathbf 1 .
```

Only centered probes test the non-vacuum sector. The vacuum vector is not
part of the mass gap.

### Definition 2.3: Mass-Gap Probe Battery

A mass-gap probe battery `G_j` is a finite set of centered gauge-invariant
local probes:

```math
G_j=\{O_1^0,\ldots,O_{N_j}^0\}.
```

The batteries are nested and cofinal if their real linear span is dense in
the declared gauge-invariant OS local sector after OS null vectors are
quotiented out.

### Definition 2.4: Operational Probe Density `MG-OBS`

`MG-OBS` holds when:

1. every probe in every `G_j` is represented by finite Wilson-loop records on
   the Paper-16 common tower;
2. the centered probes have finite continuum norms in the OS inner product;
3. the union of the probe spans is dense in the declared gauge-invariant OS
   sector;
4. all probe approximants use the same loop, counterterm, regulator/chart,
   and whole-process ledgers as Paper 16.

This is the first mass-gap gate. Without `MG-OBS`, an exponential estimate on
a small hand-picked battery proves only a finite-record decay statement, not
a spectral gap for a sector.

### Definition 2.5: First Plaquette-Clover Probe Battery `G_box`

Fix:

1. a physical block scale `ell_blk=s_0`;
2. a finite representation battery `Rep_box`, for example the fundamental
   representation and its conjugate channel, closed under the scalar real
   part used below;
3. a finite spatial localization block `B_0`;
4. a finite orientation set of plaquette planes `mu<nu`.

For each oriented plaquette or clover loop `C_{mu nu}(x,s_0)` contained in
`B_0`, define the normalized scalar loop record

```math
Q_{\rho,\mu\nu}(x)
=
{\rm Re}\,{1\over d_\rho}\chi_\rho
\!\left(U_{\partial C_{\mu\nu}(x,s_0)}\right).
```

The first plaquette-clover battery `G_box` is the centered finite set
generated by:

1. all centered one-loop records `Q_{\rho,\mu\nu}^0(x)`;
2. all centered clover averages

   ```math
   {\rm Cl}_{\rho,\mu\nu}^0(x)
   =
   \left(
   {1\over 4}\sum_{a=1}^4 Q_{\rho,\mu\nu}^{(a)}(x)
   \right)^0;
   ```

3. all centered products of at most two such records whose supports remain
   inside the one-block collar of `B_0`.

Here centering is always with respect to `W_infty`. The clover notation is a
record abbreviation for a finite average of closed Wilson-loop records. It
does not introduce a gauge-fixed field strength as primitive ontology.

### Lemma 2.6: `G_box` Is An Operational Finite Battery

Assume Paper 12's finite-battery renormalized Wilson-loop functional and
Paper 16's `CYM_WL` hold on the loop and product records appearing in
Definition 2.5. Then `G_box` satisfies the finite-battery part of `MG-OBS`.

Proof.

Every element of `G_box` is a finite real linear combination or finite
product of closed scalar Wilson-loop records in a declared representation
battery. Paper 12 supplies the finite-battery renormalized loop records,
product bounds, and smearing/removal consistency; Paper 16 supplies the
continuum functional `W_infty` used for centering. Therefore the records are
operational finite readouts on the Paper-16 tower and have finite OS norms
whenever the Paper-16 OS form is finite on the same finite product battery.
This proves finite-battery `MG-OBS` for `G_box`. It does not prove cofinal
density of the full gauge-invariant OS sector. `square`

### Definition 2.7: Cofinal Plaquette-Clover Loop Batteries `G_j`

Fix a countable dense admissible loop skeleton from Paper 13 and the
renormalized loop-battery technology of Paper 12. A cofinal
plaquette-clover loop battery sequence is a nested sequence

```math
G_{\rm box}\subset G_1\subset G_2\subset\cdots
```

constructed as follows.

For each `j`, choose:

1. a finite spatial box `B_j` with `B_j` exhausting space;
2. a finite time slab of positive-time translates used for the OS
   two-point tests;
3. a finite representation set `Rep_j`, nested and cofinal in the declared
   representation battery;
4. a finite admissible loop set `D_j` from the Paper-13 loop skeleton,
   including plaquettes, clovers, small rectangles, and their declared
   rational polygonal approximants;
5. a finite product degree `p_j`, with `p_j` increasing to infinity only
   along the countable skeleton;
6. a finite set of physical block scales `ell_{j,k}` allowed by the
   Paper-12 and Paper-16 ledgers.

`G_j` is the centered finite set generated by all normalized real scalar
Wilson-loop records in `D_j`, their declared plaquette/clover averages, and
all finite products of degree at most `p_j` whose supports remain in the
chosen box and time slab.

The sequence is cofinal for the declared gauge-invariant OS sector if the
real algebra generated by the union of the uncentered records is dense in
`A_+^{GI}` in the Paper-13 loop-continuity topology, and hence its centered
classes are dense in `{\mathcal H}_{\rm GI}\cap\Omega^\perp` after quotienting
OS null vectors.

### Theorem 2.8: Cofinal `MG-OBS` Reduction

Assume:

1. Paper 12 supplies finite-battery renormalized Wilson-loop records,
   product bounds, smearing-removal consistency, and diagonal extension on
   the nested loop batteries;
2. Paper 13 supplies a countable dense loop skeleton and loop-continuity
   modulus for the declared admissible loop class;
3. Paper 16 supplies `CYM_WL`, reflection positivity, and finite OS norms on
   every finite product battery in the sequence;
4. the declared gauge-invariant OS sector is the closure of the positive-time
   algebra generated by this countable operational loop skeleton.

Then each `G_j` satisfies finite-battery `MG-OBS`, and the sequence
`{G_j}` satisfies the density clause of `MG-OBS`.

Proof.

For fixed `j`, every element of `G_j` is a finite real linear combination or
finite product of closed scalar Wilson-loop records in a finite Paper-12
battery. The same argument as Lemma 2.6 gives operational finite-battery
`MG-OBS`. The nesting and diagonal extension from Paper 12 place all finite
batteries on the same limiting record functional. Paper 13's dense skeleton
and loop-continuity modulus identify the closure of the countable loop
algebra with the declared positive-time gauge-invariant algebra. Centering
removes the vacuum component, and quotienting by OS null vectors preserves
density in the non-vacuum OS sector. `square`

## 3. OS Hilbert Sector From Records

### Definition 3.1: Positive-Time OS Algebra

Let `A_+^{GI}` be the algebra generated by gauge-invariant local record
probes supported in positive Euclidean time. Reflection is denoted by
`theta`.

The OS sesquilinear form is

```math
\langle F,G\rangle_{\rm OS}
=
W_\infty(\theta F\,G).
```

Reflection positivity from Paper 16 says:

```math
\langle F,F\rangle_{\rm OS}\ge 0.
```

### Definition 3.2: Gauge-Invariant OS Hilbert Sector

Let `N_OS` be the null space:

```math
{\mathcal N}_{\rm OS}
=
\{F\in{\mathcal A}_+^{\rm GI}:\langle F,F\rangle_{\rm OS}=0\}.
```

The gauge-invariant OS Hilbert sector is the completion:

```math
{\mathcal H}_{\rm GI}
=
\overline{{\mathcal A}_+^{\rm GI}/{\mathcal N}_{\rm OS}}.
```

The vacuum vector is the class of `1`, denoted `Omega`.

### Definition 3.3: Euclidean Time Semigroup

For `t>=0`, let `tau_t` be Euclidean time translation. The OS time semigroup
is defined on local classes by

```math
T(t)[F]=[\tau_t F].
```

`MG-OS` holds when Paper 16's reflection positivity and Euclidean covariance
make `T(t)` a strongly continuous contraction semigroup on `Hilb_GI`.

By the Hille-Yosida/OS reconstruction step, there is a nonnegative
self-adjoint generator `H_OS` such that:

```math
T(t)=\exp(-tH_{\rm OS}).
```

This is the first place where a Hilbert-space Hamiltonian appears. It is
reconstructed from records; it is not assumed.

### Theorem 3.4: `MG-OS-CLOSE`

Assume `CYM_WL` supplies:

1. reflection positivity on `{\mathcal A}_+^{\rm GI}`;
2. Euclidean covariance of `W_infty`;
3. invariance of the OS null space under positive Euclidean time
   translations;
4. OS-norm continuity of time translations on the dense local algebra:

   ```math
   \lim_{t\downarrow 0}
   \left\|
   [\tau_tF]-[F]
   \right\|_{\rm OS}
   =
   0
   ```

   for every local positive-time gauge-invariant record `F`.

Then `MG-OS` holds: the maps `T(t)[F]=[\tau_tF]` extend to a strongly
continuous contraction semigroup on `{\mathcal H}_{\rm GI}`, and there is a
nonnegative self-adjoint generator `H_OS` such that

```math
T(t)=\exp(-tH_{\rm OS}).
```

Proof.

Reflection positivity makes the OS quotient pre-Hilbert space positive.
Euclidean covariance and null-space invariance make `T(t)` well-defined on
OS classes. Reflection positivity applied to translated positive-time
records gives the contraction estimate

```math
\|T(t)[F]\|_{\rm OS}\le \|[F]\|_{\rm OS}.
```

The OS-norm continuity clause gives strong continuity on the dense local
subspace. Since the `T(t)` are contractions, this strong continuity extends
to the Hilbert completion. The semigroup law follows from Euclidean time
translation covariance. The Hille-Yosida/OS reconstruction theorem then gives
a nonnegative self-adjoint generator `H_OS`. `square`

The nontrivial analytic input in this theorem is clause 4. In the ISP
ledger, it must come from Paper 13 loop continuity plus Paper 16 covariance
on the same whole-process tower; it is not an extra hidden Hilbert-space
axiom.

## 4. Mass Gap As A Spectral Statement

### Definition 4.1: Declared Gauge-Invariant Mass Gap `MGAP(m)`

For `m>0`, `MGAP(m)` holds when the spectrum of `H_OS` on the orthogonal
complement of the vacuum satisfies:

```math
\operatorname{spec}\!\left(H_{\rm OS}\big|_{\Omega^\perp}\right)
\subset [m,\infty).
```

The mass gap is:

```math
m_{\rm gap}
=
\sup\{m>0:{\rm MGAP}(m)\ {\rm holds}\}.
```

Paper 17's pass condition is not "some finite-volume transfer matrix has a
gap." The pass condition is `MGAP(m)` for some `m>0` after the continuum,
infinite-volume, unsmeared or renormalized-local, and cofinal-battery limits
have been taken.

### Definition 4.2: Probe-Sector Mass Gap

For a dense probe family with

```math
D\subset {\mathcal H}_{\rm GI}\cap\Omega^\perp,
```

`MGAP_D(m)` holds when every vector in `D` has spectral measure supported in
`[m,infinity)`.

If `D` is dense in `Omega^\perp` and the spectral projections are closed,
then `MGAP_D(m)` implies `MGAP(m)`.

## 5. Exponential Clustering Gate

### Definition 5.1: Connected Two-Point Record Correlator

For centered probes `O^0,P^0`, define the Euclidean time-separated
connected correlator:

```math
C_{O,P}(t)
=
W_\infty\!\left(O^0\,\theta_t(P^0)\right).
```

For positive-time OS vectors this equals the semigroup matrix element:

```math
C_{O,P}(t)
=
\langle[O^0],\exp(-tH_{\rm OS})[P^0]\rangle_{\rm OS}.
```

### Definition 5.2: Continuum Exponential Clustering `MG-EXP(m,A)`

For `m>0`, `MG-EXP(m,A)` holds on the probe batteries when, for every
centered probe `O` in the declared dense family,

```math
|C_{O,O}(t)|\le A(O)\exp(-mt)
```

for all sufficiently large `t>=0`, with `A(O)<infinity`.

The stronger bilinear form holds if, for all centered `O,P`,

```math
|C_{O,P}(t)|\le A(O,P)\exp(-mt).
```

The one-vector bound is enough for the spectral-support theorem below; the
bilinear bound is the operational clustering form one usually wants.

### Definition 5.3: Uniform Continuum Clustering Ledger `MG-EXP-CLOSE`

`MG-EXP-CLOSE(m)` holds when the exponential clustering bound is obtained as
a limit of finite-record estimates:

```math
|C_{i,O,O}(t)|
\le
A_i(O)\exp(-(m+\epsilon_i)t)+R_i(O,t),
```

where:

1. `epsilon_i -> 0`;
2. `A_i(O)` remains bounded by `A(O)` on the cofinal tail;
3. `R_i(O,t)` is dominated by `B(O) exp(-m' t)` with `m'>m` or has a
   summable tail that vanishes uniformly in the continuum limit;
4. all estimates use the same Paper-16 common tower.

This gate prevents a common mistake: proving decay at fixed cutoff or fixed
volume and then calling it a continuum mass gap.

### Definition 5.4: Marked Two-Point Paper-13--15 Import `MG-2PT-KP`

Fix a finite mass-gap probe battery `G_j`, a physical block scale
`ell_blk>0`, and a Paper-14/Paper-15 block graph containing the supports of
all probes in `G_j` and their Euclidean time translates.

`MG-2PT-KP(G_j,m_KP)` holds when the following are true for the same exact
pushed-forward block record law:

1. Paper 14 proves `FBE(s_0,rho,L)` and exports `X_14`.
2. Paper 15 has a positive numerical certificate `nCPSC(s_0,rho,L)` and
   exports `X_15(s_0,L,rho)`.
3. The Paper-13 connected-cumulant KP criterion of Definition 7.30AR applies
   not only to the finite Creutz battery but also to the marked two-point
   hulls generated by every pair `O,P` in `G_j`.
4. The Paper-15 constants are valid on these marked hulls:
   `AFRCE(A_AF,mu_AF,r_*)`, `RKP(A_AF,mu_AF,m_KP)`,
   and `eta_dec^{bd}<1`.
5. Marking the endpoint probes changes only the amplitude, or else its
   exponential loss is recorded explicitly in `Delta_bat` or `Delta_block`.
6. The comparison from physical time separation to block distance has a
   finite endpoint collar constant `c_j(O,P)`.

This definition is deliberately stronger than Paper 15's finite Creutz
export. It is the smallest Barandes-aligned extension needed for a mass-gap
claim: the extra data are still record-law cumulants and finite operational
readouts, not hidden particles or gauge-fixed microscopic fields.

### Lemma 5.5: Marked KP Gives Finite-Battery Exponential Clustering

Assume `MG-2PT-KP(G_j,m_KP)` with `m_KP>0`. Then for every centered
`O,P` in `G_j` there is a finite amplitude `A_j(O,P)` such that the
finite-block connected correlator obeys

```math
|C_{j,O,P}^{\rm blk}(t)|
\le
A_j(O,P)\exp\!\left[-{m_{\rm KP}\over \ell_{\rm blk}}\,t\right]
```

for all sufficiently large `t`, after absorbing the endpoint collar into
`A_j(O,P)`.

Proof.

In the connected-polymer representation, the connected part of the two-point
correlator is a sum over compatible marked polymers whose hull intersects
both endpoint supports. A polymer joining supports separated by Euclidean
time `t` has block diameter at least `t/ell_blk-c_j(O,P)`. The Paper-13
connected-cumulant KP criterion, with the Paper-15 `RKP` weight `m_KP`,
therefore bounds the marked sum by a finite endpoint amplitude times
`exp(-m_KP(t/ell_blk-c_j(O,P)))`. Absorb
`exp(m_KP c_j(O,P))` into `A_j(O,P)`. `square`

### Definition 5.6: Mass-Gap Rate Ledger Imported From Papers 13--15

For a fixed battery and block scale, define the raw connected-polymer rate:

```math
m_{\rm raw}
=
{m_{\rm KP}\over \ell_{\rm blk}}.
```

The Paper-15 KP weight `m_KP` may be chosen by the explicit first-gate test:

```math
0<m_{\rm KP}<\mu_{\rm AF}-h_{\rm an},
```

with

```math
\delta_{\rm KP}
=
\mu_{\rm AF}-m_{\rm KP}-h_{\rm an}
>0
```

and

```math
\eta_{\rm res}^{\rm bd}
=
C_{\rm cum}(d,r_*)A_{\rm AF}
{e^{-\delta_{\rm KP}}\over 1-e^{-\delta_{\rm KP}}}
<1.
```

The Paper-15 decoration gate also requires:

```math
\eta_{\rm dec}^{\rm bd}
=
\eta_{\rm res}^{\rm bd}+\eta_{\rm ch}^{\rm bd}
<1.
```

A canonical sufficient choice is:

```math
\begin{aligned}
m_{\rm KP}^{\rm can}
&=
{\mu_{\rm AF}-h_{\rm an}\over 2},\\
\delta_{\rm KP}^{\rm can}
&=
{\mu_{\rm AF}-h_{\rm an}\over 2}.
\end{aligned}
```

Use this choice only when the corresponding `eta_res^{bd}<1` test holds.

### Definition 5.7: Explicit Artifact-Debited Mass Ledger

Given the raw rate of Definition 5.6, define:

```math
\Delta_{\rm tot}
=
\Delta_{\rm cut}
+\Delta_{\rm vol}
+\Delta_{\rm smear}
+\Delta_{\rm block}
+\Delta_{\rm bat}
+\Delta_{\rm reg}
+\Delta_{\rm proj}.
```

The physical rate exported to the OS clustering theorem is:

```math
m_{\rm phys}
=
{m_{\rm KP}\over \ell_{\rm blk}}
-\Delta_{\rm tot}.
```

The reducible Paper-13--15 route to `MG-EXP-CLOSE` is open exactly when:

```math
{m_{\rm KP}\over \ell_{\rm blk}}
>
\Delta_{\rm tot}.
```

In the canonical half-margin branch this becomes:

```math
{\mu_{\rm AF}-h_{\rm an}\over 2\ell_{\rm blk}}
>
\Delta_{\rm tot}.
```

The losses have the following required sources:

| Loss | Required source |
| --- | --- |
| `Delta_cut` | cutoff refinement comparison along the Paper-16 common tower |
| `Delta_vol` | finite-volume exhaustion bound for marked two-point polymers |
| `Delta_smear` | Paper-12 smearing/removal and loop-continuity modulus |
| `Delta_block` | block-to-physical-distance conversion, including endpoint collars |
| `Delta_bat` | cofinal probe-battery enlargement and marked-insertion losses |
| `Delta_reg` | regulator/chart/counterterm comparison, including Paper-14 `WP` |
| `Delta_proj` | projective tower and finite-record projection defects |

Every entry must be computed on the same whole-process record law. A loss
may be zero, but it may not be silently omitted.

### Theorem 5.8: Paper-13--15 KP Import Reduces `MG-EXP-CLOSE`

Assume:

1. `CYM_WL` from Paper 16;
2. `MG-WP`;
3. `MG-2PT-KP(G_j,m_KP)` for each battery in a cofinal sequence `G_j`;
4. the amplitudes `A_j(O,P)` are finite for every fixed probe pair and stay
   locally bounded under the cofinal refinement used to approximate that
   pair;
5. the artifact losses in Definition 5.7 are bounded on the cofinal tail;
6. `m_phys>0` in Definition 5.7.

Then `MG-EXP-CLOSE(m_phys)` holds on the declared dense probe family.

Proof.

Lemma 5.5 gives finite-battery exponential clustering at raw rate
`m_raw=m_KP/ell_blk`. Transporting the estimate through cutoff refinement,
volume exhaustion, smearing removal, block conversion, battery enlargement,
regulator/chart comparison, and projective restriction can reduce the rate
only by the explicitly debited losses in Definition 5.7, because `MG-WP`
forces all comparisons to act on the same pushed-forward whole-process
record law. The remaining rate is `m_phys`. The local boundedness of the
amplitudes and the cofinality of the batteries give the limiting estimate on
each centered probe vector. Since `m_phys>0`, the limiting estimate is
exactly `MG-EXP-CLOSE(m_phys)`. `square`

### Definition 5.9: First-Battery Marked KP Certificate `BOX-2PT-KP`

`BOX-2PT-KP` is the specialization of `MG-2PT-KP` to the first
plaquette-clover battery `G_box`. It consists of the following finite data,
all computed for the same pushed-forward block record law:

1. Paper 14 `FBE(s_0,rho,L)` and export package `X_14`;
2. Paper 15 positive `nCPSC(s_0,rho,L)` after enlarging the finite
   generator battery to include the endpoint records in `G_box`;
3. marked connected-cumulant constants
   `A_box`, `mu_box`, `h_box`, `C_cum_box`, and `r_box`;
4. a Paper-15 residual KP weight `m_box` satisfying

   ```math
   0<m_{\rm box}<\mu_{\rm box}-h_{\rm box};
   ```

5. endpoint-collar and marked-insertion constants
   `c_box`, `B_box`, and `lambda_mark_box`, where
   `lambda_mark_box` is zero in the generator-normalized branch and positive
   only if marking the endpoints creates exponential generator growth;
6. a character-tail bound `eta_ch_box`.

The residual smallness test is:

```math
\delta_{\rm box}
=
\mu_{\rm box}-m_{\rm box}-h_{\rm box}
-\lambda_{\rm mark,box}
>0,
```

and

```math
\eta_{\rm res,box}^{\rm bd}
=
C_{\rm cum,box}A_{\rm box}
{e^{-\delta_{\rm box}}\over 1-e^{-\delta_{\rm box}}}
<1.
```

The combined decoration test is:

```math
\eta_{\rm dec,box}^{\rm bd}
=
\eta_{\rm res,box}^{\rm bd}
+\eta_{\rm ch,box}
<1.
```

This certificate is the first concrete target for Paper 17. It is still a
finite-battery statement; its role is to prove a nonzero clustering rate for
the named plaquette-clover records, not yet a full dense-sector mass gap.

### Lemma 5.10: `BOX-2PT-KP` Proves `MG-2PT-KP(G_box,m_box)`

If `BOX-2PT-KP` holds, then `MG-2PT-KP(G_box,m_box)` holds.

Proof.

The first two clauses give the Paper-14 and Paper-15 imports required by
Definition 5.4. The marked connected-cumulant constants extend the Paper-13
criterion to hulls with two endpoint insertions from `G_box`. The inequalities
for `eta_res,box^{bd}` and `eta_dec,box^{bd}` are exactly the Paper-15
residual and combined decoration KP tests after including the endpoint
marking cost. The constants `c_box` and `B_box` record the finite endpoint
collar and amplitude changes. Thus every clause of `MG-2PT-KP(G_box,m_box)`
is satisfied. `square`

### Definition 5.11: First Debited Mass Ledger `BOX-MASS`

The raw physical rate exported by `BOX-2PT-KP` is

```math
m_{\rm raw,box}
=
{m_{\rm box}\over s_0}.
```

Define the first-battery loss ledger:

```math
\begin{aligned}
\Delta_{\rm tot,box}
&=
\Delta_{\rm cut,box}
+\Delta_{\rm vol,box}
+\Delta_{\rm smear,box}
+\Delta_{\rm block,box}\\
&\quad
+\Delta_{\rm bat,box}
+\Delta_{\rm reg,box}
+\Delta_{\rm proj,box}.
\end{aligned}
```

The debited first-battery rate is

```math
m_{\rm phys,box}
=
{m_{\rm box}\over s_0}
-\Delta_{\rm tot,box}.
```

`BOX-MASS` holds when

```math
{m_{\rm box}\over s_0}
>
\Delta_{\rm tot,box}.
```

The canonical half-margin branch sets

```math
m_{\rm box}^{\rm can}
=
{\mu_{\rm box}-h_{\rm box}-\lambda_{\rm mark,box}\over 2}
```

and therefore requires:

```math
{\mu_{\rm box}-h_{\rm box}-\lambda_{\rm mark,box}\over 2s_0}
>
\Delta_{\rm tot,box}.
```

The loss entries mean:

| Loss | First-battery meaning |
| --- | --- |
| `Delta_cut,box` | cutoff refinement loss on plaquette/clover loop records |
| `Delta_vol,box` | finite-volume loss for polymers joining the two endpoint blocks |
| `Delta_smear,box` | Paper-12 smearing/removal loss for the plaquette and clover loops |
| `Delta_block,box` | physical-time to block-distance conversion loss, after endpoint collars |
| `Delta_bat,box` | finite enlargement from Creutz battery to `G_box` endpoint records |
| `Delta_reg,box` | regulator/chart/counterterm loss under Paper-14 `WP` |
| `Delta_proj,box` | projective restriction loss for the finite endpoint product records |

If an entry is controlled by an amplitude-only estimate, it is recorded as
zero in the rate ledger and its finite constant is absorbed into
`A_box(O,P)`. Only estimates that reduce the exponential rate contribute to
`Delta_tot,box`.

### Theorem 5.12: First Plaquette-Clover Battery Clustering

Assume:

1. `CYM_WL`;
2. finite-battery `MG-OBS` for `G_box` from Lemma 2.6;
3. `MG-WP`;
4. `BOX-2PT-KP`;
5. `BOX-MASS`.

Then `MG-EXP-CLOSE(m_phys,box)` holds on the finite battery `G_box`.

Proof.

By Lemma 5.10, `BOX-2PT-KP` gives `MG-2PT-KP(G_box,m_box)`. Lemma 5.5
therefore gives finite-battery clustering at raw rate `m_box/s_0`.
`BOX-MASS` says that this raw rate beats all rate-degrading losses in the
first-battery ledger. Transporting the finite estimate through the same
cutoff, volume, smearing, block, battery, regulator, and projective
comparisons used in Theorem 5.8 leaves the positive rate `m_phys,box`.
Thus the finite-battery version of `MG-EXP-CLOSE(m_phys,box)` holds on
`G_box`. `square`

This theorem is a genuine positive finite-battery reduction, but not yet the
mass-gap theorem. The remaining global task is to repeat the construction on
a cofinal sequence of batteries and prove that the corresponding debited
rates have a positive common lower bound.

### Definition 5.13: Cofinal Marked KP Certificates `G_j-2PT-KP`

For the cofinal battery sequence of Definition 2.7, `G_j-2PT-KP` is the
finite marked two-point certificate obtained by replacing `G_box` in
Definition 5.9 by `G_j`.

It consists of:

1. Paper 14 `FBE(s_0,rho,L_j)` and export package `X_{14,j}` on the block
   graph supporting `G_j`;
2. Paper 15 positive `nCPSC_j(s_0,rho,L_j)` after enlarging the generator
   battery to include all endpoint records in `G_j`;
3. marked connected-cumulant constants
   `A_j`, `mu_j`, `h_j`, `C_cum,j`, and `r_j`;
4. a residual KP weight `m_j` satisfying

   ```math
   0<m_j<\mu_j-h_j-\lambda_{{\rm mark},j};
   ```

5. endpoint collar and marked-insertion constants
   `c_j(O,P)`, `B_j(O,P)`, and `lambda_mark,j`;
6. a character-tail bound `eta_ch,j`.

The residual and decoration tests are:

```math
\delta_j
=
\mu_j-m_j-h_j-\lambda_{{\rm mark},j}
>0,
```

```math
\eta_{{\rm res},j}^{\rm bd}
=
C_{{\rm cum},j}A_j
{e^{-\delta_j}\over 1-e^{-\delta_j}}
<1,
```

and

```math
\eta_{{\rm dec},j}^{\rm bd}
=
\eta_{{\rm res},j}^{\rm bd}+\eta_{{\rm ch},j}
<1.
```

This is a finite certificate for each `j`. It becomes a sector certificate
only after the uniform lower-bound condition of Definition 5.15 is proved.

### Lemma 5.14: `G_j-2PT-KP` Gives Finite-Battery Clustering

Assume `G_j-2PT-KP` holds for a fixed `j`. Let `ell_j` be the physical block
scale used to compare Euclidean time separation with block distance. Then
for every centered `O,P` in `G_j` there is a finite amplitude `A_j(O,P)` such
that

```math
|C_{j,O,P}^{\rm blk}(t)|
\le
A_j(O,P)\exp\!\left[-{m_j\over \ell_j}\,t\right]
```

for all sufficiently large `t`, before the artifact-loss transport.

Proof.

The proof is Lemma 5.5 with `G_box` replaced by `G_j`. The marked
connected-cumulant KP estimate controls every polymer hull joining the two
endpoint supports. The endpoint collar contributes only to the finite
amplitude unless it has been explicitly debited through
`lambda_mark,j`. `square`

### Definition 5.15: Cofinal Debited Mass Ledger And Positive Reserve

For every `j`, define the raw rate

```math
m_{{\rm raw},j}
=
{m_j\over \ell_j}.
```

Define the total rate loss:

```math
\begin{aligned}
\Delta_{{\rm tot},j}
&=
\Delta_{{\rm cut},j}
+\Delta_{{\rm vol},j}
+\Delta_{{\rm smear},j}
+\Delta_{{\rm block},j}\\
&\quad
+\Delta_{{\rm bat},j}
+\Delta_{{\rm reg},j}
+\Delta_{{\rm proj},j}.
\end{aligned}
```

The debited cofinal rate is:

```math
m_{{\rm phys},j}
=
{m_j\over \ell_j}
-\Delta_{{\rm tot},j}.
```

The cofinal positive reserve condition `MG-UNIF(m_*)` holds if there exists
`m_*>0` such that

```math
\inf_j m_{{\rm phys},j}\ge m_*.
```

Equivalently, every finite battery must satisfy the visible reserve

```math
{m_j\over \ell_j}
\ge
m_*+\Delta_{{\rm tot},j}.
```

The canonical half-margin branch sets

```math
m_j^{\rm can}
=
{\mu_j-h_j-\lambda_{{\rm mark},j}\over 2}
```

and therefore requires the uniform inequality:

```math
\inf_j
\left[
{\mu_j-h_j-\lambda_{{\rm mark},j}\over 2\ell_j}
-\Delta_{{\rm tot},j}
\right]
>0.
```

This is the exact place where the finite-battery result can fail to become a
mass-gap theorem: `mu_j` can degrade, entropy `h_j` can grow, endpoint
marking can become too costly, the block scale can drift, or the transport
losses can consume the entire KP rate.

### Definition 5.15A: Constants-Degradation Ledger

The cofinal reserve condition depends on the following constants.

| Constant | Role | Needed behavior | Failure mode |
| --- | --- | --- | --- |
| `mu_j` | marked connected-cumulant decay exported by Paper 13--15 | bounded below after normalization | connected cumulants lose decay on larger batteries |
| `h_j` | block-polymer entropy/lattice-animal growth | bounded above, or grows slower than `mu_j` | larger batteries create too many admissible hulls |
| `lambda_mark,j` | endpoint-marking/generator growth loss | zero in the generator-normalized branch, or uniformly bounded | marked insertions secretly expand into exponentially many records |
| `ell_j` | physical block scale converting block distance to time distance | bounded above on the mass-gap probe sequence | refinement choices dilute block decay into zero physical rate |
| `Delta_cut,j` | cutoff refinement rate loss | tends to zero or is summably bounded | cutoff removal consumes the decay rate |
| `Delta_vol,j` | finite-volume exhaustion rate loss | tends to zero uniformly on local probes | clustering is only finite-volume mixing |
| `Delta_smear,j` | smearing/removal and loop-continuity rate loss | tends to zero or is uniformly reserved | local probe sharpening destroys the rate |
| `Delta_block,j` | block-to-physical conversion and collar loss | amplitude-only or uniformly bounded in rate | endpoint collars grow with separation or battery size |
| `Delta_bat,j` | battery enlargement loss | controlled under cofinal refinement | density requires increasingly costly records |
| `Delta_reg,j` | regulator/chart/counterterm comparison loss | bounded by Paper-14/Paper-16 `WP` ledgers | different charts produce incompatible rates |
| `Delta_proj,j` | projective finite-record restriction loss | tends to zero on the common tower | projection defects accumulate across batteries |

The canonical half-margin route succeeds if the degradation ledger leaves

```math
\inf_j
\left[
{\mu_j-h_j-\lambda_{{\rm mark},j}\over 2\ell_j}
-\Delta_{{\rm tot},j}
\right]
>0.
```

### Lemma 5.15B: Simple Sufficient Uniform Reserve Test

Suppose there are constants `mu_min`, `H_max`, `ell_max`, and `Delta_max`
such that for every `j`,

```math
\mu_j\ge\mu_{\rm min},
```

```math
h_j+\lambda_{{\rm mark},j}\le H_{\rm max},
```

```math
0<\ell_j\le\ell_{\rm max},
```

and

```math
\Delta_{{\rm tot},j}\le\Delta_{\rm max}.
```

If

```math
{\mu_{\rm min}-H_{\rm max}\over 2\ell_{\rm max}}
>
\Delta_{\rm max},
```

then `MG-UNIF(m_*)` holds for any

```math
0<m_*<
{\mu_{\rm min}-H_{\rm max}\over 2\ell_{\rm max}}
-\Delta_{\rm max}.
```

Proof.

The canonical half-margin expression in Definition 5.15 is bounded below by
the displayed positive difference. Choose any strictly smaller positive
`m_*`. `square`

### Theorem 5.16: Steps 1--5 Give Uniform Dense-Sector Clustering Data

Assume:

1. the cofinal battery sequence `G_j` of Definition 2.7;
2. cofinal `MG-OBS` from Theorem 2.8;
3. `G_j-2PT-KP` for every `j`;
4. all losses in Definition 5.15 are computed on the same Paper-16
   whole-process tower;
5. `MG-UNIF(m_*)` holds for some `m_*>0`.

Then every finite battery `G_j` satisfies `MG-EXP-CLOSE(m_*)` with a rate
uniformly bounded below by `m_*`, and the union of the `G_j` spans is dense
in the declared non-vacuum gauge-invariant OS sector.

Proof.

For fixed `j`, Lemma 5.14 gives raw finite-battery clustering at rate
`m_j/ell_j`. The rate transport ledger subtracts at most
`Delta_tot,j`, leaving `m_phys,j`. By `MG-UNIF(m_*)`,
`m_phys,j>=m_*` for every `j`. Thus every finite battery has the same lower
clustering rate `m_*`, though its amplitudes may depend on the chosen
finite probe pair. Theorem 2.8 gives density of the union of the centered
battery spans. `square`

### Theorem 5.17: Cofinal KP Data Prove `MG-EXP-CLOSE(m_*)`

Assume:

1. the hypotheses of Theorem 5.16;
2. `MG-WP`;
3. the cofinal sequence `G_j` is nested as in Definition 2.7;
4. finite linear combinations and products used to approximate a centered
   probe are always contained in some sufficiently large `G_j`.

Then `MG-EXP-CLOSE(m_*)` holds on the dense centered probe family

```math
D_{\rm loop}
=
\bigcup_j {\rm span}_{\mathbb R}(G_j)
\subset {\mathcal H}_{\rm GI}\cap\Omega^\perp .
```

Proof.

Let `O` be a centered probe in `D_loop`. Since the batteries are nested,
there is some `j(O)` with `O` in the real span of `G_{j(O)}`. Theorem 5.16
gives the transported finite-battery clustering estimate on `G_{j(O)}` with
rate at least `m_*`. Finite linearity expands the connected correlator of
`O` into finitely many correlators of generators from that same battery, so
the amplitudes add to a finite constant `A(O)` while the exponential rate
remains `m_*`. The same argument applies to any pair `O,P` after passing to
a common larger battery containing both. `MG-WP` ensures that all estimates
come from one Paper-16 whole-process tower and the same debited loss ledger.
Thus the limiting dense-family clustering statement is exactly
`MG-EXP-CLOSE(m_*)`. `square`

## 6. Reflection Positivity Converts Clustering To A Gap

### Theorem 6.1: Exponential OS Matrix-Element Decay Implies Spectral Support

Let `H>=0` be the OS Hamiltonian on a Hilbert space, and let `psi` be a
vector orthogonal to the vacuum. Suppose there are `A<infinity` and `m>0`
such that

```math
\langle\psi,\exp(-tH)\psi\rangle
\le A\exp(-mt)
```

for all sufficiently large `t`. Then the spectral measure of `psi` has no
support in `[0,m)`.

Proof.

Let `mu_psi` be the spectral measure of `H` for `psi`. Then

```math
\langle\psi,\exp(-tH)\psi\rangle
=
\int \exp(-t\lambda)\,d\mu_\psi(\lambda).
```

Fix `epsilon>0`. If `mu_psi([0,m-epsilon])>0`, then

```math
\int \exp(-t\lambda)\,d\mu_\psi(\lambda)
\ge
\exp\!\bigl(-t(m-\epsilon)\bigr)\,
\mu_\psi([0,m-\epsilon]).
```

Multiplying by `exp(mt)` gives a lower bound growing like
`exp(epsilon t)`, contradicting the assumed upper bound. Hence
`mu_psi([0,m-epsilon])=0` for every `epsilon>0`, so the spectral measure has
no support below `m`. `square`

### Theorem 6.2: Dense Probe Clustering Gives A Gauge-Invariant Mass Gap

Assume:

1. `CYM_WL`;
2. `MG-OBS`;
3. `MG-OS`;
4. `MG-EXP(m,A)` on a dense centered probe family in `Hilb_GI`;
5. the dense probe family is invariant under time translations up to OS
   closure.

Then `MGAP(m)` holds.

Proof.

By `MG-OS`, the time translations define `exp(-t H_OS)` with `H_OS>=0`.
For every centered probe vector `psi` in the dense family, `MG-EXP(m,A)` and
Theorem 6.1 imply that the spectral measure of `psi` has no support in
`[0,m)`.

Let `E([0,m-epsilon])` be the spectral projection of `H_OS`. It annihilates
the dense probe family. Since it is bounded, it annihilates the closure of
that family, namely `Omega^\perp`. Therefore `spec(H_OS|Omega^\perp)` is
contained in `[m,infinity)`. `square`

## 7. Artifact-Removal Gate

### Definition 7.1: Artifact Loss Ledger

Let `m_raw` be the mass scale appearing in a finite or regulated clustering
estimate. Define the artifact-debited mass:

```math
m_{\rm phys}
=
m_{\rm raw}
-\Delta_{\rm cut}
-\Delta_{\rm vol}
-\Delta_{\rm smear}
-\Delta_{\rm block}
-\Delta_{\rm bat}
-\Delta_{\rm reg}
-\Delta_{\rm proj}.
```

The terms are:

1. `Delta_cut`: cutoff refinement loss;
2. `Delta_vol`: finite-volume loss;
3. `Delta_smear`: smearing or local-probe radius loss;
4. `Delta_block`: block-scale conversion loss;
5. `Delta_bat`: finite-battery/density loss;
6. `Delta_reg`: regulator/chart/counterterm comparison loss;
7. `Delta_proj`: projective tower loss.

For the Paper-13--15 connected-polymer route, this generic ledger is the
same as Definition 5.7 with `m_raw=m_KP/ell_blk`. Thus `MG-ART(m_phys)` is
not an additional informal assumption; it is the explicit positivity
condition that the imported KP rate beats the total transport loss.

### Definition 7.2: Artifact Removal `MG-ART`

`MG-ART(m_phys)` holds when:

```math
m_{\rm phys}>0
```

and every artifact loss in Definition 7.1 is either proved to vanish in the
appropriate limit or is bounded by an explicit reserve that leaves
`m_phys>0`.

### Theorem 7.3: Artifact-Debited Clustering Gives Continuum Clustering

Assume finite-tower clustering with raw mass `m_raw`, and assume
`MG-ART(m_phys)`. Then `MG-EXP-CLOSE(m_phys)` holds.

Proof.

Transport the finite estimate through cutoff refinement, volume exhaustion,
smearing removal, block conversion, battery enlargement, regulator/chart
comparison, and projective restriction. Each transport either preserves the
exponential rate or reduces it by the corresponding `Delta` term. The
remaining rate is `m_phys`. Since `m_phys>0`, the final continuum clustering
bound has a positive mass scale. `square`

For Route A, Theorem 5.8 is the non-generic version of this statement: it
states the exact Paper-13--15 hypotheses under which the finite-tower
clustering estimate exists and identifies `m_raw` with `m_KP/ell_blk`.

## 8. Whole-Process Compatibility For Mass Gap

### Definition 8.1: Mass-Gap Whole-Process Ledger `MG-WP`

`MG-WP` holds when:

1. the probe batteries `G_j` are built from the same record tower used in
   Paper 16;
2. all clustering estimates are expectations under the same pushed-forward
   laws `Gamma_i`;
3. all artifact losses are computed from the same comparison maps,
   counterterm branches, loop approximants, and constants ledger;
4. the OS reconstruction uses the same reflection-positive functional
   obtained in Paper 16;
5. no proof composes unrecorded partial kernels as if the process were
   Markovian or divisible.

This is the mass-gap version of `HK-WP-CLOSE`.

## 9. Mass-Gap Closure Certificate

### Definition 9.1: Mass-Gap Closure `MG-CLOSE(m)`

For `m>0`, `MG-CLOSE(m)` holds when:

1. `CYM_WL` holds by Paper 16;
2. `MG-OBS` holds;
3. `MG-OS` holds;
4. `MG-EXP-CLOSE(m)` holds, either directly, by the finite-battery route of
   Theorem 5.8, or by the cofinal route of Theorem 5.17;
5. `MG-ART(m)` holds;
6. `MG-WP` holds.

### Theorem 9.2: `MG-CLOSE(m)` Proves `MGAP(m)`

If `MG-CLOSE(m)` holds, then the declared gauge-invariant OS sector has a
positive spectral gap at least `m`.

Proof.

`CYM_WL` gives the continuum record functional. `MG-OS` gives the OS Hilbert
sector and nonnegative Hamiltonian. `MG-OBS` gives a dense centered family of
gauge-invariant probe vectors. `MG-EXP-CLOSE(m)` gives the continuum
exponential clustering bound on that dense family, after `MG-ART(m)` removes
cutoff, finite-volume, smearing, block, battery, regulator, and projective
artifacts. Theorem 6.2 then gives `MGAP(m)`. `MG-WP` ensures all estimates
refer to one whole-process record law and one declared readout ledger.
`square`

### Theorem 9.3: Cofinal Paper-13--15 Route Proves A Gauge-Invariant Mass Gap

Assume:

1. `CYM_WL`;
2. `MG-OS`, supplied for example by Theorem 3.4 `MG-OS-CLOSE`;
3. `MG-WP`;
4. the cofinal battery hypotheses of Theorem 2.8;
5. `G_j-2PT-KP` for every `j`;
6. `MG-UNIF(m_*)` for some `m_*>0`;
7. the dense probe family is invariant under Euclidean time translations up
   to OS closure.

Then `MGAP(m_*)` holds in the declared gauge-invariant OS sector.

Proof.

Theorem 2.8 gives cofinal `MG-OBS` and density of the centered loop-battery
span in the non-vacuum gauge-invariant OS sector. Theorems 5.16 and 5.17
turn the cofinal marked KP certificates plus `MG-UNIF(m_*)` into
`MG-EXP-CLOSE(m_*)` on that dense centered family. In particular, the
connected Euclidean two-point functions of all dense probe vectors decay
with rate at least `m_*`. `MG-OS`, supplied by Theorem 3.4 when the
Paper-16 continuity data hold, gives the reconstructed nonnegative OS
Hamiltonian. Theorem 6.2 then gives `MGAP(m_*)`. `MG-WP` guarantees that none
of these estimates come from incompatible towers or hidden partial kernel
compositions. `square`

### Corollary 9.4: Cofinal Route Closes `MG-CLOSE`

Under the hypotheses of Theorem 9.3, `MG-CLOSE(m_*)` holds.

Proof.

Theorem 5.17 gives `MG-EXP-CLOSE(m_*)`. The positive reserve in
`MG-UNIF(m_*)` is exactly the cofinal artifact-removal statement
`MG-ART(m_*)`: every cutoff, volume, smearing, block, battery, regulator,
and projective rate loss has already been debited in `Delta_tot,j`, with a
strict positive lower remainder. Together with `CYM_WL`, `MG-OBS`, `MG-OS`,
and `MG-WP`, this is Definition 9.1. `square`

## 10. Routes To `MG-EXP`

Paper 17 has three plausible routes to `MG-EXP`. They are not equivalent.

### Route A: Connected-Polymer Exponential Clustering

Use the connected-polymer/KP technology from Papers 13--15. This is no
longer merely a named hope: Theorem 5.8 reduces `MG-EXP-CLOSE(m_phys)` to
the marked two-point extension `MG-2PT-KP`, the Paper-15 KP smallness tests,
and the explicit artifact inequality `m_KP/ell_blk>Delta_tot`.

The first concrete implementation is Theorem 5.12:

```text
CYM_WL
+ finite-battery MG-OBS for G_box
+ MG-WP
+ BOX-2PT-KP
+ BOX-MASS
=> MG-EXP-CLOSE(m_phys,box) on G_box.
```

The cofinal implementation is Theorem 5.16:

```text
cofinal G_j
+ cofinal MG-OBS
+ G_j-2PT-KP for every j
+ MG-UNIF(m_*)
=> uniform finite-battery clustering at rate m_*
   on a dense gauge-invariant OS probe family.
```

The dense-sector closure is Theorem 5.17, and the direct mass-gap closure is
Theorem 9.3:

```text
CYM_WL
+ MG-OS
+ MG-WP
+ cofinal MG-OBS
+ G_j-2PT-KP for every j
+ MG-UNIF(m_*)
=> MG-EXP-CLOSE(m_*)
=> MGAP(m_*).
```

Required estimate:

```math
|\kappa(O_x,P_y)|
\le
C(O,P)\exp\!\bigl(-m_{\rm poly}\,{\rm dist}(x,y)\bigr).
```

The burden is to show that `m_poly` survives the continuum and artifact
ledgers with positive reserve. In the notation of Theorem 5.8,
`m_poly=m_phys`.

### Route B: Transfer-Matrix Gap At Finite Cutoff Plus Uniform Continuum
Transport

At finite cutoff and finite volume, use the reflection-positive transfer
matrix to estimate a gap in the gauge-invariant sector. Then prove a uniform
lower bound survives:

```math
\begin{aligned}
m_i &\ge m_0-\Delta_i,\\
\Delta_i &\to 0,\\
m_0 &>0.
\end{aligned}
```

This is dangerous unless the finite-volume and cutoff losses are explicit.
A finite-lattice gap alone is not a continuum mass gap.

### Route C: Area-Law/Flux-Tube Input

If Paper 18 later proves a sufficiently strong confinement or area-law
result, it may imply exponential decay for selected gauge-invariant local
probes. That would feed back into `MG-EXP`.

Paper 17 should not assume this route. It may only list it as a possible
import from a later confinement theorem.

## 11. Obstruction Ledger

Paper 17 fails in one of the following typed ways:

1. **No OS sector:** reflection positivity or strong continuity is not enough
   to reconstruct the declared gauge-invariant Hamiltonian sector.
2. **Probe-density failure:** the selected glueball/field-strength proxies
   are not dense in the intended gauge-invariant sector.
3. **Finite-volume artifact:** decay exists only because the spatial volume
   is finite.
4. **Smearing artifact:** the mass scale disappears as the smearing radius or
   probe radius is removed.
5. **Cutoff artifact:** the rate vanishes as `a->0`.
6. **Battery artifact:** the rate holds only on a fixed finite list of
   probes, not on a dense sector.
7. **Regulator/chart artifact:** the rate depends on a nonphysical chart or
   comparison scheme.
8. **No exponential clustering:** connected correlations decay too slowly.
9. **Common-tower failure:** the clustering proof uses a different tower than
   Paper 16's `CYM_WL`.
10. **First-battery-only success:** `G_box` clusters with positive debited
    mass, but the result cannot be extended to a cofinal dense probe family.
11. **Uniform reserve failure:** each finite `G_j` clusters, but
    `inf_j m_phys,j=0`, so no sector-level mass gap follows.

Each obstruction is operational: it is a failure of record laws, record
maps, correlation estimates, or OS reconstruction.

## 11A. Theorem Dependency Map

The final conditional mass-gap route has the following dependency flow:

```text
CYM_WL
-> MG-OS-CLOSE
-> MG-OS
-> cofinal MG-OBS
-> G_j-2PT-KP + MG-UNIF(m_*)
-> MG-EXP-CLOSE(m_*)
-> MGAP(m_*).
```

The corresponding local theorem map is:

| Output | Supplied by | Main inputs |
| --- | --- | --- |
| finite-battery `MG-OBS(G_box)` | Lemma 2.6 | Paper 12 finite loop batteries, Paper 16 `CYM_WL` |
| cofinal `MG-OBS` | Theorem 2.8 | Paper 12 diagonal finite-battery extension, Paper 13 dense loop skeleton, Paper 16 OS norms |
| `MG-OS` | Theorem 3.4 `MG-OS-CLOSE` | reflection positivity, Euclidean covariance, null-space invariance, OS-norm continuity |
| finite-battery clustering on `G_box` | Theorem 5.12 | `BOX-2PT-KP`, `BOX-MASS`, `MG-WP` |
| uniform dense-battery clustering data | Theorem 5.16 | cofinal `G_j`, cofinal `MG-OBS`, `G_j-2PT-KP`, `MG-UNIF(m_*)` |
| dense-family `MG-EXP-CLOSE(m_*)` | Theorem 5.17 | Theorem 5.16, nesting, finite-span containment, `MG-WP` |
| spectral support from clustering | Theorem 6.1 | OS spectral theorem |
| dense probe gap | Theorem 6.2 | dense `MG-EXP`, `MG-OBS`, `MG-OS`, time-translation closure |
| abstract mass-gap closure | Theorem 9.2 | `MG-CLOSE(m)` |
| cofinal Paper-13--15 mass gap | Theorem 9.3 | `CYM_WL`, `MG-OS`, `MG-WP`, Theorem 2.8, `G_j-2PT-KP`, `MG-UNIF(m_*)` |
| cofinal `MG-CLOSE(m_*)` | Corollary 9.4 | Theorem 9.3 and the debited loss ledger |

The unresolved external estimates are exactly:

1. `MG-OS-CLOSE` continuity from the actual Paper-16/Paper-13 loop-continuity
   data;
2. `G_j-2PT-KP` for every cofinal battery;
3. `MG-UNIF(m_*)`, equivalently a positive lower bound on the debited rates.

## 12. Honest Status

Paper 17 is now complete as a conditional mass-gap reduction paper. Its
finished theorem is not an unconditional Clay-level proof; it is the precise
ISP closure:

```text
CYM_WL
+ MG-OBS
+ MG-OS-CLOSE
+ G_j-2PT-KP over a cofinal probe battery
+ MG-UNIF(m_*)
+ MG-WP
=> MG-EXP-CLOSE(m_*)
=> MGAP(m_*).
```

What has been achieved:

1. `MG-OBS` has been reduced to explicit nested Wilson-loop batteries.
2. `MG-OS` has been reduced to reflection positivity, covariance,
   null-space invariance, and OS-norm continuity.
3. `MG-EXP-CLOSE(m)` has been reduced to the Paper-13--15 marked
   connected-polymer route plus a visible cofinal reserve inequality.
4. `MGAP(m_*)` follows once those gates pass.

The remaining actual `4D SU(N)` burden is:

1. prove the OS-norm continuity clause in `MG-OS-CLOSE` from the actual
   Paper-16/Paper-13 data;
2. prove `G_j-2PT-KP` for every battery in the cofinal probe sequence;
3. prove the uniform reserve

```math
\inf_j
\left[
{m_j\over \ell_j}
-\Delta_{{\rm tot},j}
\right]
\ge m_*>0.
```

Until those three estimates are proved on the actual `4D SU(N)` trajectory,
Paper 17 has not proved a mass gap. It has, however, replaced the vague
exponential-clustering gate by a concrete Paper-13--15 reduction with
explicit constants and a final OS spectral-gap theorem.

The first finite-battery target is now fully explicit:

```text
G_box := centered plaquette/clover scalar loop records and degree-two
products in one block collar.

BOX-2PT-KP + BOX-MASS
=> MG-EXP-CLOSE(m_phys,box) on G_box.
```

This would be a real positive finite-battery clustering result. It would not
yet be a Yang-Mills mass gap until the same construction is extended to a
cofinal dense battery with a positive common lower rate.

The cofinal extension is now formulated as:

```text
G_j-2PT-KP for all j
+ MG-UNIF(m_*)
=> MG-EXP-CLOSE(m_*)
=> MGAP(m_*).
```

The remaining proof burden is no longer vague: control the growth of
`h_j`, `lambda_mark,j`, `Delta_tot,j`, and the block scales `ell_j` so that
the infimum of the debited rates stays strictly positive.
