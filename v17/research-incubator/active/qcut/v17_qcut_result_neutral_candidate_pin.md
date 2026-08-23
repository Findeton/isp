# ISP v17 — Q-Cut result-neutral candidate pin

**Status:** ACTIVE INCUBATOR CANDIDATE / NOT FROZEN / NO UNIT OPENED

**Date:** 2026-08-23

**Scientific result awarded:** none
**Authority created:** none

Working label: **Q-Cut — ordinary-positive cut-information gate**

This document is a candidate mathematical pin for possible future
authorization. It does not reopen Paper 04B, select an ontology, authorize a
construction or review, open Paper 05, or make a chronology, spacetime,
gravity, hardware, or implementation claim.

---

## 0. Prior-derivation disclosure

This pin was drafted after an author-side proof candidate, source audit, and
primary-source reconstruction already existed:

- `v17_continuous_cut_information_theorem_candidate.md`;
- `v17_continuous_cut_source_quantifier_audit.md`; and
- `v17_qcut_primary_source_reconstruction.md`.

Accordingly, a later panel cannot honestly be described as blind discovery.
If authorized, independent reviewers must reconstruct the source theorems and
proof from the frozen pin before consulting the author-side derivation. Their
task would be independent verification and counterexample search.

The present pin remains result neutral. The permitted terminal outcomes include
proof, counterexample, source insufficiency, or scope reduction forced by an
identified premise failure.

---

## 1. Reality-first question

Consider a scalable quantum preparation--reader family with an exponential
one-way quantum/classical separation. Suppose a proposed microscopic
description inserts an ordinary positive random variable at the operational
cut between preparation and a later freely chosen reader, and that this
variable approximately screens the preparation from every registered reader.

The exact question is:

> Can the positive cut be continuous, uncountable, or encoded in one exact
> real while retaining only \(o(\sqrt n)\) bits of preparation information, or
> must every such future-sufficient cut carry \(\Omega(\sqrt n)\) mutual
> information on one fixed physical task ensemble?

The gate does not ask whether all stochastic histories admit such a cut. A
genuinely indivisible whole-history law is an explicit outside branch.

---

## 2. Fixed operational task

### 2.1 Sizes and matching fraction

Freeze

$$
\alpha=\frac14,
\qquad
\mathcal N=4\mathbb N.
$$

For every \(n\in\mathcal N\), let \(\mathcal X_n=\{0,1\}^n\). Let
\(\mathcal M_n\) be the finite set of matchings containing exactly \(n/4\)
pairwise disjoint edges on \([n]\). Let

$$
\mathcal Y_n
=
\mathcal M_n\times\{0,1\}^{n/4}.
$$

No other \(\alpha\), rounding convention, graph family, or subsequence may be
substituted after evaluation.

### 2.2 Promise relation

For \(x\in\mathcal X_n\), \(\mathsf M\in\mathcal M_n\), and
\(w\in\{0,1\}^{n/4}\), the pair \((x,y)\), \(y=(\mathsf M,w)\), is promised
when there is a unique \(b\in\{0,1\}\) satisfying

$$
w=\mathsf Mx\oplus b^{n/4}.
$$

The required output is \(b\). This is the
\(\alpha\)-Partial Matching / Boolean Hidden Matching promise task at
\(\alpha=1/4\).

### 2.3 Natural hard ensemble

Freeze \(\pi_n^{\rm nat}\) by sampling:

1. \(X\) uniformly from \(\mathcal X_n\);
2. \(\mathsf M\) uniformly from \(\mathcal M_n\), independently of \(X\);
3. \(B\) uniformly from \(\{0,1\}\), independently of \((X,\mathsf M)\);
4. \(W=\mathsf M X\oplus B^{n/4}\); and
5. \(Y=(\mathsf M,W)\).

The same \(\pi_n^{\rm nat}\) applies to every candidate realizer. The frozen
quantifier order is

$$
\forall n\in\mathcal N
\quad
\forall\mathcal R\in\mathfrak R_n^+,
$$

with the task ensemble already fixed. A realizer-dependent prior is forbidden.

---

## 3. Fixed positive-cut class

For each \(n\), an admitted realizer
\(\mathcal R\in\mathfrak R_n^+\) supplies the following data.

### 3.1 Input-independent shared structure

It supplies a standard-Borel probability space

$$
(\mathcal S,\Sigma_{\mathcal S},\nu)
$$

and a random variable \(S\sim\nu\) satisfying

$$
S\perp(X,Y)
$$

under \(\pi_n^{\rm nat}\otimes\nu\). The space and measure may depend on
\(n\) and on the realizer. This gate does not yet impose uniform law
description across sizes.

### 3.2 Bundled cut carrier

It supplies a standard-Borel total carrier \((\mathcal E,\Sigma_{\mathcal E})\)
and a Borel projection

$$
p:\mathcal E\longrightarrow\mathcal S.
$$

For every \((x,s)\), it supplies a probability kernel

$$
\mu_{x,s}(de)
$$

jointly measurable in \((x,s)\), supported on the fiber
\(p^{-1}(s)\). Write \(\Lambda\in\mathcal E\) for the sampled cut value, so
that \(p(\Lambda)=S\) almost surely.

The preparation kernel may depend on \(x\) and \(s\), but not on Bob's later
input \(y\), the promise bit \(b\), or a future adaptive programme.

### 3.3 Registered response family

For every \(y\in\mathcal Y_n\), it supplies a Borel response function

$$
\xi_y:\mathcal E\longrightarrow[0,1].
$$

Given cut value \(e\), the screened reader outputs \(1\) with probability
\(\xi_y(e)\). Thus

$$
P_{\rm cut}(1\mid x,y)
=
\int_{\mathcal S}\nu(ds)
\int_{\mathcal E}\mu_{x,s}(de)\,\xi_y(e).
$$

The response functions are part of the realizer's law packet and are defined
for the entire frozen reader family before the actual \(y\) is supplied.

### 3.4 Actual registered output law

The realizer supplies a normalized binary law

$$
P_{\rm act}(\hat b\mid x,y),
\qquad
\hat b\in\{0,1\},
$$

for every promised pair. It need not be exactly cut-factorized, but must obey
both accuracy and approximate screening below.

No actual-history selector, occurrence law, microscopic trajectory, spacetime,
or energy interpretation is part of this pin.

---

## 4. Frozen numerical gates

### 4.1 Actual task accuracy

For every promised \((x,y)\) with task value \(b\), require

$$
P_{\rm act}(\hat b\ne b\mid x,y)
\le
\delta_{\rm act}
:=
\frac1{10}.
$$

### 4.2 Approximate positive screening

For every promised \((x,y)\), require

$$
\left\|
P_{\rm act}(\cdot\mid x,y)
-
P_{\rm cut}(\cdot\mid x,y)
\right\|_{\rm TV}
\le
\varepsilon_{\rm fac}
:=
\frac1{40}.
$$

### 4.3 Proof quantization and compression margins

Freeze

$$
\eta=\frac1{40},
\qquad
\Delta=\frac1{20},
\qquad
\delta_*=\frac13.
$$

The induced private-coin protocol has error at most

$$
e
=
\delta_{\rm act}+\varepsilon_{\rm fac}+\eta
=
\frac3{20},
$$

and after message-compression truncation has error at most

$$
e+\Delta
=
\frac15
<
\delta_*.
$$

These constants may not be changed after construction or review. A parametric
extension may be reported only as an additional theorem after the fixed core
is adjudicated independently.

---

## 5. Frozen information coordinate

Compute all information quantities using logarithms base two under
\(\pi_n^{\rm nat}\), \(S\sim\nu\), and
\(\Lambda\sim\mu_{X,S}\). The sole lower-bounded coordinate is

$$
C_{\rm cut}(\mathcal R;n)
:=
I(X:\Lambda\mid S)
\in[0,\infty].
$$

Conditional mutual information is the standard relative-entropy quantity on
standard-Borel spaces. If it is infinite, the lower bound is satisfied but no
finite physical-resource interpretation follows.

The pin does not substitute:

- carrier cardinality;
- coordinate dimension;
- differential entropy;
- raw message length;
- number of histories;
- source-code length;
- runtime; or
- energy, volume, stability, or precision.

Those are distinct coordinates requiring separate bridge laws.

---

## 6. Core theorem-or-counterexample target

The core target is exactly one of the following mutually exclusive outcomes.

### Q-CUT-POSITIVE

Prove that there are constants \(c>0\) and \(n_0\), independent of the
realizer, such that

$$
\forall n\in\mathcal N, n\ge n_0,
\quad
\forall\mathcal R\in\mathfrak R_n^+,
\qquad
I(X:\Lambda\mid S)
\ge
c\sqrt n.
$$

The proof must reconstruct the source lower bound, the exact HJMR
message-compression specialization, bundled-carrier measurability, complete
response quantization, correlated-input conditional independence, error
monotonicity, and data processing.

### Q-CUT-COUNTEREXAMPLE

Construct an explicit infinite family

$$
\{\mathcal R_n\in\mathfrak R_n^+\}_{n\in\mathcal N}
$$

satisfying every frozen gate but with

$$
I(X:\Lambda\mid S)=o(\sqrt n)
$$

along an infinite admissible subsequence. Every kernel, measurability claim,
error calculation, and information calculation must be explicit.

### Q-CUT-SOURCE-FAILURE

Show that a cited external theorem does not imply the needed statement and
that the gap cannot be repaired from the frozen sources without a new theorem.
The precise missing quantifier or premise must be identified.

### Q-CUT-ILL-TYPED

Show that the admitted model class or information coordinate is not
mathematically well defined. A repair changing the class, task, thresholds, or
carrier type requires a new pin; it cannot be silently inserted.

---

## 7. Quantum comparator

For the same \(\alpha=1/4\) task, the comparator sends exactly three copies of

$$
|\psi_x\rangle
=
\frac1{\sqrt n}
\sum_{i=1}^n(-1)^{x_i}|i\rangle.
$$

Each copy reveals an edge parity with probability \(2\alpha=1/2\) and declares
failure otherwise. If all three copies fail, Bob guesses fairly. The resulting
error is

$$
\frac12\left(1-2\alpha\right)^3
=
\frac1{16}
<
\frac1{10}.
$$

The total transmitted log-dimension is \(3\log_2 n\), an implementation uses
at most \(3\lceil\log_2n\rceil\) qubits, and the cq mutual information is at
most

$$
3\log_2 n=O(\log n).
$$

This comparator is used only to establish a matched operational separation:

$$
O(\log n)\ \text{qubits}
\quad\text{versus}\quad
\Omega(\sqrt n)\ \text{positive cut information}.
$$

It does not prove that Hilbert space, complex amplitudes, or the quantum state
is ontologically fundamental. It does not compare energy, apparatus size,
preparation time, or total explanatory cost.

---

## 8. Mandatory proof obligations

An accepted positive proof must establish all of the following.

1. **Source fidelity:** the natural-distribution lower bound is reconstructed
   at error \(1/3\) for \(n\in4\mathbb N\), with the source proof parameter
   and total-variation convention printed separately from Q-Cut errors.
2. **Promise typing:** HJMR applies to the promise relation, or to an arbitrary
   total extension with distribution supported on the promise.
3. **One-way identity:** the induced finite message \(Q\) obeys
   \(Q\perp Y\mid X\), hence \(I(X,Y:Q)=I(X:Q)\).
4. **Bundle measurability:** the total response-vector map is Borel on
   \(\mathcal E\).
5. **Finite quantization:** one fixed quantizer handles every
   \(y\in\mathcal Y_n\) with coordinate error at most \(1/40\).
6. **No actual-reader dependence:** the quantizer uses the whole frozen reader
   family and is not selected after seeing \(y\).
7. **Error ledger:** actual, screening, quantization, and compression errors
   sum exactly as printed.
8. **HJMR specialization:** expected communication is converted to a
   deterministic worst-case-length protocol using the charged
   \(\Delta=1/20\); HJMR's external information definition and universal
   additive \(O(1)\) term are retained.
9. **Hard lower bound:** distributional complexity at error \(1/5\) is at
   least that at error \(1/3\).
10. **Data processing:** \(Q=q(S,\Lambda)\) implies
    \(I(X:Q)\le I(X:\Lambda\mid S)\).
11. **Uniform constants:** \(c,n_0\) do not depend on the realizer.
12. **Scope ceiling:** no inference to physical memory, indivisible histories,
    ontology selection, chronology, spacetime, or gravity is made.

Failure of any obligation blocks the positive theorem at the corresponding
rung.

---

## 9. Hostile controls

The review battery must include at least:

1. one real encoding all of \(x\);
2. an uncountable carrier with overlapping conditional densities;
3. infinite conditional mutual information;
4. arbitrarily large input-independent public randomness;
5. public randomness correlated with \(X\);
6. public randomness correlated with \(Y\);
7. a preparation kernel depending on the actual future reader;
8. a response-vector label quantized only at the realized reader;
9. average reader approximation presented as uniform approximation;
10. a nonmeasurable response assignment;
11. a non-standard-Borel carrier;
12. a bundle whose fiber support condition fails;
13. a promise relation treated as a total function without justification;
14. the quantifier swap \(\forall\mathcal R\exists\pi_{\mathcal R}\);
15. a model-dependent hard prior;
16. message entropy substituted for mutual information;
17. HJMR's external information \(I(X,Y:Q)\) replaced by a different internal
    information notion, or reduced to \(I(X:Q)\) without proving conditional
    independence;
18. expected communication mistaken for worst-case message length;
19. Markov truncation applied without charging error;
20. a vanishing compression slack;
21. actual, screening, and quantization errors not added;
22. data processing used in the wrong direction;
23. idle-label cloning;
24. ontic-coordinate splitting;
25. a finite response label misreported as a finite ontology;
26. a law-sized lookup table ignored because the theorem counts only state
    information;
27. computationally intractable response-vector construction advertised as an
    efficient model;
28. the quantum comparator credited with an ontological conclusion;
29. failure of positive screening reported as failure of positive histories;
30. a genuinely indivisible law forced into the cut class by definition;
31. the laboratory one-way schedule called emergent time;
32. communication separation called spatial nonlocality;
33. established behavior called a new empirical deviation;
34. extrapolation to QFT, gravity, or continuum physics;
35. the source proof parameter \(\varepsilon_s\) identified with screening
    error, quantization mesh, or compression slack;
36. the source's unnormalized \(L^1\) distance mixed with normalized total
    variation; and
37. the universal HJMR additive term discarded instead of absorbed into a
    realizer-independent large-\(n\) threshold.

---

## 10. Result ladder and claim ceilings

```text
L0  SOURCE THEOREMS RECONSTRUCTED
L1  FINITE RESPONSE-QUANTIZATION LEMMA
L2  CORRELATED-INPUT ONE-WAY INFORMATION IDENTITY
L3  FIXED-FAMILY CONTINUOUS POSITIVE-CUT LOWER BOUND
L4  PARAMETER-UNIFORM CUT CLASSIFICATION
L5  MULTI-TIME COMPLETE-PROCESS CLASSIFICATION
L6  UNIFORM INDIVISIBLE GENERATIVE LAW
L7  PHYSICAL MEMORY / ENERGY / PRECISION BRIDGE
L8  EMPIRICAL OR PRINCIPLE-BASED ONTOLOGY SELECTION
```

The fixed pin can earn at most L3. A parametric corollary may clarify the
mathematics but cannot promote the unit past L3. L4--L8 require separately
authorized gates.

Permanent nonclaims:

```text
UNIVERSAL CLASSICAL ONTOLOGY NO-GO:      NOT AVAILABLE
BARE POSITIVE-HISTORY NO-GO:             NOT AVAILABLE
BARANDES THEORY REFUTATION:              NOT AVAILABLE
COMPLEX AMPLITUDES ONTICALLY SELECTED:   NOT AVAILABLE
PHYSICAL MEMORY OR ENERGY LOWER BOUND:   NOT AVAILABLE
NEW EMPIRICAL PREDICTION:                NONE
ENDOGENOUS TIME / CHRONOLOGY:            NONE
SPACETIME / DIMENSION / GRAVITY:         NONE
```

---

## 11. Outcome ladder

| Outcome | Meaning | Permitted continuation |
|---|---|---|
| `ACCEPT-L3` | all core obligations proved | prepare the separate uniform indivisible-law classification gate |
| `ACCEPT-L3-WITH-SCOPE` | core fixed constants proved; optional generalization fails | same continuation, with exact fixed scope |
| `COUNTEREXAMPLE` | admitted sub-\(\sqrt n\) family exists | diagnose which proposed information obstruction was false |
| `SOURCE-FAILURE` | external theorem chain does not close | prove the missing communication theorem or stop |
| `REVISE-PIN` | class is ill typed | return for fresh authority; no silent repair |
| `INCONCLUSIVE` | no proof or counterexample | no promotion and no downstream inference |

No outcome automatically authorizes another unit.

---

## 12. Primary-source versions and receipts

The future pin should bind these exact source versions:

1. D. Gavinsky, J. Kempe, I. Kerenidis, R. Raz, and R. de Wolf,
   “Exponential separations for one-way quantum communication complexity, with
   applications to cryptography,” arXiv:quant-ph/0611209v3, especially
   Sections 2 and 3.3,
   <https://arxiv.org/abs/quant-ph/0611209v3>. Retrieved PDF SHA-256:
   `6e623c66dae1406308d28edfdc16693f8c0e760196a17ff91a30901e15a0c783`.
2. P. Harsha, R. Jain, D. McAllester, and J. Radhakrishnan,
   “The communication complexity of correlation,” *IEEE Transactions on
   Information Theory* **56**, 438--449 (2010), Result 1 and Lemma V.3,
   <https://doi.org/10.1109/TIT.2009.2034824>. Retrieved author-PDF SHA-256:
   `f049e5c2ee3c16f3096ccc6b9bf4a28f27ac1fe0acd44da411eb7c081ab05222`.

These are the only load-bearing external sources. Exact retrieval metadata and
the complete author reconstruction are in
`v17_qcut_primary_source_reconstruction.md`.

---

## 13. Candidate disposition

```text
QUESTION:                     FIXED IN ACTIVE DRAFT / BYTES NOT FROZEN
TASK FAMILY:                  ALPHA=1/4 PARTIAL MATCHING, n IN 4N
HARD ENSEMBLE:                EXPLICIT NATURAL DISTRIBUTION
MODEL CLASS:                  STANDARD-BOREL ORDINARY-POSITIVE CUTS
ERROR MARGINS:                EXACT RATIONAL CONSTANTS
TARGET:                       THEOREM / COUNTEREXAMPLE / SOURCE FAILURE
AUTHOR-SIDE PROOF EXISTS:      DISCLOSED
INDEPENDENT REVIEW:           NOT YET AUTHORIZED OR PERFORMED
OFFICIAL PIN:                 NOT FROZEN
SCIENTIFIC RESULT:            NONE
DOWNSTREAM AUTHORITY:         NONE
```
