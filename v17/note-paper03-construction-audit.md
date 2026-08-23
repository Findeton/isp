# Paper 03 construction author audit

Date: 2026-08-22

Status: **RESULT-NEUTRAL AUTHOR AUDIT — READY FOR INDEPENDENT REVIEW**

This is not an independent review and awards no Paper 03 coordinate.

Audited candidate:
`v17/paper-03-relativistic-quantum-operational-adequacy.md`, SHA-256
`6506c950ec26354e063960631aaabfb759216ddf0822f3be8057dad2250036af`,
1,068 LF / 46,560 bytes, committed at
`a2a0b366ce8b1d34cd2b2235f09b8938bb08615a`.

Frozen authority:
`v17/note-paper03-relativistic-quantum-operational-adequacy-pin.md`, SHA-256
`0486f7ce04bc70c5f14d7609e4baf9244dc02195248d45d66ccb3c8a46813696`.

## 1. Disposition

The author audit independently traces the candidate through the pin's theorem
targets, 32 controls, 76 attacks, product, and scope walls. No decisive
mathematical counterexample was found. The candidate is ready for three
mutually blind reviews.

The likely ceiling remains rung 7, but it is not pre-awarded. Five scope seams
must be treated as binding during review:

1. the comparator and causal order are declared inputs;
2. states pull back under embeddings and do not canonically push forward;
3. Bell existence and the exact split-qubit arithmetic are separate controls;
4. the positive history model is global predictive bookkeeping, not local
   explanatory microphysics; and
5. no type-III, split, gauge, sector, Hadamard, or free-field fact may migrate
   from one named model into another.

## 2. Authentication and chronology

The pin, pin audit, Paper 01 adjudication, Paper 02 v2 candidate/adjudication,
empirical contract, and era charter hashes all reproduce. The candidate was
absent at pin freeze and remained the sole Paper 03 construction path before
commit #30. No review protocol or report existed when it froze.

The one untracked v16 handoff note is outside this unit and remains untouched.

## 3. Mechanical closure

The candidate contains:

```text
18 numbered theorem targets reconstructed in Theorem 11.1
one variance-correct state/covariance convention
one explicit theorem quantifier ledger
32/32 two-way controls
76/76 continuously dispositioned hostile attacks
31/31 product coordinates
one claimed green-unreviewed rung
one primary-source ledger
one explicit Barandes/ontology comparison
```

There is no evaluator, runtime, generated data, fit, lookup table, lattice, or
hidden cutoff.

## 4. Core mathematical trace

### 4.1 Variance

For $\psi:M\to N$, observables move by $\alpha_\psi$ and states restrict by

$$
\psi^*\nu=\nu\circ\alpha_\psi.
$$

The candidate never needs a canonical extension of an arbitrary state. Its
packet morphisms are intentionally partial: only transports for which every
theory, coupling, state comparison, record, and reader field is supplied are
admitted. This is coherent with locally covariant AQFT.

The phrase “compatible state class” in Section 1 is binding. For normal
represented packets, normal CP instruments preserve normality because the
posterior is a positive scalar multiple of a normal functional composed with
a normal CP map. Hadamard or other narrower classes require packet-specific
closure; absent that proof, the packet is inadmissible rather than evidence
for a universal closure theorem.

### 4.2 Instrument

With the frozen scattering convention,

$$
\mathcal J_{s,B}(A)
=(\operatorname{id}\otimes\sigma)\Theta(A\otimes B)
$$

is CP for $B\ge0$. The map $A\mapsto A\otimes B$ is CP, $\Theta$ is a
`*`-automorphism, and partial evaluation in a state is CP. A complete probe
POVM sums to $\mathcal J_{s,1}$ and normalizes probabilities. Positive-support
posteriors are states; zero-support branches carry zero mass.

The nonselective map need not be the identity in the causal future of the
coupling. The theorem uses identity only on observables spacelike to the
coupling region, where scattering locality supplies it.

### 4.3 Causal factorization

Causally ordered couplings compose in physical order. For causally disjoint
couplings, the system--probe causal-factorization theorem gives equal
instruments in either ordering. Adjacent swaps of incomparable elements
connect any two finite linear extensions, so the complete joint map and law
are schedule independent.

This is not a theorem for arbitrary CP maps and not a statement that timelike
orders commute.

### 4.4 No-signalling and steering

For a complete local POVM $\{B_a\}$ and remote effect $D_b$,

$$
\sum_a p(a,b)
=\omega(\mathcal J_{A,1}(D_b))
=\omega(D_b).
$$

The first equality needs completeness; the second needs operation locality.
Selective conditionals may differ because the branch map is not the complete
map. The singlet calibration demonstrates the distinction exactly and makes
the classical-record requirement visible.

### 4.5 Positive histories

For each branch, the substochastic kernel

$$
K_i(r,d\lambda'\mid\lambda)
=p_i(r\mid\lambda)\delta_{U_i(\lambda,r)}(d\lambda')
$$

has the correct mass. Iteration reproduces the composed instrument effect by
induction, and summing suffix outcomes proves normalization and prefix
coherence.

For finite outcomes on weak-$*$ Borel state spaces, evaluation and normalized
update are measurable on each positive-support set. Standard-Borel continuous
outcomes remain conditional on the packet's measurable instrument and regular
conditioning. No theorem is claimed on pathological quotient state spaces.

The representation is deliberately predictive. It takes the AQFT state or
complete conditional process object as the latent state. This proves
positive-history adequacy and blocks “relativistic QFT forbids every positive
history” claims. It does not reduce or explain the quantum predictive object.

## 5. Model-separation audit

### 5.1 Bell

The candidate makes two separate claims:

1. Summers--Werner supplies an existential QFT theorem: commuting spacelike
   local algebras can violate Bell inequalities in named states/models.
2. A split-qubit matrix calibration supplies exact $2\sqrt2$ arithmetic and
   a transparent steering/no-signalling premise ledger.

The second is not offered as the proof of the first. The first does not by
itself construct a Fewster--Verch probe that measures every ideal Bell
observable. Consequently the supported coordinate is **Bell compatibility**,
not a universal exact Bell-probe realization theorem.

### 5.2 Preparation contextuality

The two ensemble decompositions of $I/2$ are used only in the declared split
matrix-subalgebra/finite-region control. The packet fixes the same
complementary state, so both mixtures have one global barycenter and complete
operational profile in that control. The ontic measures differ without
procedure tags. No claim is made that every QFT local algebra comes with that
factorization.

### 5.3 Type III and split

The main construction needs no regional trace, density matrix, finite Kraus
list, or Hilbert factor. T11 is therefore a genuine refusal theorem.
Positive type-III classification remains model-specific; if reviewers find
that the cited model theorem is insufficient, the correct disposition is to
narrow that positive example, not to demote the instrument/no-signalling
theorems that use algebraic functionals only.

The split property is invoked only with separation and its own hypotheses.
The type-I factor is an interpolation for a control, not a physical lattice
cell or a universal regional decomposition.

### 5.4 Gauge and sectors

The candidate constructs a typing firewall, not a gauge theory. The DHR and
curved-sector sources show that charge/statistics conclusions require
localization, topology, conjugacy, and symmetry hypotheses. No gauge group or
particle spectrum appears in the result product.

## 6. Quotient and contextuality audit

$\mathcal P_{\rm rel}$ retains physical region, interaction, state,
calibration, record, sector, and reader data. Its presentation groupoid removes
only charts, bound names, isomorphic transport, and proved-disjoint
serialization. Therefore the quotient does not identify a physical timelike
ordering or use spacetime coordinates as hidden procedure tags.

Complete operational equivalence quantifies over constructor-closed contexts.
The standard contextual-equivalence substitution proof establishes
congruence. The result is restricted to the reachable registered interface;
new physical readers can refine it.

The preparation-contextual positive model and idle-fiber theorem are
compatible. Erasing a contextual ensemble decomposition is not an admitted
idle-fiber projection if it breaks the trusted-mixture lineage. Conversely,
an independent ignored variable with a positive projection is not selected by
operational data.

## 7. Preferred-frame and background audit

The actual positive result is:

```text
no operationally visible preferred frame in the registered packet family.
```

The candidate does not infer:

```text
no preferred structure in every microscopic completion.
```

Similarly, `Loc`, its dimension, metric, orientation, time orientation, region
net, state class, and field dynamics are standard-theory comparator inputs.
Local covariance and relative Cauchy evolution are not background
independence, metric quantization, or Einstein dynamics.

## 8. Pin-target matrix

| target | audit status | binding scope |
|---|---|---|
| T1 | covered | algebra/representation/measurability types explicit |
| T2 | covered | covariant observables, contravariant states |
| T2b | covered conditionally | no natural state; packet-specific class closure |
| T3 | covered | localized system--probe schemes only |
| T4 | covered conditionally | exact causal-factorization hypothesis |
| T5 | covered | complete nonselective localized operation |
| T6 | covered | selective steering plus record/no-control cost |
| T7 | covered | finite disjoint families, full map equality |
| T8 | covered as compatibility | QFT existence and exact matrix calibration remain separate |
| T9 | covered with cost | global contextual predictive histories |
| T10 | covered | reachable quotient and admitted idle fibers |
| T11 | covered primarily as refusal | positive type-III facts model-specific |
| T12 | covered conditionally | split/nuclearity/separation hypotheses |
| T13 | covered | cyclic density is not deterministic control |
| T14 | covered as firewall | no gauge/sector selection |
| T15 | covered as firewall | no labeled-particle ontology/Fock promotion |
| T16 | covered as scope | abstract-net plus named controls; no hidden cutoff |
| T17 | covered operationally | cannot exclude idle microstructure |
| T18 | covered | no universal law, trajectory, actuality, or spacetime ontology |

## 9. Control and attack closure

All 32 control rows have both a positive construction and a refusal. All 76
attacks are individually mapped to a definition, theorem, or explicit
nonimplication. The high-risk review targets are:

1. whether the state-class closure used by a named example is actually proved;
2. whether the scattering convention and composition order remain consistent;
3. whether no-signalling is ever inferred from commutators alone;
4. whether the Bell and split controls are accidentally conjoined;
5. whether the contextual preparation has one complete global barycenter;
6. whether type-III/split/gauge claims exceed their source hypotheses;
7. whether standard-Borel measurability is assumed outside its domain;
8. whether an idle preferred frame is silently declared absent; and
9. whether the global positive representation is misreported as explanatory
   ontology.

## 10. Product and rung audit

The 31-coordinate product is complete and mixed. The operational coordinates
can be positive while `actuality` is unconstructed, `barandes` incomplete,
and `ontology` unselected. Rung 7 is the maximum compatible with the
construction because rungs 8--9 require new physical objects absent from both
pin and candidate.

The provisional rung-7 label is semantically accurate only with its final
phrase: **WITH-GLOBAL-ONTOLOGY-DEBT**. Removing that phrase or treating it as
editorial would overclaim the result.

## 11. Disposition and next action

Disposition: `READY-FOR-INDEPENDENT-REVIEW`.

No candidate edit or implementation is authorized. The next action is a
result-neutral hostile-review protocol binding three mutually blind lenses:

1. AQFT/category/covariance;
2. quantum measurement/probability/Bell; and
3. ontology/locality/gauge/continuum.

Paper 04 and all clocks, spacetime-emergence, matter--geometry, and gravity
claims remain closed.
