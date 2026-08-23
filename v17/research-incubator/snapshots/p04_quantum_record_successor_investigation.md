# Private investigation: quantum reference records after Paper 04

Status: result-neutral, off-tree, and non-authoritative

Bound repository state: ISP v17 HEAD `1e27457`

Purpose: determine what physics, rather than notation or code, is required for a coherent quantum reference frame to yield a classical clock record

Prohibition: this note does not open a successor, retune Paper 04, award a coordinate, or authorize implementation

## Executive conclusion

Paper 04 exposed a general quantum boundary rather than a defect peculiar to its
seven-state model:

> A reversible quantum-frame transformation may depend coherently on an internal
> quantum sector, but a classical record label cannot undergo different
> transformations in those sectors while the sector coherence remains available.

There are only three exact possibilities.

1. The record transforms in the same way in every coherently connected sector.
2. The relevant sectors are superselected or decohered, so their coherence is no
   longer part of the physical state space.
3. The alleged record is retained as a noncommutative quantum memory, not yet as a
   classical outcome.

The first possibility includes an important positive escape: record a genuinely
invariant relation between clocks, rather than either frame-dependent clock
coordinate. Such a relational record can preserve coherence inside a degenerate
invariant sector. It records synchronization or correlation, not an absolute or
standalone time reading.

Finite-resource and approximate versions interpolate between these cases, but do
not evade the information--disturbance tradeoff. A readable, redundantly objective
record costs coherence, asymmetry/reference resources, entropy production, or some
combination of them.

The most honest next unit is therefore not a repaired finite clock and not a new
spacetime claim. It is a model-independent theorem-and-experiment unit provisionally
called:

> **When can a quantum reference reading become a physical record?**

Its scientific target is the quantum-to-classical interface itself. It should
separate:

- a coherent relative observable;
- a quantum memory carrying that observable;
- a classical, future-readable record;
- an objective record redundantly available to multiple readers;
- an actual configuration or happening in a Barandes-style ontology.

These are not synonyms. Paper 04 failed by crossing from the first two to the third
without constructing the physical transition.

## 1. The exact problem

Let the coherent controller or clock-rate system have Hilbert space

$$
\mathcal H_Q=\bigoplus_{a\in A}\mathcal H_a,
$$

with nonzero orthogonal projectors $P_a$. Let $R$ be a finite classical record
set and

$$
\mathcal C_R=\ell^\infty(R),
\qquad
z_r=I\otimes |r\rangle\langle r|.
$$

For a full quantum controller algebra, the classical--quantum boundary algebra is

$$
\mathcal A_{QR}=\mathcal B(\mathcal H_Q)\,\overline\otimes\,\mathcal C_R.
$$

Its center is precisely $I\otimes\mathcal C_R$. A classical record sector is
therefore not merely a diagonal matrix in a temporarily chosen basis. It is a
central, copyable, nondemolition-readable alternative in the declared boundary
type.

Suppose a symmetry or change of reference description is implemented by

$$
U_g=\sum_{a\in A}P_a\otimes V_{\sigma_a(g)},
$$

where each $V_{\sigma_a(g)}$ permutes the record labels. Paper 04 used exactly
this architecture, with the shift depending on a coherent charge sector.

## 2. The center-preservation theorem

### Theorem 1 -- exact classical-record covariance

Assume the full algebra $\mathcal B(\mathcal H_Q)$ is admitted, including
off-diagonal operators between every pair of sectors. The adjoint action
$\operatorname{Ad}_{U_g}$ restricts to an automorphism of the classical--quantum
algebra that preserves its classical record center if and only if

$$
\sigma_a(g)=\sigma_b(g)
$$

as permutations of $R$ for every $a,b$.

More generally, suppose the controlled action already normalizes a physical
subalgebra $\mathcal M_Q\subseteq\mathcal B(\mathcal H_Q)$. Define $a\sim b$
whenever an admitted operator has a nonzero $P_a\mathcal M_QP_b$ block, and
take the transitive closure. Preservation of the classical center then holds if
and only if $\sigma_a(g)$ is constant on every $\sim$-component.

### Proof

For each classical projector,

$$
U_g z_r U_g^\dagger
=\sum_a P_a\otimes z_{\sigma_a(g)r}
=\sum_{s\in R}
\left(\sum_{a:\,\sigma_a(g)r=s}P_a\right)\otimes z_s.
$$

In the full-controller algebra this is central only if every coefficient of
$z_s$ is a scalar multiple of the identity. Each coefficient is a projection,
so it must be either $0$ or $I$. Hence all nonzero sectors send $r$ to the same
$s$. Applying this for every $r$ gives one sector-independent permutation.

For a restricted controller algebra, commutation with an admitted off-diagonal
block $P_aXP_b$ forces $\sigma_a(g)r=\sigma_b(g)r$ for every $r$. Equality
therefore propagates along the coherence graph. Conversely, constancy on every
coherence component makes the image commute with the restricted algebra and
preserves the corresponding classical center. $\square$

### Corollary 1 -- Paper 04's trilemma

A construction cannot simultaneously retain:

1. a classical record algebra;
2. sector-dependent reversible record covariance; and
3. coherence between sectors on which the permutations differ.

This is independent of dimension, the choice $\mathbb Z_7$, and Python or Rust.

### Corollary 2 -- crossed products do not create classical outcomes

Enlarging the algebra so that the controlled translations become inner can make
the coherent action mathematically well typed. The enlarged algebra is then
noncommutative. It supplies a quantum reference observable or quantum memory,
not by itself a central classical record. A separate classicalization instrument
is still required.

## 3. The information--disturbance theorem

The same boundary appears dynamically. Consider two coherent sectors and a
record-producing isometry

$$
|0\rangle|e_*\rangle\mapsto |\phi_0\rangle|e_0\rangle,
\qquad
|1\rangle|e_*\rangle\mapsto |\phi_1\rangle|e_1\rangle.
$$

For an input $(|0\rangle+|1\rangle)/\sqrt2$, tracing out the record multiplies
the system's off-diagonal term by

$$
c=\langle e_1|e_0\rangle.
$$

If the record states are perfectly distinguishable, $c=0$ and the coherence is
destroyed. If the coherence is perfectly retained, $|c|=1$ and the record states
are identical up to phase, so the record contains no sector information.

For two pure record states, optimal distinguishability $D$ and residual visibility
$V$ obey

$$
D^2+V^2=1,
\qquad
D=\sqrt{1-|c|^2},
\qquad
V=|c|.
$$

For general mixed records, trace distance and fidelity give the corresponding
inequalities. This is the same physical content as the standard which-way
duality bound, not a peculiarity of relational clocks.

If the record is copied into $m$ independent environmental fragments, the pure
branch overlap becomes $c^m$. Redundant accessibility drives distinguishability
toward one and interference visibility toward zero whenever $|c|<1$.

### Theorem 2 -- no informative, perfectly nondisturbing classical clock record

On a code subspace containing coherent superpositions of distinct clock-rate
sectors, an exactly recoverable evolution cannot produce a classical record whose
statistics distinguish those sectors. Equivalently, an informative classical
complementary channel implies disturbance of the code.

This is a special case of information--disturbance and no-broadcasting. The
record may nondestructively report a commuting pointer observable, but it cannot
objectively broadcast arbitrary noncommuting quantum information.

## 4. What established quantum physics says

### 4.1 Quantum reference frames

Operational quantum-reference-frame work defines a frame as a physical quantum
system equipped with a covariant POVM and constructs relative effects and
operational equivalence classes. It supports the lesson that observable quantities
are relational and that familiar absolute observables are recovered only when the
frame is sufficiently localizable. It does not imply that every frame-coordinate
map is a classical record-producing instrument.

Relevant primary sources:

- [Operational Quantum Frames](https://arxiv.org/abs/2304.07021)
- [Operational Quantum Reference Frame Transformations](https://arxiv.org/abs/2303.14002)
- [Relativity of Quantum States and Observables](https://arxiv.org/abs/1604.02836)
- [Symmetry, Reference Frames, and Relational Quantities](https://arxiv.org/abs/1703.10434)
- [Quantum mechanics and the covariance of physical laws in quantum reference frames](https://arxiv.org/abs/1712.07207)

The safe inference is: construct a covariant relational POVM first; then construct
its instrument and physical record carrier separately.

### 4.2 Temporal reference frames and measurements

Measurements relative to nonideal quantum clocks are not uniquely obtained by
conditioning a timeless state. Distinct operational constructions agree in ideal
limits but can differ for finite clocks, and nonideal clocks can induce temporal
nonlocality or nonunitarity in the conditioned description.

- [Measurement events relative to temporal quantum reference frames](https://arxiv.org/abs/2308.10967)
- [The Trinity of Relational Quantum Dynamics](https://arxiv.org/abs/1912.00033)
- [Interacting quantum clocks](https://arxiv.org/abs/1712.00081)

This makes a finite-resource clock instrument, not an ideal phase projector, the
right primitive for the next test.

### 4.3 Symmetry and the WAY/asymmetry resource

Under symmetric processing, perfectly measuring an asymmetric observable requires
a perfectly asymmetric reference resource. Finite, nonorthogonal group orbits lead
to imperfect measurement or disturbance. This is the resource-theoretic form of the
Wigner--Araki--Yanase limitation.

- [An information-theoretic account of the Wigner--Araki--Yanase theorem](https://arxiv.org/abs/1212.3378)
- [The WAY theorem and the quantum resource theory of asymmetry](https://arxiv.org/abs/1209.0921)
- [Quantum measurements constrained by symmetry](https://arxiv.org/abs/1303.6536)
- [Reference frames, superselection rules, and quantum information](https://arxiv.org/abs/quant-ph/0610030)

Therefore a claimed exact clock reading must carry an explicit reference/asymmetry
resource ledger. A perfect, cost-free, finite reference is not available merely by
declaring covariance.

### 4.4 Finite autonomous clocks

Finite clocks can approximate ideal control well, and quantum clocks can outperform
classical clocks of the same information capacity. But autonomous clock performance
has backreaction and thermodynamic costs; accuracy, resolution, dimension, energy,
and entropy production are physical resources.

- [Autonomous quantum machines and the finite sized Quasi-Ideal clock](https://arxiv.org/abs/1607.04591)
- [Autonomous quantum clocks: does thermodynamics limit our ability to measure time?](https://arxiv.org/abs/1609.06704)
- [Quantum clocks are more precise than classical ones](https://arxiv.org/abs/1806.00491)

The correct target is consequently an error-versus-resource theorem, not exact
ideal clock behavior at finite cost.

### 4.5 Classical objectivity and redundant records

Decoherence suppresses selected coherences, but classical objectivity requires more
than a diagonal reduced density matrix. Spectrum-broadcast structure captures the
redundant, independently readable imprint of a commuting pointer variable in
multiple environmental fragments.

- [Objectivity Through State Broadcasting](https://arxiv.org/abs/1305.3247)
- [Quantum origins of objectivity](https://arxiv.org/abs/1312.6588)
- [Roads to objectivity](https://arxiv.org/abs/2007.04276)
- [Noncommuting mixed states cannot be broadcast](https://arxiv.org/abs/quant-ph/9511010)
- [Fringe Visibility and Which-Way Information](https://doi.org/10.1103/PhysRevLett.77.2154)

This gives a demanding operational definition of a classical clock record: several
disjoint readers should recover the same label without appreciably disturbing the
record, and the residual coherence cost must be measured.

### 4.6 Crossed products and relativistic QFT

Crossed-product constructions can supply invariant joint field--reference algebras
and are important in QFT and semiclassical gravity. They are promising for the
coherent layer, not a derivation of a classical outcome or actual event.

- [Quantum reference frames, measurement schemes and the type of local algebras in QFT](https://arxiv.org/abs/2403.11973)
- [Quantum Reference Frames from Top-Down Crossed Products](https://arxiv.org/abs/2405.13884)

The algebraic enlargement must therefore remain upstream of, and distinct from,
the record-producing stochastic instrument.

## 5. What Barandes's ontology adds

Barandes's stochastic--quantum correspondence treats the Hilbert-space description
as a representation of an indivisible stochastic process on a configuration space.
The configuration and the stochastic law are primary; wave functions and
coherences are representational. Measurements are ordinary physical interactions
within a larger stochastic process, and a device ends in one of its outcome
configurations with the appropriate probability.

- [The Stochastic-Quantum Correspondence](https://arxiv.org/abs/2302.10778)
- [Quantum Systems as Indivisible Stochastic Processes](https://arxiv.org/abs/2507.21192)
- [A Deflationary Account of Quantum Theory](https://arxiv.org/abs/2602.01043)

Applied here, Barandes would likely insist on the following separation:

1. The coherent pointer in the Hilbert dilation is not automatically the actual
   record configuration.
2. Decoherence is correlation leakage in the Hilbert representation; by itself it
   does not identify which configuration actually obtains.
3. A clock outcome must appear in the enlarged configuration space and in the
   indivisible transition law for clock plus apparatus plus environment.
4. A division event, if claimed, must be proved from the stochastic law rather than
   inferred from diagonalization or from a convenient intermediate time slice.

This strengthens, rather than weakens, the Paper 04 rejection. The missing object is
not an extra projector. It is the physical record-producing process and its actual
configuration outcome.

## 6. The viable architectures

| Architecture | Keeps controller coherence? | Produces a classical record? | Covariant? | Physical cost or missing item |
|---|---:|---:|---:|---|
| State-independent record permutation | Yes | Yes | Yes, when one permutation acts on all coherent sectors | Cannot encode sector-dependent rate |
| Sector superselection | No cross-sector coherence admitted | Yes | Yes componentwise | Changes the observable algebra/ontology |
| Decohering measurement | No, to the measured resolution | Yes | Yes if instrument and apparatus are covariant | Entropy, disturbance, apparatus, preferred pointer interaction |
| Coherent quantum memory | Yes | No, not yet | Potentially | Needs later classicalization/actualization |
| Crossed-product record algebra | Yes | Not centrally classical | Potentially | Needs a chosen commutative event algebra and instrument |
| Relational invariant POVM | Sometimes, within degenerate fibers | Yes after an instrument | Yes by construction | Resolution/localizability/asymmetry limits |
| Finite approximate clock | Approximately | Approximately | Approximately | Error, energy, dimension, backreaction, calibration |
| Redundant objective record | Only for unrecorded conjugate coherences | Yes, strongly | Must be checked | Environment fragments and spectrum-broadcast dynamics |
| Barandes configuration record | Hilbert coherence is secondary | Yes ontologically if law supplies it | Must be law-level | Configuration space, indivisible joint law, division/actuality |

No row gives exact informative classical recording, exact sector coherence, and
sector-dependent covariance simultaneously. That absence is the theorem, not a
failure of imagination.

### 6.1 An exact relational-record witness already latent in the Paper 04 parent

The rejected Paper 04 candidate tried to retain the raw A coordinate $\alpha$ as
a classical record even though its gauge transformation depended on the coherent
charge $q$:

$$
\alpha\longmapsto\alpha+(1+q)g.
$$

The B coordinate transforms as

$$
\beta\longmapsto\beta+2g.
$$

The combination

$$
y=2\alpha-(1+q)\beta\pmod 7
$$

is therefore exactly gauge invariant. Define the projection-valued measure

$$
E_y=
\sum_{\substack{q,\alpha,\beta:\\
2\alpha-(1+q)\beta=y}}
P_q\otimes|\alpha\rangle\langle\alpha|_A
\otimes|\beta\rangle\langle\beta|_B\otimes I_M.
$$

The $E_y$ are mutually orthogonal, sum to the identity, and commute with the
frozen gauge action. Consequently

$$
W_{\rm rel}=\sum_y E_y\otimes|y\rangle_{R_{\rm rel}}
$$

is an exact gauge-invariant measurement isometry when the output record transforms
trivially. Its Lüders instrument is complete and preserves the physical subspace.

More explicitly, for a neutral seven-state pointer with cyclic shift $X$, the
unitary

$$
V_{\rm rel}=\sum_yE_y\otimes X^y
$$

commutes with the gauge representation and writes $y$ into a pointer initialized
at zero. This constructs an exact global symmetric premeasurement. It also admits
an exact three-stage factorization through correctly typed covariant quantum
memories: the partial values transform nontrivially and become invariant only at
the final boundary. They must not be read as classical records along the way.
Autonomous switching and spacetime locality remain unconstructed. That boundary is
analyzed separately in
`/private/tmp/p04_relational_record_implementation_analysis.md`.

The construction is general. If a group permutes joint frame/controller basis
labels $x$ and $f(x)$ is constant on its orbits, then

$$
E_y=\sum_{x:f(x)=y}|x\rangle\langle x|
$$

defines an invariant PVM. The associated measurement preserves precisely the
coherences lying inside one $f$-fiber and destroys coherences between different
record values. Thus invariant relational coarse graining is the exact condition
under which an informative classical record and some quantum coherence can coexist;
it never preserves coherence that the record itself distinguishes.

This does not contradict the center theorem. The raw A record attempted to make a
frame-dependent label transform sector by sector. The new instrument instead
measures one invariant quantum observable and writes its invariant eigenvalue into
one ordinary classical register.

The witness has nontrivial behavior on the frozen sources:

$$
\begin{array}{c|c}
\text{source}&y\\
\hline
\mathrm{U0}&0\\
\mathrm{UAO}&2\\
\mathrm{UBO}&-1\equiv6
\end{array}
$$

For both coherent components of UCOH,

$$
(q,\alpha,\beta)=(0,s,2s)
\quad\text{or}\quad
(1,2s,2s),
$$

and each gives $y=0$. Hence

$$
E_0|\Psi_{\rm UCOH}\rangle=|\Psi_{\rm UCOH}\rangle.
$$

The relational measurement records $y=0$ with certainty without destroying the
UCOH coherence. It succeeds because it learns nothing about which $q$ component
occurred; both components belong to the same degenerate relational eigenspace.

This is the strongest positive route found in the investigation. Its scope is also
exact:

- it records a gauge-invariant clock relation or offset;
- it does not produce either standalone clock coordinate;
- it does not identify a monotonic sequence of events;
- it does not produce an arrow of time;
- it does not make the gauge-orbit parameter physical;
- it does not prove objectivity, division, or actuality.
- it is a joint parent-level observable involving A, B, and Q; a typed sequential
  quantum-memory circuit exists, but its autonomous scheduling and spacetime-local
  realization have not been constructed;
- on the stopped $q=6$ sector it remains an invariant label but is not evidence
  that A functions as a clock.

Einstein's operational intuition favors precisely this kind of object: physical
time is established through coincidences and comparisons among clocks, not by an
unobservable absolute coordinate. The next unit should therefore lead with this
invariant PVM as its exact positive witness, while keeping the classicalization,
future-reader, finite-resource, and Barandes-configuration gates fully open.

## 7. Recommended two-layer architecture

The most conservative architecture has two explicitly different layers.

### Layer Q -- coherent relational reference

Construct:

- the physical constrained Hilbert or algebraic state space;
- a covariant frame POVM;
- invariant relative observables;
- the full noncommutative quantum memory;
- frame-change maps only on their proven common domain;
- an exact resource ledger for localization/asymmetry.

This layer may preserve coherent superpositions of clock rates. Its outputs are
quantum information, not yet facts.

### Layer R -- record-producing physical process

Construct:

- apparatus and environment degrees of freedom;
- a covariant instrument with a declared commutative outcome algebra;
- an explicit quantum-to-classical channel or stochastic interaction;
- the post-measurement state and all future readers;
- redundancy/objectivity witnesses;
- disturbance, entropy, energy, and accuracy costs;
- in a Barandes route, the actual configuration space and indivisible law.

The interface $Q\to R$ is allowed to be irreversible. Indeed, if it is informative,
some irreversibility or discarded coherence is normally the point.

The three coherent arithmetic stages can also be embedded in one fixed symmetric
Hamiltonian using a four-state perfect-transfer program chain. This removes
time-dependent laboratory switching but not the background evolution parameter,
initial program endpoint, or reversible program ordering. It is therefore a valid
autonomous laboratory controller and an invalid proof of emergent chronology. The
exact construction and firewall appear in the companion implementation analysis.

The invariant label can additionally be copied into any finite number of neutral
orthogonal memories. After an explicit dephasing or inaccessible-fragment channel,
this yields an exact redundant operational record whose independent readers agree.
Only the commuting label is broadcast. This constructs operational objectivity for
the registered coarse graining, while leaving complete division and actual outcome
selection unconstructed.

This is not dualistic. Both layers describe one physical apparatus at different
levels of operational access. The distinction prevents a reversible coordinate
change from impersonating an irreversible fact-formation process.

## 8. A bounded successor unit

### Proposed title

**Quantum reference records: covariance, coherence, and the formation of clock facts**

### Immutable base

- repository base: v17 commit `1e27457`;
- Paper 03 v3.2 terminal operational representation;
- Paper 04 terminal rejection and exact salvage only;
- no modification of the seven-state fixture to fit a desired answer;
- no import of spacetime, gravity, or a preferred external time as an explanation.

### One-attempt rule

Freeze the complete mathematical law, target theorems, resource ledger, and
experimental controls before construction. Permit code-only repairs. Any semantic
counterexample terminates the unit; there is no automatic v2 chain.

### Target theorem package

1. **Center theorem.** Prove Theorem 1 for finite and standard-Borel record
   algebras, including restricted coherence graphs.
2. **Instrument theorem.** Characterize covariant instruments whose classical
   outcome algebra is preserved by the symmetry.
3. **Information--disturbance theorem.** Bound retained controller coherence by
   record distinguishability.
4. **Redundancy theorem.** Relate $m$ independently readable copies to coherence
   decay and spectrum-broadcast error.
5. **WAY resource theorem.** Bound accuracy by frame asymmetry/localizability.
6. **Relational-outcome theorem.** Determine when an invariant relative POVM avoids
   sector-dependent label covariance.
7. **Typed staging and classicalization theorem.** Verify each intermediate
   covariant quantum-memory boundary, type the final quantum-memory-to-classical-
   record arrow, and prove all-reader future sufficiency in the licensed
   experiment family.
8. **Barandes lift test.** Determine whether a configuration-space stochastic model
   reproduces the same instrument without treating Hilbert coherence as ontology.
9. **Division test.** Keep stable record, objective record, and complete division as
   independent coordinates.
10. **Finite-resource theorem.** State explicit error bounds rather than replacing
    finite devices by ideal clocks.
11. **No-hidden-reference theorem.** Account for every asymmetry source, scheduler,
    calibration reference, and external phase standard.
12. **No-gravity promotion theorem.** Clock-record success alone does not yield
    causal order, metric, proper time, or Einstein dynamics.

## 9. Required hostile controls

1. Quantum pointer renamed as a classical record.
2. Diagonal reduced state treated as an actual outcome.
3. Identity-only covariance family.
4. Outcome label transformed by an unrecorded coherent control.
5. Hidden external phase or time reference.
6. Source-dependent apparatus chosen after seeing the input.
7. Superselection silently imposed after freezing coherent sources.
8. Dephasing silently inserted as a frame change.
9. Quantum eraser counted as simultaneous persistent classical record.
10. Record readable by only one privileged global observable.
11. Redundant copies that share one hidden memory rather than independent fragments.
12. Approximate equality promoted to exact covariance.
13. Accuracy fitted on the evaluation cases.
14. Zero-resolution clock passing a covariance check.
15. Infinite energy or dimension hidden inside an ideal localization limit.
16. POVM supplied without an instrument.
17. Instrument supplied without post-measurement states.
18. Post-measurement states supplied without future readers.
19. Stable record mistaken for a complete division.
20. Classical record algebra changed to a crossed product after a failure.
21. Controller coherence tested only with commuting readers.
22. Record objectivity inferred from mutual information alone.
23. Environment traced out without a physical accessibility statement.
24. External laboratory time used to prove that internal time emerged.
25. One successful finite fixture generalized to arbitrary groups or QFT.
26. Clock disturbance ignored when it changes subsequent dynamics.
27. Covariant state map assumed to lift to a covariant complete instrument.
28. Barandes terminology used without a configuration, stochastic law, and actual
    outcome variable.

## 10. The decisive laboratory control

The cleanest experiment is a quantum-controlled clock-rate interferometer.

1. Prepare a rate/control qubit in $(|0\rangle+|1\rangle)/\sqrt2$.
2. Couple a finite clock so the two sectors accumulate distinct relational phase
   histories.
3. Couple the clock reading to $m$ independently addressable memory fragments.
4. Measure the optimal distinguishability $D_m$ of the recorded rate-dependent
   readings.
5. Recombine the control sectors and measure interference visibility $V_m$.
6. Test covariance under at least one nonidentity change of relational frame,
   transforming the POVM, apparatus, memories, and calibration together.
7. Run a quantum-eraser control before any memory becomes irreversible.
8. Run a classicalization control in which the memories are amplified and
   redundantly read.

For pure conditional memory states with one-copy overlap $c$,

$$
V_m=|c|^m,
\qquad
D_m=\sqrt{1-|c|^{2m}},
\qquad
D_m^2+V_m^2=1.
$$

The experiment should not be sold as discovering time. Its value is sharper: it
tests the exact physical price of turning a relational quantum clock correlation
into a public classical fact.

An implementation platform could use superconducting qubits, trapped ions, or
photonic path/phase degrees of freedom. Platform choice must follow, not precede,
the frozen operational equivalence class.

The discriminator is experimentally conventional even though its interpretation
here is new. Which-path dephasing has been directly observed in electronic
interferometers, and internal quantum clocks have been proposed precisely as
which-path detectors whose proper-time distinguishability reduces visibility:

- [Dephasing in electron interference by a which-path detector](https://www.nature.com/articles/36057)
- [Quantum interferometric visibility as a witness of general-relativistic proper time](https://arxiv.org/abs/1105.4531)
- [Effect of environment on the interferometry of clocks](https://arxiv.org/abs/2002.05883)
- [Quantum test of local position invariance with internal clock interferometry](https://arxiv.org/abs/2301.11258)

The proposed successor would not need to observe a gravitational effect. Its first
empirical target is the record/coherence law itself, with the relational invariant
record as a protected-degeneracy control and the raw sector-sensitive reading as
the dephasing arm.

## 11. Outcome ladder

The unit must permit all of the following terminal outcomes.

1. **CLASSICAL-RECORD-INCOMPATIBLE.** No admitted instrument supplies the required
   record without violating covariance or coherence constraints.
2. **QUANTUM-REFERENCE-OBSERVABLE-ONLY.** A covariant relative POVM exists, but no
   classical record has been constructed.
3. **COHERENT-QUANTUM-MEMORY-CONSTRUCTED.** A full quantum pointer exists with a
   later classicalization step still unconstructed.
4. **APPROXIMATE-COVARIANT-RECORD.** A finite-resource instrument succeeds with
   explicit error, disturbance, and calibration bounds.
5. **OBJECTIVE-CLASSICAL-RECORD.** Redundant independent readers recover the same
   commuting record within a frozen tolerance.
6. **BARANDES-CONFIGURATION-RECORD.** An independently specified indivisible
   stochastic model contains the apparatus outcome as an actual configuration.
7. **COMPLETE-DIVISION-CONSTRUCTED.** Only if exact future sufficiency is proved;
   this is not implied by any earlier rung.

None of these outcomes awards intrinsic chronology, proper time, spacetime,
gravity, or actuality beyond its explicit stochastic configuration model.

## 12. Why this is the right next scientific move

The programme had been trying to make a clock by combining:

- a constrained quantum state;
- a frame reduction;
- a phase label;
- a retained classical record.

Paper 04 showed that these ingredients do not compose automatically. The root
mistake was conflating three distinct operations:

1. changing a quantum description;
2. coherently storing quantum information;
3. creating a classical fact.

Known quantum physics already says that the third operation is constrained by
information--disturbance, symmetry resources, decoherence, and thermodynamics.
Barandes adds the ontological demand that the fact be an actual configuration of
the enlarged physical process, not merely a branch of a Hilbert-space dilation.

A successor centered on that interface is therefore conservative, physically
motivated, and experimentally connected. It does not invent a new substrate. It
asks exactly where ordinary quantum physics changes from coherent relational
possibility to a stable physical record, and whether the Barandes ontology can
represent that transition without extra ad hoc structure.

## 13. Distance to gravity

Even the strongest outcome would close only an operational prerequisite for
geometry. Physical clocks are needed to calibrate duration and radar distance, but
gravity additionally requires:

- intrinsic causal ordering;
- a family of localized events or regions;
- dimension and Lorentzian signature;
- scale and metric reconstruction;
- dynamical stress--energy observables;
- backreaction and constraint propagation;
- equivalence-principle tests;
- agreement of clock, propagation, and order-volume routes.

Crossed products and quantum clocks appear in semiclassical-gravity research, but
using those formalisms does not derive gravity. The proposed unit should therefore
be judged valuable if it clarifies the record interface, even if the gravity
coordinate remains exactly closed.

## 14. Recommendation

Do not repair Paper 04 and do not open a general relational-time construction yet.
If the user authorizes a successor, freeze one model-independent quantum-record
boundary unit on base `1e27457` with the theorem package and attacks above.

The preferred construction order is:

1. center-preservation/no-go theorem;
2. covariant relational POVM;
3. explicit instrument and quantum memory;
4. classicalization and redundant-reader test;
5. finite-resource error tradeoff;
6. optional Barandes configuration-space lift;
7. only then reconsider operational clocks.

That order follows the physics. It prevents the programme from obtaining time by
putting a classical clock into the notation before the universe has physically
made a record.
