# ISP v17 — exact law universe for the U-Gen gate

**Status:** PRIVATE / NONBINDING / NOT A PIN / NO UNIT AUTHORIZED  
**Date:** 2026-08-23  
**Scientific result awarded:** none  
**Authority created:** none

This document replaces the schematic phrase “all uniform indivisible laws” by
two literal, set-sized mathematical classes. It does not select a model, assume
that nature is computable, repair Paper 04B, or open chronology, spacetime, or
gravity.

The construction is deliberately result-neutral. Standard Hilbert dynamics is
an admitted positive control. Barandes-style endpoint laws are admitted at
their proved scope. Global or noncomputable laws are classified rather than
discarded. The gate asks where the complete quantum predictive content enters;
it does not reject a candidate for failing to use preferred vocabulary.

---

## 1. Decision forced by Paper 01

An existence-only U-Gen question would be vacuous. On a fixed universal gate
grammar, the standard quantum evaluator is one finite rule that assigns an
ordinary positive probability measure to every completed record transcript.
Paper 01 already gives the more general per-process record-history
representation.

The nontrivial questions are instead:

1. **uniformity:** is one law fixed before system size, circuit depth, context,
   and held-out continuation are known?
2. **input location:** is an arbitrary target process supplied as contingent
   data, or generated from a fixed primitive law?
3. **nomological residue:** are the fixed primitives merely a Hilbert/process
   law in another notation, or is phase-complete structure derived from
   independently stated stochastic principles?
4. **multi-time completeness:** does the law determine every admitted
   intervention and continuation, rather than endpoint matrices only?
5. **temporal premise:** is the construction prefix-autonomous, globally
   constrained, retrocausal, measurement-dependent, or empirically different?
6. **selection:** does any observation or independent physical principle
   distinguish the candidate from operationally equivalent rivals?

These coordinates are independent. In particular,

$$
\text{uniform generation}
\not\Longrightarrow
\text{Hilbert-free nomology}
\not\Longrightarrow
\text{ontology selection}.
$$

---

## 2. Fixed scalable laboratory grammar

### 2.1 Types

Fix the finite typed signature $\Sigma_{\rm UQ}$ with generating wire types:

- $Q$, a two-level laboratory system;
- $B$, a retained classical bit;
- $F$, a retained success/failure bit; and
- $I$, the monoidal unit.

Finite tensor words in these types are the system interfaces. A label such as
$Q$ denotes a supplied laboratory port, not a claim that Hilbert space is
ontic. Likewise, tensor notation denotes independently wireable ports in the
registered laboratory grammar, not a derived spatial relation.

### 2.2 Primitive physical procedures

The finite primitive list contains:

1. identities, swaps, and the structural maps of a strict typed symmetric
   monoidal syntax;
2. preparation $\mathtt{zero}:I\to Q$;
3. gates $H,T,T^\dagger:Q\to Q$ and
   $\mathtt{CNOT}:Q\otimes Q\to Q\otimes Q$;
4. a nondestructive computational-basis instrument
   $M_Z:Q\to Q\otimes B$;
5. discard and reset procedures;
6. a trusted recorded fair coin $I\to B$;
7. classical copy, erase, Boolean control, and failure-record operations; and
8. physical readers for every retained $B$ and $F$ output.

Finite Boolean controllers may choose a typed subprogram using earlier
retained bits. Coherent record, erasure, and leaked-environment tests are built
from $\mathtt{zero}$, $\mathtt{CNOT}$, discard, and $M_Z$; they are not separate
answer-bearing primitives.

### 2.3 Program set

$\mathsf{Prog}_\Sigma$ is the set of finite, well-typed, acyclic syntax DAGs.
The inductive constructors are primitive insertion, identity, swap, sequential
gluing of matching ports, disjoint tensor union, recorded fair-coin choice,
same-output-type Boolean branching on an earlier retained bit, discard, and
reader attachment. Each DAG carries:

- its typed input and output ports;
- its supplied laboratory precedence relation;
- the physical origin of every setting and retained record; and
- a finite string encoding over a fixed alphabet.

Two encodings denote the same syntax object only when there is a typed DAG
isomorphism preserving external ports, primitive labels, record ancestry, and
the supplied precedence relation, together with the ordinary structural
associativity/unit/symmetry coherence. Equal operational predictions do not
identify two physical procedures in this syntax.

Hence $\mathsf{Prog}_\Sigma$ is countable. The supplied precedence relation is
an experiment interface. It is not fundamental time or endogenous chronology.

A preparation is a program $\omega:I\to A$. An experiment after that
preparation is a program $e:A\to B$. The pair is evaluated as $e\circ\omega$.
This keeps contingent preparation separate from fixed law without allowing an
arbitrary process tensor to enter as an unnamed “state.”

### 2.4 Physical program versus answer advice

The program is a legitimate input because it records which physical
operations were actually wired. It may grow with the experiment. It may not
carry:

- an arbitrary table of the desired outcome probabilities;
- a new primitive named after each target circuit;
- a real number whose unregistered digits encode the answer family; or
- a whole process matrix supplied outside the primitive grammar.

Replacing one subprogram by another changes only that syntax subtree and its
declared physical inputs. It does not authorize a new law, root state, global
fit, or advice string.

---

## 3. The exact quantum comparator

### 3.1 Gate-language semantics

Let

$$
\mathcal Q_\Sigma:\mathsf{Prog}_\Sigma\longrightarrow
\mathsf{QInstr}_{\rm fd}
$$

be the standard finite-dimensional quantum instrument semantics:

- $Q\mapsto\mathbb C^2$;
- $B$ and $F$ map to classical centers with retained records;
- the named gates map to their standard matrices;
- $M_Z$ maps to the complete projective instrument, including its
  post-measurement boundary;
- physical randomization maps to the corresponding recorded mixture; and
- sequential, tensor, adaptive, discard, and coarse-graining operations use
  the standard complete-instrument rules.

This functor is the empirical comparator. It is not built into the candidate
law definition.

### 3.2 Exact and closure targets

The **exact target** is every finite program in $\mathsf{Prog}_\Sigma$. This is
already scalable in qubit number, depth, adaptive branches, records, and
continuations.

The **controlled closure target** consists of finite-dimensional states,
channels, and instruments compiled into this grammar to a preregistered
diamond/strategy error. Ancillary dilation, computational-basis measurement,
and a fixed inverse-closed universal gate set supply the standard route.
Solovay--Kitaev gives density and controlled compilation in fixed finite
dimension. No polynomial-in-system-size efficiency is inferred from that
statement.

Exact gate-language adequacy and approximate closure adequacy are reported
separately. Approximation errors must compose under an explicit bound; they may
not silently grow with depth or dimension.

### 3.3 Complete operational profile

For every preparation-program pair $(\omega,e)$, the comparator profile
$\Phi_Q(\omega,e)$ contains:

- the complete transcript distribution;
- every normalized positive-support post-event boundary;
- all compatible continuations and adaptive conditionals;
- null and failure outputs;
- retained-record semantics; and
- the registered physical resource outputs wherever the comparator supplies
  them, together with an explicit UNSPECIFIED status otherwise.

Final-output equality alone is not adequacy. Candidate resource use is always
exposed, but equality of resources is required only when both sides have a
matched operational resource convention.

---

## 4. A set-sized Borel law universe

The first class must not assume that nature is computable.

### 4.1 Common coding carrier

Let $\mathcal N=\mathbb N^{\mathbb N}$ be Baire space. Every admitted history
space is represented by a Borel subset of $\mathcal N$ equipped with a
countable separating cylinder algebra. Countable discrete and finite spaces
embed as special cases. For every program $p$, let $\mathcal R_p$ be the
canonical standard-Borel type of the physical records retained by that
program, with canonical record truncations
$\tau_{q,p}:\mathcal R_q\to\mathcal R_p$ for $p\preceq q$.

For each encoded program $p=e\circ\omega$, a Borel-law code $u$ supplies:

1. a Borel history space $\mathcal H^u_p\subseteq\mathcal N$;
2. a probability measure $\Gamma^u_p$ on $\mathcal H^u_p$;
3. Borel readers for complete transcripts, failures, and resources;
4. for every physical prefix $p\preceq q$, a mandatory Borel record-prefix
   map $\pi^u_{q,p}:\mathcal H^u_q\to\mathcal R_p$;
5. optionally, a full ontology-prefix map
   $\rho^u_{q,p}:\mathcal H^u_q\to\mathcal H^u_p$ when the candidate claims
   that the same microscopic prefix referent exists across future contexts;
6. inverse-image data for registered coarse-grainings and presentation
   changes; and
7. any designated configuration, native cut, division, gauge, and actuality
   structures claimed by the candidate.

All programs and all named maps form countable families. Borel subsets, Borel
maps, and probability measures on the fixed coding carrier admit real codes.
The complete family can therefore be coded by one element of Baire space.

Concretely, for each finite sequence $s\in\mathbb N^{<\mathbb N}$ let $[s]$
be the corresponding basic clopen cylinder in $\mathcal N$. A probability
measure is coded by the real sequence

$$
m_p(s)=\Gamma^u_p([s])
$$

satisfying

$$
m_p(\varnothing)=1,
\qquad
m_p(s)=\sum_{j\in\mathbb N}m_p(s^\frown j),
$$

plus the stated Borel support condition for $\mathcal H^u_p$. These cylinder
values uniquely determine the measure. Borel maps are coded by compatible
preimages of a countable generating family. Because the program, event, and
map indices are countable, their complete code remains one real rather than a
proper class.

### 4.2 Definition: $\mathsf{BULaw}_\Sigma$

$\mathsf{BULaw}_\Sigma$ is the subset of Baire-space codes satisfying the
typing, probability, naturality, intervention, and input-accounting axioms in
Sections 6--9 below.

It is a literal set. Its semantic validity need not be decidable. The quotient
by the presentation equivalence in Section 10 is also a set.

This observation is bookkeeping, not physics: it merely makes universal and
existential quantifiers well formed.

### 4.3 Noncomputable members

A member may contain noncomputable measures or constants. Such a member is not
rejected. It must, however, state how finite physical agents prepare,
calibrate, or read the required quantities. A noncomputable real cannot support
an explanatory-compression or predictive-access claim merely because it is
called one parameter.

---

## 5. The effectively presented uniform subclass

Compression, finite-law, and literal uniformity claims require a narrower
class.

### 5.1 Effective presentations

Fix once and for all:

- the finite encoding alphabet;
- the parser for $\mathsf{Prog}_\Sigma$;
- encodings of named cylinder events and registered maps;
- rational accuracy requests $k\in\mathbb N$; and
- one universal prefix-free evaluator language.

An **effective U-law code** is one finite binary string $u$ that uniformly
provides:

1. a recursively presented Polish/Borel history space for every program;
2. a total routine
   $$
   \mathtt{Prob}_u(p,a,k)\in\mathbb Q
   $$
   satisfying
   $$
   \left|\mathtt{Prob}_u(p,a,k)-\Gamma^u_p(a)\right|\le2^{-k}
   $$
   for every named cylinder event $a$;
3. total inverse-image routines for mandatory record-prefix, reader, and
   coarse-graining maps, plus any optional ontology-prefix maps claimed;
4. a unique-extension certificate: the named cylinder values define one
   normalized countably additive Borel probability measure; and
5. a uniform descriptor/compiler interface as in Section 5.2.

Computational efficiency is not required. Totality and one fixed description
are required. If a candidate claims physical sampling efficiency, that is an
additional resource theorem.

### 5.2 Structural descriptor interface

The code supplies a recursively presented typed descriptor algebra
$\mathsf D_u$ and a compiler

$$
\mathsf{Desc}_u:\mathsf{Prog}_\Sigma\to\mathsf D_u
$$

obeying the printed structural recursions

$$
\begin{aligned}
\mathsf{Desc}_u(q\circ p)
  &=\mathsf{Seq}_u(\mathsf{Desc}_u(q),\mathsf{Desc}_u(p)),\\
\mathsf{Desc}_u(p\otimes q)
  &=\mathsf{Ten}_u(\mathsf{Desc}_u(p),\mathsf{Desc}_u(q)),
\end{aligned}
$$

and analogous rules for physical randomization, adaptive control, discard, and
coarse-graining.

The descriptor may be a local update rule, tensor network, action, global
constraint, variational problem, or simply the faithfully encoded physical
program. The final probability law may remain indivisible; descriptor
composition is not stochastic-kernel division.

This interface rules out post-hoc per-program refitting. It does not rule out a
compact all-at-once law merely because the solver sees the completed physical
program.

### 5.3 Definition: $\mathsf{EULaw}_\Sigma$

$\mathsf{EULaw}_\Sigma\subset\mathsf{BULaw}_\Sigma$ consists of the valid
finite effective codes satisfying Sections 5.1--5.2 and the common axioms.
It is countable.

There is no per-$n$, per-depth, per-context, or per-process advice sequence.
A finite tuple of computable physical constants is allowed only through finite
Cauchy-name programs inside $u$. Calibrated run-dependent quantities enter as
physical records and their requested precision is charged.

### 5.4 Oracle/advice stratum

A Borel law that needs an oracle $z\in\mathcal N$ belongs to
$\mathsf{OULaw}_\Sigma(z)$, not $\mathsf{EULaw}_\Sigma$. The oracle may be a
legitimate physical postulate. Its information, preparation, stability, and
access mechanism are independent inputs. It cannot be advertised as a finite
uniform compression of the quantum target.

This nested construction avoids the false dichotomy “computable or
unphysical.”

---

## 6. Common law axioms

### U0 — typed probability law

Every $\Gamma^u_p$ is normalized and countably additive on its printed Borel
history space. Readers and restriction maps are measurable and type correct.
Null conditionals remain undefined or explicitly typed; they are never filled
by arbitrary values.

### U1 — record-prefix coherence and optional ontology restrictions

For $p\preceq q\preceq r$,

$$
\pi^u_{r,p}
=
\tau_{q,p}\circ\pi^u_{r,q},
\qquad
\pi^u_{p,p}=\mathsf{Rec}^u_p.
$$

Thus every longer history has a well-typed restriction to the physical records
already retained at $p$. If the candidate additionally supplies full
ontology-prefix maps, they obey

$$
\rho^u_{r,p}=\rho^u_{q,p}\circ\rho^u_{r,q},
\qquad
\rho^u_{p,p}=\mathrm{id},
$$

and their record reader agrees with $\pi^u_{q,p}$. Full ontology-prefix maps
are not mandatory because requiring one microscopic referent across
incompatible future contexts would assume away contextual ontology. Neither
kind of map makes the prefix a future-sufficient stochastic state.

### U2 — forward prefix consistency

In the forward-autonomous stratum, if an independently generated future choice
is made only after prefix $p$, then every extension $q$ obeys

$$
(\pi^u_{q,p})_*\Gamma^u_q
=
(\mathsf{Rec}^u_p)_*\Gamma^u_p.
$$

If a context-stable microscopic prefix $\rho^u_{q,p}$ is claimed, the stronger
condition $(\rho^u_{q,p})_*\Gamma^u_q=\Gamma^u_p$ is also required.

Adaptive future choices may depend on retained prefix records through a
registered controller. The controller, its memory, and its random seed belong
to the program.

A candidate may reject U2 only by entering the separately printed global,
retrocausal, or measurement-dependent stratum.

### U3 — physical setting entry

Whenever a reader's law depends on a setting, that dependence enters through a
declared physical port, registered common parent, or explicitly global
boundary law. A setting outside the declared causal ancestry may instead have
no effect. An evaluator-only setting index with no physical carrier is
inadmissible.

### U4 — local substitution without law replacement

For every typed context $C[-]$, replacing $p$ by $p'$ changes
$\mathsf{Desc}_u(C[p])$ through the registered subtree only. The law code,
unrelated root data, calibration split, and held-out set remain fixed.

This does not demand local stochastic factorization. It demands that a changed
laboratory operation is not answered by choosing a different theory.

### U5 — complete randomization affinity

If a registered independent recorded coin program selects $p$ with its
physically generated probability $r$ and $q$ otherwise, the complete history
law is the corresponding physical mixture, with the coin record retained.
Exact finite programs generate dyadic $r$ from the fair-coin primitive;
additional calibrated randomizers belong to the controlled closure with their
precision exposed. This does not identify distinct physical preparation
procedures that happen to have the same operational average.

### U6 — independent roots

Separately prepared, dynamically noninteracting roots with no shared boundary
data have product history law. Their exposed resources combine by the
registered monoidal rule: addition only for quantities declared extensive,
maximum or another rule where physically appropriate. Entangled, common-cause,
or globally constrained roots must be typed as such; they are not silently
factorized.

### U7 — reader and coarse-graining naturality

For every registered Borel reader $c$,

$$
\Gamma^u_{c\circ p}=c_*\Gamma^u_p
$$

at the complete output type. Readers cannot manufacture mass, change earlier
records, or define the microhistory after the fact.

### U8 — held-out stability

The same $u$, primitive interpretations, contingent-input rules, and error
budgets apply to all registered sizes, depths, adaptive branches, and held-out
continuations. Calibration data are disjoint from evaluation data.

### U9 — resource visibility

Any physical clock, memory, communication channel, precision-bearing control,
environment, failure branch, preparation device, or global coordination
resource used by the law appears in the complete profile. Mathematical
evaluator runtime is not automatically physical resource use.

### U10 — actuality separation

Normalization does not imply that one history is actual. A one-history claim
is recorded as an actuality postulate or a further selected law. Operational
adequacy alone cannot award it.

---

## 7. Complete operational adequacy

Let $\Phi_u(p)$ be the complete operational profile obtained by applying all
registered readers and all compatible continuations to $\Gamma^u_p$.

### 7.1 Exact adequacy

On the exact gate-language domain,

$$
\Phi_u\simeq\Phi_Q
$$

means a natural equality/isomorphism preserving physical ports, retained
record meanings, randomization procedures, failures, continuation
probabilities, and every resource coordinate defined on both sides. Additional
candidate resources remain visible even when the abstract comparator has no
matched coordinate.

### 7.2 Approximate adequacy

For the compiled closure domain, freeze

$$
D_{\mathcal E}(u,Q)
=
\sup_{p\in\mathcal E_{\rm reg}}
d_p\bigl(\Phi_u(p),\Phi_Q(p)\bigr),
$$

where $d_p$ is the complete instrument/comb metric and includes every
compatible continuation. The tolerance $\varepsilon_{\rm phys}$ and its
scaling law freeze before construction.

### 7.3 Reachable continuation quotient

At every prefix, identify two candidate boundary descriptions exactly when all
registered future continuations return the same complete operational laws.
Call the quotient $\mathsf{Cont}_u$.

If $u$ is completely adequate, Paper 02's logic forces $\mathsf{Cont}_u$ to be
naturally equivalent, on the registered domain, to the phase-complete quantum
continuation object. This is an operational residue theorem. It does not imply
that Hilbert vectors are ontic, and it does not decide whether the residue was
derived or inserted nomologically.

---

## 8. Native division and indivisibility

Fix a physical prefix $p$ and its registered future-extension family
$\mathsf{Fut}(p)$.

### 8.1 Licensed positive division

A licensed positive cut consists of one standard-Borel variable $\Lambda_p$
with fixed physical semantics across all future extensions, a preparation
kernel $\eta_p(d\lambda\mid\text{past})$, and for every future program $f$ a
response kernel $K_f(dz\mid\lambda)$ such that:

1. all complete future transcript laws factor through the same $\Lambda_p$;
2. $\Lambda_p$ is prepared before the independently chosen future setting;
3. intervention substitution acts through registered physical ports;
4. all positive-support post-event boundaries are reproduced; and
5. null, failure, and resource outputs are included.

The full completed history or the table $f\mapsto P(z\mid f)$ is not a free
compact cut state. It may be used only with its information and physical-access
cost charged.

### 8.2 Carrier-relative nondivision

A candidate is nondivisible at $p$ relative to a declared native carrier when
no licensed factorization exists on that carrier. It is **resource-robustly
nondivisible** at a registered bound when no licensed positive cut below that
bound exists.

No absolute statement that “no positive variable exists” is licensed. A large
enough response table or preparation label can always restore formal
sufficiency on a finite experiment domain.

### 8.3 Q-Cut interface

On the fixed partial-matching family, the private Q-Cut candidate tests any
licensed positive cut obeying its independence, fixed-error, and measurability
premises. U-Gen does not generalize that theorem by rhetoric. It records one of
four branches:

1. positive cut information has the proved lower bound;
2. no licensed cut exists on the native carrier;
3. a charged premise such as future dependence or oracle advice is used; or
4. the candidate fails the quantum target.

---

## 9. Independent-input and advice ledger

Every evaluation has five syntactically distinct inputs:

| Input | Status |
|---|---|
| universal law code $u$ | fixed once for the entire scalable family |
| finite primitive/calibration packet $\kappa$ | fixed before held-out evaluation; physical precision charged |
| preparation $\omega$ | contingent physical program generated by the grammar |
| experiment $e$ | actual physical wiring and adaptive controls |
| advice $a_{n,e}$ | forbidden in $\mathsf{EULaw}_\Sigma$; charged in an advice/oracle stratum |

### 9.1 Target-process injection

If adequacy requires a compiler

$$
J:W\longmapsto(\kappa_W,\omega_W,e_W,a_W)
$$

for an arbitrary quantum state, channel, comb, or process tensor $W$, and
$W$ is recoverable from answer-bearing data that are not generated by the
fixed primitive composition rules, the result is a representation with
target-process injection.

A compositional compiler from a physically specified gate circuit to the
corresponding local program $e_W$ is not automatically illicit: it records
which apparatus was built. It counts as target injection only when arbitrary
process-level degrees of freedom enter through fresh primitives, calibrated
numbers, root data, or advice rather than being generated by the fixed law and
the registered structural semantics. This distinction is decided by the
compiler's tensor/sequential/substitution naturality and its input ledger, not
by whether the symbol $W$ appears.

### 9.2 Fixed quantum primitive debt

A finite $H,T,\mathtt{CNOT}$ Born evaluator does not inject a fresh $W$ for
each circuit. It is genuinely uniform. Nevertheless, the complex gate
semantics, tensor rule, and Born rule remain fixed quantum nomological inputs.
The correct classification is `UNIFORM-QUANTUM-NOMOLOGY`, not “derived
stochastic physics.”

### 9.3 Derived-input gain

A stochastic candidate earns derived-input gain only if some comparator input
is proved to follow from older independently stated principles without an
equally strong surrogate in $u$, $\kappa$, $\omega$, $e$, an oracle, or a
global boundary condition.

The proof uses an explicit dependency graph or compositional simulation, not
raw code length. A naturally invertible renaming is not derived-input gain.

### 9.4 Compact algorithms are laws, not automatically tricks

A finite algorithm that computes the complete quantum family is not rejected
merely because it can inspect the whole program. If it is fixed, typed,
intervention-compatible, and empirically adequate, it is a legitimate
nomological candidate. The remaining questions are its independent premises,
causal/global status, resource outputs, and empirical selection.

This clause prevents the anti-table firewall from becoming an aesthetic ban on
unfamiliar laws.

---

## 10. Presentation equivalence and physical classification

### 10.1 Presentation equivalence

Two codes $u,v$ are presentation-equivalent when there is a program-natural
family of Borel isomorphisms

$$
\alpha_p:\mathcal H^u_p\to\mathcal H^v_p
$$

that preserves all measures, physical prefix maps, readers, retained record
meanings, intervention ports, failures, and exposed resources.

Measurable coordinate changes and gauge-equivalent dilations satisfying this
criterion are presentation changes. Idle-label inflation need not be
isomorphic—especially for finite atomic histories—and can represent a genuinely
different but empirically unresolved ontology. It belongs to an empirical
equivalence fiber and cannot be selected by the registered data merely because
it is larger.

### 10.2 Orthogonal classification coordinates

Every candidate receives one entry on each axis:

| Axis | Values |
|---|---|
| multi-time scope | endpoint / restricted interventions / complete registered process |
| uniformity | per-target / advice-indexed / one Borel/oracle code / effectively uniform |
| process input | injected $W$ / fixed quantum primitives / independently derived primitives |
| cut structure | positive divisible / positive high-cost / native nondivision / unclassified |
| temporal premise | forward-prefix / global-consistent / retrocausal / measurement-dependent |
| causal-port status | supplied wiring / native locality principle / violated / untested |
| empirical status | exact equivalent / tolerance-equivalent / forced deviation / refuted |
| actuality | absent / postulated / independently selected |

No single label, including `STOCHASTIC`, `INDIVISIBLE`, or `UNIFORM`, replaces
this vector.

### 10.3 Reality-identification rule

Passing U-Gen can earn complete-law existence, uniformity, an input reduction,
a scalable theorem, or a premise classification. Ontology truth requires an
independent physical principle or a separating observation. Lower description
length is not such a principle.

---

## 11. Basic propositions to be independently reviewed

These are author-side propositions, not accepted results.

### Proposition A — countable target syntax

$\mathsf{Prog}_\Sigma$ is countable because every program is a finite
well-typed string/DAG over a finite alphabet.

### Proposition B — set-sized Borel universe

The family of all Section 4 codes is a subset of Baire space. Hence universal
quantification over $\mathsf{BULaw}_\Sigma$ and its presentation quotient is
set-theoretically legitimate.

### Proposition C — countable effective subclass

$\mathsf{EULaw}_\Sigma$ is countable because its members are finite binary
programs. Semantic validity may be undecidable without affecting countability.

### Proposition D — nonempty complete control

The fixed quantum gate semantics, followed by one whole-program dilation and
Born evaluation of every retained record, gives a member of
$\mathsf{EULaw}_\Sigma$ at exact gate-language scope. It is classified as
complete, effectively uniform, positive on completed records, and
`UNIFORM-QUANTUM-NOMOLOGY`.

This proposition proves that the class does not exclude the empirical target
by definition. Its histories can be taken to be the retained record
transcripts, with canonical record truncation; it need not assert a microscopic
configuration at every unmeasured prefix. It does not prove a stochastic-native
derivation.

### Proposition E — Paper 01 placement

Paper 01's generic construction belongs to the complete positive Borel class
when its arbitrary target process $W$ is admitted as input. Its generic theorem
therefore occupies the target-process-injection stratum. Restricting $W$ to the
output of the fixed gate functor yields Proposition D, but changes the input
question rather than strengthening Paper 01 retroactively.

### Proposition F — continuation residue

Every completely adequate member, regardless of microscopic carrier, has a
reachable all-continuation quotient naturally equivalent to the registered
quantum predictive object. Thus deleting Hilbert syntax cannot delete
phase-complete operational structure.

The proposition does not decide whether a microscopic positive law explains
that structure more deeply.

---

## 12. Control and mutant matrix

### C0 — terminal answer table

Supply one probability array for each program as contingent advice.

**Expected:** Borel representation at best; fails effective uniformity and
input accounting.

If the entire infinite family is frozen inside one real law code, it instead
occupies the one-Borel/oracle-code stratum and carries the full table as
nomological information. It earns no finite-description or derived-input gain.

If one fixed finite algorithm computes all arrays, it no longer fails merely
for being algorithmic. It enters the fixed-nomology audit.

### C1 — Paper 01 generic Born compiler

Supply arbitrary $W$, build a dilation, and push forward modulus-square record
probabilities.

**Expected:** complete positive representation; target-process injection.

### C2 — fixed Hilbert gate law

Use the fixed matrices, tensor rule, dilation, and Born rule for all programs.

**Expected:** complete and effectively uniform positive control; quantum
nomological residue explicit; no ontology selection.

### C3 — Barandes endpoint law

Supply a fixed configuration set, contingent standalone probabilities, and
first-order $\Gamma(t\leftarrow t_0)$ at division events.

**Expected:** valid endpoint indivisible process at its proved scope; not yet a
complete U-Gen member unless every registered middle intervention and
continuation is determined. The 2026 process-tensor extension is stated as a
conjectural/future connection, so it may not be presumed.

### C4 — hypothetical complete Barandes extension

Add a single stochastic-native rule that determines all adaptive instruments,
post-event boundaries, and scalable programs without arbitrary $W$ input.

**Expected:** the central positive candidate. Its placement depends on whether
the unistochastic/Hilbert lift is derived, gauge, or independent nomological
data. No verdict is pre-awarded.

### C5 — one exact real

Encode every target answer in one real coupling.

**Expected:** oracle/advice stratum unless one fixed physical law generates and
accesses the digits. Coordinate count gives no compression. Required precision
and access are charged.

### C6 — compact global history law

Use one variational or boundary rule over the complete physical program.

**Expected:** may pass uniformity. It enters the global-consistent stratum if
prefix records remain invariant under independently chosen future extensions;
otherwise it enters retrocausal/measurement-dependent scope. It is not rejected
for being all-at-once.

### C7 — local classical Markov model

Use finite positive cut states, free settings, and Bell-local update kernels.

**Expected:** fails the universal quantum target on registered interference,
contextuality, Bell, or communication controls; the exact failed premise must
be printed.

### C8 — PR-box law

Use a uniform no-signalling superquantum box for the Bell subgrammar.

**Expected:** proves that positivity plus no-signalling does not select the
quantum target. It is empirically wrong as a universal quantum comparator and
must be excluded, if at all, by an independently stated physical principle.

### C9 — future-program preparation compiler

Prepare a hidden variable using the later setting or complete future program.

**Expected:** fails the forward-prefix stratum; may enter a declared global or
retrocausal branch with all independence and signalling consequences exposed.

### C10 — idle ontology inflation

Tensor every history with an unobserved arbitrary Borel label.

**Expected:** empirical fiber only unless a measure-preserving natural
isomorphism actually exists. It may be a distinct ontology, but cannot create
empirically selected explanatory capacity or a physical resource lower bound.

---

## 13. Hostile questions a future pin must answer

1. Is $\mathcal Q_\Sigma$ an empirical comparator or silently a candidate
   primitive?
2. Does the claimed stochastic law determine instruments or only endpoints?
3. Can two process tensors share all native candidate data but differ under a
   middle intervention?
4. Is a fixed gate program legitimate physical input while an answer table is
   excluded for an exact typed reason?
5. Does the descriptor interface accidentally force Markov division?
6. Can one finite solver recognize programs globally, and if so is it honestly
   classified rather than banned aesthetically?
7. Are noncomputable laws admitted without being credited with finite
   compression?
8. Can an exact real hide nonuniform advice at zero cost?
9. Are preparation, law, physical program, and advice syntactically distinct?
10. Does local substitution change only the physical subtree?
11. Are prefix consistency and causal-port locality independent premises?
12. Is supplied laboratory order being promoted to time?
13. Does an all-at-once law preserve earlier retained records under later free
    choices?
14. Is relative nondivision being overstated as absence of every positive
    sufficient carrier?
15. Does the cut theorem's independence premise actually apply?
16. Is the complete continuation quotient reconstructed without making it
    ontic by definition?
17. Does a fixed stochastic primitive derive phase-complete structure or encode
    it in calibrated constants/response rules?
18. Are tensor factorization and Tsirelson's bound derived stochastically or
    imported through the Hilbert lift?
19. Are resource comparisons physical or merely source-code comparisons?
20. Does any positive result shrink an empirical class or only supply another
    representative?

---

## 14. Scope and nonclaims

This exact class does not establish:

- that any stochastic-native complete generator exists;
- that Barandes's endpoint theory already supplies process tensors;
- that complex amplitudes are fundamental or eliminable;
- that computability is a law of nature;
- that shorter laws are more likely or more real;
- that one actual history is selected;
- Bell locality, causal order, internal time, Lorentz covariance, QFT, a
  continuum limit, spacetime, or gravity.

Its sole achievement, if it survives review, is to make the U-Gen quantifiers
and classification axes exact enough that a theorem or countermodel has a
well-defined subject.

Private ceiling:

```text
P17-PRIVATE-UGEN-EXACT-SET-SIZED-LAW-CLASS
NO SCIENTIFIC RESULT / NO MODEL / NO SUCCESSOR OPENED
```

---

## 15. Primary-source anchors

1. J. A. Barandes, “Quantum Systems as Indivisible Stochastic Processes,”
   especially the fixed configuration space, contingent standalone
   distribution, first-order transition laws, division events, and external
   target-time interface,
   <https://arxiv.org/html/2507.21192v1>.
2. J. A. Barandes, M. Hasan, and D. Kagan, “The CHSH Game, Tsirelson's Bound,
   and Causal Locality,” especially the Hilbert factorization in the proof and
   the conjectural process-tensor connection,
   <https://arxiv.org/html/2512.18105>.
3. J. A. Barandes, “The Born Representation Theorem and the Unistochastic
   Theorem,” especially the bounded unistochastic dilation of finite stochastic
   matrices, <https://arxiv.org/html/2608.04354>.
4. C. M. Dawson and M. A. Nielsen, “The Solovay--Kitaev algorithm,” especially
   the finite inverse-closed universal instruction-set theorem,
   <https://arxiv.org/html/quant-ph/0505030>.
5. G. Chiribella, G. M. D'Ariano, and P. Perinotti, “Theoretical framework for
   quantum networks,” <https://arxiv.org/abs/0904.4483>.
6. F. A. Pollock, C. Rodriguez-Rosario, T. Frauenheim, M. Paternostro, and
   K. Modi, “Operational Markov Condition for Quantum Processes,”
   <https://arxiv.org/abs/1801.09811>.
