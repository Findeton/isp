# JRH hostile delta review — Seat Q: quantum / EPR / QFT

**Frozen protocol.** `v16/note-jrh-delta-protocol.md` at commit
`1c225a2f0bb0e9209e9e5990de3a8eb03eab8076`, protocol SHA-256
`67a893be19ba8f2ccfbbd9ad1855e74ac3841a7cacbc2d4b7947b9126f457ffe`.

**Frozen repaired target.** Commit
`99f2352db3f3723cf709d0cb3d7a3949d2e42c63`.

| artifact | independently observed SHA-256 |
|---|---|
| `v16/paper-01-joint-relational-history-law.md` | `2f5d79266231d036fab180855a8b2ba80d652544e5b3ff55f8a0bee60e228a78` |
| `v16/code/jrh_exact.py` | `05979a992eb9b3b5c21b29af5736b85cadba744cf847404cb84ab7e6516ff53c` |
| `v16/code/jrh_output.txt` | `396f931ade115a2c6cf644bcb670fa2160c6696dc2925426451bf3d8b05901ff` |
| `v16/code/jrh_receipt.json` | `abe43f42492e88dfc9a279ca95d7143ce8e6e024bca318122d6ff99c3681de99` |
| `v16/note-jrh-adjudication.md` | `56f8e67bb22484ee5d366bcfc5a5adc325f103c7f33c200a0c8fa9567291d14f` |

**Independence.** I did not read either operator/gravity original report or
either operator/gravity delta report. I rebuilt the mandatory quantum and
finite algebra with a fresh exact rational/Gaussian-rational implementation
before using the candidate source for integrity checks. I did not import,
copy, or mechanically translate its arithmetic helpers. The source was loaded
only later to test its public build path, determinism, and portability.

## Executive judgment

The repaired finite result survives hostile review. The object actually built
is a fixed-factor CP boundary instrument; its nominal geometry is exactly
eliminable classical feed-forward; its displayed unconditioned division map
is entanglement breaking; and the rational interference fixture proves that
this map cannot be installed at every microscopic rewrite. The repairs now
say all of that. They no longer promote the toy to dynamical geometry, a
Hamiltonian, a field theory, a particle census, or a QFT/GR deviation.

The refined whole-history proposal is coherent as a **state-dependent
decoherence functional** once all histories have compatible boundary types.
It is not yet sufficient to make the stronger sentence in the abstract true:
exact decoherence and normalization for one boundary state do not, by
themselves, make the induced branch maps a trace-preserving quantum
instrument on arbitrary allowed inputs. I give a two-dimensional exact
counterexample below. Operator-level normalization (or an equivalent
all-input condition) is missing. This is a new blocker to accepting the
candidate-to-instrument bridge as written, but not a demolition of the exact
finite primary verdict: the paper already labels the fundamental dynamics
unselected and unproved.

Two smaller repairs remain. First, a generic continuous CPTP semigroup has a
Lindblad generator, not necessarily a Hamiltonian; Hamiltonian emergence needs
a strongly continuous unitary group (or a selected unitary dilation), not
merely “continuity or a semigroup/group law.” Second, objective actualization
requires a preferred, refinement-stable record partition and an account of
what is actual between divisions; the paper explicitly postulates selection
but has not yet made that postulate unique or compositional.

## 1. Independent exact rebuild

### 1.1 Feed-forward eliminability

For every input bit `g` and outcome `z`, I enumerated the repaired successor:

| `g` | `z = record` | nominal `G'` | nominal `C'` |
|---:|---:|---:|---:|
| 0 | 0 | 0 | 0 |
| 0 | 1 | 1 | 1 |
| 1 | 0 | 1 | 0 |
| 1 | 1 | 0 | 1 |

Thus `G' = g xor z` and `C' = z` on the entire finite domain. The only later
probe reads the same reconstructed label; the input collar never enters the
successor. Retaining `(g,z)` reproduces every declared nominal
geometry/collar prediction without either output field.

**Finding QD-01 — CLOSED.** The repaired paper states the exact eliminability
theorem and refuses the dynamic-geometry interpretation. This is not merely a
renaming: it gives the reconstruction map, notes that the input collar is
ignored, and demands a future relation/transport rewrite with a downstream
effect.

### 1.2 HJW preparation blindness and the nonlinear control

Using

`E_Z = {(1/2,|0>),(1/2,|1>)}`

and

`E_X = {(1/2,|+>),(1/2,|->)}`,

direct exact addition gives the same density operator `I/2`. For the fixed
Z-instrument, both decompositions give the same complete unnormalized blocks:

`J_0(I/2) = diag(1/2,0)`,

`J_1(I/2) = diag(0,1/2)`.

This special calculation is backed by the general linear identity

`sum_j p_j J_z(rho_j) = J_z(sum_j p_j rho_j)`.

Therefore all ensemble realizations of one density operator, not only the two
displayed ensembles, are indistinguishable under this fixed typed instrument.
The remote-ensemble premise is the one classified constructively by
[Hughston, Jozsa, and Wootters](https://doi.org/10.1016/0375-9601(93)90880-9).

I separately evaluated the deliberately nonlinear ensemble statistic

`N(E) = sum_j p_j (Tr[Z rho_j])^2`.

It gives `N(E_Z)=1`, `N(E_X)=0`, while `N(I/2)=0` even though the average of
the two pure Z-state values is `1`. With the Bell purification, Alice's Z/X
choice therefore selects Bob's registered number `1/0` under the standard
steering semantics. This is the intended exact preparation-context control,
not a candidate physical law. The static-state and trace-rule assumptions
behind the broader no-signalling/linearity result matter, as the primary
analysis of [Simon, Buzek, and Gisin](https://arxiv.org/abs/quant-ph/0102125)
also makes explicit.

**Finding QD-02 — CLOSED.** The repaired text now licenses exactly
fixed-factor preparation blindness and refuses only the registered
decomposition-reading control. It no longer generalizes that refusal to every
ontic pure-state dynamics, and it leaves changing-factorization no-signalling
open.

### 1.3 Bell entanglement breaking and interference placement

Applying the unconditioned Z division channel to Alice's half of
`|Phi+>` gives exactly

`(1/2)|00><00| + (1/2)|11><11|`.

The state is separable and has purity `1/2`. This is the canonical
measure-and-prepare behavior characterized by
[Horodecki, Shor, and Ruskai](https://arxiv.org/abs/quant-ph/0302031).

For the independent two-path fixture

```text
R = [[3/5, 4/5], [-4/5, 3/5]],
```

the two amplitudes returning to the first output after two steps are `9/25`
and `-16/25`. Keeping the intermediate alternative unresolved gives

`|9/25 - 16/25|^2 = 49/625`.

Recording the intermediate route instead gives

`(9/25)^2 + (16/25)^2 = 337/625`.

The gap is not an implementation artifact: it is precisely the cross-term
removed by the intermediate record. A positive classical distribution over
the two fine routes cannot reproduce both contexts while retaining those same
route weights. This is the finite reason to place a division instrument only
at a genuine record boundary. It is consistent with quantum-measure and
decoherent-history motivations, but does not select the proposed functional
([Sorkin](https://arxiv.org/abs/gr-qc/9401003)).

**Finding QD-03 — CLOSED.** The paper now publishes both exact consequences,
distinguishes the boundary shadow from the microscopic law, and does not use a
classical positive history probability as the explanation of interference.
Pre-division coherence and a later CP shadow are mutually compatible in
principle; this fixture proves the placement constraint, not the proposed
dynamics.

### 1.4 Arity, cycles, holonomy, logarithms, and rivals

The connected simple-graph cycle ranks `E - V + 1` are respectively `0`, `0`,
and `1` for an edge, a three-vertex path, and a triangle. The repaired
three-edge transports give

```text
U01 = i X,
U12 = i Y,
U20 = I,
H = U20 U12 U01 = diag(i,-i).
```

Hence `Tr(H)=0` and `det(H)=1`. Under independent vertex-frame changes the
closed product transforms by conjugation at the base vertex. For the tested
`g0=X`, `g1=Z`, `g2=I`, I obtain `H'=diag(-i,i)` with the same trace and
determinant. Reversing the oriented loop gives `H^dagger`. This is a proper
finite holonomy calculation, unlike an open two-edge product; it still is not
a gravitational curvature observable.

For the frozen transfer `diag(1,i)`, the phase-lift witnesses are
`-7,-3,1,5,9`, and the full pair family is `(4m,1+4n)`. A clock duration,
units, sign convention, and logarithm branch are additional data. Finally,
on `|0>`, the Z and X rival instruments give exact record distributions
`(1,0)` and `(1/2,1/2)` while sharing the declared weak safety surface. They
are different observables, so this is nonselection by an uncalibrated surface,
not sameness of physical law.

**Finding QD-04 — CLOSED.** The triangle has been closed and gauge-tested; the
full logarithm family is stated; the Z/X claim is scoped to a common
uncalibrated carrier and grammar; two actors are viable for the finite
projective occurrence; and three actors are only the first loop in this graph
family, not a minimum interaction arity.

## 2. Original defect closure audit

I used the frozen joint adjudication and my own original Seat-Q report, not the
other seats' reports. The repaired disposition is:

| original panel defect | delta status | reason |
|---|---|---|
| projective qubit toy promoted to dynamic geometry | **CLOSED** | Exact feed-forward erasure is now the theorem; dynamic geometry is `REFUSED`. |
| unused/copy-only collar presented as continuation geometry | **CLOSED** | Input collar irrelevance is published and the delivered collar is rejected. |
| open path presented as triangle holonomy | **CLOSED** | Three oriented edges, inverse reversals, vertex gauges, trace and determinant are supplied. |
| incomplete relabelling/diamond payload coverage | **CLOSED** | The repaired nominal fixture tests every registered payload field; no general covariance theorem is inferred. |
| binary expectation control used against semiclassical gravity | **CLOSED** | It is scoped to the binary pointer alphabet and no semiclassical-gravity conclusion survives. |
| fixed-factor Bell result overpromoted to growing geometry | **CLOSED** | Fixed-factor scope is explicit; relational-algebra/sector no-signalling is `OPEN`. |
| one nonlinear control used to kill the ontic branch | **CLOSED** | Only that registered control is refused; all other ontic laws remain `OPEN`. |
| entanglement-breaking consequence omitted | **CLOSED** | The exact Bell image, separability, and purity are now central. |
| division map allowed at every microscopic rewrite | **CLOSED** | Exact `49/625` versus `337/625` blocks that reading. |
| five logarithm witnesses presented as the ambiguity | **CLOSED** | Full `(4m,1+4n)` family and clock/units debt are stated. |
| transfer eigenmodes promoted to particles/fields | **CLOSED** | Species, vacuum, statistics, scattering, and QFT limit are all `OPEN`. |
| “same ontology” for Z/X | **CLOSED** | Replaced by same uncalibrated carrier/output grammar and weak-surface nonselection. |
| untyped “no forced deviation” machine conclusion | **CLOSED** | The deviation claim is now `OPEN / UNTYPED`; the invalid stronger gate is gone. |
| inconsistent consequence tags and weak source selftest | **CLOSED** | Receipt/paper vocabulary agrees and the observed-digest path is actually mutated. |
| “right correction” language implying derivation from the old walk | **CLOSED** | It is called a consistent replacement and existing-walk reconstruction remains `OPEN`. |
| objective outcome actualization left implicit | **PARTIAL** | It is now an explicit stochastic postulate, but its preferred record partition and cross-refinement consistency are not selected. |
| Hamiltonian ontology inferred from a one-step logarithm | **PARTIAL** | Nonuniqueness is scoped correctly, but the emergence conditions still conflate a generic semigroup with a unitary group. |

No original defect has merely been renamed. The two partial rows are residual
conditions on the speculative successor, not a resurrection of the rejected
finite claims.

## 3. Three objects that must remain separate

### Object I: the exact boundary instrument

`J_z(rho)=P_z rho P_z` is a concrete CP, trace-nonincreasing branch map and
`sum_z J_z` is trace preserving on the fixed input space. Its complete
classical-quantum output is affine. The displayed unconditioned channel is
entanglement breaking. All of those statements are exact properties of the
finite Z fixture.

### Object II: the general history functional

The proposal

`K_A = sum_(h in A) a[h] V[h]`,

`D(A,B)=Tr(K_A rho_boundary K_B^dagger)`

is a representation schema. If every `K_A` has one common input and output
type and `rho_boundary >= 0`, then Hermiticity and strong positivity follow
algebraically. For any finite event list and coefficients, the quadratic form
is the trace of `L rho_boundary L^dagger` for the corresponding linear
combination `L`. Additivity follows if disjoint union is represented by
operator addition. None of those facts chooses `a[h]`, `V[h]`, a record
partition, or a physical fixed point.

### Object III: the local exponential ansatz

`a[h]=product_v exp(-I_v[h]/2+i Theta_v[h])` is a proper subset of possible
weights and is explicitly unselected. Local factorization does not by itself
give relational locality, gauge invariance, refinement consistency, a CP
boundary process, no-signalling, or a continuum limit. Those must be imposed
or derived separately.

**Finding QD-05 — CLOSED.** The repaired paper mostly maintains these type
boundaries. It does not transfer the finite fixture's CP, Bell, holonomy, or
interference results to the general functional or local ansatz. The one
remaining illicit promotion is the claim that decoherence of the proposed
functional by itself yields a CP instrument; that is isolated next.

## 4. Exact counterexample to automatic instrument emergence

The abstract says that “A CP instrument ... emerge[s]” at a partition where
the functional decoheres. The formal section defines decoherence and
normalization for the particular `rho_boundary`. Those conditions license a
probability distribution for that state, but not necessarily an instrument on
the input state space.

Take the exact two-dimensional example

```text
rho = |0><0|,
K0  = diag(3/5, 2),
K1  = (4/5)|1><0|.
```

For the partition `{A0,A1}`:

```text
D(A0,A0) = 9/25,
D(A1,A1) = 16/25,
D(A0,A1) = D(A1,A0) = 0,
D(Omega,Omega) = 1.
```

The functional is strongly positive, the partition exactly decoheres for the
declared boundary state, and the diagonal probabilities normalize. Yet

`K0^dagger K0 + K1^dagger K1 = diag(1,4)`,

not the identity. In particular, `K0` maps input `|1><1|` to an output of
trace `4`; that branch is not trace nonincreasing. Thus these maps do not form
a quantum instrument on arbitrary boundary inputs.

There are two clean repairs:

1. Weaken the abstract/formal claim to **state-relative decoherent
   probabilities and conditional branch maps**; or
2. require an operator instrument condition, for example
   `K_alpha^dagger K_alpha <= I` and
   `sum_alpha K_alpha^dagger K_alpha = I` for every licensed division
   partition. A sufficient history-language alternative is normalization and
   exact decoherence for every allowed input density operator, not only the
   realized `rho_boundary`; the all-input cross conditions become operator
   identities and normalization yields completeness.

For more general histories, one branch may need several Kraus operators rather
than the single `K_alpha` form. The condition should then be stated for the
full CP map, not only one class operator.

**Finding QD-06 — NEW-BLOCKER.** Decoherence at one boundary state does not
imply a CP trace-preserving instrument. This blocks terminal acceptance of the
candidate-to-instrument bridge as worded. It does not trigger rejection of the
paper's exact primary result because the general functional is explicitly a
candidate, its weights and division law are explicitly missing, and the
already-built boundary instrument has independent Kraus completeness.

## 5. Conditions the candidate still needs

The finite formula is coherent only after the following obligations are made
mathematically explicit.

### 5.1 Changing relation carriers and types

- Each `V[h]` must have a common domain `H(B_-)` and common codomain
  `H(B_+)`, or each history-dependent codomain must be embedded by a specified
  isometry into a common physical boundary space. Otherwise `sum_h a[h]V[h]`
  and the cross-history trace are untyped.
- If different geometries are put in orthogonal direct-sum sectors, their
  off-diagonal terms vanish by construction. That may be appropriate for
  already recorded geometry, but it cannot simultaneously represent coherent
  unrecorded geometry alternatives. A nontrivial cross-geometry physical inner
  product, common kinematic space, or explicit superselection rule must decide
  which case applies.
- Gauge-equivalent histories need a quotient, gauge fixing with the correct
  measure, or group averaging. Automorphism factors must prevent duplicate
  counting.

### 5.2 Gluing and process consistency

- Regional gluing needs an associative contraction over a complete shared
  boundary type, including sums/integrals and any resolution of identity.
- The result must not depend on an unphysical cut. Sequential and disjoint
  gluing need typed identities analogous to link products/comb causality, not
  only scalar multiplication. The primary quantum-network framework makes
  these normalization constraints explicit
  ([Chiribella, D'Ariano, and Perinotti](https://arxiv.org/abs/0904.4483)).
- Refinement requires a directed family of event algebras and push-forward
  maps with cylindrical consistency. Overlaps must not double-count a history.
- Changing factorization requires embeddings or channels between local
  observable algebras. A fixed partial trace cannot define relational
  locality after carrier creation/deletion.

### 5.3 Positivity, normalization, and coarse graining

- For fixed types, `rho_boundary >= 0` and the Gram form make strong
  positivity automatic; this is a consistency property of the representation,
  not a dynamical selector.
- Normalization `D(Omega,Omega)=1` must be stated at the appropriate scope: for
  one prepared boundary state if only state-relative probabilities are meant,
  or operatorially/all-input if a reusable instrument is meant.
- Disjoint coarse graining must satisfy `K_(A union B)=K_A+K_B` and the event
  algebra must be closed under the questions used. Refinement push-forward
  must preserve the full complex functional, not only its diagonal.
- A probability partition needs exhaustiveness as well as decoherence. For the
  conditional formula, `H alpha` must be a typed intersection/concatenation,
  `D(H,H)>0`, and `{H alpha}` must be an exhaustive decoherent refinement of
  `H`; otherwise its diagonal terms need not sum to the denominator.

### 5.4 Division, records, and actualization

- Exact medium decoherence is enough for probability sum rules, but record
  permanence is stronger. Gell-Mann and Hartle's primary analysis stresses
  that strong decoherence preserves the past under future extensions
  ([Gell-Mann and Hartle](https://arxiv.org/abs/gr-qc/9509054)). The candidate
  correctly names permanence, but it needs a theorem on its chosen gluing law.
- “One alpha becomes actual” needs a preferred physical record algebra or a
  unique compatible family of stable record partitions. Otherwise multiple
  incompatible decoherent partitions can supply different sample spaces.
  Starting from records is a viable strategy, not a completed selector
  ([Hartle](https://arxiv.org/abs/1608.04145)).
- The ontology must say whether a fine relational/geometry trajectory is
  actual between divisions but not probabilistically resolved, or whether only
  the coarse recorded past is actual until the next division. The current
  phrase “one actual relational history” permits both readings.
- Approximate decoherence needs a norm, an error bound on all relevant
  coarse-grained probabilities, stability under refinement/future extension,
  and an accumulation bound. The paper correctly declares that theorem
  missing and uses exact zeros only in the finite claim.

**Finding QD-07 — PARTIAL.** The formula is a coherent finite candidate after
common boundary typing, and “one actual history” is not an illicit classical
probability distribution over unrecorded routes. The paper explicitly
postulates stochastic actualization and does not smuggle in an approximate
division threshold. It still lacks the common-space/gluing identities,
all-input normalization needed for an instrument, preferred record partition,
and refinement-stable actualization rule listed above.

## 6. EPR, no-signalling, and the ontic pure-state fork

The repaired EPR claim is at the correct scope. On a fixed `A tensor B`
factorization, summing Alice's outcomes and applying a linear instrument to
Bob cannot expose which HJW ensemble Alice remotely realizes. Complete
positivity also gives fixed-ancilla safety. This does not answer what counts
as “Bob” when an outcome changes the relation carrier.

For changing carriers, a valid theorem must identify relational local
observable algebras before and after each branch, specify the sector embedding
or comparison map, quantify over all remote pre-contact instruments, and show
equality of Bob's complete unconditioned boundary functional. In process
language it also needs the relevant causality constraints under every allowed
intervention, not just equality of one reduced density matrix. Process tensors
show why multitime operational consistency contains more information than
one-time channels
([Pollock et al.](https://arxiv.org/abs/1512.00589)). The paper states this
debt rather than claiming it solved.

The ontic pure-state branch is not excluded by the registered nonlinear
counterexample. The paper's two necessary escape conditions are sensible:
preparation-independent composite dynamics wherever steering is operational,
or extra ontic structure that cannot be remotely selected. They are not
sufficient for a viable quantum theory. Such a theory must also reproduce the
observed conditional steering/Bell correlations, define which interventions
are operationally allowed, and prove parameter independence for the complete
composite law. Declaring steering “unphrasable” without reproducing the
empirical protocol would be loss of scope, not a success.

**Finding QD-08 — CLOSED.** Fixed-factor HJW/no-signalling and the registered
nonlinear failure are stated exactly and independently reproduced.

**Finding QD-09 — PARTIAL.** The pure-state fork now gives necessary safety
conditions and leaves the general branch open, which is correct. Add the
equally necessary empirical obligation to reproduce conditional steering and
Bell correlations; inaccessible decomposition data alone does not complete
the branch.

## 7. Hamiltonian reconstruction

The one-step nonuniqueness result is exact. It establishes that one transfer
plus one chosen duration does not select a logarithm, energy scale, sign
convention, or dilation. It does not prove that no Hamiltonian representation
exists, and the paper now says so.

The remaining issue is in the positive emergence sentence. Continuity and a
semigroup law on a fixed Hilbert space do not generally yield a self-adjoint
Hamiltonian. A strongly continuous **unitary group** has a self-adjoint
generator (Stone's theorem). A strongly continuous CPTP semigroup generally
has a dissipative GKSL/Lindblad generator, not `-i[H,·]` alone
([Gorini, Kossakowski, and Sudarshan](https://doi.org/10.1063/1.522979);
[Lindblad](https://doi.org/10.1007/BF01608499)). A non-Markovian process may
not admit even a time-homogeneous generator. A selected unitary dilation can
recover a Hamiltonian on a larger fixed space, but the environment, embedding,
clock, and branch are additional choices, as the paper already notes.

**Finding QD-10 — PARTIAL.** Replace “continuity or a semigroup/group law” by
the precise alternatives: a strongly continuous one-parameter unitary group
for a Hamiltonian on the effective sector; a CPTP semigroup for a general
Lindbladian; or a selected unitary dilation for a larger-space Hamiltonian.
The exact logarithm-ambiguity verdict itself is closed.

## 8. Fields, interactions, species, and deviations

A sum over histories with local-looking weights is not yet a quantum field
theory. A QFT limit needs at least a compatible net/functor of local
observable algebras, causal commutation or an equivalent locality axiom,
vacuum/reference phase, spectrum condition, exchange statistics, stable
excitation sectors, scattering or other asymptotic observables, cluster
properties, renormalization/refinement control, and a continuum scale map.
General-boundary amplitudes can organize region composition, but their state
spaces, gluing, probability interpretation, and vacuum axioms are substantive
inputs, not consequences of calling a boundary relational
([Oeckl](https://arxiv.org/abs/hep-th/0509122)).

Likewise, pair, triple, and higher effective vertices may coexist only after an
all-region/all-support law is supplied. The pair instrument proves two-actor
quantum viability at its typed boundary scope; it does not prove a two-actor
gravitational event. The triangle proves the first loop of one simple-graph
family, not a species, field quantum, or universal arity. The choice inventory
correctly marks the all-`n` law missing.

No particle or species follows from finite transfer eigenvectors. Species
would require a selected phase/vacuum plus stable irreducible excitation or
superselection sectors, permutation/braid statistics, and observables that
identify them. No affine-coset value, channel translation, cosmological
constant, dimensionful scale, matter-gravity coupling, GR limit, QFT limit, or
deviation is derived.

Finally, “no deviation is typed” does not mean “there is no deviation.” A
deviation claim needs a benchmark observable defined in both the selected ISP
limit and QFT/GR, a common calibration/scale, and a quantitative prediction.
The paper now keeps geometry-induced decoherence, metric noise,
higher-curvature terms, modified dispersion, and the very existence of a
forced deviation open.

**Finding QD-11 — CLOSED.** The field analogy is demoted, pair/triple/all-`n`
claims are correctly separated, particles/species are unselected, and every
QFT/GR/constant/deviation claim is conservatively open or refused. No
kill-condition promotion survives.

## 9. Consequence reclassification

| topic | paper classification | delta status | highest licensed statement |
|---|---|---|---|
| boundary CP instrument | FORCED | **CLOSED** | The exact fixed-factor Z instrument exists. |
| dynamic geometry/backreaction | REFUSED / OPEN | **CLOSED** | Copied geometry is refused; genuine backreaction remains open. |
| two actors | FORCED / OPEN | **CLOSED** | Projective occurrence forced; gravitational occurrence open. |
| three actors | FORCED / REFUSED | **CLOSED** | First simple-graph cycle forced; minimum arity refused. |
| all-`n` interactions | MISSING in choice inventory | **OPEN** | Arbitrary support is permitted in principle but no extension law exists. |
| fixed-factor EPR/no-signalling | FORCED | **CLOSED** | All decompositions of one `rho` give the same complete output. |
| changing-factorization no-signalling | OPEN | **OPEN** | Local algebras and sector embeddings are absent. |
| registered nonlinear control | REFUSED | **CLOSED** | It is non-affine and gives the exact steering signal. |
| general ontic pure-state law | OPEN | **PARTIAL** | Not ruled out; must also reproduce steering/Bell data under a no-signalling composite law. |
| displayed division map preserves coherence | REFUSED | **CLOSED** | It is entanglement breaking; coherence must live before division or elsewhere. |
| general complex history representation | PERMITTED | **PARTIAL** | Coherent finite representation is permitted; typing, gluing, normalization, and selection are unproved. |
| objective actualization | postulated | **PARTIAL** | One successor may be postulated actual; preferred records and refinement compatibility are missing. |
| one-step Hamiltonian uniqueness | REFUSED | **CLOSED** | Infinite logarithm lifts remain after a clock choice. |
| Hamiltonian emergence | OPEN | **PARTIAL** | Needs a unitary group or selected dilation; a generic semigroup yields a Lindbladian. |
| fields/QFT | OPEN | **OPEN** | No local algebra net, vacuum, statistics, continuum, or scattering structure. |
| particles/species | OPEN | **OPEN** | No selected phase or stable sectors. |
| affine-coset grammar | OPEN | **OPEN** | Untouched by this unit. |
| channel affine translation | REFUSED as selected by CP/TP | **CLOSED** | Unital and reset CPTP examples prove nonselection. |
| cosmological/affine constant | OPEN | **OPEN** | No continuum constraint system or value. |
| Newton/area/absolute scale | REFUSED | **CLOSED** | No dimensionful input or transmutation/calibration mechanism. |
| matter-gravity coupling | OPEN | **OPEN** | Neither side of a calibrated response law is typed. |
| GR limit | OPEN | **OPEN** | No action, constraints, refoliation/deformation closure, or continuum map. |
| geometry-induced decoherence/noise | OPEN | **OPEN** | Finite dephasing is ordinary record forgetting. |
| higher curvature/modified dispersion | OPEN | **OPEN** | Neither comparison observable nor coefficient/scale exists. |
| forced QFT/GR deviation | OPEN | **CLOSED** | Correct status is open/untypeable, not absent. |
| existing ISP walk reconstruction | OPEN | **OPEN** | No map from the committed walk to this fixture or candidate. |

## 10. Artifact and reproducibility audit

- Paper and receipt contain the same 28 consequence rows and the same 16
  choice rows byte for byte.
- Every consequence uses exactly one member of the registered five-word set
  `FORCED`, `CONDITIONAL`, `PERMITTED`, `REFUSED`, `OPEN`; the present rows use
  a subset of that set consistently.
- Each of the six machine-equal claim strings occurs exactly once in the paper
  and transcript and equals the receipt.
- All target artifact hashes agree with the frozen protocol and receipt.
- I independently recomputed every receipt seal, the ledger chain, and final
  ledger head `0fa34c09d2105cf9`.
- All 37 gates are recorded passing. All 13 registered mutants move their
  named object and die at their named gate. All 13 live source anchors match
  their frozen bytes and equal the explicit accessor read set.
- `python3 v16/code/jrh_exact.py --selftest` exits `0` and changes no target
  artifact hash. Unknown CLI syntax exits `2` before writing. The named
  `FEEDFORWARD_BREAK` mutant exits `3` at `G-C2` without writing.
- After the science rebuild, I loaded the candidate for diagnostic purposes,
  ran its core twice in memory, and ran it from `/tmp`; the results were
  byte-identical and the foreign-working-directory result matched. The core
  build path does not invoke git.
- I did not run the plain artifact writer because this seat is authorized to
  write only this review. Transcript/receipt equality, in-memory rebuild,
  selftest, mutation, and foreign-CWD diagnostics cover the relevant behavior
  without mutating candidate artifacts.

**Finding QD-12 — CLOSED.** The repaired scientific artifacts and integrity
machinery match the frozen target. I found no circular numerical gate, hidden
write, nondeterminism, off-tree dependency, or source-anchor mismatch. Passing
integrity checks authenticate the finite claims; they do not validate the
unproved history weights.

## 11. Required fixes and highest licensed verdicts

Before terminal publication, I require three focused changes:

1. Replace automatic “CP instrument emergence” from state-relative
   decoherence with either state-relative probability language or explicit
   operator/all-input instrument normalization and trace-nonincreasing
   conditions. Carry the same distinction into gluing and conditioning.
2. Replace the generic semigroup-to-Hamiltonian wording with the unitary-group,
   Lindbladian, and selected-dilation alternatives.
3. Make the actualization debt explicit at the point of the postulate: select
   a preferred stable record partition, require compatibility under future
   extension/refinement, and state what is actual between divisions. Add the
   obligation to reproduce conditional steering/Bell correlations to the
   ontic-pure-state fork.

With those repairs, the highest licensed exact verdict remains
`BOUNDARY-INSTRUMENT-CONSISTENT-BUT-FUNDAMENTAL-DYNAMICS-UNSELECTED`.
The highest licensed status of the dynamical proposal is
`COMPLEX-RELATIONAL-HISTORY-LAW-CANDIDATE-UNPROVED`. Dynamic geometry, a
selected joint successor law, changing-factorization no-signalling, QFT, GR,
species, constants, scales, and deviations remain open.

ACCEPT-WITH-FIXES
