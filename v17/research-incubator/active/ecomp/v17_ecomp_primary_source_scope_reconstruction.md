# ISP v17 — E-Comp primary-source scope reconstruction

**Status:** ACTIVE AUTHOR-SIDE / PRIMARY-SOURCE RECONSTRUCTION / NOT A REVIEW
**Date:** 2026-08-23
**Scientific result awarded:** none
**Authority created:** none

This document reconstructs the precise interface between E-Comp and the
current Barandes formulation. Its purpose is to prevent a small algebraic
theorem from being misreported either as a refutation of indivisible quantum
theory or as a derivation of quantum composition.

---

## 1. Fixed sources and receipt

### S1 — indivisible stochastic dynamics

Jacob A. Barandes, *Quantum Systems as Indivisible Stochastic Processes*,
arXiv:2507.21192v1:

<https://arxiv.org/html/2507.21192v1>

The arXiv page identifies version 1 and the manuscript itself is dated
August 11, 2026. A PDF retrieved on 2026-08-23 was used for the equation-level
reconstruction below:

```text
SHA-256  109cfcf80e59f10023673395c4f5200d5a3e5894b9a3a99855d7f402edf064aa
pages    35
```

The receipt authenticates the consulted bytes; the PDF is not a v17 premise
artifact and is not copied into the candidate package.

### S2 — endpoint unistochastic representation

Jacob A. Barandes, *The Born Representation Theorem and the Unistochastic
Theorem*, arXiv:2608.04354:

<https://arxiv.org/html/2608.04354>

S2 is used only for the scope statement that endpoint unistochastic
representability is broad, including through bounded enlargement. E-Comp does
not audit or rely on the proof of that theorem.

### S3 — composite-system comparator

Jacob A. Barandes, Mohammad Hasan, and David Kagan, *The CHSH Game,
Tsirelson's Bound, and Causal Locality*, arXiv:2512.18105:

<https://arxiv.org/html/2512.18105>

S3 is a comparator for the distinction between a supplied parent law and a
uniform rule that generates interacting parent laws. No CHSH result is used in
the E-Comp proof.

---

## 2. What S1 supplies

### 2.1 Kinematics, contingent state, and law

S1 treats a configuration space as fixed for each model. Its standalone
probability distribution is contingent between runs. The transition
probabilities are fixed nomological data.

This supports the E-Comp separation among:

```text
configuration carrier       fixed model ingredient
preparation distribution    contingent state
transition family           dynamical law
```

E-Comp's two-state carrier and basis preparations are declared control data.
They are not claimed to be the unique ontology of a qubit or of nature.

### 2.2 First-order indivisible law

S1 equation (18) defines first-order transition matrices

$$
\Gamma_{ij}(t\leftarrow t_0)=p(i,t\mid j,t_0),
$$

and equations (19)--(20) give the law-of-total-probability relation

$$
p(t)=\Gamma(t\leftarrow t_0)p(t_0).
$$

The conditioning time $t_0$ must be an admitted division event, whereas the
target time is free. S1 expressly does not require every intermediate time to
be a division event. Its equations (22)--(23) introduce the attempted
factorization whose failure is indivisibility.

This licenses E-Comp to compare complete first-order laws from an initial
division to a later target without inserting a hidden trajectory or a
stochastic state at the unmeasured intermediate syntax boundary.

### 2.3 Measurement and division

S1's dynamical axiom states that division events may arise through physical
interactions and names measurement as an example. E-Comp nevertheless declares
its reader $m$ and its division behavior explicitly; it does not infer a
universal measurement theorem from the source.

### 2.4 Complete target law may be primitive nomology

For arbitrary targets from an admitted division, S1 permits the model's fixed
law to contain the relevant transition matrix directly. Therefore a complete
Barandes model can supply the two-use transition $\Gamma_{bb}$ independently
of the isolated one-use endpoint $G$.

This fact is binding:

```text
E-COMP DOES NOT CLAIM THAT A COMPLETE FIXED BARANDES LAW LACKS Γ_bb.
```

E-Comp asks the different logical question whether $\Gamma_{bb}$ follows from
the restricted packet containing only $G$, the typed reader, and the stated
nondivision predicate. It does not.

---

## 3. Gauge reconstruction

S1 equation (25) introduces a nonunique potential matrix through

$$
\Gamma_{ij}=|\Theta_{ij}|^2.
$$

Equations (29)--(30) allow entrywise phase changes in $\Theta$. S1 treats these
as gauge because downstream Hilbert-space ingredients change consistently so
that empirical probabilities do not.

The resulting firewall is:

1. two matrices with the same isolated modulus squares are not thereby two
   physical laws;
2. no isolated lift phase may be called an ontic observable;
3. a complete gauge transformation must preserve every registered outcome
   probability; and
4. two completed native laws that give different probabilities to one fixed
   preparation and reader are not gauge presentations of that complete
   experiment.

E-Comp respects this firewall. It does not claim that $H$ and $V$ are distinct
physics at the isolated endpoint. Instead, it uses them to construct two
different completions of an intentionally incomplete positive packet:

$$
|H|^{\odot2}=|V|^{\odot2}=G,
$$

but

$$
|H^2|^{\odot2}=I_2,
\qquad
|V^2|^{\odot2}=X.
$$

Once the preparation and final reader are fixed, these completed positive laws
make different predictions. The difference is not an isolated phase
observable; it is the missing cross-operation composition datum.

---

## 4. The source-independent mathematical theorem

Let

$$
q(U)=|U|^{\odot2}
$$

and define $U\sim V$ iff $q(U)=q(V)$. The registered $H,V$ pair proves that
$\sim$ is not a congruence under multiplication. If an endpoint-only product
$\star$ satisfied

$$
q(U_2U_1)=q(U_2)\star q(U_1)
$$

for all unitaries, then the identical endpoint input pair $(G,G)$ would have
to yield both $I_2$ and $X$. This is impossible.

This theorem is independent of any interpretation of amplitudes. It says that
the modulus-square endpoint quotient cannot inherit the full sequential
product. It does not prohibit:

1. a richer positive whole-history law;
2. a gauge-covariant lift;
3. a larger physical carrier or dilation;
4. a direct complete-program assignment; or
5. full empirical calibration that supplies the missing datum.

Each remedy must simply be counted as structure beyond the isolated endpoint
matrix.

---

## 5. Full-calibration counterfactual

A laboratory Hadamard is not operationally defined only by its basis-input,
basis-output one-use probabilities. Process tomography or phase-sensitive
continuations distinguish it from $V$. If those complete calibration data are
placed in the antecedent, then $H$ and $V$ are not two completions of the same
physical primitive.

That observation does not weaken E-Comp. It identifies the missing input:

```text
BARE POSITIVE ENDPOINT G          insufficient for sequential composition
FULL PROCESS CALIBRATION          supplies phase-sensitive continuation data
UNIFORM FUNDAMENTAL THEORY        must explain or lawfully encode those data
```

The research question is therefore not whether experiments distinguish the
members. They do. It is whether a proposed fundamental stochastic ontology
generates the calibrated composition structure from independently physical
principles or simply supplies each complete transition family as law.

---

## 6. S2 and dilation scope

S2 strengthens the case that representing a finite stochastic endpoint by a
unitary construction—possibly after enlargement—is not by itself a selective
physical explanation. E-Comp accordingly makes no claim of nonfactorization
through every larger carrier.

Its rank argument is precisely carrier-relative:

$$
\operatorname{rank}(KG)\le1
$$

for every stochastic continuation $K$ on the printed two-state intermediate
carrier, whereas $I_2$ and $X$ have rank two. A larger carrier changes the
declared extension and must be charged for its variables and continuation
law.

---

## 7. S3 and parent-law scope

S3 uses a parent conditional stochastic law for composite systems and obtains
subsystem behavior by marginalization. This demonstrates a legitimate route:
the complete parent may carry information absent from isolated subsystem
endpoints.

E-Comp does not deny that route. It sharpens the next question: whether one
uniform physical principle generates the required parent laws across arbitrary
interactions and interventions, or whether the complete parent law is supplied
case by case. That is outside the E-Comp theorem and belongs to a later
composition-lift classification.

---

## 8. Quantifier ledger

| Claim | Status at author-side scope |
|---|---|
| The printed $Q,M,V$ block families are normalized | exact candidate calculation |
| They agree on the isolated endpoint packet | exact candidate calculation |
| $Q$ and $V$ are nondivisible through the printed carrier at $bb$ | exact candidate rank proof |
| Endpoint equivalence is not a multiplication congruence | exact candidate theorem |
| A full fixed Barandes law may supply $\Gamma_{bb}$ | source-supported scope |
| Barandes derives every complete law from $G$ alone | not claimed; not located |
| Isolated lift phases are ontic | prohibited |
| Complex Hilbert amplitudes are the unique remedy | not established |
| A larger dilation is impossible | not claimed |
| Quantum composition, QFT, spacetime, or gravity is derived | no |

---

## 9. Present disposition

```text
PRIMARY-SOURCE INTERFACE:       RECONSTRUCTED AUTHOR-SIDE
GAUGE DISTINCTION:              BINDING
FIXED-LAW REFUTATION:           NO
ENDPOINT NO-CONGRUENCE THEOREM: SOURCE-INDEPENDENT CANDIDATE
INDEPENDENT SOURCE REVIEW:      NOT AUTHORIZED / NOT RUN
SCIENTIFIC RESULT:              NONE
```
