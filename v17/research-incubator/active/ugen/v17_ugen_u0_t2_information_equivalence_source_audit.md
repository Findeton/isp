# ISP v17 — U-Gen U0-T2 information-equivalence source audit

**Status:** ACTIVE AUTHOR-SIDE PRIMARY-SOURCE AUDIT / NO RESULT
**Date:** 2026-08-23
**Scientific result awarded:** none
**Authority created:** none
**Official pin/review opened:** no

This audit reconstructs the prior art needed to decide whether a proposed
native-law input packet already contains the complete quantum process it is
supposed to predict.

Its companion mathematical gate is
v17_ugen_u0_t2_no_equivalent_input_criterion.md.

The answer cannot be reduced to file size, parameter count, or a blacklist of
complex notation. A target can be hidden by a change of coordinates, by
tomographic data, by an opaque program, by an action compiler, or by splitting
its information across preparation, control, and reader fields. Conversely,
ordinary masses, couplings, apparatus settings, and boundary records are not
answer import merely because a genuine physical law can use them.

The source reconstruction therefore separates:

1. operational equivalence;
2. statistical informativeness;
3. complete multi-time predictive objects;
4. tomographic reconstruction;
5. description/resource accounting; and
6. the computability limit on detecting arbitrary hidden encodings.

---

## 1. Primary sources fixed for this audit

The claims below are limited to these sources and versions or published
identifiers, accessed on 2026-08-23.

1. David Blackwell,
   [“Comparison of Experiments”](https://projecteuclid.org/euclid.bsmsp/1200500222),
   *Proceedings of the Second Berkeley Symposium on Mathematical Statistics
   and Probability*, 1951, pp. 93–102.
2. David Blackwell,
   [“Equivalent Comparisons of
   Experiments”](https://doi.org/10.1214/aoms/1177729032),
   *Annals of Mathematical Statistics* **24** (1953), 265–272.
3. Robert W. Spekkens,
   [“Contextuality for preparations, transformations, and unsharp
   measurements”](https://arxiv.org/abs/quant-ph/0406166),
   arXiv:quant-ph/0406166; published as
   [Phys. Rev. A 71, 052108](https://doi.org/10.1103/PhysRevA.71.052108).
4. Felix A. Pollock, César Rodríguez-Rosario, Thomas Frauenheim,
   Mauro Paternostro, and Kavan Modi,
   [“Non-Markovian quantum processes: complete framework and efficient
   characterisation”](https://arxiv.org/abs/1512.00589),
   published as
   [Phys. Rev. A 97, 012127](https://doi.org/10.1103/PhysRevA.97.012127).
5. Felix A. Pollock, César Rodríguez-Rosario, Thomas Frauenheim,
   Mauro Paternostro, and Kavan Modi,
   [“Operational Markov condition for quantum
   processes”](https://arxiv.org/abs/1801.09811),
   published as
   [Phys. Rev. Lett. 120, 040405](https://doi.org/10.1103/PhysRevLett.120.040405).
6. Giulio Chiribella, Giacomo M. D'Ariano, and Paolo Perinotti,
   [“Theoretical framework for quantum
   networks”](https://arxiv.org/abs/0904.4483),
   published as
   [Phys. Rev. A 80, 022339](https://doi.org/10.1103/PhysRevA.80.022339).
7. Robin Blume-Kohout, John King Gamble, Erik Nielsen, Jonathan Mizrahi,
   Jonathan D. Sterk, and Peter Maunz,
   [“Robust, self-consistent, closed-form tomography of quantum logic gates
   on a trapped ion qubit”](https://arxiv.org/abs/1310.4492).
8. Jorma Rissanen,
   [“Modeling by shortest data
   description”](https://doi.org/10.1016/0005-1098(78)90005-5),
   *Automatica* **14** (1978), 465–471.
9. H. G. Rice,
   [“Classes of recursively enumerable sets and their decision
   problems”](https://doi.org/10.1090/S0002-9947-1953-0053041-6),
   *Transactions of the American Mathematical Society* **74** (1953),
   358–366.
10. The version-bound Barandes sources reconstructed in
    v17_ugen_u0_barandes_source_completion_audit.md.

This is a scope reconstruction, not an independent re-proof of every cited
theorem.

---

## 2. Blackwell comparison: what one data source can simulate

Blackwell compares statistical experiments by decision performance. In the
finite setting, an experiment $A$ is at least as informative as $B$ when the
outcomes of $B$ can be generated from those of $A$ by a stochastic
post-processing, often called a garbling.

Writing the experiment kernels as $K_A$ and $K_B$, the relevant relation is

$$
K_B = G K_A
$$

for some stochastic kernel $G$.

Two experiments are Blackwell-equivalent when each can simulate the other.
This is useful for U0 because it is insensitive to harmless changes of
presentation. Renaming outcomes, changing coordinates, adding independent
noise that can be discarded, or replacing a sufficient statistic by an
equivalent one should not change the answer-import classification.

But Blackwell comparison alone cannot distinguish:

1. data from law;
2. a physical cause from a predictive encoding;
3. a legitimate boundary condition from a target process table; or
4. a universal nomology from per-experiment advice.

If a physical law maps a mass and a field setting to an output distribution,
then the input becomes predictive only through that law. Blackwell ordering
does not say whether the law is explanatory, supplied, or circular.

**U0 lesson:** use Blackwell-equivalence for representation resistance and
data-processing monotonicity, not as a complete definition of native input.

---

## 3. Operational equivalence: quotient procedures before judging ontology

Spekkens formulates preparations, transformations, and measurements as
operational procedures and bases noncontextuality on their operational
equivalences. U0 needs the prior step without presupposing noncontextuality:
procedures that give the same probabilities in every registered continuation
belong to one operational equivalence class.

For two procedures $x$ and $x'$, write

$$
x \simeq_{\mathrm{op}} x'
$$

when every admitted reader and continuation gives the same record law.

The quotient is essential for two reasons.

1. Gauge-related Hilbert coordinates, gate-set similarity transforms, label
   permutations, and presentation refinements must not be counted as
   different target physics.
2. A candidate cannot hide answer information in which representative of an
   operationally equivalent class it chooses.

The quotient is always relative to a registered continuation grammar. A
finite endpoint battery may identify procedures that a later coherent or
adaptive continuation separates. Therefore U0-T2 must freeze the complete
test grammar before it freezes equivalence classes.

**U0 lesson:** the target is an operational quotient of complete-process
statistics, not a preferred wavefunction, basis, gauge, or gate label.

---

## 4. Process tensors and combs: examples of quantum-complete inputs

Pollock and collaborators define a process tensor as the multilinear map from
sequences of control operations to output states. They prove that it fully
describes arbitrary discrete-time quantum processes at the stated scope,
including non-Markovian ones, and show how informationally complete operations
tomographically reconstruct it.

Chiribella, D'Ariano, and Perinotti develop quantum combs and the link product
for quantum networks. A comb describes a multi-step quantum network and its
contraction with inserted operations determines the resulting network.

These objects are not merely convenient state labels. Relative to their
admitted operation grammar, they are complete predictive objects:

$$
\text{process tensor or comb}
+\text{inserted controls}
\longmapsto
\text{all registered outcome probabilities}.
$$

Consequently, giving a U0 candidate the target process tensor, comb, Choi
operator, or an invertible encoding of one is answer import. Re-expressing it
as a positive table, tensor network, real matrix, latent state, or history
kernel does not change that classification.

The process-tensor work also gives a useful resource warning. Full
tomography can require a number of linearly independent control sequences
that grows exponentially with process depth, although structured processes
may admit compressed representations. Compression does not by itself create
explanation: a compressed tensor remains target-complete if it reconstructs
the same operational quotient.

**U0 lesson:** complete-process prediction, rather than endpoint agreement,
sets the target-information boundary.

---

## 5. Operational Markov tests: controls are part of the object

The operational Markov criterion of Pollock and collaborators uses causal
breaks and variations of prior controls. It shows why a state-to-state
transition table is not generally a complete process description: detectable
memory depends on what interventions are inserted.

For U0 this blocks two shortcuts.

1. Equal uncontrolled trajectories or endpoint kernels do not establish equal
   complete processes.
2. A hidden-state model cannot declare a seam divisible merely by naming a
   latent variable. The restart must be licensed by physical preparations and
   readers.

It also sharpens target equivalence: two packets are equivalent only if they
agree on the registered interventions, including adaptive and retained/erased
seam controls.

**U0 lesson:** the no-equivalent-input gate must be intervention-complete and
cannot be formulated only on passive time series.

---

## 6. Gate-set tomography: raw calibration data can already be the answer

Gate-set tomography self-consistently estimates preparations, gates, and
measurements from circuit data and predicts further testing experiments.
The reconstructed matrices have gauge freedom, but the complete circuit
probabilities are gauge invariant.

This supplies two hostile controls.

1. A packet containing a tomographically complete gate set is a
   target-complete quantum packet even if it does not contain a wavefunction.
2. A packet containing the informationally complete calibration probabilities
   from which that gate set is reconstructed may also be answer-equivalent.
   Calling those numbers “calibration” does not make them independent physical
   primitives.

By contrast, a physical pulse duration, source voltage, material composition,
or apparatus geometry is not automatically a gate matrix. It may be an
admissible control coordinate if measured independently and if the candidate's
fixed law, rather than a target-derived lookup table, predicts what it does.

**U0 lesson:** audit the informational completeness of calibration, not just
the names of its fields.

---

## 7. Description length: necessary accounting, insufficient ontology

Rissanen's minimum-description-length programme formalizes the idea that a
model and its parameters should be charged alongside the data they encode.
U0 needs the same bookkeeping instinct:

$$
L(\text{law})+
L(\text{instance data})+
L(\text{precision})+
L(\text{decoder})
$$

must be counted.

This catches:

1. one answer table per program;
2. exponentially growing hidden memory;
3. infinite-precision real-number encodings;
4. a neural network trained on the held-out process;
5. a short key whose uncharged external database contains the answer; and
6. moving information from “state” to “reader” or “control.”

But short description is neither necessary nor sufficient for physical
explanation.

1. A short opaque seed may decompress to the entire target.
2. A physically real large apparatus may require a long description without
   being answer laundering.
3. Code length depends on the frozen language and precision.
4. A simple law can still be wrong.

**U0 lesson:** description and resource ledgers are vetoes and comparison
coordinates, not ontology selectors.

---

## 8. Rice's theorem: there is no universal answer-laundering scanner

Rice proved that every nontrivial extensional property of the partial
computable function computed by an arbitrary program is undecidable.

For U0, fix a nontrivial computable target function $q$ at the registered
finite-precision interface. The property

$$
\text{“program } z \text{ computes } q\text{”}
$$

is a nontrivial semantic property. No algorithm can decide it for every
arbitrary program $z$.

Therefore U0 cannot honestly promise a universal verifier that detects every
possible encoding of a target process in:

1. opaque program code;
2. unrestricted neural-network weights;
3. arbitrary computable real encodings;
4. encrypted payloads with hidden decoders; or
5. external oracle calls.

The correct response is procedural and mathematical:

1. freeze a bounded input language;
2. require transparent typed fields and dependency graphs;
3. register permitted neutral and comparator decoders;
4. require proof certificates for claimed opaque components;
5. reject unverifiable semantic payloads rather than assuming they are clean;
6. state that the gate is complete only relative to the frozen language.

This limitation is not specific to positive stochastic theories. It applies
to any programme that tries to distinguish a law from an arbitrarily hidden
answer by automatic inspection.

**U0 lesson:** T2 must be proof-carrying and class-relative.

---

## 9. Relation to the Barandes source-completion problem

The Barandes audit located the missing map

$$
\mathcal S_{\mathcal N}:
(S,b,c,R)
\longmapsto
\Gamma^{\mathcal N}_{S,b,c,R}.
$$

If $\Gamma$ is supplied separately for every target experiment, then the
source-completion problem has not been solved. At endpoint scope, the answer
has been entered directly. At complete-process scope, the supplied first-order
law may still be insufficient, but insufficiency is not a derivation.

A native Barandes-facing candidate must therefore satisfy both:

1. **no import:** its instance packet is not complete-process-equivalent under
   the frozen neutral, quantum-comparator, tomography, and advice decoders;
2. **positive generation:** one fixed independently motivated law maps that
   packet to the held-out complete record process.

The first without the second is merely under-specification. The second without
the first is compilation.

---

## 10. Source-conditioned classification

The sources support a layered classification rather than a binary slogan.

| class | meaning |
|---|---|
| direct-equivalent | target probabilities are present up to neutral recoding |
| quantum-complete | a wavefunction, channel, process tensor, comb, action, or equivalent quantum predictive object is supplied |
| tomographically complete | calibration data reconstruct the target operational quotient |
| advice-equivalent | opaque target-specific code, weights, real numbers, or oracle data decode to the target |
| physically admissible input | independently calibrated physical data remain noncomplete before the candidate law acts |
| under-specified | no answer is imported, but no law generates the missing predictions |
| undecided | opaque semantics prevent a certificate either way |

No class in this table proves that a candidate is empirically correct.

---

## 11. What the sources do not establish

The sources do not prove:

1. that an ordinary-positive native quantum law exists;
2. that such a law is impossible;
3. that Hilbert space is ontic;
4. that every physical control must have a short description;
5. that Blackwell equivalence alone identifies answer import;
6. that a process tensor is the ontology rather than a complete comparator;
7. that all hidden encodings can be detected algorithmically;
8. that one finite fixture settles QFT or gravity; or
9. that a stochastic outcome needs a hidden deterministic selector.

---

## 12. Maximum legitimate claim

> Primary prior art supports a representation-resistant, intervention-complete
> and resource-charged audit of target-equivalent input. Complete process
> tensors, combs, tomographically complete gate sets, and their lossless
> encodings carry the target predictive surface, while ordinary physical
> parameters need not. Blackwell comparison controls harmless recodings,
> operational equivalence fixes the target quotient, and Rice's theorem
> requires the audit to remain proof-carrying and relative to a frozen input
> language. These facts define a gate; they neither construct nor refute a
> native indivisible stochastic law.

The source audit and companion criterion complete U0-T2 author-side only.
The downstream U0-T3 companion files now construct the
configuration-neutral schema and its nontrivial-fiber witnesses, but bind no
real apparatus or target data. No candidate, official pin, review, result, or
successor paper is opened.
