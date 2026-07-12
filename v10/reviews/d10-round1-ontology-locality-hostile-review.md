# D10 hostile review, round 1: ontology, locality, gauge, capacity, and profinite scope

**Referee:** independent hostile ontology/locality/gauge audit  
**Date:** 2026-07-11  
**Verdict:** **MAJOR REVISION — PRIMARY `KINEMATICS-ONLY` CEILING ACCEPTED, SECONDARY LOCALITY/CAPACITY/GAUGE LABELS NOT YET ACCEPTED**

## Frozen package audited

The review used the artifact manifest and claim boundary frozen in
`v10/data/d10-pre-review-receipt.md`:

- `v10/note-d10-bloch-celestial-selection-protocol.md`
- `v10/note-d10-literature-audit-bloch-celestial.md`
- `v10/note-d10-bloch-celestial-investigation.md`
- `v10/relativistic-isp-v10-paper11-many-clocks-few-factors-is-an-exact-kinematic-bridge.md`
- `v10/code/d10_bloch_lorentz_exact.py`
- `v10/code/d10_finite_clock_convergence.py`
- `v10/code/d10_relational_scir_packet.py`
- `v10/code/d10_reproducibility_audit.py`

Frozen hashes reproduced:

```text
26e61c146b328b5eae14994594f79bb70421a275a35de464b4245e482dc42a46  note-d10-bloch-celestial-selection-protocol.md
435a4c183d908a7e2191de455946a78d20287421020adfff5b80c6de4b2feee7  note-d10-literature-audit-bloch-celestial.md
cd3e7109078daa3e7688fa3c5e639ef5094e414a752c7b338cbdf5fdf33ac06e  note-d10-bloch-celestial-investigation.md
500e5e92cb11b6941486350c716a21705d3a2a9f9e3d506fb8d0567756d7fba7  relativistic-isp-v10-paper11-many-clocks-few-factors-is-an-exact-kinematic-bridge.md
8d9d05f6ea95d4c522f8cf7bde9d05d88e1bb712bf65c3eaf5da21cc8fc155b8  d10_bloch_lorentz_exact.py
32b5be41cb73c41d9804c2576c3297aa5ba3d9d044fa6a4283e7a003c708f7ed  d10_finite_clock_convergence.py
5417d17efcbfed942701f9cf9512327aaa665bf3ba489d6aec72f4456225290b  d10_relational_scir_packet.py
527fd9bbd4cc19f0741b33bfb4812be424fb83f32bcad6a620f1a4e54149bde4  d10_reproducibility_audit.py
```

Independent execution reproduced:

```text
d10_bloch_lorentz_exact.py       101/101
d10_finite_clock_convergence.py   97/97
d10_relational_scir_packet.py     32/32
```

and the frozen receipt digests. No exact algebraic or reported finite-geometry
mismatch was found. The openings below concern what those computations are
allowed to mean.

## Accepted core before hostile openings

The following mathematical content survives:

1. `Herm_2(C)` is four-dimensional over the reals; its positive cone is
   linearly isomorphic to the `1+3` Lorentz cone, and normalized rank-one rays
   form `CP^1`, diffeomorphic to `S^2`.
2. The same Lorentz-cone construction exists in other dimensions through
   real, quaternionic, octonionic rank-two shadows and generic spin factors.
   Cone kinematics does not select `3+1`.
3. Finite direction sets define outer polyhedral approximations with the
   reported support/radial errors.
4. A finite `H/T` alphabet generates finite, growing sets of exact complex
   qubit projectors.
5. Supplied `SU(2)` link matrices obey endpoint gauge covariance, and a loop
   product transforms by conjugation.
6. A supplied `SL(2,C)` congruence preserves determinant but is generally
   nonunitary and changes trace.
7. The frozen papers explicitly refuse complex selection, time-scale
   derivation, physical Bloch/celestial identity, full boost gauge, and
   order/influence equivalence.

These support an algebraic/kinematic investigation. They do not yet support
all of the secondary receipt labels.

## Numbered hostile openings

### O1 — The Bloch/celestial identification still begins by importing the structures it is meant to explain

**Severity:** **MAJOR**

**Evidence:** The exact bridge starts from the chosen algebra
`Herm_2(C)`, its complex involution, the Pauli basis, the Euclidean quadratic
form on three Pauli coefficients, and normalized rank-one projectors. From
those inputs, `CP^1 ~= S^2` and `t^2-|x|^2` follow exactly.

What is not derived is:

- why the primitive record algebra is complex rather than real,
  quaternionic, or another spin factor;
- why the Pauli coefficient space is physical space;
- why the trace coefficient is physical time;
- why the Fubini–Study/projective sphere is the celestial sky;
- why the antipodal relabeling that changes `t+u.x` to `t-u.x` has physical
  orientation;
- or why one internal pure-state manifold supplies spacetime null covectors.

The manuscript acknowledges most of this, and the alternative spin-factor
census makes the nonselection decisive. Nevertheless, `EXACT-QUBIT-LORENTZ-
BRIDGE` must remain an **ordered-space isomorphism conditional on choosing the
complex qubit**, not a bridge selected by SHARD/SCIR.

**Required repair:** consistently name the positive result
`CONDITIONAL-COMPLEX-QUBIT/LORENTZ-CONE ISOMORPHISM`. Keep physical
Bloch/celestial identity as a declared candidate requiring a record-native
map of states, effects, orientation, scale, order, and influence.

### O2 — Projective effects are not yet clocks, and the time coordinate is external to a normalized qubit

**Severity:** **MAJOR**

**Evidence:** The exact object called a directional clock is

$$
q_u(X)=\operatorname{Tr}(P_uX)=t+u\cdot x.
$$

This is a positive linear evaluation on the supplied ordered vector space. It
does not tick, order records, define elapsed proper time, advance under a click
law, or carry a physical temporal unit. For a normalized qubit, `Tr rho=1`
fixes `t=1/2`; the fourth factor disappears as a variable scale.

The relational packet restores `Delta t=1` only by declaration and maps the
Bloch vector to `Delta x`. That inserts a global unit click interval, a
three-component displacement interpretation, and the relative light-speed
scale. The paper correctly calls this a declared shadow, but the title and
`MANY-CLOCKS-FOUR-FACTORS` label can still be read as an operational clock
construction.

**Required repair:** call the `P_u` objects `directional positive
functionals` or `clock-shadow evaluations` until a record click, elapsed-time
observable, and unit/scale map are supplied. Keep
`NORMALIZED-QUBIT-HAS-NO-TIME-SCALE` load-bearing in every summary.

### O3 — “No external sphere sampler” is false without the qualifier “in the rewrite rule”

**Severity:** **MAJOR**

**Evidence:** `d10_relational_scir_packet.py` does not sample `S^2` to choose
an `H/T` rewrite. That is a genuine positive result. But the same executable's
`sampled_support` function constructs 50,000 Fibonacci directions using
global `(x,y,z)` coordinates, trigonometric functions, `pi`, and the golden
angle. The separate convergence executable uses a 120,000-direction
Fibonacci sphere and globally embedded Platonic direction sets.

Therefore the output

```text
external_sphere_sampler=ABSENT
```

is unqualified and literally incorrect. An external sphere is absent from
the **generator** but present in the **coverage diagnostic** and in the finite
cone benchmark.

This distinction matters: the diagnostic presupposes the global round sphere
against which the candidate is scored. It cannot be evidence that SCIR has
internally identified that sphere as physical.

**Required repair:** print and state
`external_sphere_sampler_in_rewrite=ABSENT` and
`external_global_S2_coverage_diagnostic=PRESENT`. Separate generated
projector count from externally scored angular coverage.

### O4 — Finite-dimensional qubit state is not by itself a finite record-capacity theorem

**Severity:** **MAJOR**

**Evidence:** D10 proves:

- three token names `H,T,SEAL`;
- a finite reachable set at every finite word depth;
- and a three-real-dimensional normalized qubit state space.

It does not prove a bound on:

- exact amplitude-description length;
- accumulated word/provenance length;
- numeric precision of the current projector;
- evidence/KL content;
- distinguishable zero-error states;
- or total collar storage.

The exact states lie in `Q(sqrt(2),i)`, but coefficient numerators/denominators
and the shortest preparation word can grow with depth. The code stores the
entire word string while deduplicating projectors. A continuum of possible
qubit states is finite-dimensional but does not have a finite exact classical
alphabet. Conversely, finite accessible quantum information is a different
operational resource. D4–D5 already required these notions not to slide.

The proposed distributed resolution may be viable if every gate token is a
new bounded record and the growing history, rather than one collar, stores the
word. That encoding is not executed here, and `SEAL` is only a string in a
tuple.

**Required repair:** downgrade `FINITE-RECORD-DIRECTION-REFINEMENT` to
`FINITE-ALPHABET/FINITE-DEPTH PROJECTOR REFINEMENT`. State the capacity metric
and audit per-record token, exact state description, provenance, evidence,
and total-history storage separately before claiming the SHARD record ceiling
is satisfied.

### O5 — The SU(2) diamond is supplied connection algebra, not yet a sealed SCIR-local construction

**Severity:** **MAJOR**

**Evidence:** The exact gauge cell hand-assigns four link matrices
`U_ba,U_ca,U_db,U_dc` and four local basis matrices. It correctly proves path
endpoint covariance and conjugation of the loop. But it contains no:

- SCIR opportunity/eligibility law that creates a link;
- record-local storage/provenance or exactly-once ownership of links;
- screen/collar type or orientation check;
- seal decision or committed holonomy record;
- update rule deriving link values;
- or transported state/effect Born experiment around the diamond.

The code label `sealed holonomy trace gauge invariant` is especially
premature. It proves a Wilson-loop-like conjugacy invariant of supplied
unitaries, not a seal. This repeats the D6 distinction between generic
matrix/RN identities and a physical sealed record.

**Required repair:** rename the result `SUPPLIED-SU2-CONNECTION DIAMOND
GAUGE-COVARIANCE`. Reserve `sealed diamond holonomy` for a typed, owned,
locally created loop record with a seal/outcome law. Treat link transport as
additional packet data, not as derived by SCIR.

### O6 — The local-gauge tests import the complex tensor product and do not establish SCIR locality

**Severity:** **MAJOR**

**Evidence:** “Disjoint local frame changes commute” is checked with

```text
(GX tensor I)(I tensor GZ)=(I tensor GZ)(GX tensor I).
```

This imports the standard complex tensor-product composite—the same
composition/local-tomography structure whose derivation is open. It proves an
algebraic fact about disjoint tensor factors, not that arbitrary SCIR
instruments on spacelike-disjoint record collars commute.

The local Born check conjugates a state and effect at one frame by the same
unitary. It does not transport a state or effect along a link, compare two
diamond paths operationally, or prove every sealed probability/causal test is
gauge invariant.

**Required repair:** restrict G4's PASS to `single-site Born covariance and
supplied-link path covariance in the chosen complex tensor model`. Keep local
tomography/composite choice imported. A SCIR-local theorem needs typed
collars, disjoint rewrite maps, link-carried states/effects, and probability
equality under independent local gauges.

### O7 — The “construction-order gauge” receipt does not execute competing construction schedules

**Severity:** **CRITICAL**

**Evidence:** The final packet gate creates all positions first, then forms
two orderings of sibling labels and two dictionaries:

```python
state_a = {n: positions[n] for n in order_a}
state_b = {n: positions[n] for n in order_b}
check(state_a == state_b, "disjoint sibling construction order is gauge")
```

Dictionary equality ignores insertion order, and both dictionaries read the
same already-computed immutable entries. The gate is true without executing
either order as a rewrite schedule. It does not test:

- two sequential instrument compositions;
- probability normalization after each schedule;
- provenance/ID allocation;
- interaction with shared ancestors/collars;
- or canonical pushforward from presentation histories.

The separate tensor-product commutation gate concerns local basis changes,
not record construction.

**Required repair:** remove the construction-order PASS. Either label this
`static sibling-position assignment is order-insensitive`, or execute two
actual local rewrite schedules from one initial state and compare their full
marked-history canonical pushforwards. The secondary gauge verdict cannot
rely on this gate.

### O8 — `local_influence=PASS` is an offline reachability property of a supplied global parent dictionary

**Severity:** **MAJOR**

**Evidence:** The influence control freezes a global `parents` dictionary and
computes descendants by repeatedly scanning every entry. It confirms that a
chosen rooted forest has no path from node 1 into another branch/component.
No stochastic instrument is changed and no continuation distributions are
compared.

This does not implement the paper's own definition of influence—change of
later sealed-record probabilities under a local intervention. It also does
not show a record-local update algorithm, since the diagnostic inspects the
whole supplied graph. A future rule may create a joining carrier; the static
forest says nothing about that law.

**Required repair:** replace `local_influence=PASS` with
`SUPPLIED-ANCESTRY-REACHABILITY=PASS; INTERVENTIONAL-INFLUENCE=OPEN`.
An influence test must vary one local instrument, propagate through incident
messages only, and compare exact continuation distributions, including
disconnected and possible joining sectors.

### O9 — SU(2) removes a supplied basis redundancy but does not derive absence of a global spatial frame

**Severity:** **MODERATE/MAJOR**

**Evidence:** Independent endpoint transformations show that predictions
formed covariantly from supplied links need not depend on basis labels. This
is a valid relational representation.

But all matrices are still written in one global computational basis, the
network and link values are hand-assigned, and no local rule creates or
calibrates them. Gauge covariance shows that the global basis is redundant;
it does not derive the connection or prove the physical universe contains no
background frame/connection data. Holonomy itself is relational but can carry
global information.

**Required repair:** say `no preferred basis is required after a supplied
SU(2) connection is given`, not `SCIR has derived a global-frame-free spatial
geometry`. Add link-generation/calibration and local ownership gates before a
stronger claim.

### O10 — Full SL(2,C) cannot yet be gauge without a dual Born/effect law

**Severity:** **MAJOR OPENING, HONESTLY ACKNOWLEDGED**

**Evidence:** The exact boost preserves determinant and changes trace. On the
event cone this is the standard Lorentz congruence. On normalized qubit states
it is a nonunitary filter with state-dependent renormalization/branch weight.

If states transform as `rho -> A rho A^dagger`, Born pairings are not
invariant when effects are transformed by the same congruence. A gauge
calculus needs an appropriate dual/contragredient transformation, a measure or
normalization density, and proof that all outcome probabilities and sealing
weights are unchanged. Treating every nonunitary filter as gauge would erase
physical branch probabilities.

The paper explicitly leaves this open; that refusal passes hostile review.

**Required preservation:** `FULL-SL2C-GAUGE-OPEN` must remain. The next receipt
must freeze state, effect, instrument, normalization, and seal transformations
and prove Born-probability invariance before calling boosts gauge.

### O11 — The positivity cone is not yet the record order cone, much less the influence cone

**Severity:** **MAJOR**

**Evidence:** `X >= 0` defines an algebraic cone. Calling it an `order cone`
is mathematically legitimate as an ordered-vector-space term, but it is not
yet the partial order of SHARD records. The packet's record order is the
separately supplied parent forest. The Bloch increment map that embeds that
forest in `(t,x)` is declared.

The influence object is weaker still: the receipt computes graph
reachability, not intervention-dependent continuation measures. Therefore no
equality, containment, or scaling relation among:

1. positive-matrix order;
2. record ancestry order;
3. accumulated Bloch-coordinate cone;
4. and operational influence support

has been proved.

The manuscript states the main gap correctly, so `ORDER-INFLUENCE-LINK-OPEN`
passes. The receipt should use `ALGEBRAIC-POSITIVITY-CONE` until the ancestry
map and intervention law are supplied.

### O12 — The profinite correction is mathematically and ontologically correct

**Severity:** **PASS / NO REPAIR DEMAND**

**Evidence:** A profinite inverse limit of finite discrete compact spaces is
totally disconnected, so it cannot literally equal connected `S^2`. The
papers correctly separate:

- a profinite finite-history carrier;
- the projective pure-state space of a finite algebra;
- and metric/Hausdorff refinement of finite direction nets.

They do not use “projective state space” as “projective inverse limit,” and
they do not claim the finite numerical nets prove a profinite construction of
the sphere. This part should be preserved.

One ceiling remains: the audited finite nested nets and depth-12 `H/T` family
show improvement, not by themselves an infinite convergence theorem. Any
density claim must stay tied to the separately cited synthesis theorem or a
new all-depth proof.

### O13 — Complex structure and local tomography remain imported, including in the candidate packet

**Severity:** **MAJOR OPENING, HONESTLY ACKNOWLEDGED**

**Evidence:** The real/complex parameter counts correctly expose the local-
tomography distinction, and the literature audit correctly treats relevant
reconstruction theorems as conditional. The candidate nevertheless starts
with:

- a complex two-level state space;
- complex conjugation;
- the complex tensor product;
- `H/T` complex gates;
- and Born evaluation.

Thus the candidate is evidence of consistency/existence inside imported
complex quantum mechanics, not evidence that sealed records or SCIR select
complex structure or local tomography.

**Required preservation:** keep `COMPLEX-SELECTION-NOT-DERIVED`. Do not use the
candidate's successful gauge or finite-grammar tests as an independent
selection argument, since they are downstream of the selected algebra and
composite rule.

### O14 — The primary `KINEMATICS-ONLY` verdict is honest; three secondary positives need renaming

**Severity:** **MAJOR VERDICT REPAIR**

**Evidence:** The primary verdict correctly refuses physical dimension
selection, time scale, boost gauge, order/influence equivalence, Einstein
dynamics, units, and `G`. It is the strongest honest layer verdict in the
package.

However:

- `MANY-CLOCKS-FOUR-FACTORS` promotes effects to clocks;
- `FINITE-RECORD-DIRECTION-REFINEMENT` promotes finite grammar/depth to a
  record-capacity theorem;
- `RELATIONAL-SU2-DIAMOND-GAUGE` promotes supplied link algebra and an
  unsealed loop to a SCIR/sealed-diamond construction.

**Required repair:** retain `KINEMATICS-ONLY`, but revise the secondary ledger
to something like:

```text
CONDITIONAL-COMPLEX-QUBIT/LORENTZ-CONE-ISOMORPHISM
+ FOUR-FACTOR-DIRECTIONAL-EVALUATIONS
+ FINITE-ALPHABET/FINITE-DEPTH-PROJECTOR-REFINEMENT
+ SUPPLIED-SU2-CONNECTION-GAUGE-COVARIANCE
- COMPLEX/LOCAL-TOMOGRAPHY-SELECTION-NOT-DERIVED
- NORMALIZED-QUBIT-TIME/SCALE-MAP-NOT-DERIVED
- PHYSICAL-SEAL/LINK/SCIR-LOCALITY-NOT-DERIVED
- FULL-SL2C-BORN-GAUGE-OPEN
- ANCESTRY/ORDER/INFLUENCE-LINK-OPEN
= KINEMATICS-ONLY
```

## Exact receipt evidence

The following frozen outputs reproduced:

```text
D10 BLOCH-LORENTZ EXACT RECEIPT
checks=101
exact_bridge=PASS
alternative_spin_factors=EXHIBITED
complex_selection=NOT_IMPLIED_BY_CONE
local_gauge_diamond=PASS
full_lorentz_gauge=REQUIRES_NONUNITARY_SL2C_EXTENSION
provisional_scope=KINEMATIC_AND_CONDITIONAL

D10 FINITE CLOCK CONVERGENCE RECEIPT
checks=97
precision_decimal_digits=90
finite_cones=OUTER_POLYHEDRAL_APPROXIMATIONS

D10 RELATIONAL SCIR PACKET RECEIPT
checks=32
depth12_projectors=113
depth12_sampled_support=0.914143429015
bloch_increment_map=DECLARED_NOT_DERIVED
order_influence_cone_equivalence=OPEN
```

The numerical and algebraic results are not in dispute. The exact frozen
code itself supplies the evidence for the ontology repairs:

- the external Fibonacci sampler is present in the coverage function;
- links and bases are hand-assigned matrices;
- the seal is an unused token string;
- construction-order equality compares precomputed dictionaries;
- influence is descendant reachability in a global parent map;
- the time/space increment is declared;
- and the boost is proved nonunitary and trace changing.

## Mandatory openings before round 2

1. Separate the conditional qubit/Lorentz ordered-space isomorphism from the
   physical Bloch/celestial identification.
2. Rename projective evaluations as clock shadows until a click/time law is
   supplied.
3. Report the external `S^2` diagnostic honestly while preserving its absence
   from the rewrite generator.
4. State and audit a record-capacity resource; do not infer it from finite
   dimension or token-count alone.
5. Downgrade the SU(2) result to supplied-connection gauge covariance and
   remove unexecuted sealing.
6. Replace the static dictionary order check with actual rewrite-schedule
   commutation or remove construction-order PASS.
7. Replace global reachability `local_influence=PASS` with an exact
   intervention/continuation test or keep influence open.
8. Keep complex tensor composition/local tomography imported.
9. Specify how relative link values are generated, owned, transported, and
   read locally; gauge covariance alone does not do this.
10. Preserve the full SL(2,C)/Born-weight opening and add dual state/effect
    probability gates before any boost-gauge claim.
11. Keep algebraic positivity, ancestry, coordinate shadow, and operational
    influence as four distinct objects.
12. Preserve the corrected profinite/projective/metric separation.
13. Revise the secondary verdict labels while retaining
    `KINEMATICS-ONLY`.

## Verdict

**MAJOR REVISION.** The primary conclusion is substantially honest: D10 has
found a sharp conditional kinematic isomorphism and has not derived physical
`3+1`, a global time scale, Lorentz-gauge dynamics, or an influence cone.

The package nevertheless overgrades its candidate implementation. It has a
finite complex-qubit grammar, supplied SU(2) connection algebra, external
sphere coverage diagnostics, a declared null-edge coordinate shadow, and
static ancestry reachability. It does not yet have a sealed SCIR-local link
law, physical construction-order gauge, finite-capacity encoding theorem, or
interventional influence dynamics.

The accepted headline is:

> Conditional on importing a complex qubit, its ordered positive cone is the
> `1+3` Lorentz cone and its rank-one projective rays form an internal `S^2`.
> Finite gate words refine internal projective directions. The identification
> of those objects with physical clocks, space, time, boosts, and causal
> influence remains unbuilt.

