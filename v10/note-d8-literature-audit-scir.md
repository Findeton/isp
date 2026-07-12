# D8 literature audit — SCIR precedents and remaining physical content

**Search date:** 2026-07-11.  The SCIR construction ledger was frozen before
this search.  This is a targeted primary-literature comparison, not proof of
priority or an exhaustive bibliography.

## 1. Closest mathematical predecessor: quantum Petri/event nets

The closest discovered formalism is the 2025 construction of Quantum Petri
Nets with event-structure semantics:

- J. Saan Joachim, M. de Visme, and S. Haar, [Quantum Petri Nets with Event
  Structures semantics](https://arxiv.org/abs/2508.14531), 2025.

It combines local Petri-net transitions, quantum valuations, true concurrency,
unfolding semantics, and composition.  SCIR's finite typed port grammar,
disjoint-event concurrency, and local quantum maps are therefore not original.

The difference is physical scope.  The QPN paper supplies a semantics for a
given quantum net.  SCIR adds SHARD's root record, locally emitted opportunity
tokens, integrated-evidence exponential firing, durable pointer seals,
provenance/capacity accounting, and the demand that the generated causal net
itself be the pregeometry.  Those additions specify a physical interpretation
and stochastic realization; they do not constitute a new concurrency theorem.

## 2. Quantum causal histories

Quantum causal histories already assign finite matrix algebras to events and
completely positive maps to causal relations:

- E. Hawkins, F. Markopoulou, and H. Sahlmann, [Evolution in Quantum Causal
  Histories](https://arxiv.org/abs/hep-th/0302111), 2003.
- F. Markopoulou, [Quantum causal
  histories](https://arxiv.org/abs/hep-th/9904009), 1999.

They establish that local quantum evolution on a discrete causal
pre-spacetime can be sufficient and that appropriate unitary evolution can be
recovered.  SCIR differs by making the event graph grow through an explicit
local rewrite grammar and by adding a seal/flash law.  The local CP/unitary
layer is established prior art.

## 3. Relativistic flash processes

Tumulka's interacting relativistic GRW flash theory is strikingly close to the
SCIR probability construction:

- R. Tumulka, [A Relativistic GRW Flash Process With
  Interaction](https://arxiv.org/abs/2002.00482), 2020.

It starts from local Tomonaga–Schwinger unitary evolution, inserts discrete
flashes, constructs their joint distribution as a POVM, proves normalization,
and proves independence from admissible ordering by commuting spacelike
operators.  It is nonlocal at the quantum level while satisfying parameter
independence/no-signalling.

Its declared limitations mark SCIR's intended extension: Tumulka assumes a
background spacetime, a given interacting unitary evolution, and fixed
distinguishable particles; the paper explicitly does not supply a variable-
particle-number version.  SCIR instead uses a variable record graph and typed
creation/bridge rewrites.  The flash/POVM/order-independence mechanism itself
is not original.

## 4. Stochastic graph rewriting

Rule algebras and stochastic rewriting already give conditional rewrite
rules, structural constraints, CTMC semantics, and pattern-observable
dynamics:

- N. Behr and J. Krivine, [Rewriting Theory for the Life Sciences: A Unifying
  Theory of CTMC Semantics](https://arxiv.org/abs/2003.09395), 2020.

SCIR's bounded local opportunity creation and exponential race are a quantum/
record adaptation of this established architecture.  The finite rule grammar
and its numerical rates remain physical input in both cases.

## 5. Quantum causal graph dynamics

Variable quantum graphs and locality have also been treated directly:

- P. Arrighi and S. Martiel, [Quantum Causal Graph
  Dynamics](https://arxiv.org/abs/1607.06700), 2016.

They show that global unitary causal evolution of a quantum time-varying graph
decomposes into finite-depth local gates.  This is strong support for SCIR's
finite local-unitary compression, but their discrete global steps and graph
distance are not SCIR's construction-order-free evidence clocks.  The theorem
does not select the local gates.

Quantum graphity likewise demonstrates background-independent dynamical
graphs and emergent low-dimensional locality, but begins with a supplied
Hamiltonian and fixed vertex set:

- T. Konopka, F. Markopoulou, and S. Severini, [Quantum Graphity: a model of
  emergent locality](https://arxiv.org/abs/0801.0861), 2008.

## 6. Renormalization as a selector

The strongest causal-set refinement selector found does not yield uniqueness.
The cosmic renormalization transformation has a **line** of fixed points,
precisely transitive-percolation dynamics, and no other fixed points/cycles:

- X. Martin, D. O'Connor, D. Rideout, and R. Sorkin, [On the
  “renormalization” transformations induced by cycles of expansion and
  contraction in causal set cosmology](https://arxiv.org/abs/gr-qc/0009063),
  2000.

Thus renormalization can reduce an infinite coupling family to one parameter
without choosing that parameter.  It does not replace SCIR's local coupling
packet.  Transitive percolation is also classical and does not supply the
record instrument.

## 7. Priority and originality verdict

Every structural component of SCIR has a close predecessor:

| SCIR component | closest searched predecessor |
|---|---|
| typed rewrite grammar | Petri nets / stochastic graph rewriting |
| true concurrent order quotient | probabilistic/quantum event structures |
| event-local CP maps | quantum causal histories |
| variable quantum graph locality | quantum causal graph dynamics |
| exponential flashes and POVM normalization | relativistic GRW flash process |
| Born pointer outcomes | quantum instruments/operational quantum theory |
| full-history/path law | Barandes ISP and process-tensor traditions |
| coupling-space reduction | causal-set cosmic renormalization |

SCIR is therefore a **SHARD-specific physical assembly**, not a new
mathematical formalism.  The searched sources did not combine all of:

```text
pregeometric variable record birth;
locally emitted candidate tokens rather than arbitrary tuple scanning;
evidence-time unit exponential firing;
finite record capacity and provenance;
retained-holonomy/Born sealing;
construction-order quotient;
downstream cone/dimension testing.
```

That negative search result does not establish originality.

## 8. Literature-imposed claim ceiling

The literature strengthens the case that SCIR is mathematically viable and
weakens any uniqueness claim.  A finite quantum net plus local instruments
and rates is enough to define a complete process; no known covariance,
concurrency, renormalization, or consistency theorem selects the net and its
local unitary couplings.

The defensible D8 result can therefore be:

```text
COMPLETE-COMPRESSED RULEBOOK:
  yes, once the finite grammar/root/local instruments are declared.

DERIVED BORN/SURVIVAL/ORDER/PROJECTIVITY:
  yes, conditional on that packet and the corpus premises.

UNIQUE OR PARAMETER-FREE FUNDAMENTAL LAW:
  no.
```

This is not a defect specific to SCIR.  It is the same status as an action or
Hamiltonian with measured particle content and couplings.  The remaining
scientific task is empirical identification and universality: determine which
small grammar/coupling packets flow to quantum matter and Lorentzian 3+1
geometry.

