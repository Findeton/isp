# D7 literature and priority audit — extension rulebooks

**Search date:** 2026-07-11.  This note was written after the independent
architecture ledger was frozen.  The search is broad and targeted, not a
claim to have exhausted all mathematics and physics.  “No direct match found”
means only that the stated queries and citation trails did not return one.
Technical comparisons below use primary papers wherever available.

## 1. Search target

The target was not merely a stochastic process.  It was the specific object
frozen in `note-d7-extension-rulebook-characterization.md`: a covariant,
null-inclusive law on typed marked finite record-extension packages, with
root and bridge sectors, full-history dependence, construction-order gauge,
recorded locality, projective consistency, a seal/instrument, and no use of
an emergent metric as primitive input.

The independent candidate architectures were searched component by component
and as combinations.  Search families included:

```text
causal-set sequential growth / covtree / order-invariant measures;
quantum sequential growth and quantal measures;
chains with complete connections and Gibbs specifications;
Ruelle transfer operators and Doob h-transforms;
Papangelou intensities, Hawkes processes, spatial birth-death laws;
chemical reaction networks and stochastic graph rewriting;
probabilistic event structures and true concurrency;
quantum instruments, combs, process tensors, and causal boxes;
Barandes indivisible stochastic processes;
targeted combinations with “causal set” and h-transform, Papangelou,
Ruelle, marked growth, support process, or bridge birth.
```

## 2. Closest prior lines

### 2.1 Classical causal-set sequential growth

Rideout and Sorkin derive a **family**, not one unique dynamics, from discrete
general covariance and a causality condition.  This is the closest physics
precedent for a birth law whose auxiliary element order is gauge:

- D. Rideout and R. Sorkin, [A Classical Sequential Growth Dynamics for
  Causal Sets](https://arxiv.org/abs/gr-qc/9904062), 2000.
- S. Varadarajan and D. Rideout, [A general solution for classical sequential
  growth dynamics of causal sets](https://arxiv.org/abs/gr-qc/0504066), 2006.

The lesson is decisive for SHARD.  Covariance and causality can classify a
large lawful family while leaving coupling data.  They do not justify a
unique “uniform” member.

Brightwell and Luczak formulate construction-order gauge directly as
order-invariance of measures on causal-set growth histories.  They exhibit
fixed causal sets with one, many, or no order-invariant measures:

- G. Brightwell and M. Luczak, [Order-invariant measures on causal
  sets](https://arxiv.org/abs/0901.0240), 2011.

Dowker and collaborators formulate a manifestly covariant random walk on the
covtree of finite stem sets.  A walk induces a measure on the covariant stem
sigma algebra, but physically motivated selection of walks remains a further
problem:

- F. Dowker et al., [A manifestly covariant framework for causal set
  dynamics](https://arxiv.org/abs/1910.07292), 2020.

**Priority effect:** Architecture A and SHARD's construction-order quotient
are not new as general ideas.  SHARD adds marks, factors, seals, ownership,
and record capacity, but those additions do not themselves select numerical
transition weights.

### 2.2 Quantum sequential growth

Quantum sequential growth replaces transition probabilities by consistent
positive operators or decoherence data.  Gudder constructs such processes
and action-generated examples:

- S. Gudder, [Quantum Sequential Growth
  Processes](https://arxiv.org/abs/1303.0433), 2013.

A recent attempt to impose Bell causality on quantum sequential growth shows
that natural formulations can force a commutative event algebra and that a
general noncommutative solution remains open:

- A. Srivastava and S. Surya, [Implementing Bell causality in Quantum
  Sequential Growth](https://arxiv.org/abs/2603.25503), 2026.

**Priority effect:** Architecture F is not new.  Positivity, normalization,
and projective consistency constrain a supplied quantum process but do not
derive its decoherence functional or instrument.

### 2.3 Full-history stochastic laws

The idea that the complete past, rather than the latest small state, enters
the next conditional law is established in chains with complete connections
and Gibbs specifications:

- R. Fernandez and G. Maillard, [Chains with complete connections: General
  theory, uniqueness, loss of memory and mixing
  properties](https://arxiv.org/abs/math/0305026), 2003.
- R. Fernandez and G. Maillard, [Chains with complete connections and
  one-dimensional Gibbs measures](https://arxiv.org/abs/math/0305025), 2003.

Barandes' indivisible stochastic-process program explicitly permits
non-Markovian generalized stochastic laws:

- J. Barandes, [Indivisible Stochastic Processes, Quantum Theory, and the
  Foundations of Physics](https://arxiv.org/abs/2507.21192), 2025.

**Priority effect:** treating a complete path measure as primitive, and
recovering next-step conditionals from it, is not original.  It resolves the
existence of a rulebook only by positing that rulebook at path level.

### 2.4 Transfer operators, Gibbs laws, and positive transforms

Ruelle transfer operators, DLR Gibbs specifications, positive eigenfunctions,
and Doob transforms contain the mathematical core of Architecture B:

- L. Cioletti, A. Lopes, and M. Stadlbauer, [Ruelle Operator for Continuous
  Potentials and DLR-Gibbs Measures](https://arxiv.org/abs/1608.03881), 2016.
- R. Chetrite and H. Touchette, [Nonequilibrium Markov processes conditioned
  on large deviations](https://arxiv.org/abs/1405.5157), 2015.

The generalized Doob transform changes jump rates by a positive ratio between
the destination and source.  That is the direct predecessor of
`w_H(xi) h(H+xi)/h(H)`.

**Priority effect:** the positive harmonic completion is not original.  The
possible SHARD-specific work is to prove when its local factor messages and
sealed-history restrictions exist—not to claim the transform itself.

### 2.5 Point-process proposal laws

Papangelou conditional intensities supply history/configuration-relative
birth rates, while Hawkes laws supply self- and mutually-exciting event
intensities:

- H.-O. Georgii and H. Yoo, [Conditional intensity and Gibbsianness of
  determinantal point processes](https://arxiv.org/abs/math/0401402), 2004.
- A. Hawkes, [Spectra of Some Self-Exciting and Mutually Exciting Point
  Processes](https://doi.org/10.1093/biomet/58.1.83), 1971.

**Priority effect:** Architecture E is not new.  Calling the points “records”
does not derive base intensity, response kernel, support affinity, or quantum
outcome structure.

### 2.6 Reaction and stochastic rewriting laws

Typed graph-rewrite rules with structural application conditions and CTMC
rates are a mature framework.  They explicitly distinguish the grammar of
allowed rewrites from the numerical stochastic mechanics:

- N. Behr and J. Krivine, [Rewriting Theory for the Life Sciences: A Unifying
  Theory of CTMC Semantics](https://arxiv.org/abs/2003.09395), 2020.
- N. Behr, V. Danos, and I. Garnier, [Combinatorial Conversion and Moment
  Bisimulation for Stochastic Rewriting
  Systems](https://arxiv.org/abs/1904.07313), 2019.

**Priority effect:** Architecture D's typed ports, multileg reactions,
capacity constraints, and propensities are not original as a mathematical
scheme.  The SHARD question is which rewrite grammar and rates follow from
sealed-record physics, if any.

### 2.7 True concurrency and probabilistic event structures

Probabilistic event structures formulate causality, conflict, and genuine
concurrency without treating arbitrary interleavings as physical:

- N. Ghahremani and J. Bradfield, [On probabilistic stable event
  structures](https://arxiv.org/abs/2012.10188), 2020.

**Priority effect:** the distinction between an auxiliary global interleaving
and a true concurrent partial-order history is not original.  It strongly
supports SHARD's refusal to interpret the builder counter as universe time.

### 2.8 Quantum instruments with memory

Quantum combs, process tensors, and causal boxes provide compositional
quantum processes with memory, typed interfaces, and operational interventions:

- G. Chiribella, G. D'Ariano, and P. Perinotti, [Theoretical framework for
  quantum networks](https://arxiv.org/abs/0904.4483), 2009.
- F. Pollock et al., [Operational Markov Condition for Quantum
  Processes](https://arxiv.org/abs/1801.09811), 2018.
- C. Portmann et al., [Causal Boxes: Quantum Information-Processing Systems
  Closed under Composition](https://arxiv.org/abs/1512.02240), 2015.

**Priority effect:** typed quantum memory/instrument composition is not new.
SHARD's seal and finite record ontology may impose a distinctive physical
interpretation, but no unique process tensor follows from that interpretation.

## 3. Architecture-by-architecture priority verdict

| independent architecture | closest established predecessor | verdict |
|---|---|---|
| A. direct covariant extension kernel | causal-set growth/covtree/order-invariant measures | not original |
| B. local transfer plus positive `h` | Ruelle operator and generalized Doob transform | not original |
| C. closure-defect proposal | Gibbs/action-weighted proposal plus SHARD closure diagnostic | combination found, no unique derivation |
| D. residual-capacity reaction | chemical reaction networks and stochastic graph rewriting | not original |
| E. self-exciting support | Papangelou/Hawkes point processes | not original |
| F. projective quantum instrument | quantum sequential growth, combs, process tensors | not original |
| G. maximum caliber/uniformity | maximum-entropy inference | not a physical derivation |

## 4. What was not found

The targeted searches did **not** find a paper deriving this entire package
from finite sealed records alone:

```text
typed marked extension grammar
+ explicit null/root/bridge sectors
+ record-carried no-silent collars
+ construction-order quotient with physical orientation retained
+ finite-capacity/provenance accounting
+ positive projective completion
+ a quantum-capable seal/instrument
+ metric-free local input.
```

That absence is not a priority claim.  Every major mathematical component has
clear predecessors, and the exact assembly may exist under different
terminology.  The defensible novelty level is therefore:

> a SHARD-specific synthesis and problem decomposition, with exact finite
> nonselection witnesses—not a discovered final law and not a claim of a new
> stochastic or quantum formalism.

## 5. Literature-imposed correction to the research question

The question “Which known consistency principle forces the one true
rulebook?” is probably malformed.  Each closest literature class contains
families, multiple phases/boundary conditions, free activities, free rewrite
rates, or free process functionals.

The next scientifically answerable question is:

> Which additional empirical or microscopic physical postulate selects a
> member of the admissible SHARD extension-law class, and what continuum
> predictions distinguish that member?

That postulate cannot merely repeat covariance, projectivity, full-history
dependence, finite information, or “preserve existing relationships.”  Those
are consistency gates already known to host many laws.

