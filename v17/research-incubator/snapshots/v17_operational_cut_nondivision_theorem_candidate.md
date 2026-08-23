# ISP v17 — operational cut-capacity and nondivision theorem candidate

**Status:** PRIVATE / NONBINDING / NOT A PIN / NOT AN AUTHORIZED PAPER  
**Date:** 2026-08-23  
**Scientific result awarded:** none  
**Official authority created:** none

This note develops one rigorous branch of the private positive-history cost
programme. It does not reopen Paper 04B, select a clock parent, open Paper 05,
or make a spacetime or gravity claim.

---

## 1. Central result

There is a known family of one-way quantum experiments for which a compact
quantum carrier succeeds but any finite ordinary-positive state that screens
the preparation from the later measurement choice must be exponentially
larger in the quantum message length.

This yields a clean v17 classification:

> A compact ordinary-positive history ontology reproducing this family must
> either lack a positive future-sufficient state at the intermediate cut,
> consume unbounded or growing classical cut capacity, relax the independence
> of the later intervention, or introduce another explicitly charged physical
> resource.

This is not a no-go against positive histories. It identifies where their
irreducibility has to reside.

The result gives a scalable information-theoretic version of Paper 01's
two-Hadamard observation:

$$
|H^2|^2\ne |H|^2|H|^2.
$$

The two-Hadamard example shows that one particular unrecorded cut has no
two-state positive restart. The present family shows that every finite
positive restart at a matched operational cut either grows exponentially in
the compact quantum message length or ceases to be a restart state at all.

---

## 2. Why this route is physically cleaner

The theorem begins with an operational task and a proved resource separation,
not with a favored ontology.

The inference order is:

$$
\text{registered preparation--measurement task}
\longrightarrow
\text{observed/quantum success profile}
\longrightarrow
\text{all positive cut realizers}
\longrightarrow
\text{capacity lower bound or premise escape}.
$$

No graph, lattice, microscopic entity, spacetime dimension, or causal-set
structure is assumed. The finite alphabet appears only in one theorem branch;
continuous and whole-history alternatives remain live and are classified
separately.

---

## 3. The registered task family

Fix an even integer \(n\) and a constant

$$
0<\alpha\le \frac14.
$$

Alice receives

$$
x\in\{0,1\}^n.
$$

Bob receives an \(\alpha\)-matching \(M\), consisting of \(\alpha n\)
disjoint pairs from \([n]\), and a string

$$
w\in\{0,1\}^{\alpha n}.
$$

Regard \(M\) as an \(\alpha n\times n\) binary matrix. The promise is that
there is a bit \(b\) such that

$$
w=Mx\oplus b^{\alpha n}.
$$

Bob must output \(b\) with worst-case probability at least \(2/3\).

Operationally:

1. Alice's choice \(x\) prepares one physical carrier.
2. The carrier crosses a registered cut.
3. Only after the preparation side is fixed, Bob applies the measurement
   indexed by \(y=(M,w)\).
4. Bob emits one classical record \(\hat b\).
5. Shared randomness may be allowed, but it is independent of \(x\) and
   \(y\).

This is the \(\alpha\)-Partial Matching task of Gavinsky, Kempe, Kerenidis,
Raz, and de Wolf.

---

## 4. Quantum comparator

Alice can encode \(x\) in the phase pattern

$$
|\psi_x\rangle
=
\frac1{\sqrt n}
\sum_{i=1}^n(-1)^{x_i}|i\rangle.
$$

Bob measures in two-dimensional subspaces associated with his matching. When
one of the registered edges \((i_\ell,j_\ell)\) is selected, the relative
phase reveals

$$
x_{i_\ell}\oplus x_{j_\ell},
$$

which Bob compares with \(w_\ell\) to recover \(b\). A constant number of
copies suffices for constant \(\alpha\) and bounded error.

The published communication bounds are

$$
Q^1(\alpha\mathrm{PM})
=O\!\left(\frac{\log n}{\alpha}\right)
$$

qubits and

$$
R^1(\alpha\mathrm{PM})
=\Theta\!\left(\sqrt{\frac n\alpha}\right)
$$

classical randomized one-way bits.

The reduction below uses the input-independent shared randomness as public
coins. Any official pin must reproduce the source's exact randomized/public-
coin and worst-case-error conventions rather than silently weaken or strengthen
them.

For fixed \(\alpha\), the comparison is therefore

$$
O(\log n)\ \text{qubits}
\qquad\text{versus}\qquad
\Omega(\sqrt n)\ \text{classical bits}.
$$

The separation is unconditional and exponential in the quantum message
length. It is not based on an unproved computational-complexity conjecture.

---

## 5. Positive cut-sufficient realizers

Let \(s\) be shared randomness with law \(\nu\), independent of the freely
chosen inputs \(x\) and \(y=(M,w)\).

A **finite positive cut-sufficient realizer** consists of:

1. a finite boundary carrier \(\Lambda_{n,s}\);
2. a positive preparation law

   $$
   \mu_{x,s}(\lambda)
   \ge 0,
   \qquad
   \sum_{\lambda}\mu_{x,s}(\lambda)=1;
   $$

3. a positive response law

   $$
   \xi_{y,s}(\hat b\mid\lambda)
   \ge0,
   \qquad
   \sum_{\hat b}\xi_{y,s}(\hat b\mid\lambda)=1;
   $$

4. the screening/factorization identity

   $$
   P(\hat b\mid x,y)
   =
   \int\nu(ds)
   \sum_{\lambda\in\Lambda_{n,s}}
   \mu_{x,s}(\lambda)
   \xi_{y,s}(\hat b\mid\lambda);
   $$

5. worst-case success at least \(2/3\) on every promised input; and
6. a worst-case cut capacity

   $$
   C_n
   =
   \sup_s\left\lceil\log_2|\Lambda_{n,s}|\right\rceil.
   $$

The word **sufficient** matters. Conditional on \((\lambda,s,y)\), the future
record is independent of the earlier preparation label \(x\). The cut state
therefore contains everything from the past that the future experiment can
use.

This is stronger than merely assigning a positive probability to each complete
laboratory history. A whole-history law may be positive without admitting this
factorization at the cut.

---

## 6. The theorem candidate

### Theorem — finite positive cut-capacity lower bound

For fixed \(0<\alpha\le1/4\), every finite positive cut-sufficient realizer of
the \(\alpha\)-Partial Matching family with worst-case error at most \(1/3\)
satisfies

$$
C_n
=
\Omega\!\left(\sqrt{\frac n\alpha}\right).
$$

For fixed \(\alpha\),

$$
C_n=\Omega(\sqrt n),
$$

whereas the quantum carrier requires only \(O(\log n)\) qubits.

### Proof

Assume such a realizer exists.

Alice and Bob first sample or consult the shared variable \(s\). Alice, knowing
\((x,s)\), samples \(\lambda\) according to \(\mu_{x,s}\) and sends Bob the
index of \(\lambda\). This requires no more than \(C_n\) bits in the frozen
worst-case alphabet convention.

Bob knows \((y,s,\lambda)\). He samples \(\hat b\) from
\(\xi_{y,s}(\cdot\mid\lambda)\). By the screening identity, the resulting
one-way randomized protocol has exactly the same output law as the proposed
positive realizer and therefore succeeds with worst-case probability at least
\(2/3\).

It follows that

$$
R^1(\alpha\mathrm{PM})\le C_n.
$$

The published lower bound

$$
R^1(\alpha\mathrm{PM})
=\Omega\!\left(\sqrt{\frac n\alpha}\right)
$$

therefore implies the claimed inequality. QED.

### Corollary — exponential separation in compact message length

For fixed \(\alpha\), let \(q_n=\Theta(\log n)\) be the number of transmitted
qubits in the explicit quantum protocol. Then

$$
C_n=2^{\Omega(q_n)}.
$$

This is a resource separation between a positive future-sufficient classical
boundary and a quantum boundary. It is not a claim that nature literally runs
a classical simulation algorithm.

The separated coordinate is **one-way capacity across the registered cut**.
The theorem does not say that the entire quantum experiment is exponentially
cheaper in energy, laboratory time, control complexity, or preparation work.
Alice receives the full \(n\)-bit input and preparing its phase pattern may
itself require resources growing with \(n\). Those coordinates must be counted
separately in any total physical comparison.

---

## 7. Why a complete-process ontology inherits the bound

The theorem uses only one output task, whereas v17 demands complete
instruments, adaptive continuations, records, and failures.

That does not weaken the lower bound. Any model reproducing the larger complete
experiment profile must reproduce every registered subexperiment, including
the \(\alpha\)-Partial Matching reader. Therefore a complete positive
cut-sufficient ontology with the same independence and finite-capacity
premises inherits the bound.

The converse is not true: passing this one task does not establish complete
quantum-process adequacy. The family is a lower-bound witness, not a complete
theory test.

---

## 8. What the theorem establishes physically

It establishes that the quantum carrier's compactness cannot be reproduced by
a small finite classical probability state that is simultaneously:

- prepared without knowing the later measurement choice;
- sufficient for every registered later response;
- transmitted through the declared cut;
- ordinary-positive at that cut; and
- bounded in classical message capacity.

Thus the relative phases in \(|\psi_x\rangle\) are not removable bookkeeping
under this interface. They are a compact carrier of counterfactual response:
the later matching decides which parity becomes accessible.

The theorem does **not** establish that complex amplitudes are ontic. It
establishes that every adequate compact boundary must contain an equivalent
phase-complete response capacity or reject positive cut sufficiency.

This is exactly the kind of invariant-structure gain the reality-identification
contract permits.

It is not by itself an empirical wedge: the quantum/classical task separation
is established physics. Its v17 value is to constrain the architecture and
resource location of any proposed positive ontology.

---

## 9. The Barandes/ISP interpretation

Barandes-style indivisibility is not refuted by the theorem. It is one of the
classified escape branches.

If an ISP law assigns a positive measure to complete preparation--measurement
histories but no positive state at the intermediate cut screens \(x\) from all
future choices \(y\), then the reduction in Section 6 does not apply. The law
is genuinely indivisible across that cut.

This has a precise physical meaning:

> The compactness is not carried by a small classical restart state. It is
> carried by the irreducible response structure of the whole experiment.

That is not yet an explanation of quantum theory. The next question becomes
whether one uniform indivisible law generates this response structure without
receiving the full quantum process or a separate table for each experiment.

The theorem therefore sharpens the Barandes research programme:

$$
\text{ordinary positivity on actual records}
\quad+\quad
\text{compact quantum response}
\quad\Longrightarrow\quad
\text{scalable positive nondivision or another charged resource}.
$$

Indivisibility becomes a resource-bearing structural claim rather than a
verbal reinterpretation.

---

## 10. Exhaustive premise-escape ledger

The theorem is useful only if every escape is named honestly.

### E1 — large finite predictive carrier

Retain positive cut sufficiency and accept

$$
C_n=\Omega(\sqrt n).
$$

This is scientifically coherent. It says that the positive ontology carries
exponentially more finite classical message capacity than the compact quantum
carrier for this family.

### E2 — continuous or infinite-precision carrier

Use an uncountable \(\Lambda\) or exact analog variable. The finite-alphabet
theorem no longer applies.

This is not a free victory. A future theorem must freeze accessible precision,
noise robustness, regularity of the response maps, preparation energy/time,
and whether one coordinate hides an arbitrarily large lookup table. No cost is
awarded merely from coordinate count.

### E3 — positive nondivision at the cut

Keep ordinary probabilities on complete histories but deny the screening
identity. The future response cannot be reconstructed from a positive
intermediate state independent of the earlier preparation.

This is the native Barandes/ISP branch. It carries a composition obligation:
show one uniform whole-process law, compatible with freely inserted
interventions, rather than a separately compiled joint table for every
\((x,y)\).

### E4 — retained phase-complete nonclassical boundary

Use a quantum state, operator-algebraic functional, amplitude object, signed or
quasiprobability boundary, or an operationally equivalent noncommutative
boundary. This accepts the compact nonclassical predictive structure while
leaving its ontology open.

### E5 — measurement dependence

Allow the root or cut distribution to depend on Bob's future choice \(y\):

$$
\mu_{x,y}(\lambda).
$$

The one-way reduction fails because intervention independence is lost. The
theory must then state whether the dependence is a preferred global boundary,
superdeterministic correlation, retrocausal constraint, or another mechanism,
and derive its empirical wedge or nonselection status.

### E6 — backward or extra communication

Allow information about \(y\) to reach the preparation side, or introduce an
unprinted global coordinator. The resource is then not one-way. Its direction,
capacity, physical carrier, and relativistic status must be registered.

### E7 — nonuniform compilation

Give each \(n\), matching family, or complete program a separately selected
positive law. This avoids a uniform carrier theorem only by relocating the
target into law-instance data. The compiler/table size belongs to the resource
ledger.

### E8 — empirical deviation

Predict a success profile different from the quantum comparator. This is a
legitimate physical theory branch. Its parameters must be fixed independently
and the deviation tested prospectively.

These branches are alternatives, not defects by definition. The theorem's job
is to prevent movement among them from being hidden.

---

## 11. Relation to the private cost trilemma

The general private trilemma was

$$
\text{predictive-state cost}
\quad\lor\quad
\text{context/coordination cost}
\quad\lor\quad
\text{composition cost}.
$$

The present theorem earns one exact finite-alphabet branch:

$$
\boxed{
\text{positive cut sufficiency}
\ \Longrightarrow\ 
C_n=\Omega(\sqrt n)
}
$$

for a quantum family requiring only \(O(\log n)\) qubits.

If positive cut sufficiency is rejected, the remaining scientific work is not
to declare victory. It is to distinguish:

- lawful indivisibility under every admitted intervention;
- hidden access to the whole experimental program;
- nonuniform recompilation; and
- a genuinely new causal or boundary principle.

This is the first theorem-shaped anchor for the wider cost programme.

---

## 12. Hostile controls

An official version would have to preregister at least the following.

1. The matching \(M\) leaks into Alice's preparation device.
2. The promise bit \(b\) is cached in shared randomness.
3. Shared randomness is not independent of \((x,y)\).
4. A variable-length message is reported by average rather than worst-case
   cost.
5. Failure/postselection probability is omitted.
6. The output is correct only on an average distribution while worst-case
   success is claimed.
7. A continuous variable hides the entire \(x\) table at infinite precision.
8. Preparation precision or energy is treated as free.
9. Bob receives a side channel carrying part of \(x\).
10. Alice receives a backward channel carrying part of \(y\).
11. One law is compiled per matching rather than uniformly over \(M\).
12. The ontology is inflated with idle states and the inflated cardinality is
    mistaken for the minimal capacity.
13. The quantum comparator's repeated copies are undercounted.
14. The classical comparator is denied shared randomness while the quantum
    comparator receives an analogous free resource.
15. A lower bound on a finite cut state is advertised against continuous or
    indivisible histories.
16. A computational communication task is advertised as a direct experimental
    deviation of ISP.
17. The promise problem is silently replaced by a total task.
18. The \(\alpha\le1/4\) theorem is quoted at \(\alpha=1/2\) without the
    required modification.
19. Final-output success is promoted to complete-process adequacy.
20. Lower resource cost is promoted to ontological truth.

---

## 13. Remaining theorem work

The finite-alphabet corollary is strong but not the final v17 cost theorem.
The next mathematical questions are:

1. Can the bound be stated in a one-shot information-capacity or robust
   covering form that treats continuous noisy carriers?
2. Which regularity and precision assumptions make that extension physically
   invariant?
3. Can a complete multi-slot process family turn positive nondivision into a
   quantitative memory or context lower bound?
4. Can a uniform indivisible positive law attain \(O(\log n)\) physical
   resources without retaining the quantum state as input?
5. Can an intervention test distinguish lawful whole-history indivisibility
   from future-setting leakage or nonuniform compilation?
6. How does the bound transform under approximate complete-profile distance,
   not merely success on one Boolean reader?

The first and fifth questions are the most important for ontology. They decide
whether indivisibility is a genuine physical organization or a name for hidden
context.

---

## 14. Result ladder

```text
L0  KNOWN QUANTUM/CLASSICAL COMMUNICATION SEPARATION
L1  POSITIVE CUT-FACTORIZATION REDUCTION
L2  FINITE-ALPHABET CUT-CAPACITY LOWER BOUND
L3  ROBUST CONTINUOUS/INFORMATION-CAPACITY EXTENSION
L4  COMPLETE MULTI-TIME INTERVENTION EXTENSION
L5  UNIFORM INDIVISIBLE-LAW CLASSIFICATION
L6  PHYSICAL RESOURCE OR EMPIRICAL WEDGE
L7  ONTOLOGY SELECTION UNDER INDEPENDENT PRINCIPLES/DATA
```

This private note reaches a candidate proof of L2 by reduction to the published
communication lower bound. It does not claim L3--L7.

---

## 15. Recommended official scope, if separately authorized

A future pin should be a classification/no-go unit, not a proposed law. It
should freeze:

- the \(\alpha\)-Partial Matching experiment family and promise;
- error and worst-case conventions;
- shared-randomness independence;
- the exact positive cut-sufficiency factorization;
- finite-alphabet capacity;
- the complete-profile inheritance claim;
- E1--E8 as nonconflated branches;
- the twenty hostile controls;
- the L0--L7 ceiling; and
- an explicit prohibition on spacetime, gravity, or ontology-selection
  promotion.

Independent review would need at least:

1. communication complexity / information theory;
2. quantum foundations / ontological models; and
3. Barandes indivisibility / process composition.

No such unit is authorized by this note.

---

## 16. Primary-source anchors

- D. Gavinsky, J. Kempe, I. Kerenidis, R. Raz, and R. de Wolf,
  “Exponential separations for one-way quantum communication complexity, with
  applications to cryptography,” STOC 2007,
  <https://arxiv.org/abs/quant-ph/0611209>.
- A. Montina, “Epistemic View of Quantum States and Communication Complexity
  of Quantum Channels,” *Physical Review Letters* **109**, 110501 (2012),
  <https://doi.org/10.1103/PhysRevLett.109.110501>.
- B. Doolittle and E. Chitambar, “Certifying the Classical Simulation Cost of
  a Quantum Channel,” *Physical Review Research* **3**, 043073 (2021),
  <https://doi.org/10.1103/PhysRevResearch.3.043073>.
- J. Bowles, M. T. Quintino, and N. Brunner, “Certifying the Dimension of
  Classical and Quantum Systems in a Prepare-and-Measure Scenario with
  Independent Devices,” *Physical Review Letters* **112**, 140407 (2014),
  <https://doi.org/10.1103/PhysRevLett.112.140407>.
- J. Sikora, A. Varvitsiotis, and Z. Wei, “Device-independent dimension tests
  in the prepare-and-measure scenario,” *Physical Review A* **94**, 042125
  (2016), <https://doi.org/10.1103/PhysRevA.94.042125>.

---

## 17. Root pre-review audit

This is a private author audit, not independent review.

| Coordinate | Audit verdict | Reason |
|---|---|---|
| source task and promise | pass | matches the cited \(\alpha\)-Partial Matching definition for \(0<\alpha\le1/4\) |
| bounded-error quantum upper bound | pass with source scope | explicit phase-state protocol uses \(O(\log n/\alpha)\) qubits |
| randomized classical lower bound | pass with source scope | cited theorem gives \(\Theta(\sqrt{n/\alpha})\) one-way bits |
| positive-factorization reduction | pass | sampling \(\lambda\) and transmitting its finite label constructs the randomized one-way protocol |
| shared randomness | high-risk but typed | required independent of inputs; exact public-coin convention must be authenticated in review |
| complete-profile inheritance | pass one-way | complete adequacy implies adequacy on this registered subexperiment, not conversely |
| continuous carrier extension | not earned | precision-aware or information-capacity theorem remains open |
| whole-history/indivisible no-go | not earned | failure of cut sufficiency is an explicit live branch |
| total physical resource advantage | not earned | only communication across the cut is bounded |
| new empirical prediction | none | this is an architectural constraint from established quantum information |
| ontology selection | none | nonclassical predictive capacity is forced; its representation is not selected |
| chronology, spacetime, gravity | closed | no relevant structure is constructed |

Private ceiling:

```text
P17-CANDIDATE-FINITE-POSITIVE-CUT-CAPACITY-LOWER-BOUND
WITH-INDIVISIBILITY-ESCAPE-AND-NO-ONTOLOGY-SELECTION
```

The finite-alphabet assumption has subsequently been removed in a separate
private candidate using hard-ensemble mutual information and finite
response-vector quantization:
`/private/tmp/v17_continuous_cut_information_theorem_candidate.md`.
That successor does not alter this note's own scoped ceiling.
