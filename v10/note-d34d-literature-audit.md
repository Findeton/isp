# D34d literature audit — predictive states, lumpability and quantum memory

**Status:** targeted primary-literature audit, 2026-07-13. This note does not
claim priority. It identifies which D34d ideas are standard mathematical
structure and which work is specific to the SHARD D34b–D34c architecture.

## 1. Classical predictive states

Shalizi and Crutchfield, [*Computational Mechanics: Pattern and Prediction,
Structure and Simplicity*](https://arxiv.org/abs/cond-mat/9907176), define
causal states by equivalence of pasts that give the same conditional future
law and establish minimality/optimality of the resulting predictive
representation. D34d's `[h]_pred` is the same abstract move. It is not an
original SHARD theorem.

The SHARD-specific questions begin after that definition:

- which causal/predictive state is carried by typed records or collars;
- whether it is bounded, distributed, or global;
- whether D34b's actor generator closes on it;
- how it composes with D34c quantum event records.

The repaired exact HMM is a diagnostic. It shows that a three-state hidden
realization can induce a growing family of observer predictive beliefs:
`2,3,...,13` reachable classes through depths `1..12`. A small hidden
realization therefore does not imply a finite observed predictive quotient.

Marzen and Crutchfield, [*Informational and Causal Architecture of
Discrete-Time Renewal Processes*](https://arxiv.org/abs/1408.6876), analyze
renewal-process causal states and emphasize that elapsed time/event count is
the predictive statistic except in special waiting-time families. D34d's
exponential-versus-uniform-renewal comparison is an elementary instance of
that established structure: exponential memorylessness removes age, while a
general renewal state retains it.

## 2. Markov-chain projections and lumpability

Geiger and Temmel, [*Lumpings of Markov Chains, Entropy Rate Preservation, and
Higher-Order Lumpability*](https://arxiv.org/abs/1212.4375), distinguish strong
`k`-lumpability—Markovity of the lumped process for every starting
distribution—from stationary or law-relative properties. D34d round 1 was
correctly rejected for using “lumpability” without keeping those scopes apart.

The replacement carries three separate objects:

1. a strongly lumpable positive control;
2. a non-strongly-lumpable chain whose projection is Markov from a declared
   initial law because the offending state is unreachable;
3. a declared uniform-initial projection proved non-Markov by the exact
   `3/8 != 7/20` history witness.

Thus the general lumpability criterion is literature structure. The exact
specimens and their use to discipline SHARD record projections are local to
this investigation.

## 3. Quantum operational memory

Pollock et al., [*Operational Markov Condition for Quantum
Processes*](https://arxiv.org/abs/1801.09811), formulate a necessary and
sufficient operational Markov condition using multi-time processes: after a
causal break blocks the system-carried past, future statistics must not retain
dependence on earlier instruments. This is why D34d's original comparison of
coherent and path-recorded experiments did not establish non-Markovianity of
one fixed process.

The repaired Q8 gate now matches the required architecture. One fixed process
starts from a correlated system–environment state. Past choices `I` and `X`
are followed by the same nonzero `P=0` causal-break outcome and the same
`P=0` repreparation. A fixed later `CNOT(E->P)` produces certain `P=0` versus
certain `P=1`. The result is an exact finite operational-memory witness, not a
general reconstruction of the complete SHARD process tensor.

Taranto et al., [*Quantum Markov Order*](https://arxiv.org/abs/1805.11341),
show that non-Markov quantum processes cannot have finite Markov order with
respect to every possible instrument and motivate instrument-specific quantum
Markov order. Their follow-up, [*The Structure of Quantum Stochastic Processes
with Finite Markov Order*](https://arxiv.org/abs/1810.10809), analyzes the
corresponding process structures. These results forbid upgrading D34d's finite
rebit/causal-break exhibit into a universal finite-memory statement.

## 4. What is and is not new here

Not new:

- full-history Markovization;
- future-equivalence/causal-state prediction;
- strong versus law-relative lumpability;
- exponential memorylessness and age-augmented renewal states;
- process-tensor/causal-break definitions of quantum memory;
- instrument dependence of finite quantum Markov order.

Specific contributions of the D34d investigation, conditional on delta
review:

- the explicit D34b generator/state inventory and the separation of global
  strong-Markov closure from support-local generator terms;
- the actual D34b counterexample `B->A: 1/4 -> 1/8`, proving A's own tip is
  not predictively sufficient;
- the stopping-scope and clock-transformation table for the chosen actor law;
- the bounded/unbounded record-capacity ledger;
- the exact bridge from the D34c diamond to durable-record insufficiency;
- the exact fixed three-slot causal-break witness and the explicit fork between
  retaining a joint boundary state and eliminating it into a reduced process
  memory.

The open theoretical problem is now sharper: characterize the smallest
record-carried, possibly growing boundary/process state that screens every
licensed future of a region in the interacting SHARD web. Neither the
literature nor D34d currently proves that this state has bounded width.
