# D10 — can SCIR select the Bloch–celestial `S^2` and `3+1`?

**Status:** round-1 hostile-review repairs complete; awaiting round-2 closure,
2026-07-11. The pre-review version is hash-frozen in
`v10/data/d10-pre-review-receipt.md`; repairs are enumerated in
`v10/note-d10-round1-opening-repairs.md`.

## 1. Result in one paragraph

The v9 slogan **many clocks, few factors** has an exact and unusually natural
conditional ordered-space realization: every `2 x 2` complex Hermitian object has four real factors
`(t,x1,x2,x3)`, while its rank-one directional questions form `CP^1 = S^2`;
positivity is exactly the round future cone `t >= |x|`. Finite directional
families give outer polyhedral approximations, and a finite `H/T/SEAL` grammar
can generate increasingly dense projective directions without storing
infinitely many numbers or sampling an external sphere. But the investigation
does **not** derive `3+1`. Existing SHARD record observables do not select the
complex rank-two factor over real, quaternionic, or generic spin factors; a
normalized qubit does not itself supply the unbounded temporal scale used by
the cone; the Bloch-to-spatial-increment map remains declared; `SU(2)` frame
gauge supplies rotations but not boosts; and the order cone has not been shown
to equal the dynamical influence cone. The frozen primary verdict is therefore
`KINEMATICS-ONLY`, with a strong conditional SCIR candidate retained.

## 2. The exact identity

Let

\[
X=tI+x_1\sigma_x+x_2\sigma_y+x_3\sigma_z.
\]

Then

\[
\operatorname{tr}X=2t,
\qquad
\det X=t^2-|x|^2,
\qquad
\lambda_\pm=t\pm |x|.
\]

Therefore

\[
X\succeq0 \quad\Longleftrightarrow\quad t\ge |x|.
\]

The normalized rank-one boundary elements are

\[
P_u={I+u\cdot\sigma\over2},\qquad u\in S^2,
\]

and

\[
\operatorname{tr}(P_uX)=t+u\cdot x.
\]

Changing `u -> -u` gives the v9 clock-shadow convention `t-u.x`. Thus one
four-factor object answers a continuum of directional positive-functional
questions. These are not operational clocks until a click/time/unit map is
supplied, and they are not independent stored scalars.

The repaired exact receipt passes **109/109** frozen checks under rational or
`Q(sqrt(2),i)` arithmetic. It includes Pauli algebra, null projectors,
directional evaluations, comparison-class determinant forms, supplied-link
gauge diamonds, and an exact `SL(2,C)` boost. The displayed proof supplies the
universal theorem; the executable supplies exact generating identities and
representative witnesses.

## 3. Why this is precisely “many clocks, few factors”

For any finite direction set `U_K={u_1,...,u_K}`, define

\[
q_k(X)=\operatorname{tr}(P_{u_k}X)=t+u_k\cdot x.
\]

There may be hundreds of readings, but their data matrix has at most four
latent columns: the constant/trace factor and three Pauli factors. Increasing
`K` increases directional resolution without increasing the dimension of
`X`.

This resolves only the objection that one record must store infinitely many
independent clock scalars. A finite-dimensional state and finite instrument
alphabet can define many correlated questions. It does **not** establish a
per-record bound on exact state description, provenance, or evidence/KL
content. `S^2` is the continuum of possible projective questions admitted by
the algebra, not an infinite list of independent classical readings inside one
record; the remaining capacity notions stay open.

## 4. Finite clock-shadow cones and the meaning of “rounder”

The finite clock cone is

\[
C_U=\{(t,x):t\ge\max_{u\in U}u\cdot x\}.
\]

It contains the round cone because finitely many inequalities miss directions.
For unit `x`, let

\[
m(U)=\min_{|x|=1}\max_{u\in U}u\cdot x.
\]

The worst radial excess of the finite cone is

\[
R(U)={1\over m(U)}-1.
\]

The 90-decimal receipt enumerates all spherical Voronoi triple candidates and
independently checks them with 120,000 deterministic probe directions. It
passes **99/99** frozen checks, including three-dimensional span and
origin-interiority hypotheses. The closest origin-centered supporting facet
contains an affinely independent triple, proving completeness of the
triple-normal enumeration on these sets.

| direction set | `K` | support `m(U)` | worst radial excess |
|---|---:|---:|---:|
| tetrahedral | 4 | 0.333333333333333333 | 200.00% |
| octahedral | 6 | 0.577350269189625765 | 73.21% |
| cubic | 8 | 0.577350269189625765 | 73.21% |
| icosahedral | 12 | 0.794654472291766123 | 25.84% |
| dodecahedral | 20 | 0.794654472291766123 | 25.84% |
| dual icosa+dodeca | 32 | 0.842128148500700271 | 18.75% |

A separately nested family improves from 200% at `K=4` to 15.81% at `K=26`.
Adding directions never worsens the support error.

This sharpens v9's numerical result. V9 found that its occupancy statistic `F`
looked close to the round reference by roughly `K=12–16`. D10's worst-direction
metric says a 12-direction cone can still have a 25.8% extremal radial gap.
There is no contradiction: `F` is an average cloud-shape statistic, whereas
`R(U)` deliberately finds the largest unsampled angular hole. “Looks round” at
finite resolution is weaker than “is the exact round cone.”

## 5. The anti-selection theorem

The cone identity is not unique to complex qubits. Rank-two Hermitian algebras
over the real division algebras have ordered-space dimensions

```text
Herm_2(R): 3 real factors -> 1+2 Lorentz cone;
Herm_2(C): 4 real factors -> 1+3 Lorentz cone;
Herm_2(H): 6 real factors -> 1+5 Lorentz cone;
Herm_2(O): 10-factor rank-two spin shadow -> 1+9 Lorentz cone.
```

More generally, every spin factor `R + R^n` has positivity cone

\[
t\ge |x|,\qquad x\in\mathbb R^n.
\]

Hence “local state space is a Lorentz cone” leaves `n` arbitrary. It does not
select `n=3`.

The most promising selector is local tomography. Parameter counting gives

```text
rebit:  K_A=3, K_AB=10, 10-3*3=+1;
qubit:  K_A=4, K_AB=16, 16-4*4=0.
```

But v8 Paper 2 already proved that, in the record arena it audited, the sealed
moment data are field-blind while this deficit changes. The complex-over-real
choice lies outside the information committed by those records. D10 finds no
new SHARD principle that closes that wall.

Reconstruction theorems can recover complex quantum theory from Jordan
systems, local tomography, suitable composition, and an existing qubit. Those
are valid conditional theorems. They do not show that sealing or diamonds
derive local tomography or the qubit.

### Selection-gate ledger

| proposed selector | D10 status | reason |
|---|---|---|
| Born rule | counterexample | real Hilbert/Jordan models also have squared-norm Born instruments |
| Bell/CHSH | counterexample | the D9 real-plane Bell packet does not require the missing `Y` direction |
| local tomography | conditional selector | selects complex structure in stated reconstruction classes, but is not derived by records |
| sealed holonomy phase | current-arena no-go | v8 showed shared seals do not force an out-of-real-plane phase |
| diamonds | insufficient | constrain composition/path comparison after link data exist; do not select the scalar field |
| finite grammar | insufficient | finite universal grammars exist once a local algebra is chosen |
| homogeneity/self-duality | insufficient | leads to the Jordan family, not uniquely `Herm_2(C)` |

The selection layer therefore fails at the current axiom set.

## 6. A local SCIR candidate without an external sphere oracle in generation

D10 constructed a bounded finite packet:

```text
local collar: one complex qubit;
continuation tokens: APPLY_H, APPLY_T;
terminal token: SEAL;
link data: relative frame transport;
state update: local unitary/Kraus instrument;
directional record: a rank-one projector generated by the local word.
```

`H` and `T` have entries in `Q(sqrt(2),i)`. Starting from one projector, finite
words generate the following exact finite direction families:

| maximum word depth | distinct projectors | sampled support minimum |
|---:|---:|---:|
| 0 | 1 | -0.99998 |
| 2 | 3 | -0.67596 |
| 4 | 8 | 0.00552 |
| 6 | 19 | 0.68094 |
| 8 | 35 | 0.68379 |
| 10 | 64 | 0.86545 |
| 12 | 113 | 0.91414 |

The repaired packet receipt passes **43/43** frozen checks. The depth-12
Fibonacci diagnostic samples support `0.914143429015`; an independent hostile
convex-hull rebuild gives the true finite-set support
`0.912486956834076`, or 9.5906% radial excess. No random `S^2` direction is
supplied to the rewrite law; the external sphere is present only in the
coverage diagnostic. This is a real
answer to one v9 opening: a finite local rulebook can expose more and more
channel directions without enlarging the gate alphabet or local Hilbert
dimension. That statement is weaker than a proved SHARD evidence-capacity
bound.

It is not a selection or record-capacity theorem. The `H/T` alphabet and
complex qubit are primitive packet data; finite alphabet and finite depth do
not bound exact amplitude-description length, accumulated provenance, or
per-record evidence. Those capacity metrics remain open.

## 7. Relational frames and diamond holonomy

Give each record its own qubit frame. A link from `a` to `b` carries `U_ba`.
Under independent frame changes,

\[
U_{ba}\mapsto V_bU_{ba}V_a^\dagger.
\]

Along a diamond, each path transforms only at its endpoints; the closed loop
transforms by conjugation. Its trace and spectrum are gauge invariant. D10
verifies these statements exactly. Disjoint local frame changes commute.

This establishes covariance of a **supplied** relational `SU(2)` rotation
connection. It does not derive link birth, ownership, calibration, or a
physical holonomy seal, and it does not assume that a computer updates a
global spatial frame.

## 8. The boost opening

Spatial rotations correspond to `SU(2)` conjugation. Proper orthochronous Lorentz
transformations require

\[
X\mapsto AXA^\dagger,\qquad A\in SL(2,\mathbb C).
\]

D10's rational diagonal example passes the determinant test exactly and gives
the expected `t-z` boost. But it also proves

```text
A is not unitary;
Tr(AXA†) is not generally Tr(X).
```

For the Hermitian event cone this is a coordinate-frame transformation. For a
normalized quantum state the same matrix looks like a nonunitary filter whose
branch probability changes. SCIR currently has a clean unitary local-frame
gauge, but no derived rule identifying nonunitary filters with harmless changes
of spacetime frame.

Therefore `SU(2)` covariance cannot be advertised as Lorentz covariance. The
missing structure is an `SL(2,C)`-covariant unnormalized event/effect calculus
whose Born weights and sealing remain gauge-consistent.

## 9. The normalization/time opening

The Lorentz cone consists of **unnormalized** positive matrices. A normalized
qubit has `Tr rho=1`, fixing `t=1/2`; it occupies one Bloch-ball slice rather
than spacetime.

To obtain an event displacement, SCIR must choose one of the following:

1. use an unnormalized branch weight as the temporal factor;
2. pair the normalized qubit with an independent local click interval;
3. accumulate Bloch-direction increments along record ancestry;
4. construct `X` from another positive collar observable.

D10's candidate uses option 3 in its simplest form:

\[
\Delta t=1,\qquad \Delta x=r,qquad |r|=1.
\]

Every parent edge is then null. This is local and exact, but it is explicitly a
declared shadow map. The click law does not force a Bloch vector to be spatial
displacement, nor does it fix the relative units of `Delta t` and `Delta x`.

This is also why D10 does not set metres, seconds, `c`, or Newton's `G`.

## 10. Order cone versus influence cone

Within the chosen complex-tensor packet, the repaired test actually composes
two disjoint instruments in both schedules and obtains the same normalized
state; an overlapping control differs by order. A local Bernoulli-source
intervention changes exactly the downstream sealed-mark continuation
probabilities on a bounded copied-mark forest and leaves the other branch and
disconnected component unchanged. This is a finite packet test, not a general
SCIR theorem; joining sectors are untested.

But two distinct objects remain:

- **order cone:** pairs passing all directional inequalities;
- **influence cone:** locations where changing a local instrument changes the
  distribution of later sealed records.

D10 has not proved equality, containment, or a scaling relation between them.
The finite forest law gives a bounded interventional influence support; the Bloch clock-shadow cone
is a declared coordinate shadow. Calling the latter physical spacetime before
the two are connected would repeat the category error identified at the end of
v9.

## 11. Profinite spaces: the corrected connection

D3's variable-history space can be profinite: finite truncations are compatible
and cylinder probabilities define the infinite history law. But a connected
`S^2` cannot itself be a profinite inverse limit of finite discrete spaces,
because profinite spaces are totally disconnected.

The correct diagram is

```text
finite SCIR histories  ->  profinite history carrier
        |
        +-> finite local algebra with projective state space S^2
        +-> finite sampled direction nets converging metrically toward S^2
```

The history carrier preserves the past. The local algebra supplies the sphere.
Metric refinement supplies rounder finite shadows. These are three different
constructions.

## 12. What D9's failed one-coupling test now means

D9 refuted

```text
Bell partial-iSWAP transfer probability = geometric diffusion fraction.
```

D10 shows a better possible relationship:

```text
shared operational algebra / channel manifold,
distinct dynamical couplings and distinct roles.
```

The Bell packet and celestial clocks may both use a complex qubit's projective
geometry without sharing one raw coupling. This survives D9. What does not yet
survive is the claim that SCIR derives that shared algebra or turns it into the
physical influence cone.

## 13. Frozen verdict

The gate results are:

| layer | result |
|---|---|
| A conditional complex-qubit algebra | PASS |
| B finite outer approximation | PASS |
| B infinite generated convergence | CONDITIONAL on imported density theorem |
| C unique complex/rank-two selection | FAIL under current axioms |
| D Bloch sphere physically equals celestial sphere | DECLARED CANDIDATE, not derived |
| E finite-depth local direction generation | PASS conditionally; capacity open |
| E chosen-packet seal/schedule/forest intervention | PASS at finite declared scope |
| E physical link birth/ownership/holonomy seal | OPEN |
| E full Lorentz frame gauge | OPEN; `SU(2)` alone insufficient |
| E order/influence equivalence | OPEN |

Under the predeclared verdicts:

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

The conditional branch is nevertheless strong:

> If SCIR's primitive local operational system is the complex rank-two Jordan
> factor, if an unnormalized event scale is lawfully paired with it, and if
> `SL(2,C)` covariance and influence-cone equivalence are supplied, then “many
> clocks, few factors” gives `S^2` and a round `3+1` causal cone without a
> global update order or infinitely many simultaneous classical clock
> registers. A separate per-record evidence/description-capacity audit is
> still required.

That conditional statement is the precise remainder. It is substantially more
informative than either “the Bloch sphere is spacetime” or “the resemblance is
irrelevant.”
