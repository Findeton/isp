# Relativistic ISP v10 Paper 11: Many Clocks, Few Factors Is an Exact Kinematic Bridge, Not Yet a Derivation of `3+1`

## Complex rank-two positivity, finite celestial approximants, relational SCIR frames, and the surviving selection/boost/influence gaps

**Status:** round-1 hostile-review repairs complete; awaiting round-2 closure,
2026-07-11. Protocol, verdict classes, comparison algebras, and
anti-circularity gates were frozen before D10 executables, numerical outcomes,
literature search, or hostile review. The pre-review artifact hashes remain in
`v10/data/d10-pre-review-receipt.md`; every repair is itemized in
`v10/note-d10-round1-opening-repairs.md`.

### Reproducibility package

- `v10/note-d10-bloch-celestial-selection-protocol.md` — frozen protocol;
- `v10/code/d10_bloch_lorentz_exact.py` — 109 frozen exact checks;
- `v10/code/d10_finite_clock_convergence.py` — 99 frozen checks at 90-decimal
  working precision plus an independent 120,000-direction probe;
- `v10/code/d10_relational_scir_packet.py` — 43 frozen exact/finite-packet checks and a
  deterministic finite-depth coverage diagnostic;
- `v10/note-d10-literature-audit-bloch-celestial.md` — post-freeze audit;
- `v10/note-d10-bloch-celestial-investigation.md` — full result ledger;
- `v10/data/d10-pre-review-receipt.md` — frozen submitted commands, outputs,
  hashes, and claim boundary; the final receipt is issued only after review
  closure.

## Abstract

V9 replaced a fixed count of independent record clocks with a directional
channel manifold. In four-dimensional Minkowski space the causal order is the
intersection of null-clock inequalities indexed by the celestial `S^2`; finite
direction sets give polyhedral cones, while the continuum gives the round
Lorentz cone. V10's SCIR rulebook subsequently supplied a finite local quantum
instrument grammar but did not identify its type/coupling packet. This paper
tests whether the two constructions meet at the minimal complex quantum factor.

They do meet exactly at the kinematic level. The ordered space of `2 x 2`
complex Hermitian matrices has the expansion `X=tI+x.sigma`, determinant
`t^2-|x|^2`, positive cone `t>=|x|`, and normalized rank-one boundary
`CP^1=S^2`. Every directional clock-shadow evaluation is the positive
functional `Tr(P_u X)=t+u.x`, so arbitrarily many directional evaluations
depend on four real factors. A 109-check exact receipt
verifies this identification, its local `SU(2)` gauge behavior, diamond
holonomy, comparison-algebra dimensions, local-tomography counts, and an exact
`SL(2,C)` boost. A 90-decimal spherical-Voronoi calculation quantifies finite
outer-cone errors. A bounded `H/T/SEAL` SCIR candidate generates 113 exact
projective directions by word depth 12 without an external sphere sampler in
the generator; external Fibonacci spheres remain explicit coverage
diagnostics. Finite alphabet/depth does not by itself prove a per-record
evidence or exact-description capacity bound.

The bridge does not derive physical `3+1`. Real, complex, quaternionic, and
generic spin factors produce Lorentz cones in different dimensions. The
existing sealed-record arena does not select the complex factor; normalized
qubit states remove the temporal scale; the candidate Bloch increment is
declared; `SU(2)` supplies rotations but boosts require nonunitary `SL(2,C)`
congruences; and the directional order cone is not yet tied to the propagation
of marked influence. The predeclared verdict is therefore
`KINEMATICS-ONLY`. D9's failed one-coupling identification is replaced by a
sharper viable hypothesis: a shared operational channel algebra with distinct
dynamical couplings.

## 1. Question and inherited boundary

The V9 construction established

\[
M^{1,3}\text{ causality}
=\bigcap_{u\in S^2}\{\Delta t-u\cdot\Delta x\ge0\}.
\]

Its growth studies showed why independent finite clocks remain polyhedral and
why directionally correlated clocks can approach the round reference. The
slogan was:

> many clocks, few factors.

The open question was the origin of the `S^2`. V9 inserted directions in an
already defined sphere. SCIR later introduced finite typed Hilbert collars and
local instruments, but its type and coupling table remained primitive physics.

D10 tests the candidate identification

\[
S^2_{\rm celestial}\stackrel{?}{=}S^2_{\rm qubit\ projective}.
\]

The equality of manifolds is not treated as physical identity by inspection.
The frozen protocol separates algebra, approximation, selection,
identification, and dynamics.

## 2. Exact rank-two theorem

### Theorem 2.1 — complex rank-two positivity is the `3+1` Lorentz cone

Every complex Hermitian `2 x 2` matrix has a unique real expansion

\[
X=tI+\sum_{j=1}^3x_j\sigma_j.
\]

Its eigenvalues are `t+|x|` and `t-|x|`. Consequently,

\[
X\succeq0\iff t\ge|x|,
\qquad
\det X=t^2-|x|^2.
\]

#### Proof

The Pauli anticommutator is

\[
\{\sigma_i,\sigma_j\}=2\delta_{ij}I,
\]

so `(x.sigma)^2=|x|^2I`. Its eigenvalues are `+|x|` and `-|x|`, yielding the
stated eigenvalues after adding `tI`. Their product is the determinant and their
nonnegativity is equivalent to `t>=|x|`. `□`

### Theorem 2.2 — the null directions are the Bloch sphere

For every unit vector `u in S^2`,

\[
P_u={I+u\cdot\sigma\over2}
\]

is a normalized rank-one projector. Every normalized rank-one projector has
this form. Thus the normalized null rays form

\[
\mathbb{CP}^1\simeq S^2.
\]

Moreover,

\[
\operatorname{Tr}(P_uX)=t+u\cdot x.
\]

#### Proof

The Pauli identity gives `(u.sigma)^2=I`, hence `P_u^2=P_u`, `Tr P_u=1`,
and `det P_u=0`. Conversely every trace-one Hermitian matrix has the Bloch
form `(I+r.sigma)/2`; rank one forces `|r|=1`. The evaluation follows from
`Tr sigma_i=0` and `Tr(sigma_i sigma_j)=2 delta_ij`. `□`

### Corollary 2.3 — many clocks, four factors

For any number `K` of directional projectors, the vector

\[
(\operatorname{Tr}P_{u_1}X,\ldots,\operatorname{Tr}P_{u_K}X)
\]

is a linear image of the four coefficients `(t,x1,x2,x3)`. Increasing `K`
refines angular interrogation but does not add latent dimension.

The written proof establishes the universal theorem. The exact receipt verifies
its generating identities and representative rational/`Q(sqrt(2),i)`
witnesses. No floating comparison is load-bearing.

## 3. Finite celestial shadows

For a finite direction family `U`, define

\[
C_U=\{(t,x):t\ge h_U(x)\},
\qquad
h_U(x)=\max_{u\in U}u\cdot x.
\]

Since `h_U(x)<=|x|`, `C_U` is an outer polyhedral approximation of the Lorentz
cone. Its worst unit-direction support is

\[
m(U)=\min_{|x|=1}h_U(x),
\]

and its worst radial excess is `m(U)^(-1)-1`.

D10 enumerates the spherical Voronoi vertices determined by all non-collinear
direction triples at 90-decimal precision. A deterministic 120,000-point
Fibonacci sphere independently approaches every returned minimum.

| `U` | `K` | `m(U)` | radial excess |
|---|---:|---:|---:|
| tetrahedron | 4 | 0.333333333333333333 | 2.000000 |
| octahedron | 6 | 0.577350269189625765 | 0.732051 |
| cube | 8 | 0.577350269189625765 | 0.732051 |
| icosahedron | 12 | 0.794654472291766123 | 0.258409 |
| dodecahedron | 20 | 0.794654472291766123 | 0.258409 |
| dual union | 32 | 0.842128148500700271 | 0.187468 |

The tetrahedral and octahedral controls reproduce exactly `1/3` and
`1/sqrt(3)`. The repaired receipt also verifies that every tested set spans
three dimensions and has the origin in its convex-hull interior. Thus the
minimum is the centered inradius: a closest supporting facet contains an
affinely independent triple whose normal is enumerated. Extra triple normals
are harmless sphere points.

### Lemma 3.1 — dense nested directions converge

If finite sets `U_n` are nested and their union is dense in compact `S^2`, then
their covering radii tend to zero and `m(U_n)->1`.

#### Proof

For any `epsilon>0`, compactness gives a finite `epsilon`-net chosen from the
dense union. Nesting places that entire finite net inside some `U_N`; every
later `U_n` is at least as fine. Hence the covering radius is eventually at
most `epsilon`. Taking `epsilon->0` gives the claim. `□`

For the positive `H/T` word family, applying this lemma is conditional on the
imported Clifford+T density theorem; inverses introduce no new alphabet because
`H^-1=H` and `T^-1=T^7`. The finite receipts alone do not prove the limit.

This calculation and V9's `F` calculation answer different questions. `F` can
be close to its round-cloud reference while a small worst-case angular hole
remains. The exact round cone requires a dense continuum limit, not merely a
finite shape score below a protocol line.

## 4. Why the cone does not select four dimensions

### Proposition 4.1 — rank-two alternatives

For a real normed division algebra `F` of real dimension `q`, the rank-two
Hermitian ordered space has `q+2` real dimensions and the spin-factor form

\[
\mathbb R\oplus\mathbb R^{q+1}.
\]

The cases `F=R,C,H,O` therefore give the Lorentz dimensions

```text
1+2, 1+3, 1+5, 1+9.
```

Generic spin factors `R + R^n` supply `1+n` Lorentz cones for arbitrary `n`.
Thus Lorentz-cone positivity alone cannot select `n=3`. `□`

### Proposition 4.2 — local tomography is external to the present records

Real symmetric and complex Hermitian state-parameter counts give

```text
real two-level:    K_A=3, K_AB=10, deficit +1;
complex two-level: K_A=4, K_AB=16, deficit 0.
```

Local tomography distinguishes these composite rules. Reconstruction results
in the literature use it, with further Jordan/composition assumptions and an
existing qubit, to select complex quantum theory.

V8 Paper 2 established that the current sealed degree-`(1,1)` record moments
are invariant under its complex-to-real comparison while the deficit changes.
The selecting datum is not a functional of the audited record data. D10
reproduces the counts but finds no new record-internal selector.

Consequently the implication

\[
\text{sealed records}\Longrightarrow Herm_2(\mathbb C)
\]

is unavailable under the present axioms.

## 5. Finite local generation without an `S^2` oracle

D10's conditional packet uses one complex qubit collar and the finite local
opportunity types

```text
APPLY_H, APPLY_T, SEAL.
```

All finite-depth states lie exactly in `Q(sqrt(2),i)`. Projectors rather than
state vectors remove global phase. The reachable set is nested and finite at
every depth:

| depth | projectors | sampled support |
|---:|---:|---:|
| 0 | 1 | -0.999980 |
| 2 | 3 | -0.675960 |
| 4 | 8 | 0.005515 |
| 6 | 19 | 0.680940 |
| 8 | 35 | 0.683787 |
| 10 | 64 | 0.865446 |
| 12 | 113 | 0.914143 |

This demonstrates finite-alphabet, finite-depth projector refinement. The
alphabet and local Hilbert dimension stay fixed while words become longer.
It does not prove a bound on exact amplitude-description length, accumulated
provenance, evidence/KL content, or total collar storage. Those capacity
notions remain separate. The synthesis literature supplies the broader
universality context.

The `SEAL` token is now an executed complete projective pointer instrument:
on the `H|0>` state it gives exact Born weights `1/2,1/2`, normalized branches,
and durable repeated outcomes. In the imported complex tensor model, two
disjoint instruments are actually composed in both schedules and agree; an
overlapping control differs by order. These are finite chosen-packet tests,
not a general derivation of SCIR locality or composition.

The packet does not explain why nature chooses the complex qubit or this gate
alphabet. It is an existence construction inside SCIR's declared finite packet
freedom.

## 6. Relational rotations on a supplied connection

Let each record have its own local basis and each incident link carry a
relative unitary `U_ba`. Under local basis changes,

\[
U_{ba}\mapsto V_bU_{ba}V_a^\dagger.
\]

Path transports along a diamond transform only at their endpoints. A based
loop transforms by conjugation, so its trace and spectrum are connection-gauge
invariants. D10 verifies these identities exactly with vertex-local basis
changes. Disjoint local changes commute in the chosen imported complex tensor
model.

This supplies covariance after a relative `SU(2)` connection is given. It does
not derive link birth, values, ownership, calibration, transport instruments,
or a physical holonomy seal. No preferred basis is required after the
connection is supplied; stronger global-frame claims are not made.

## 7. Why `SU(2)` is not yet Lorentz covariance

The determinant-preserving action on Hermitian events is

\[
X\mapsto AXA^\dagger,
\qquad A\in SL(2,\mathbb C).
\]

For `A in SU(2)`, trace is preserved and the action is a spatial rotation. The
group `SL(2,C)` is the two-to-one cover of the proper orthochronous Lorentz
group with kernel `{+I,-I}`, while `PSL(2,C)` is isomorphic to
`SO^+(1,3)`; general `A` includes boosts. The exact receipt uses

\[
A=\begin{pmatrix}2&0\\0&1/2\end{pmatrix}
\]

to verify determinant preservation and the exact `t-z` boost coefficients. It
also verifies `A^dagger A != I` and trace change.

This creates a physical distinction. On an unnormalized event cone the action
is a frame change. On normalized quantum states the same matrix is a
nonunitary filter and changes outcome weights before renormalization. SCIR has
Kraus instruments, but no theorem makes all such filters gauge. A full
Bloch–celestial theory needs a consistent `SL(2,C)` event/effect gauge and Born
weight law, not only local `SU(2)` rotations.

## 8. Time is not contained in a normalized qubit

The state `rho=(I+r.sigma)/2` has fixed trace. It occupies a three-dimensional
slice of the four-dimensional cone. The temporal factor `t` reappears only for
unnormalized positive matrices or after adjoining another scalar.

Possible constructions include an unnormalized branch weight, a local click
interval, an accumulated ancestry coordinate, or another positive collar
observable. None is forced by the rank-two theorem.

D10 tests the declared shadow

\[
\Delta t=1,\qquad\Delta x=r,
\]

for pure Bloch direction `r`. Parent edges are exactly null. In a separate
bounded-forest test, a local source intervention changes exactly its copied
descendants' sealed-mark continuation probabilities and leaves the other
branch and disconnected component unchanged. But
the map from internal Bloch direction to spatial displacement is packet data,
not a consequence of sealing.

The relative scale between the two increments is also undeclared. D10
therefore sets neither physical metres/seconds nor `c` nor Newton's `G`.

## 9. Order and influence remain different observables

Directional inequalities define an order cone. A marked-intervention test
defines an influence cone by comparing continuation measures. These need not
coincide.

The chosen bounded-forest packet proves an interventional continuation result
for its copied classical mark. Joining sectors remain untested. It does not
prove that the support
of this change, expressed in accumulated Bloch coordinates, approaches the
directional Lorentz cone. The missing equality is dynamical and empirical, not
an algebra identity.

This gap blocks the interpretation of the cone as the signal cone seen by
emergent excitations.

## 10. Profinite histories do not become a connected sphere

The D3 history carrier is an inverse limit of compatible finite history
truncations. Such a profinite space is totally disconnected. The connected
channel manifold `S^2` cannot literally be that inverse limit.

In the conditional D10 construction, `S^2` is instead the pure projective state
space of a finite algebra. Individual histories visit finite subsets; finite
direction nets can converge to the sphere in a metric sense. Profinite history
extension, projective state-space reconstruction, and metric net convergence
are distinct operations.

## 11. Relation to D9

D9 falsified one raw-parameter identity: the partial-iSWAP strength that makes
a Bell pair did not make the V9 diffusion shadow geometrically acceptable.
D10 does not revive that equality.

It replaces it with a different hypothesis:

> quantum correlations and causal geometry may share the same local
> operational projective manifold while their instruments have different
> couplings and coarse-grained roles.

The exact rank-two bridge makes this hypothesis mathematically economical.
The selection, boost, time-scale, and influence gaps keep it conditional.

## 12. Verdict

The frozen layer results are

```text
A conditional complex-qubit algebra      PASS
B finite outer directional approximation PASS
B infinite generated convergence         CONDITIONAL on imported density
C unique complex rank-two selection      FAIL under present record axioms
D physical Bloch/celestial identity       DECLARED CANDIDATE
E finite-depth direction generation       PASS; record capacity open
E chosen seal/schedule/forest tests       PASS at finite declared scope
E physical link birth/holonomy seal       OPEN
E full Lorentz gauge                      OPEN
E order/spacetime-influence equivalence   OPEN
```

Therefore

```text
CONDITIONAL-COMPLEX-QUBIT/LORENTZ-CONE-ISOMORPHISM
+ FOUR-FACTOR-DIRECTIONAL-POSITIVE-EVALUATIONS
+ FINITE-OUTER-CONE-APPROXIMATIONS
+ FINITE-ALPHABET/FINITE-DEPTH-PROJECTOR-REFINEMENT
+ CHOSEN-PACKET-SEAL/SCHEDULE/FOREST-INTERVENTION-TESTS
+ SUPPLIED-SU2-CONNECTION-GAUGE-COVARIANCE
- COMPLEX/LOCAL-TOMOGRAPHY-SELECTION-NOT-DERIVED
- NORMALIZED-QUBIT-TIME/SCALE-MAP-NOT-DERIVED
- PHYSICAL-LINK/SEAL/CAPACITY-NOT-DERIVED
- FULL-SL2C-BORN-GAUGE-OPEN
- JOINING/ORDER/SPACETIME-INFLUENCE-LINK-OPEN
= KINEMATICS-ONLY
```

This is not a negative result about relevance. It identifies the qubit
rank-two algebra as the sharpest known meeting point of SHARD's quantum records
and V9's celestial clocks. It also specifies exactly why that meeting point is
not yet a derivation of the observed spacetime.

## 13. Claim boundary and next falsifier

This paper does not claim:

- originality of the qubit–Lorentz correspondence;
- derivation of the complex numbers or local tomography;
- that a Bloch sphere is physical space by diffeomorphism alone;
- a literal profinite construction of `S^2`;
- full Lorentz covariance from `SU(2)`;
- a per-record evidence or exact-description capacity theorem from finite
  Hilbert dimension;
- derivation of link birth, ownership, calibration, or a physical holonomy
  seal from supplied connection covariance;
- equality of order and influence cones;
- Einstein dynamics, an absolute metric, or Newton's `G`.

The next decisive receipt should not be another shape-only run. It must define
an unnormalized `SL(2,C)`-covariant SCIR event/effect packet, freeze how Born
weights transform, and compare its marked influence front with its directional
order cone. If that cannot be done without treating a physical filter as gauge
or importing a global time scale, the Bloch–celestial identification fails as
spacetime dynamics even though its kinematic theorem remains exact.

## 14. Round-1 hostile review and repair record

Three independent reviewers—mathematics, ontology/locality/gauge, and a
clean-room rebuild—reproduced the core theorem, all six finite-cone support
minima, the full projector-count sequence
`1,2,3,5,8,13,19,26,35,48,64,85,113`, and the boost calculation. All three
returned `MAJOR REVISION` because the pre-review package omitted its registered
comparison-determinant gate and overgraded its capacity, sealing,
construction-order, influence, and supplied-connection tests.

The repair is auditable rather than silent:

- pre-review hashes and outputs remain in `d10-pre-review-receipt.md`;
- the three reviews remain unchanged in `v10/reviews/`;
- `note-d10-round1-opening-repairs.md` maps every opening to a disposition;
- executable counts are now frozen at `109`, `99`, and `43`;
- normal/optimized stdout hashes are gated;
- missing rank-two determinant forms, hull hypotheses, a real seal instrument,
  executed schedule comparison, overlapping control, and finite forest
  intervention were added;
- every stronger physical label was downgraded as shown in the verdict.

The hostile correction does not weaken the primary conclusion. It makes its
scope exact: the result is a conditional ordered-space isomorphism plus finite
candidate tests, not yet a selected or dynamically wired spacetime law.

## References

1. P. Arrighi and C. Patricot, *A Note on the correspondence between Qubit
   Quantum Operations and Special Relativity*, arXiv:quant-ph/0212135.
2. H. Barnum and A. Wilce, *Local tomography and the Jordan structure of
   quantum theory*, arXiv:1202.4513.
3. G. Niestegge, *Local tomography and the role of the complex numbers in
   quantum mechanics*, arXiv:2001.11421.
4. H. Barnum, M. Graydon, and A. Wilce, *Composites and Categories of Euclidean
   Jordan Algebras*, arXiv:1606.09331.
5. V. Kliuchnikov, D. Maslov, and M. Mosca, *Fast and efficient exact synthesis
   of single qubit unitaries generated by Clifford and T gates*,
   arXiv:1206.5236.
6. M.-O. Renou et al., *Quantum theory based on real numbers can be
   experimentally falsified*, Nature 600, 625–629 (2021).
7. T. Hoffreumon and M. P. Woods, *Quantum theory based on real numbers cannot
   be experimentally falsified*, arXiv:2603.19208 (2026 preprint).
8. Relativistic ISP v8 Paper 2; v9 notes `round-cone-mechanisms` and
   `3p1-manifoldweb`; v10 Papers 9–10.
