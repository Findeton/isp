# Relational sum over processes

## A stochastic-first autonomous extension of \(\mathbf\Gamma_D\)

### Abstract

Paper 13D constructs an exact point-free conditional law
\(\mathbf\Gamma_D\). Paper 17B proves that this law does not determine how
often different unmarked process complexes occur. This paper asks whether
known quantum physics and the stochastic-quantum correspondence supply a
principled successor architecture.

The answer is constructive but deliberately incomplete. Feynman's
sum-over-histories principle, decoherence-functional quantum mechanics,
general-boundary gluing, process-matrix laboratory discipline, and group
field theory jointly motivate a dimension-neutral sum over complete typed
relational processes. They do not determine its process activities, relative
phases, or continuum measure. We prove an occurrence-gauge theorem: arbitrary
positive process activities, and in the quantum case arbitrary sector phases,
are invisible to every accepted conditional probability in
\(\mathbf\Gamma_D\). A Hilbert-space or amplitude representation therefore
exists nonuniquely and cannot by itself close the cosmology.

The primary successor target is a complete point-free indivisible stochastic
law \(\Gamma_\star\). A relational field action can organize that law, and a
complex potential, unitary dilation, or decoherence functional may represent
it, but none is automatically fundamental. Its process couplings are new
physical constants. They must be fixed by nongeometric microscopic evidence
or an independently proved consistency principle before any dimension
analysis. The first live discriminator asks whether a “both alternatives”
whole experiment violates the calibrated mixture of its one-alternative
controls. A nonzero residual refutes mixture factorization; it does not choose
between a fundamental complex amplitude and a larger indivisible stochastic
law. Neither representation presently selects a dimension, metric, or actual
history.

## 1. Binding input and question

This investigation binds:

- terminal Paper 13D law SHA-256
  `3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9`;
- terminal Paper 13D adjudication SHA-256
  `ae2c4ef066335c39a0b8057c897c947b06e4270be67d1ed3ec59bf8d6d0a00c9`;
- Paper 17B, ordinary SHA-256
  `e426fd19d29fa0fa8621b4e6402e9b45fc3d4d820164dc6322b920dfa1e38ef9`;
  and
- Paper 17B construction note, ordinary SHA-256
  `55c08b40e74a9706feee69c5f0080b4247f675bfc5db04294c5edf74fa607307`.

The question is

> Can currently known quantum principles motivate one autonomous,
> point-free law over complete relational process complexes while retaining
> \(\mathbf\Gamma_D\) exactly as its conditional experimental sector?

The word *motivate* is important. A familiar formalism does not count as a
derivation of its action, coupling constants, base measure, or boundary
state.

We permanently refuse to infer actualization, chronology, dimension,
signature, topology, scale, metric, curvature, gravity, or continuum physics
from the existence of a formal sum.

## 2. What is missing

Let \(\mathcal X\) be the groupoid of unmarked physical process complexes and
let \(\mathcal H_\chi\) be the complete physical history classes over
\(\chi\). Paper 13D supplies

\[
  \Gamma_D(H\mid \chi,a),
  \qquad H\in\mathcal H_\chi,
\]

for every admitted typed marking \(a\). It does not supply a relative
propensity between \(\chi\) and \(\chi'\).

There are therefore three distinct layers:

1. \(\mathsf{Exec}_D\): which typed operations are lawful;
2. \(\mathbf\Gamma_D\): what outcomes occur conditional on a complete
   experiment; and
3. an autonomous occurrence law: which unmarked process complex exists.

Quantum notation does not collapse these layers. An amplitude assigned only
after selecting \(\chi\) is still conditional dynamics. A cosmological law
requires relative weights or amplitudes across different \(\chi\).

## 3. Fundamental law and optional quantum representation

### 3.1 Fundamental indivisible stochastic extension

The conservative extension is

\[
 \Gamma_\star(\chi,H)
 =\Pi_{\rm phys}(\chi)\,\Gamma_D(H\mid\chi),
\]

with a point-free normalized process marginal \(\Pi_{\rm phys}\).

This is not a Markovization. \(H\) remains a complete indivisible history,
and factorization is permitted only at Paper 13D's certified complete
divisions. Native nondivision cuts remain nondivisions.

This branch is closest to the Paper 13D ontology: one process complex and one
history are actual, while probability is a propensity over alternatives.

### 3.2 Optional quantal representation or extension

A history-level quantum representation or enlarged extension may assign a
decoherence functional

\[
 D_\star(A,B),
 \qquad A,B\subseteq
 \Omega_\star:=\{(\chi,H)\},
\]

which is:

1. hermitian, \(D_\star(A,B)=D_\star(B,A)^*\);
2. finitely biadditive on disjoint alternatives;
3. normalized, \(D_\star(\Omega_\star,\Omega_\star)=1\);
4. strongly positive on every finite event family; and
5. invariant under the accepted presentation groupoid.

The associated quantum measure is

\[
 \mu_\star(A)=D_\star(A,A).
\]

Ordinary probabilities are available only on decoherent partitions. Exact
recovery of Paper 13D therefore requires, for every admitted marked sector,

\[
 D_{\chi,a}(H,H')
 =\delta_{HH'}\Gamma_D(H\mid\chi,a)
\]

on the complete physical-history partition, or an operationally equivalent
recorded coarse graining.

If this object is taken as fundamental, it is a larger ontology: before
decoherence, alternative process complexes are amplitude alternatives rather
than ordinary mutually exclusive ontic possibilities. Barandes's
stochastic-quantum correspondence offers a different reading. There the
complete stochastic law is fundamental and Hilbert-space potentials,
unitaries, and density matrices are secondary, partly gauge-dependent
representations. The mere existence of \(D_\star\) or complex amplitudes does
not decide between these readings.

### 3.3 Barandes-first hierarchy

The hierarchy closest to the accepted Paper 13D ontology is

\[
 \text{complete indivisible }\Gamma_\star
 \longrightarrow
 \text{complex potential or dilation}
 \longrightarrow
 \text{Hilbert-space predictions}.
\]

Interference then means that a complete “both alternatives” law is not the
classical mixture of two different complete one-alternative laws. It need not
mean that the alternatives are fundamental ontic process complexes carrying
primitive complex amplitudes.

Decoherence is likewise derived after the whole stochastic law and its
environment are specified: correlations leak into environmental degrees of
freedom, and the reduced Hilbert representation loses its off-diagonal
coherences. This explains stable classical-looking alternatives but does not
select the missing autonomous law or its process marginal.

## 4. The occurrence-gauge theorem

### Theorem 1 -- classical occurrence gauge

Let \(W(\chi,H\mid a)\) be any positive unnormalized joint weight whose
conditional histories recover \(\Gamma_D\). For every positive point-free
function \(c(\chi)\), define

\[
 W_c(\chi,H\mid a)=c(\chi)W(\chi,H\mid a).
\]

Then every Paper 13D conditional probability is unchanged.

#### Proof

For fixed \(\chi,a\),

\[
 \frac{W_c(\chi,H\mid a)}
 {\sum_{H'}W_c(\chi,H'\mid a)}
 =
 \frac{c(\chi)W(\chi,H\mid a)}
 {c(\chi)\sum_{H'}W(\chi,H'\mid a)}
 =\Gamma_D(H\mid\chi,a).
\]

The multiplier cancels. It nevertheless changes the marginal propensity of
\(\chi\). \(\square\)

### Corollary 1 -- generator activities are invisible conditionally

Let \(N_\gamma(\chi)\) count physical occurrences of autonomous generator
type \(\gamma\). For arbitrary positive activities \(\lambda_\gamma\),

\[
 c_{\boldsymbol\lambda}(\chi)
 =\prod_\gamma\lambda_\gamma^{N_\gamma(\chi)}
\]

leaves every accepted conditional exact while changing the autonomous
ensemble.

The fusion activity \(\lambda\) of Paper 17B is the smallest instance of this
general gauge freedom.

### Theorem 2 -- quantum sector gauge

Suppose amplitudes \(\mathcal A(\chi,H)\) recover an accepted conditional
sector. For any nonzero complex number

\[
 z(\chi)=r(\chi)e^{i\theta(\chi)},
\]

the transformation

\[
 \mathcal A(\chi,H)\longmapsto
 z(\chi)\mathcal A(\chi,H)
\]

leaves normalized probabilities internal to fixed \(\chi\) unchanged.
It changes cross-complex weights through \(r\) and changes any future
cross-complex interference through \(\theta\).

Thus \(\mathbf\Gamma_D\) identifies neither process activities nor relative
sector phases.

### Scientific consequence

This is the root obstruction. Known quantum physics can tell us what kind of
object an autonomous law might be. It cannot reconstruct the object's missing
couplings and phases from conditional probabilities that are invariant under
them.

## 5. What Paper 13D's matrix \(R\) does and does not supply

Paper 13D contains the exact amplitude motif

\[
 R=
 \begin{pmatrix}
 3/5&-4/5\\
 4/5&3/5
 \end{pmatrix},
 \qquad B=|R|^2,
 \qquad C=|R^2|^2.
\]

This is real quantum inspiration, not decorative notation. It explains the
difference between a coherent two-step whole law \(C\) and the recorded
classical composition \(B^2\).

But it supplies only a relative phase structure for one declared two-state
primitive. It does not say:

- how amplitudes of two different unmarked process complexes compare;
- what phase belongs to fusion relative to a tensor antichain;
- what activity suppresses or enhances additional generator occurrences;
- what environment coherently dilates erasure; or
- what measure makes an infinite sum over complexes meaningful.

The local \(R\) is therefore an amplitude seed, not an autonomous action.

## 6. Why an amplitude lift is not yet new physics

### Proposition 1 -- trivial diagonal lift

Every finite classical joint law has a strongly positive decoherence
functional

\[
 D(\omega,\omega')
 =\delta_{\omega\omega'}P(\omega).
\]

Equivalently, assign mutually orthogonal environment tags

\[
 |A_\omega\rangle=\sqrt{P(\omega)}|\omega\rangle.
\]

This is a quantal representation of a classical law, with no interference.

### Proposition 2 -- phase nonuniqueness

Writing

\[
 A_H=\sqrt{\Gamma_D(H\mid\chi,a)}e^{i\theta_H}
\]

does not select the phases \(\theta_H\). If the amplitudes are added directly,
the resulting coarse probabilities generally fail Paper 13D's ordinary
additivity. If orthogonal tags are added to restore additivity, the phases
become unobservable.

So a square-root construction proves representability, not a physical
interference law.

### Dilation result

Quantum dilation theorems and Barandes's stochastic-quantum correspondence
show that stochastic laws can be represented within enlarged unitary quantum
systems. That is useful for constructing a lossless mathematical carrier for
noninvertible maps. It does not uniquely select:

- the enlarged environment;
- the unitary dilation;
- the process-complex marginal;
- cross-complex phases; or
- which dilation degrees of freedom are physical.

The correct outcome is therefore

```text
P17C-AMPLITUDE-LIFT-EXISTS-NONUNIQUELY
```

not “the autonomous quantum law has been derived.”

## 7. The decisive physical test: failure of mixture factorization

Before introducing fundamental amplitudes over process complexes, one must
first test the weaker and representation-neutral statement that a complete
two-route experiment is not a stochastic mixture of its separately calibrated
one-route controls.

### Definition 1 -- matched reconvergent controls

Two nonisomorphic one-route controls \(\chi_1,\chi_2\) and one complete
both-route experiment \(\chi_{12}\) are matched if:

1. they have the same complete typed source and target boundary;
2. the same complete final reader can be applied;
3. no stable record available to the reader distinguishes which complex
   occurred; and
4. \(\chi_{12}\) enables both routes while the matched controls enable each
   route separately, with all apparatus and source changes explicitly typed.

### Definition 2 -- mixture-factorization residual

For final reader outcome \(r\), define

\[
 I_r=
 P(r\mid\chi_{12})
 -P_{\rm incoh}(r\mid\chi_1,\chi_2),
\]

where the incoherent reference uses independently calibrated alternative
weights, not an assumed one-half mixture.

If some \(I_r\ne0\), the hypothesis that \(\chi_{12}\) is merely a random
mixture of \(\chi_1\) and \(\chi_2\) is false. Two explanations remain open:

1. \(\chi_{12}\) has its own indivisible stochastic whole law, as in a
   Barandes-style formulation; or
2. the routes are represented by complex contributions with a physical
   relative phase.

The residual alone cannot distinguish them. If every exhaustive matched test
has \(I_r=0\), fundamental cross-complex amplitudes remain unearned, but the
stochastic occurrence-law problem still remains.

Paper 13D does not contain the autonomous alternative weights or the matched
three-experiment family needed to run this test. The present result is

```text
P17C-MIXTURE-FACTORIZATION-INTERFERENCE-UNTESTED
```

### Erasure is not recoherence

Paper 13D's eraser maps record sectors to a later erased boundary. A many-to-one
record map does not prove that environmental which-process information has
been removed or that interference has returned. Recoherence in a Hilbert
representation requires an explicit reversible environmental dilation and a
recovered residual. In a stochastic ontology, the corresponding requirement
is an exact whole-law restoration test, not a primitive claim about
amplitudes.

Thus stable-record loss and amplitude recoherence remain distinct coordinates.

## 8. Relational action as an architecture, not yet a quantum law

The closest known architecture is the relation between field actions and
their diagrammatic expansions, generalized by group field theory to sums over
combinatorial complexes. The schematic action alone is not quantum. Its
interpretation is fixed only by the weight rule:

\[
 P(\chi)\propto e^{-S_{\rm rel}(\chi)}
 \quad\text{is a positive stochastic model}
 \quad\text{for real }S_{\rm rel}\text{ and finite }Z,
\]

whereas

\[
 \mathcal A(\chi)\propto
 e^{iS_{\rm rel}(\chi)/\hbar}
 \quad\text{is a complex-amplitude model}.
\]

A complex-valued field is not by itself sufficient; quantum content requires
coherent addition, an amplitude-to-probability rule, and observable
interference.

### 8.1 Dimension-neutral relational fields

Associate fields \(\varphi_b\) to complete Paper 13D boundary types and their
point-free configurations. A schematic action is

\[
 S_{\rm rel}[\varphi]
 =\frac12\langle\varphi,K\varphi\rangle
 +\sum_\gamma \lambda_\gamma V_\gamma[\varphi].
\]

Here:

- \(K\) glues only exactly compatible typed boundary data;
- each \(V_\gamma\) is one autonomous physical generator family;
- \(\lambda_\gamma\) is its process activity or coupling; and
- the complete action is invariant under the Paper 13D presentation groupoid.

An amplitude interpretation has the schematic expansion

\[
 Z
 =\sum_{[(\chi,H)]}
 \frac{1}{|\operatorname{Aut}(\chi,H)|}
 \mathcal A_{\boldsymbol\lambda}(\chi,H).
\]

The automorphism factor is justified only when derived from the labeled
expansion or an explicitly frozen groupoid-cardinality measure. It must not be
silently mixed with a different unlabeled base measure.

### 8.2 No geometry in the interaction vocabulary

Unlike ordinary spin foams, this action may not presuppose:

- a Lorentz or rotation group;
- simplices of a fixed dimension;
- a fixed interaction valence selected to encode dimension;
- a lattice, embedding, manifold, or topology; or
- an externally ordered growth stage.

Its vertices and propagators must be derived only from the accepted typed
relational law. Dimension is a later statistical output.

### 8.3 Native nondivision remains atomic

A Paper 13D generator that is nondivisible through a declared intermediate
boundary enters as one whole interaction. The field action may not split it
into positive intermediate kernels. Gluing occurs only at certified complete
divisions.

This is how either a stochastic diagram law or an amplitude sum can respect
Barandes-like non-Markovian dynamics.

### 8.4 Experiments are insertions, not autonomous laws

External preparation, intervention, and reader marks enter a generating
functional as typed insertions or sources. They are not autonomous interaction
vertices. In a closed model, a setting device must instead be a physical
subcomplex satisfying Paper 17B's positive-support, exogeneity,
mechanism-fidelity, exclusion, and conditional-recovery gates.

This borrows the laboratory-slot discipline of process matrices without
treating the laboratory choice as cosmological propensity.

## 9. Stochastic law and derived amplitude representations

### 9.1 Positive classical action

The minimal grand-canonical candidate family is

\[
 \Pi_{\boldsymbol\lambda}(\chi)
 =\frac1{Z(\boldsymbol\lambda)}
 \frac1{|\operatorname{Aut}\chi|}
 \prod_\gamma
 \lambda_\gamma^{N_\gamma(\chi)},
\]

when the partition function exists. The autonomous history law is then

\[
 \Gamma_{\star,\boldsymbol\lambda}(\chi,H)
 =\Pi_{\boldsymbol\lambda}(\chi)
 \Gamma_D(H\mid\chi).
\]

This family is valuable because it is explicit, covariant, and honest about
its new constants. It is not selected by current evidence.

### 9.2 Optional amplitude action

An optional amplitude representation replaces positive activities by complex
vertex amplitudes and supplies a boundary state and decoherence functional.
Schematically,

\[
 \mathcal A(\chi,H)
 =\frac1{|\operatorname{Aut}(\chi,H)|}
 \prod_{v\in\chi}
 \lambda_{\tau(v)}e^{i\theta_{\tau(v)}}
 \;\mathcal A_D(H\mid\chi),
\]

with contractions determined by \(K\).

Neither \(\mathcal A_D\) nor the phases \(\theta_\gamma\) are uniquely fixed by
\(\Gamma_D\). Paper 13D's \(R\) constrains one primitive subamplitude only.

### 9.3 Recommended ordering

The complete indivisible stochastic \(\Gamma_\star\) should be constructed
first. Its stochastic-quantum potentials and dilations should then be
classified as nonunique representations. A nonzero mixture-factorization
residual requires an indivisible whole law for the both-route experiment; it
does not by itself require a fundamental amplitude ontology. A fundamental
decoherence functional should be introduced only if an additional principle
or observation discriminates it from all complete stochastic realizations.

## 10. Normalization and infinite complexes

A formal diagram expansion is not automatically a probability law.

### 10.1 Classical requirement

For every finite physical restriction \(\Omega_N\), one needs a normalized
law \(P_N\). For restrictions \(N<M\), the physical restriction map
\(\rho_{M\to N}\) must obey

\[
 (\rho_{M\to N})_*P_M=P_N.
\]

The limit must live on the point-free physical cylinder algebra. A cutoff or
birth label is auxiliary and may not become a clock.

### 10.2 Quantal requirement

For a decoherence functional one analogously needs compatible finite
restrictions

\[
 D_M(\rho^{-1}A,\rho^{-1}B)=D_N(A,B)
\]

and an extension theorem on the chosen event algebra. Quantum sequential
growth research shows that this extension is nontrivial even when covariance
is easy to state.

### 10.3 Divergence control

The number of process complexes can grow faster than an exponential in
occurrence number. A factor \(e^{-\alpha N}\) is therefore not guaranteed to
normalize the law. Perturbative field sums may be asymptotic, and a Euclidean
continuation changes the physical interpretation unless independently
justified.

The theory must prove one of:

1. absolute normalization of a positive law;
2. a constructive or resummed quantal definition;
3. a consistent finite-volume/projective family; or
4. a physically justified conditional cosmological state.

## 11. What can select the new couplings?

Known quantum field theories normally take their couplings as new physical
constants. Symmetry constrains the allowed terms but rarely fixes every
coefficient.

For the relational action, a coupling may be accepted only through one of:

1. cancellation of a demonstrated anomaly or inconsistency;
2. a unique fixed point of an independently defined intrinsic
   coarse-graining transformation;
3. an exact conservation or composition theorem that fixes the coefficient;
4. calibration from nongeometric microscopic occurrence statistics; or
5. a new symmetry that truly relates the affected generator sectors.

The calibration data must be frozen before any dimension estimator is
opened.

The following are not selectors:

- setting every activity to one;
- choosing maximum entropy without a physical base measure and constraints;
- tuning to a critical point because continuum behavior is desired;
- choosing the law that yields dimension four;
- maximizing records, response, manifoldlikeness, or stability;
- preferring the shortest serialization; or
- treating renormalizability alone as uniqueness.

Renormalization-group ideas are promising only after an intrinsic
coarse-graining map is defined. Group-field theories can possess multiple
phases and fixed points; the word *fixed point* does not itself select one.

## 12. Exact hostile controls

Any proposed autonomous law must survive all of the following.

1. **Occurrence gauge:** explicitly show which new datum fixes every
   \(c(\chi)\) freedom.
2. **Sector phase:** explicitly show which experiment fixes relative
   cross-complex phases.
3. **Diagonal-lift nonkill:** a trivial orthogonal amplitude representation
   must not count as quantum process interference.
4. **Dilation nonkill:** a nonunique unitary dilation must not count as a
   selected ontology.
5. **Antichain/star:** derive, rather than choose, their relative fusion
   activity.
6. **Label cloning:** relabeling a representative adds no physical weight.
7. **Orbit mass:** sum orbit multiplicity correctly; do not substitute one
   representative's weight.
8. **Base measure:** labeled, unlabeled, and groupoid-cardinality conventions
   may not be silently exchanged.
9. **Spectator:** a disconnected spectator changes local ratios only through
   the declared tensor rule.
10. **Staged/simultaneous:** distinct physical complexes are not identified
    because their endpoints match.
11. **Nondivision:** no hidden intermediate positive kernel is inserted.
12. **Record/decoherence:** stable distinguishability and decoherence are
    checked separately.
13. **Eraser/recoherence:** erasure of a readable field is not accepted as
    restored interference.
14. **External source:** a laboratory insertion cannot act as an autonomous
    interaction.
15. **Internal device:** conditioning on a correlated device record cannot
    replace an intervention theorem.
16. **Cutoff:** auxiliary maximum size, ordering, or truncation cannot alter
    the limit.
17. **Projective consistency:** finite-size normalizations must agree under
    physical restriction.
18. **Coupling freeze:** all activities and phases are frozen before geometry.
19. **Melonic/branched-polymer outcome:** a dominant combinatorial phase with
    branched-polymer statistics is a legitimate negative result, not something
    to tune away.
20. **No dimension-by-valence:** interaction arity may not encode the desired
    dimension in advance.
21. **No phase-by-output:** phases may not be fitted to recover a preferred
    interference or causal order.
22. **Multiple fixed points:** failure of uniqueness is reported as a family,
    not resolved by taste.
23. **Actualization:** a propensity or quantum measure does not select one
    actual history without a separate interpretation or rule.
24. **Cross-complex test:** quantum promotion requires an operational
    reconvergence residual, not analogy with Feynman diagrams.

## 13. A physics-first construction programme

### Stage A -- process-history space

Construct the standard-Borel or finite-cylinder event space of point-free
\((\chi,H)\), retaining occurrence multiplicity and incidence rather than a
set of onset orbits.

### Stage B -- autonomous versus marked vocabulary

Classify each Paper 13D generator as an autonomous vertex, external insertion,
reader, internal apparatus component, stable future, or eraser. Refuse any
ambiguous role.

### Stage C -- occurrence-gauge basis

Enumerate the independent point-free generator counts and interaction motifs.
Prove which activities are physically independent under tensor, fusion, and
groupoid covariance.

### Stage D -- classical baseline

Construct the most general normalized positive occurrence family compatible
with those constraints. Report all free couplings. Do not choose them by
geometry.

### Stage E -- stochastic-quantum representation classification

Classify all complex potentials, unitary dilations, amplitude lifts, and
decoherence-functional representations that recover each Paper 13D marked
sector, including the constraints inherited from \(R\). Identify the remaining
gauge, phase, environment, and ontology freedom.

### Stage F -- mixture-factorization discriminator

Construct matched one-route and both-route controls with complete readers. A
nonzero residual rejects mixture factorization. Separately test whether any
observation distinguishes a fundamental amplitude theory from a complete
indivisible stochastic realization.

### Stage G -- relational action

Freeze \(K\), the allowed \(V_\gamma\), the base measure, boundary state,
couplings, and any phases. Review the mathematics before implementation.

### Stage H -- existence

Prove normalization or a constructive/projective limit. A formal divergent
series does not pass.

### Stage I -- conditional recovery

Prove that every accepted Paper 13D experiment, intervention, reader,
division, nondivision, stable future, eraser, response, tensor, fusion, and
varying-size restriction is recovered exactly.

### Stage J -- only then return to Paper 17

Generate covariant varying-size ensembles and test operational chronology and
dimension with all couplings already frozen.

## 14. Outcome ladder

```text
P17C-INPUT-P13D-GAMMA-BOUND
P17C-POINTFREE-PROCESS-HISTORY-SPACE-CONTRACT-CONSTRUCTED
P17C-OCCURRENCE-GAUGE-THEOREM-CONSTRUCTED
P17C-INDIVISIBLE-STOCHASTIC-AUTONOMOUS-LAW-UNSELECTED
P17C-AMPLITUDE-LIFT-EXISTS-NONUNIQUELY
P17C-MIXTURE-FACTORIZATION-INTERFERENCE-UNTESTED
P17C-DECOHERENCE-DERIVATION-FROM-FULL-GAMMA-UNTESTED
P17C-FUNDAMENTAL-QUANTAL-ONTOLOGY-NOT-REQUIRED
P17C-RELATIONAL-FIELD-ACTION-CONTRACT-CONSTRUCTED
P17C-GENERATOR-COUPLINGS-UNSELECTED
P17C-NORMALIZED-SUM-OVER-COMPLEXES-UNCONSTRUCTED
P17C-INTERNAL-INTERVENTION-REALIZATION-UNCONSTRUCTED
P17C-DIMENSION-NONE-OCCURRENCE-LAW-UNBOUND
P17C-METRIC-UNCONSTRUCTED
P17C-ACTUALIZATION-UNCONSTRUCTED
```

## 15. Decision

Known quantum physics does provide a compelling design:

> Build a covariant, dimension-neutral indivisible stochastic
> \(\Gamma_\star\) whose complete diagrams are the accepted point-free process
> complexes and whose whole generators and marked sectors recover
> \(\mathbf\Gamma_D\). Then derive and classify its complex-potential,
> dilation, and field-action representations.

But it does not provide the numerical action. The activities and cross-complex
phases are new physics and are exactly invisible to the accepted conditional
law.

The recommended next result is therefore not “quantize \(\Gamma_D\).” It is:

1. prove the process-history and relational-action contracts;
2. construct the complete positive indivisible occurrence family;
3. classify stochastic-quantum representations without promoting one;
4. run the matched mixture-factorization discriminator; and
5. freeze new couplings only from nongeometric evidence or a unique
   consistency theorem.

Whether the residual vanishes or not, \(\Gamma_\star\) remains the primary
Barandes-compatible target. A nonzero residual means the both-route law is
indivisible, not that complex amplitudes are fundamental. A fundamental
decoherence-functional \(D_\star\) remains optional unless separately
discriminated. Dimension remains closed until the autonomous law is normalized
and its new constants are fixed independently.

## 16. Primary literature and exact scope

- R. P. Feynman, *Space-Time Approach to Non-Relativistic Quantum
  Mechanics*: https://doi.org/10.1103/RevModPhys.20.367

  Supplies the sum of complex contributions and action-phase architecture;
  it does not derive this paper's relational action.

- R. D. Sorkin, *Quantum Measure Theory and its Interpretation*:
  https://arxiv.org/abs/gr-qc/9507057

  Supplies the single-history, quantum-measure, and preclusion architecture;
  it does not select a Paper 13D decoherence functional.

- M. Gell-Mann and J. B. Hartle, *Decoherent Histories Quantum Mechanics
  with One Real Fine-Grained History*:
  https://arxiv.org/abs/1106.0767

  Supports treating recorded decoherent coarse histories probabilistically.

- J. B. Hartle, *Decoherent Histories Quantum Mechanics Starting with
  Records of What Happens*: https://arxiv.org/abs/1608.04145

  Motivates the record/decoherence gate; it does not make erasure equivalent
  to recoherence.

- F. Dowker and A. Kent, *On the Consistent Histories Approach to Quantum
  Mechanics*: https://arxiv.org/abs/gr-qc/9412067

  Establishes why consistency alone does not provide a unique predictive
  history selection principle.

- R. Oeckl, *General boundary quantum field theory: Foundations and
  probability interpretation*: https://arxiv.org/abs/hep-th/0509122

  Motivates typed boundary amplitudes and gluing without a preferred slicing;
  it does not fix the amplitudes.

- O. Oreshkov, F. Costa, and C. Brukner, *Quantum correlations with no
  causal order*: https://arxiv.org/abs/1105.4464

  Motivates global-process and local-laboratory consistency without assuming
  a global causal order; admissibility still does not select one process.

- M. Reisenberger and C. Rovelli, *Spin foams as Feynman diagrams*:
  https://arxiv.org/abs/gr-qc/0002083

  Demonstrates how a field action can generate a sum over 2-complexes. Its
  geometric group and simplicial content are not inherited here.

- D. P. Rideout and R. D. Sorkin, *A Classical Sequential Growth Dynamics
  for Causal Sets*: https://arxiv.org/abs/gr-qc/9904062

  Shows that covariance and causality can constrain a growth law while
  leaving a coupling family. Birth order is not imported as physical time.

- F. Dowker et al., *The causal set approach to quantum gravity*:
  https://doi.org/10.1007/s41114-019-0023-1

  Reviews quantum sequential growth and the nontrivial extension problem for
  decoherence functionals.

- M. Finocchiaro and D. Oriti, *Renormalization of group field theories for
  quantum gravity*: https://arxiv.org/abs/2004.07361

  Motivates coupling flow and phase analysis, while documenting that these
  remain open dynamical questions rather than automatic selectors.

- R. Gurau and J. P. Ryan, *Melons are branched polymers*:
  https://arxiv.org/abs/1302.4386

  Provides the exact warning that a dominant combinatorial quantum phase can
  be branched-polymer-like rather than manifoldlike.

- J. A. Barandes, *Quantum Systems as Indivisible Stochastic Processes*:
  https://arxiv.org/abs/2507.21192

  Makes ordinary configuration-space trajectories and indivisible stochastic
  laws primary while treating Hilbert-space objects as secondary
  representations.

- J. A. Barandes, *The Stochastic-Quantum Correspondence*:
  https://arxiv.org/abs/2302.10778

  Derives Hilbert-space representations of generalized stochastic systems and
  describes decoherence as leakage of correlations into an environment. The
  representation and decoherence analysis do not select the missing
  occurrence law or convert measurement probabilities into happening
  probabilities.

- W. F. Stinespring, *Positive Functions on C*-Algebras*:
  https://doi.org/10.1090/S0002-9939-1955-0069403-4

  Supplies the dilation architecture for completely positive maps; dilation
  is representation, not unique physical completion.

## 17. Mode statement

This is a mathematical and literature investigation only. No Python, Rust,
evaluator, random case, result artifact, dimension fit, metric object, or
geometry reconstruction was created or run.
