# ISP v17 — continuous positive cut-information theorem candidate

**Status:** ACTIVE INCUBATOR / AUTHOR THEOREM CANDIDATE / NOT FROZEN

**Date:** 2026-08-23

**Scientific result awarded:** none
**Official authority created:** none

This note extends the finite-alphabet cut-capacity candidate to
continuous and noisy ordinary-positive carriers. It does not reopen Paper 04B,
select a parent, authorize Paper 05, or make chronology, spacetime, or gravity
claims.

The exact external theorem chain is reconstructed, with retrieved-source
hashes and convention checks, in
`v17_qcut_primary_source_reconstruction.md`. That reconstruction is author-side
work, not independent review.

---

## 1. Executive result

For the Boolean Hidden Matching / \(\alpha\)-Partial Matching preparation--
measurement family, an ordinary-positive intermediate variable can be
continuous, uncountable, or written in one coordinate. That does not remove
the information burden.

Under a hard registered input ensemble, every positive intermediate variable
that approximately screens the preparation from all later measurement choices
must satisfy

$$
I(X:\Lambda\mid S)
=
\Omega\!\left(\sqrt{\frac n\alpha}\right),
$$

provided the total prediction, factorization, and quantization error remains
strictly below \(1/2\).

Here:

- \(X\) is the preparation label;
- \(S\) is input-independent shared randomness;
- \(\Lambda\) is the possibly continuous cut variable; and
- the mutual information is computed under the natural hard distribution used
  in the source proof for the registered task.

For fixed \(\alpha\), the explicit quantum carrier uses only \(O(\log n)\)
qubits and has quantum information bounded by its \(O(\log n)\) log-dimension.

The physical classification is therefore:

$$
\boxed{
\begin{aligned}
&\text{large positive cut information}\\
&\quad\lor\quad\text{failure of positive cut sufficiency}\\
&\quad\lor\quad\text{intervention dependence or another charged premise.}
\end{aligned}
}
$$

This closes the “one exact real number” loophole at the level of operational
information. It does not rule out genuinely indivisible whole-history laws.

---

## 2. Why mutual information is the correct next invariant

Raw coordinate number, topology, or carrier cardinality is not reliable:

- one real can encode an arbitrarily large finite table;
- idle labels can inflate any state space;
- a discontinuous bijection can change coordinate dimension;
- infinite precision can be hidden in notation; and
- ontic labels may be operationally redundant.

Mutual information under a frozen preparation ensemble avoids several of
these defects:

1. it is invariant under measurable bijective relabeling;
2. adding input-independent idle variables does not increase it;
3. deterministic coarse-graining cannot increase it;
4. an exact real encoding of the full preparation table is charged by the
   information it actually carries, not by the number of coordinates; and
5. infinite-information carriers are reported as such rather than called
   one-dimensional and cheap.

It is still not a universal physical cost. It is ensemble-relative and does
not directly measure energy, apparatus size, preparation time, or ontology.
Those walls remain explicit.

---

## 3. Operational task and source theorem

Fix \(n\), \(0<\alpha\le1/4\), with \(\alpha n\in\mathbb N\), and the
partial Boolean function

$$
f_{n,\alpha}(x,y)
=
\operatorname{BHM}_{\alpha}(x,y)
$$

with Alice's input \(x\in\{0,1\}^n\), Bob's matching-and-bit-string input
\(y=(\mathsf M,w)\), and the standard promise

$$
w=\mathsf Mx\oplus b^{\alpha n}.
$$

This is the \(\alpha\)-Partial Matching problem in its source paper. For every
fixed constant error threshold \(\delta_*<1/2\), its published randomized
one-way communication complexity obeys

$$
R_{\delta_*}(f_{n,\alpha})
=
\Theta\!\left(\sqrt{\frac n\alpha}\right).
$$

The message-compression lemma is stated for functions and explicitly extends
to relations. We use that relation form on the promise domain; equivalently,
extend the partial function arbitrarily off the promise and use an input
distribution supported entirely on promised pairs. No off-promise correctness
claim enters the lower bound.

The original proof supplies a natural hard distribution rather than merely an
unspecified minimax witness. Define

$$
\pi^{\rm nat}_{n,\alpha}(X,Y)
$$

by sampling \(X\) uniformly from \(\{0,1\}^n\), sampling \(\mathsf M\)
uniformly from all \(\alpha n\)-edge matchings, sampling a fair independent
bit \(B\), setting

$$
W=\mathsf M X\oplus B^{\alpha n},
\qquad
Y=(\mathsf M,W),
$$

and taking the task value to be \(B\). Gavinsky--Kempe--Kerenidis--Raz--de
Wolf prove directly that, for every fixed \(\delta_*<1/2\), deterministic
one-way protocols with average error at most \(\delta_*\) under this same
ensemble require

$$
D^{\pi^{\rm nat}_{n,\alpha}}_{\delta_*}(f_{n,\alpha})
=
\Omega_{\delta_*}\!\left(\sqrt{\frac n\alpha}\right).
$$

More explicitly, their Section 3.3 uses a source parameter
\(\varepsilon_s>0\) and proves that communication below

$$
\gamma_{\rm PM}\varepsilon_s\sqrt{n/\alpha}
-\log_2(1/\varepsilon_s)
$$

leaves advantage at most

$$
\varepsilon_s+\frac32\sqrt{\varepsilon_s}.
$$

For every fixed \(\delta_*<1/2\), choose \(\varepsilon_s\) so this advantage
is smaller than \(1/2-\delta_*\), then absorb the additive logarithm into a
large-\(n\) threshold. Thus the hard ensemble is fixed by the experiment
family before any positive cut model is inspected. The quantifier order is

$$
\exists\,\pi^{\rm nat}_{n,\alpha}
\quad
\forall\,\text{admitted positive-cut models},
$$

not a model-dependent choice of a favorable prior.

The exact message-compression source is Harsha--Jain--McAllester--
Radhakrishnan, Definition V.1 and Lemma V.3. They define transcript
information cost as the external quantity \(I(XY;T)\), minimize it over
protocols of the required error, and prove for a nonproduct input law
\(\pi\) that

$$
D^{\pi,1}_{e+\Delta}(f)
\le
\frac{2IC^{\pi,1}_e(f)+O(1)}{\Delta}.
$$

For a particular one-way private-coin protocol with finite message \(Q\) and
average error at most \(e\), minimization implies
\(IC^{\pi,1}_e(f)\le I(XY;Q)\). Hence there is a universal constant
\(C_{\rm H}\ge0\), independent of the model and \(n\), such that

$$
D^\pi_{e+\Delta}(f)
\le
\frac{2I(X,Y:Q)+C_{\rm H}}{\Delta}.
$$

Because a one-way private message is generated from \(X\) and Alice's private
randomness alone,

$$
Q\perp Y\mid X,
\qquad
I(X,Y:Q)=I(X:Q).
$$

The proof first simulates the message with public randomness and expected
communication, then uses Markov truncation and fixes the random strings to
obtain the displayed deterministic worst-case-length protocol at the charged
additional error \(\Delta\). It therefore implies that every such protocol
whose error lies a fixed positive amount below \(\delta_*\) under the natural
hard distribution has

$$
I(X:Q)
=
\Omega\!\left(\sqrt{\frac n\alpha}\right).
$$

The hard ensemble and fixed slack are parts of the theorem. The claim is not
that every arbitrary laboratory prior produces the same mutual information.

---

## 4. Continuous positive cut model

Let \((\mathcal S,\Sigma_S,\nu)\) be a standard-Borel shared-randomness space.
Require

$$
S\perp (X,Y).
$$

Let \((\mathcal E,\Sigma_E)\) be a standard-Borel total cut carrier with a
Borel projection

$$
p:\mathcal E\to\mathcal S.
$$

Write \(\mathcal E_s=p^{-1}(s)\). The cut random variable \(\Lambda\) takes
values in \(\mathcal E\) and obeys \(p(\Lambda)=S\) almost surely. A
continuous positive cut model supplies:

1. preparation kernels

   $$
   \mu_{x,s}(de),
   $$

   jointly Borel in \((x,s)\) and supported on \(\mathcal E_s\);

2. measurable binary response kernels

   $$
   \xi_y(\hat b\mid e),
   \qquad \hat b\in\{0,1\};
   $$

3. a factorized prediction

   $$
   P_{\rm fac}(\hat b\mid x,y)
   =
   \int\nu(ds)
   \int_{\mathcal E_s}\mu_{x,s}(de)
   \xi_y(\hat b\mid e);
   $$

4. an actual registered output law \(P_M\) whose worst-case task error on every
   promised input is at most \(\delta\); and
5. a uniform approximate-screening bound

   $$
   \sup_{(x,y)\in\operatorname{Dom}(f_{n,\alpha})}
   \left\|P_M(\cdot\mid x,y)-P_{\rm fac}(\cdot\mid x,y)\right\|_{\rm TV}
   \le \varepsilon_{\rm fac}.
   $$

Exact positive cut sufficiency is the special case
\(\varepsilon_{\rm fac}=0\).

The model may be continuous and non-Markovian elsewhere. The theorem uses only
this one registered cut and does not assume a global stochastic division.

---

## 5. Information coordinate

Under the natural hard ensemble \(\pi^{\rm nat}_{n,\alpha}\), define

$$
C_{\rm info}(M;n,\alpha)
=
I(X:\Lambda\mid S).
$$

This is an extended nonnegative real number. If it is infinite, the lower bound
is satisfied but no finite-resource conclusion follows.

The conditioning on \(S\) prevents free public randomness from being counted
as preparation information. Because \(S\) is independent of \(X\),

$$
I(X:S,\Lambda)
=
I(X:\Lambda\mid S).
$$

If the shared variable is correlated with \(X\) or \(Y\), the independence
premise fails and the model enters the measurement-dependence branch.

---

## 6. Finite response-vector quantization lemma

For fixed \(n\), Bob's admissible input set \(\mathcal Y_n\) is finite, even
though it is very large.

Because every response kernel is Borel on \(\mathcal E\), for every
\(e\in\mathcal E\) define its complete binary response vector

$$
r(e)
=
\bigl(
\xi_y(1\mid e)
\bigr)_{y\in\mathcal Y_n}
\in[0,1]^{|\mathcal Y_n|}.
$$

Fix a mesh \(\eta>0\), put \(K=\lceil1/\eta\rceil\), and map each coordinate
\(p\in[0,1]\) to \(\lfloor Kp\rfloor/K\), with \(p=1\) retained as \(1\).
This is a Borel map into a finite grid with maximum coordinate error at most
\(1/K\le\eta\). Call the resulting finite label

$$
Q_{\eta}=q_{\eta}(S,\Lambda).
$$

Since \(S=p(\Lambda)\), this notation means the Borel function of the total
cut value obtained by composing its finite response vector with the grid map;
including \(S\) explicitly only displays the fiber context.

For each label \(q\), let \(\widetilde r_y(q)\) be its representative response
probability. Then

$$
\left|
\widetilde r_y(Q_{\eta})
-
\xi_y(1\mid\Lambda)
\right|
\le\eta
$$

for every \(y\), almost surely.

The quantized label is finite because the response family is finite. It may be
enormous; its bit length is irrelevant to the information inequality below.

By data processing,

$$
I(X:Q_{\eta})
\le
I(X:S,\Lambda)
=
I(X:\Lambda\mid S).
$$

---

## 7. Operational protocol induced by the quantized carrier

Construct a private-coin one-way protocol as follows.

1. Alice receives \(x\).
2. She privately samples \(S\sim\nu\).
3. She samples \(\Lambda\sim\mu_{x,S}\), supported on
   \(p^{-1}(S)\).
4. She sends the finite label \(Q_{\eta}=q_{\eta}(S,\Lambda)\) to Bob.
5. Bob receives \(y\) and outputs \(1\) with probability
   \(\widetilde r_y(Q_{\eta})\).

Bob does not need \(S\). Its entire effect on every registered response is
already contained in the response-vector label. Thus public shared randomness
has been internalized into Alice's private sampling without being charged as
preparation information.

Conditional on \(X=x\), the sampling of \((S,\Lambda,Q_\eta)\) is independent
of Bob's correlated promise input \(Y\). Hence

$$
Q_\eta\perp Y\mid X,
$$

which is the exact one-way premise needed to replace
\(I(X,Y:Q_\eta)\) by \(I(X:Q_\eta)\) in message compression.

This construction is information-theoretic. The kernels and the entire finite
reader family are treated as the known protocol specification, and no efficient
algorithm for evaluating or transmitting the raw response vector is claimed.
Law-description size, compilation complexity, and runtime are separate resource
coordinates; a nonuniform lookup table cannot be advertised as explanatory
compression merely because the present lower bound counts mutual information.

The quantized protocol differs from \(P_{\rm fac}\) in binary-output total
variation by at most \(\eta\). It therefore differs from the actual model by at
most

$$
\varepsilon_{\rm fac}+\eta.
$$

If the actual model's task error is at most \(\delta\), the induced protocol's
error is at most

$$
\delta+\varepsilon_{\rm fac}+\eta.
$$

---

## 8. Continuous cut-information theorem candidate

### Theorem

Fix constants \(0<\alpha\le1/4\), \(\delta\),
\(\varepsilon_{\rm fac}\), \(\delta_*\), and \(\eta\), all independent of
\(n\), such that

$$
\delta+\varepsilon_{\rm fac}<\delta_*<\frac12.
$$

$$
0<\eta<
\delta_*-\delta-\varepsilon_{\rm fac}.
$$

Equivalently, the induced protocol has a fixed positive error slack

$$
g_{\rm err}
=
\delta_*-\delta-\varepsilon_{\rm fac}-\eta
>0.
$$

Then there are constants \(c>0\) and \(n_0\), depending only on the frozen
task and error constants, such that for every admissible
\(n\ge n_0\) with \(\alpha n\in\mathbb N\), every standard-Borel positive cut
model in Section 4 obeys, under the natural hard distribution
\(\pi^{\rm nat}_{n,\alpha}\),

$$
I(X:\Lambda\mid S)
\ge
c\sqrt{\frac n\alpha}.
$$

The implicit constant may depend on the fixed error thresholds and \(\alpha\)
convention, but not on the particular positive model.

### Proof

The response-vector quantization lemma constructs a finite private-coin message
\(Q_{\eta}\). The induced one-way protocol has task error at most

$$
\delta+\varepsilon_{\rm fac}+\eta
<
\delta_*.
$$

Set

$$
e=\delta+\varepsilon_{\rm fac}+\eta.
$$

The message is one-way private coin and satisfies
\(I(X,Y:Q_\eta)=I(X:Q_\eta)\). Since this particular protocol is one
competitor in the definition of \(IC_e\), apply
Harsha--Jain--McAllester--Radhakrishnan Lemma V.3 with any fixed
\(0<\Delta<\delta_*-e\). It gives

$$
D^{\pi^{\rm nat}_{n,\alpha}}_{e+\Delta}(f_{n,\alpha})
\le
\frac{2I(X:Q_\eta)+C_{\rm H}}{\Delta}.
$$

Since \(e+\Delta<\delta_*\), monotonicity of distributional complexity in the
allowed error and the natural-distribution lower bound give

$$
D^{\pi^{\rm nat}_{n,\alpha}}_{e+\Delta}(f_{n,\alpha})
\ge
D^{\pi^{\rm nat}_{n,\alpha}}_{\delta_*}(f_{n,\alpha})
=
\Omega_{\delta_*}\!\left(\sqrt{\frac n\alpha}\right).
$$

Rearranging, retaining the universal additive constant, and using that
\(\Delta\) is fixed independently of \(n\), yields

$$
I(X:Q_\eta)
=
\Omega\!\left(\sqrt{\frac n\alpha}\right).
$$

The additive \(C_{\rm H}\) is absorbed only by increasing the common
large-\(n\) threshold. It is not set to zero.

Because \(Q_{\eta}\) is a deterministic function of \((S,\Lambda)\), data
processing and input independence of \(S\) give

$$
I(X:Q_{\eta})
\le
I(X:S,\Lambda)
=
I(X:\Lambda\mid S).
$$

Combining the inequalities proves the result. QED.

### Fixed Q-Cut corollary

Set

$$
\alpha=\frac14,
\quad
\delta=\frac1{10},
\quad
\varepsilon_{\rm fac}=\eta=\frac1{40},
\quad
\Delta=\frac1{20},
\quad
\delta_*=\frac13.
$$

Then the induced protocol error before compression is \(3/20\), and after
the charged truncation it is \(1/5<1/3\). If

$$
D^{\pi_n^{\rm nat}}_{1/3}(f_n)\ge c_{\rm PM}\sqrt n
$$

for all \(n\ge n_{\rm PM}\), the source and compression bounds give

$$
c_{\rm PM}\sqrt n
\le
D^{\pi_n^{\rm nat}}_{1/5}(f_n)
\le
40I(X;Q_\eta)+20C_{\rm H}.
$$

Consequently

$$
I(X;\Lambda\mid S)
\ge
I(X;Q_\eta)
\ge
\frac{c_{\rm PM}}{40}\sqrt n-\frac{C_{\rm H}}2.
$$

After one realizer-independent increase of the size threshold,

$$
I(X;\Lambda\mid S)\ge\frac{c_{\rm PM}}{80}\sqrt n.
$$

These are the fixed constants used by the candidate pin. Neither
\(c_{\rm PM}\) nor \(C_{\rm H}\) is assigned an unsourced numerical value.

---

## 9. Quantum comparison

For the same task family, Alice can prepare

$$
|\psi_x\rangle
=
\frac1{\sqrt n}
\sum_{i=1}^{n}(-1)^{x_i}|i\rangle
$$

and send \(O(1/\alpha)\) copies, as in the source quantum protocol. For fixed
\(\alpha\), this is a constant number. The transmitted Hilbert space has
log-dimension \(O(\log(n)/\alpha)\), hence \(O(\log n)\) at fixed \(\alpha\).
For any preparation ensemble, the classical--quantum mutual information is
bounded by the log-dimension, so

$$
I(X:Q)=O(\log n).
$$

Thus the matched cut comparison is

$$
I(X:Q)=O(\log n)
\qquad\text{versus}\qquad
I(X:\Lambda\mid S)=\Omega(\sqrt n)
$$

for fixed \(\alpha\).

This does not violate Holevo's theorem. Bob is not extracting all of \(x\).
His later choice \(y\) determines which relational phase question is asked.
The quantum state compactly preserves the family of possible responses.

---

## 10. What has actually become invariant

The theorem is insensitive to:

- replacing \(\Lambda\) by a measurably isomorphic coordinate system;
- writing the full carrier in one real variable;
- appending input-independent idle noise;
- splitting one ontic label into redundant clones; and
- using a finite or continuous representation.

What is lower-bounded is preparation information retained in a positive
future-sufficient boundary under the hard operational ensemble.

This is stronger than raw cardinality but weaker than a total physical-memory
theorem. A laboratory memory device may encode mutual information with
different energy, volume, stability, and precision costs. Those relations
require additional physics.

---

## 11. Consequences for “one exact real”

Suppose the full preparation \(x\) is deterministically injected into one real
coordinate

$$
\lambda=f(x).
$$

Then its mutual information with \(X\) is exactly \(H(X)\). More generally,
if a randomized real coordinate is sufficient for every later matching
response, its mutual information under the hard ensemble is charged, and the
theorem forces at least

$$
\Omega(\!\sqrt{n/\alpha})
$$

bits of preparation information.

Calling \(\lambda\) “one variable” therefore provides no compression. To turn
coordinate count into physical economy, the theory would have to bound
precision, noise tolerance, preparation dynamics, and readout response.

---

## 12. Indivisibility remains the central live branch

The theorem assumes that a positive cut variable approximately screens the
preparation from the future reader.

An indivisible whole-history law may instead have

$$
P(\hat b\mid x,y)
$$

without any \(\Lambda\) for which

$$
P(\hat b\mid x,y)
=
\int\mu_x(d\lambda)\xi_y(\hat b\mid\lambda).
$$

Then neither the finite-capacity theorem nor the mutual-information theorem
applies. This is not a loophole to close by definition; it is the exact
Barandes/ISP possibility to investigate.

But it now carries a precise obligation:

> Construct one uniform, intervention-compatible indivisible law that produces
> the scalable response family without receiving the quantum state, the future
> program, or a separate joint table as uncounted input.

If such a law exists, its explanatory gain would lie in lawful whole-process
organization—not in a small classical intermediate state.

The precursor contract for testing that obligation is preserved in
`../../snapshots/v17_uniform_indivisible_law_classification_gate.md`. Its root
audit orders a split-before-pin sequence: this continuous theorem first,
multi-time/uniform-generation classification second, and a separate
causal-locality/Tsirelson gate only after a complete stochastic interface
exists.

---

## 13. Premise-escape ledger

### E1 — accept the information burden

Retain positive cut sufficiency and accept

$$
I(X:\Lambda\mid S)=\Omega(\sqrt n).
$$

This is coherent and may still be physically economical on other resource
coordinates.

### E2 — deny positive cut sufficiency

Use a genuinely indivisible whole-history law. The next gate is uniformity and
intervention compatibility, not cut-state compression.

### E3 — correlate shared structure with inputs

Allow \(S\not\perp(X,Y)\). This is measurement dependence, a common-boundary
condition, superdeterministic correlation, or another physical mechanism. It
must be named and tested.

### E4 — allow future-dependent preparation

Use \(\mu_{x,y}\) instead of \(\mu_x\). This introduces backward information,
retrocausal structure, or whole-program compilation.

### E5 — use a nonpositive or noncommutative cut boundary

Retain amplitudes, operators, signed/quasiprobability data, or another
phase-complete nonclassical state. The representation changes; the compact
response structure remains.

### E6 — lose a constant success margin

If

$$
\delta+\varepsilon_{\rm fac}\ge\frac12,
$$

the model does not provide a nontrivial bounded-error solution to the task and
the lower bound need not apply.

### E7 — change the experiment family

The theorem is not universal over all physical tasks. A smaller reader family
may require less information. The exact experiment domain must remain printed.

### E8 — predict a deviation

A candidate may disagree with the quantum task statistics. That creates an
empirical branch only after its parameters and error profile are independently
fixed.

---

## 14. Hostile controls

1. Count coordinate dimension instead of mutual information.
2. Encode \(x\) in one exact real and declare unit cost.
3. Append idle noise and claim increased explanatory capacity.
4. Let shared randomness depend on \(x\), \(y\), or the promise bit.
5. Let the response-vector quantizer depend on the actual future \(y\) rather
   than the entire registered reader family.
6. Quantize only average responses while claiming worst-case error.
7. Omit approximate-factorization error from the total error budget.
8. Choose \(\eta\) after seeing the result.
9. Use an error threshold approaching \(1/2\) while retaining a constant-gap
   asymptotic claim.
10. Replace the fixed natural hard distribution with a favorable prior.
11. Claim the lower bound for every preparation ensemble.
12. Count public randomness as preparation information despite independence.
13. Fail to count it when it is correlated with the inputs.
14. Apply data processing in the wrong direction.
15. Assume that finite response-vector quantization makes the ontology itself
    discrete.
16. Promote a mutual-information bound into an energy or spacetime-volume
    bound without a bridge law.
17. Compare quantum and classical cut information while ignoring total
    preparation/control resources.
18. Treat failure of screening as failure of all positive histories.
19. Treat lawful nondivision as earned without a uniform intervention theorem.
20. Promote compact nonclassical response capacity into complex-amplitude
    ontology selection.
21. Infer chronology from the one-way laboratory schedule.
22. Infer locality from absence of backward communication in this task.
23. Promote established quantum-information behavior into a novel empirical
    wedge.
24. Generalize from this promise family to arbitrary QFT or gravity.
25. Swap \(\exists\pi\,\forall M\) for the weaker post-hoc order
    \(\forall M\,\exists\pi_M\).
26. Cite the Jain--Radhakrishnan--Sen multi-round theorem as though it were the
    exact one-round source used here.
27. Use the expected-length correlation-simulation result without the Markov
    truncation and deterministic fixing needed for distributional complexity.
28. Forget that \(\alpha n\) must be integral, or silently change the matching
    convention along the scaling sequence.
29. Replace HJMR's printed external information \(I(XY;Q)\) by the different
    internal quantity \(I(X;Q\mid Y)\).
30. Treat the source proof parameter \(\varepsilon_s\) as the Q-Cut screening
    error or compression slack.
31. Mix the source's unnormalized \(L^1\) total-variation convention with the
    normalized convention used for binary screening.
32. Set the HJMR additive \(O(1)\) term to zero instead of absorbing it into a
    uniform large-\(n\) threshold.

---

## 15. Result ladder

```text
L0  FINITE-ALPHABET CUT-CAPACITY LOWER BOUND
L1  HARD-ENSEMBLE MESSAGE-INFORMATION LOWER BOUND
L2  STANDARD-BOREL RESPONSE-QUANTIZATION REDUCTION
L3  APPROXIMATE CONTINUOUS CUT-INFORMATION LOWER BOUND
L4  MULTI-SLOT COMPLETE-PROCESS EXTENSION
L5  UNIFORM INDIVISIBLE-LAW CLASSIFICATION
L6  PHYSICAL MEMORY / PRECISION / ENERGY BRIDGE
L7  EMPIRICAL OR INDEPENDENT-PRINCIPLE ONTOLOGY SELECTION
```

This private candidate reaches L3 by combining published results with the
response-vector quantization lemma. It does not claim L4--L7.

---

## 16. Root pre-review audit

This is an author audit, not independent review.

| Coordinate | Verdict | Reason |
|---|---|---|
| BHM communication lower bound | pass with source scope | published for constant bounded error and \(0<\alpha\le1/4\) |
| hard-distribution information lower bound | pass with source scope | the original proof fixes the natural uniform \(X,\mathsf M,B\) ensemble; HJMR Lemma V.3 supplies compression |
| standard-Borel carrier | candidate pass | only measurable finite response family and ordinary kernels are used |
| response-vector quantization | candidate pass | finite \(\mathcal Y_n\) gives a finite uniform mesh and pointwise response error \(\le\eta\) |
| public randomness removal | candidate pass | sample \(S\) privately and transmit its quantized complete response label; data processing charges only input-correlated content |
| approximate-factorization robustness | candidate pass | TV errors add before applying the constant-gap information theorem |
| fixed-slack quantifier | candidate pass | \(\delta_*-(\delta+\varepsilon_{\rm fac}+\eta)=g_{\rm err}>0\) is fixed independently of \(n\), so message compression preserves the asymptotic constant |
| quantum mutual-information comparison | pass with log-dimension scope | fixed \(\alpha\) uses a constant number of \(n\)-dimensional carriers |
| computational efficiency | refused | the response-vector reduction is existential and may be nonuniform or computationally enormous |
| total physical-cost claim | refused | preparation, energy, time, and hardware coordinates are not bounded |
| indivisible-history no-go | refused | failure of positive cut sufficiency is explicitly live |
| ontology selection | refused | response capacity is constrained; representation remains open |
| empirical novelty | none | uses established communication behavior |
| chronology / spacetime / gravity | closed | no endogenous order or geometry is constructed |

Highest-risk points for independent review are:

1. exact constants and quantifiers in HJMR Lemma V.3 and the natural-distribution lower bound;
2. measurability of the response-vector map for bundled carriers;
3. transformation of public shared randomness into the finite private message;
4. error accounting for approximate screening; and
5. whether any accepted ISP interface uses a weaker notion than the screening
   identity printed here.

Private ceiling:

```text
P17-CANDIDATE-CONTINUOUS-POSITIVE-CUT-INFORMATION-LOWER-BOUND
WITH-APPROXIMATE-SCREENING-AND-INDIVISIBILITY-ESCAPE
```

---

## 17. Source anchors

- D. Gavinsky, J. Kempe, I. Kerenidis, R. Raz, and R. de Wolf,
  “Exponential separations for one-way quantum communication complexity, with
  applications to cryptography,” arXiv `quant-ph/0611209v3`,
  <https://arxiv.org/abs/quant-ph/0611209v3>.
- P. Harsha, R. Jain, D. McAllester, and J. Radhakrishnan, “The communication
  complexity of correlation,” *IEEE Transactions on Information Theory*
  **56**, 438--449 (2010), especially Result 1 and Lemma V.3,
  <https://doi.org/10.1109/TIT.2009.2034824>.
- Exact retrieved-byte receipts and the complete source derivation are in
  `v17_qcut_primary_source_reconstruction.md`.
