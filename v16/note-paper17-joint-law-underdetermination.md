# Paper 17 joint-law underdetermination note

Date: 2026-08-20

Status: **MATHEMATICS CONSTRUCTED / UNREVIEWED / NO IMPLEMENTATION**

## 1. Authority and unchanged input

This note records the authorized investigation of whether an independently
motivated principle extends the accepted conditional law

$$
\mathbf\Gamma_D:
\mathsf{Experiment}_D\to
\mathsf{Prob}(\mathsf{CompleteHistories})
$$

to a joint process--history law. It is bound to:

- terminal Paper 13D law SHA-256
  `3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9`;
- terminal Paper 13D adjudication SHA-256
  `ae2c4ef066335c39a0b8057c897c947b06e4270be67d1ed3ec59bf8d6d0a00c9`;
- pre-investigation Paper 17 SHA-256
  `10b7c67eefa4cb364ec95660ca21444a078c045b96078337fcb640e18ce64fa8`;
  and
- pre-investigation Paper 17 revision-note SHA-256
  `9549d5f0b9715eb074b9938d1b668115750ca047c03d8262b81b3c764106621c`.

No Paper 13D object, operation, probability, parameter, or outcome is changed.

## 2. Physical typing correction

A complete experiment includes both an unmarked process complex $[\chi]$ and
a typed preparation/intervention/reader protocol $[a]$. Here $[\chi]$ is
obtained by forgetting only those marks while retaining the complete typed
execution diagram, boundary sorts, generators, and physical carrier; $[a]$ is
their transported typed fibre. The pair reconstructs the accepted experiment
up to its action groupoid. A distribution over
the investigator's choice of $[a]$ is experimental design, not automatically
a law of nature. The physical target is

$$
\widehat\Gamma([\chi],[H]\mid[a]),
$$

unless the setting apparatus is itself modeled inside the closed physical
complex and history.

## 3. Compatible-extension theorem

Every joint law that preserves the accepted Paper 13D conditional law has,
on positive-mass process classes, exactly the form

$$
\widehat\Gamma([\chi],[H]\mid[a])
=
\Pi([\chi]\mid[a])
\mathbf\Gamma_D([H]\mid[\chi],[a]).
$$

This follows immediately by marginalizing over complete physical history
classes and applying the definition of conditional probability. For an
exogenous protocol that does not select the physical complex, one must add

$$
\Pi([\chi]\mid[a])
=
\frac{
\mathbf 1_{[a]\in\mathsf A([\chi])}\Pi_{\rm phys}([\chi])
}{
\sum_{[\chi']}
\mathbf 1_{[a]\in\mathsf A([\chi'])}\Pi_{\rm phys}([\chi'])
}.
$$

This permits the protocol to restrict attention to complexes on which its
typed addresses exist, but forbids it from dynamically reweighting complexes
inside that support. Protocols with the same compatible support must induce
the same marginal.

Thus the missing physics is exactly $\Pi_{\rm phys}$. Under the exogeneity
condition, equivalently, it is a process-selection action

$$
S_{\rm proc}([\chi])=-\log\Pi_{\rm phys}([\chi])+\text{constant},
$$

with $S_{\rm proc}=+\infty$ on zero-mass classes.

Any extra history-dependent term retunes rather than merely extends the
accepted conditional physics.

## 4. Exact nonuniqueness witness

For every $n\geq2$, the accepted category supplies:

- $e_n^\otimes$, the tensor of $n$ independent singleton components, whose
  onset precedence is an $n$-element antichain; and
- $e_n^\star$, the same components followed by one simultaneous $n$-ary
  fusion, whose onset precedence is a height-two star.

For every $\lambda>0$,

$$
\Pi_\lambda(e_n^\otimes\mid n)=\frac1{1+\lambda},
\qquad
\Pi_\lambda(e_n^\star\mid n)=\frac{\lambda}{1+\lambda}
$$

defines a point-free covariant component-deletion family with the exact same
Paper 13D conditional history laws. The fusion activity has no label clock and
can be chosen independently of remote tensor factors. Nevertheless, for the
number $R$ of comparable onset pairs,

$$
\mathbb E_\lambda[R]=\frac{\lambda}{1+\lambda}n.
$$

Height, ordering fraction, and interval statistics also change with
$\lambda$. Covariance, deletion, tensor locality, and exact conditional
recovery therefore do not select a chronology law or a universal dimension.

## 5. Candidate principles

The following candidates were checked and do not uniquely close the gap:

1. uniform or groupoid-cardinality weighting is not normalizable over
   arbitrarily long distinct traces;
2. maximum entropy/caliber requires a base measure and structural constraints;
3. exchangeability/projectivity permits a large family of finite marginals;
4. classical sequential growth adds Markov births and free couplings;
5. a sum over process complexes needs cross-complex amplitudes or a
   decoherence functional;
6. algorithmic weighting imports a code or universal machine;
7. normalized Gamma likelihood is one for every chosen experiment, while
   entropy/response weighting is a new output-targeting selector;
8. a Gamma fixed point is undefined because Gamma outputs histories, not the
   next process complex; and
9. invariance under every lawful process insertion is nonnormalizable on an
   infinite orbit of distinct staged traces.

Barandes's distinction between fixed transition laws and contingent
standalone distributions supports this diagnosis: multiplying them produces a
joint law, but the conditional transition law does not determine the
standalone distribution.

## 6. Result and stopping line

The result is

```text
P17-PARTIAL-GAMMA-RELATIVE-PRECEDENCE-CONSTRUCTED
P17-PROCESS-SELECTION-ACTION-UNCONSTRUCTED
P17-JOINT-LAW-NOT-DERIVABLE-FROM-GAMMA-D-ALONE
P17-CHRONOLOGY-VALUED-ENSEMBLE-UNDERDETERMINED
P17-DIMENSION-NONE-ENSEMBLE-SELECTION-UNBOUND
```

This is an identifiability theorem, not a proof that no deeper principle can
exist. A future process action must be frozen as new physics before any
chronology or dimension analysis. It must be point-free, whole-diagram based,
normalizable, projectively consistent, tensor-local under a declared rule,
conditionally exact, non-Markovizing, and forbidden from using dimension or
manifold scores in its definition.

No implementation is authorized by this result.

## 7. Primary literature routing

- Barandes, *Quantum Systems as Indivisible Stochastic Processes*, Section
  2.1: https://arxiv.org/html/2507.21192v1#S2.SS1
- Rideout and Sorkin, *A Classical Sequential Growth Dynamics for Causal
  Sets*: https://arxiv.org/abs/gr-qc/9904062
- Varadarajan and Rideout, *A general solution for classical sequential
  growth dynamics of Causal Sets*: https://arxiv.org/abs/gr-qc/0504066
- Dixit et al., *Maximum Caliber: a general variational principle for
  dynamical systems*: https://arxiv.org/abs/1711.03450
- Aldous, *Exchangeability and Continuum Limits of Discrete Random
  Structures*: https://www.stat.berkeley.edu/~aldous/Papers/me128.pdf
- Dowker and Halliwell, *Quantum mechanics of history: The decoherence
  functional in quantum mechanics*:
  https://doi.org/10.1103/PhysRevD.46.1580
