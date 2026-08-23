# ISP v17 — Barandes source-scope audit for U-Gen

**Status:** PRIVATE / NONBINDING / PRIMARY-SOURCE AUDIT  
**Date:** 2026-08-23  
**Scientific result awarded:** none  
**Authority created:** none

This note determines what the current Barandes papers actually supply to a
uniform complete-process gate. It distinguishes an absence in the cited source
from an impossibility theorem and from a refutation of the ontology.

---

## 1. Sources fixed for this audit

1. J. A. Barandes, “Quantum Systems as Indivisible Stochastic Processes,”
   arXiv:2507.21192v1, manuscript dated August 11, 2026,
   <https://arxiv.org/html/2507.21192v1>.
2. J. A. Barandes, M. Hasan, and D. Kagan, “The CHSH Game, Tsirelson's Bound,
   and Causal Locality,” arXiv:2512.18105v1, manuscript dated August 11, 2026,
   <https://arxiv.org/html/2512.18105>.
3. J. A. Barandes, “The Born Representation Theorem and the Unistochastic
   Theorem,” arXiv:2608.04354, accessed August 23, 2026,
   <https://arxiv.org/html/2608.04354>.

This is a scope audit, not an independent proof audit of every theorem in those
papers.

---

## 2. What the single-system paper literally supplies

### 2.1 Kinematics

Section 5 states that for each model one picks a configuration space whose
members are possible physical configurations. The configuration space is fixed
across real-world runs of that model. The ontology is explicitly described as
realist and non-relational in the perspectival sense.

Therefore v17 may inherit:

```text
ONE PICKED CONFIGURATION SPACE PER MODEL
```

It may not inherit:

```text
BACKGROUND-INDEPENDENT RELATIONAL CONFIGURATION SPACE
UNIQUE CONFIGURATION SPACE OF THE UNIVERSE
```

### 2.2 Contingent state

The standalone distribution $p(i,t)$ is contingent and may vary between runs.
It is linked between target times by the fixed transition laws. This supports
the v17 law/state distinction and contradicts treating the standalone
distribution as a universal selector.

### 2.3 Dynamical law

Section 2.2, equations (18)--(21), states that the laws contain first-order
transition probabilities

$$
\Gamma_{ij}(t\leftarrow t_0)
=
p(i,t\mid j,t_0)
$$

from admitted conditioning times $t_0$—division events—to target times $t$.
Only the corresponding law-of-total-probability relation is required. The
transition law need not divide through arbitrary intermediate times.

Section 5 restates this as the dynamical axiom. Measurement is described as an
interaction with another system that can generate division events.

This supports:

```text
FIXED FIRST-ORDER ENDPOINT LAW
CARRIER-RELATIVE DIVISION / NONDIVISION
MEASUREMENT AS PHYSICAL INTERACTION
```

It does not by itself print a category of arbitrary inserted instruments and
their post-intervention boundaries.

### 2.4 External time interface

The law is indexed by target times and conditioning times. The target time may
be earlier or later than the conditioning time, so the paper does not impose a
fundamental arrow merely by notation. Nevertheless, the real-valued time
parameter is supplied. The paper does not derive an internal clock or
background-free chronology.

---

## 3. What the stochastic--quantum dictionary supplies

### 3.1 Modulus-square lift

Section 3 introduces a potential matrix $\Theta$ with

$$
\Gamma_{ij}(t\leftarrow0)
=
|\Theta_{ij}(t\leftarrow0)|^2.
$$

The potential is explicitly nonunique. The paper then uses Kraus/Stinespring
dilation to obtain a unitary representation when necessary and calls the
resulting relationship the stochastic--quantum theorem.

The 2026 Unistochastic Theorem strengthens endpoint breadth: any finite
stochastic matrix can be obtained by marginalization from a bounded larger
unistochastic matrix. This makes endpoint unistochastic representability broad;
it does not select quantum multi-time laws by itself.

### 3.2 Schur--Hadamard gauge

Section 3.2 declares arbitrary entrywise phase changes of $\Theta$ to be gauge
transformations, with downstream Hilbert ingredients transformed so that all
empirical predictions remain unchanged.

Therefore two potential matrices with the same $\Gamma$ are not automatically
two physical extensions. A valid phase counterexample must keep the complete
physical intervention meanings fixed and show that the *native stochastic
composition data* fail to determine their common-continuation probabilities.
Changing one Hilbert lift while refusing to transform the rest of the
experiment is not source-faithful.

### 3.3 Exact inference for U-Gen

The gauge result prevents a naive claim:

```text
SAME ISOLATED GAMMA + DIFFERENT THETA => DIFFERENT PHYSICS.
```

It does not establish the stronger claim:

```text
ISOLATED SUBSYSTEM GAMMAS UNIQUELY DETERMINE EVERY COMPOSITE INTERVENTION.
```

The latter requires a native rule for composing physical systems, apparatus,
settings, and readers.

---

## 4. Composite systems in the CHSH paper

### 4.1 Composite kinematics

The first postulate states

$$
\mathcal C_{QR}=\mathcal C_Q\times\mathcal C_R.
$$

Section 3.1.1 supplies a parent conditional law

$$
p(q_t,r_t\mid q_0,r_0)
$$

and derives subsystem marginals from it. Factorization of that parent law
defines noninteraction; interacting dynamics need not factorize.

This is real compositional structure: Cartesian-product configuration
kinematics and parent-to-subsystem marginalization are printed.

### 4.2 What is not derived there

The parent conditional law is *defined/supplied*. The paper does not present a
general map that takes two arbitrary subsystem laws plus a typed interaction
procedure and uniquely generates the interacting parent law.

Thus the source supports:

```text
SUBSYSTEMS ARE MARGINALS OF A PARENT STOCHASTIC SYSTEM
NONINTERACTION HAS A FACTORIZATION TEST
```

It does not yet support:

```text
ONE UNIFORM COMPOSITION FUNCTOR GENERATES EVERY PARENT LAW
FROM SUBSYSTEM LAWS AND LOCAL INTERACTION PRIMITIVES.
```

This distinction is the heart of U-Gen.

### 4.3 Overarching experiment as one parent

The CHSH construction explicitly considers an overarching system containing
Alice, Bob, Charlie, the two particles, and their environment. Local operations
are described as indivisible stochastic processes, and the complete parent
system can in principle receive one joint conditional law.

Therefore a failure to derive that joint law from smaller packets would **not**
refute the claim that a fixed complete experiment can be represented as one
indivisible stochastic system. It would show that scalable generation requires
additional parent-law/composition data.

---

## 5. Causality and locality scope

The CHSH paper defines absence of causal influence through conditional
independence of subsystem marginals from another subsystem's initial
configuration. Causal locality then uses spatial separation, elapsed target
time, the speed of light, and light cones.

These are meaningful physical premises on a supplied spacetime background.
They do not derive spacetime, distance, $c$, cone orientation, or chronology.

The Tsirelson proof translates to a unitary representation, requires

$$
(\mathcal{AB})_{xy}
=
\mathcal A_x\otimes\mathcal B_y,
$$

and applies the standard CHSH operator bound. The paper motivates this
factorization by causal locality. A future stochastic-native audit must decide
whether the factorization follows from independently stated stochastic parent
laws or imports the relevant quantum tensor structure through the
representation.

No conclusion on that proof is awarded here.

---

## 6. Multi-time/process-tensor status

Near equation (40), the CHSH paper says:

> “We conjecture” that the quantum description of the displayed non-Markovian
> conditional probability is a quantum-comb or process-tensor case.

The associated construction concerns memories of configurations at division
events and a multi-time dephasing channel. It is explicitly future work, not a
proved complete adaptive-instrument equivalence.

Consequently:

```text
PROCESS-TENSOR CONNECTION:     PUBLISHED CONJECTURE
COMPLETE INTERVENTION FUNCTOR:  NOT ESTABLISHED BY THESE SOURCES
ENDPOINT STOCHASTIC LAW:        ESTABLISHED AT PRINTED SCOPE
```

Absence from these sources is not an impossibility theorem. A later paper or a
new construction could supply the missing interface.

---

## 7. Correct source-faithful U-Gen question

The source does not hand v17 one globally typed family
$\{\mathfrak B_A\}_{A\in\Sigma}$ with a complete composition functor. A future
pin must therefore introduce a **base embedding datum** $\iota_0$ containing:

1. the configuration carrier assigned to every registered laboratory system;
2. the isolated endpoint stochastic packet assigned to each primitive
   preparation, setting device, operation, record, and reader;
3. the physical record meanings and the parent-to-subsystem marginal maps
   explicitly inherited from the source; and
4. the restriction map from candidate endpoint experiments to the published
   packet.

$\iota_0$ may not contain a composite-program response table, an interacting
parent law, a relative phase alignment between independently embedded
operations, or future-continuation probabilities. Cross-context gauge
transport and interacting composition belong to the extension law and must be
charged there.

Then define

$$
\mathsf{Ext}_{\rm src}(\mathfrak B;\iota_0)
=
\{u:
u\text{ is a complete U-law extending the fixed source-faithful }
\iota_0\}/\simeq.
$$

The admissible set $\mathsf{Emb}(\mathfrak B,\Sigma)$ of base embeddings must
also be printed. This prevents the phrase “restricts to Barandes” from doing
untyped work and prevents the embedding itself from carrying the missing
composition law.

The theorem asks whether this extension set is empty, operationally nonunique,
or unique at a printed quotient. It does **not** ask whether Barandes's
fixed-system representation theorem is false.

---

## 8. Phase-sensitive hostile control, correctly typed

Identity and a diagonal phase operation have the same isolated
configuration-basis transition matrix. A mixing continuation can distinguish
their standard quantum procedures.

This is not yet a counterexample to Barandes because:

1. isolated potential phases are gauge;
2. physical apparatus and readers must transform consistently; and
3. the full parent system may have different native joint stochastic laws for
   the two physical procedures.

The valid hostile question is:

> Given fixed source-faithful primitive embeddings and no fresh parent answer
> table, does one native composition law generate the distinct complete parent
> stochastic laws required by the two common continuations?

If yes, the composition datum carries the phase-complete capacity. If no, the
published endpoint packet is insufficient for uniform experiment generation.
Either outcome is informative.

---

## 9. Source-scope conclusions

```text
FIXED CONFIGURATION ONTOLOGY:              YES, PER MODEL
CONTINGENT STANDALONE DISTRIBUTION:         YES
FIRST-ORDER ENDPOINT TRANSITION LAWS:       YES
DIVISION / NONDIVISION:                     YES, CARRIER RELATIVE
MEASUREMENT AS INTERACTION:                 YES
COMPOSITE CONFIGURATION CARTESIAN PRODUCT:  YES IN CHSH SOURCE
PARENT-TO-SUBSYSTEM MARGINALIZATION:        YES
UNIFORM INTERACTING-PARENT GENERATOR:       NOT LOCATED / NOT CONSTRUCTED
COMPLETE ADAPTIVE PROCESS FUNCTOR:          NOT CONSTRUCTED
PROCESS-TENSOR CONNECTION:                 CONJECTURAL
SCHUR--HADAMARD LIFT PHASES:                GAUGE AT COMPLETE-TRANSFORM SCOPE
EXTERNAL TARGET/CONDITIONING TIME:          YES
RELATIONAL INTERNAL TIME:                   NO
SPACETIME OR GRAVITY DERIVATION:            NO
```

The U-Gen direction survives, with one mandatory wording correction:

> A nonunique or missing uniform composition extension identifies additional
> nomological input required for a scalable universal theory. It does not, by
> itself, refute the fixed-system stochastic--quantum correspondence.

Private ceiling:

```text
P17-PRIVATE-BARANDES-SOURCE-SCOPE-AUDIT
NO PROOF AUDIT / NO EXTENSION / NO REFUTATION / NO UNIT OPENED
```
