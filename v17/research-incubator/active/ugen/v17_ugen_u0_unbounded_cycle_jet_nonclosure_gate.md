# ISP v17 — U0 unbounded cycle-jet nonclosure gate

**Status:** ACTIVE AUTHOR-SIDE CLASS-BOUNDED THEOREM/CONTROL PACKET
**Date:** 2026-08-23
**Scientific result awarded:** none
**Native U0 candidate constructed:** no
**Official pin/review/U0-T4 opened:** no

---

## 0. Reality-first question and exact answer

The preceding probability-jet gate established that a regular autonomous
first-order law on the instantaneous stochastic kernel cannot generate
nontrivial coherent quadratic departure from an identity boundary. It left
open a finite higher-jet or memory-bearing positive law.

This packet asks:

> Can one fixed finite probability jet, together with phase-blind structural
> data, close the dynamics uniformly as the physical system grows?

At one exact standard-quantum control scope, the answer is no.

For every prescribed finite jet order \(K\), there is an odd cycle longer
than \(K\) and a conjugate pair of coherent endpoint laws such that:

1. the support graph, system size, edge magnitudes, spectrum, and every
   conjugation-even descriptor agree;
2. the complete stochastic-kernel Taylor jets agree through order \(K\);
3. the directed transition laws differ at the cycle length; and
4. when independently typed oriented ports and a reversible sign control are
   supplied, that physical comparator distinguishes the two members.

Consequently no deterministic, locally unique, fixed-order differential
closure on the stochastic kernel, using only those common descriptors, can
generate both held-out control responses uniformly over cycle size.

This is not a no-go for ordinary-positive ontology, local microscopic laws,
finite memory at fixed system size, or Barandes indivisibility. It identifies
the exact missing coordinate: a source law must contain or generate an
independently physical conjugation-odd relational distinction, carry a richer
source state, or assign the whole boundary law without inferring it from a
fixed finite probability jet.

---

## 1. Binding ontology and authority firewalls

The cycle construction is a comparator, not a proposed world.

1. Its finite vertices are supplied preparation/reader records, not
   fundamental discrete entities or a spacetime lattice.
2. Its graph is a calibrated interaction support, not an ontic web.
3. Its parameter \(\tau\) is a supplied separation coordinate, not derived
   external time, proper time, or an operational clock.
4. Its complex edge weights belong to the standard-quantum control. No
   fundamental phase field, \(U(1)\) target, bundle, connection, or holonomy
   is inherited by U0.
5. N1/N1A remain Nelson controls only. No diffusion, trajectory, Euclidean
   space, or N1B enters.
6. G1/G2 remain compiler and source-origin controls.
7. MG0 remains downstream and performs no selection here.
8. Barandes remains a serious guiding hypothesis, not a preselected
   conclusion.

This packet is an author-side bounded no-go plus escape ledger. It does not
open an official pin, review, model, or successor paper.

---

## 2. Version-bound primary-source and priority boundary

The source scope was checked on 2026-08-23 against:

1. Balázs Endre Szigeti, Gábor Homa, Zoltán Zimborás, and Norbert Barankai,
   [Short time behavior of continuous time quantum walks on graphs](https://arxiv.org/abs/1905.03914),
   Physical Review A **100**, 062320 (2019).
2. Zoltán Zimborás, Mauro Faccin, Zoltán Kádár, James D. Whitfield,
   Ben P. Lanyon, and Jacob Biamonte,
   [Quantum Transport Enhancement by Time-Reversal Symmetry Breaking](https://arxiv.org/abs/1208.4049),
   Scientific Reports **3**, 2361 (2013).
3. Jacob Biamonte and Jacob Turner,
   [Topological classification of time-asymmetry in unitary quantum processes](https://arxiv.org/abs/1703.02542),
   arXiv:1703.02542.
4. Massimo Frigerio, Claudia Benedetti, Stefano Olivares, and
   Matteo G. A. Paris,
   [Quantum-classical distance as a tool to design optimal chiral quantum walks](https://arxiv.org/abs/2106.11685),
   Physical Review A **105**, 032425 (2022).
5. Y. Aharonov and D. Bohm,
   [Significance of Electromagnetic Potentials in the Quantum Theory](https://doi.org/10.1103/PhysRev.115.485),
   Physical Review **115**, 485--491 (1959).
6. Jason Doukas,
   [On the emergence of quantum mechanics from stochastic processes](https://arxiv.org/abs/2602.22095),
   arXiv:2602.22095v2 (2026).
7. Jacob A. Barandes,
   [Quantum Systems as Indivisible Stochastic Processes](https://arxiv.org/abs/2507.21192),
   arXiv:2507.21192.

### 2.1 Established prior art

The inspected sources already establish that:

1. short-time continuous-time quantum-walk amplitudes are sums over graph
   paths;
2. graph distance fixes the leading power in nonchiral controls;
3. multiple path amplitudes can interfere in chiral controls;
4. phases on trees are removable by presentation gauge;
5. the invariant phase information of a graph is carried by loops;
6. time-asymmetric probability transport requires appropriate non-bipartite
   loop structure; and
7. cycle-phase effects become visible only after alternatives can traverse
   the relevant topology.

Those statements are not v17 discoveries.

### 2.2 Author-side contribution requiring later priority review

No exact source was located in the inspected primary set for the combined
statement proved below:

1. full stochastic-kernel equality of the conjugate odd-cycle jets through
   every order strictly below the cycle length;
2. the exact first unequal derivative

\[
\Gamma_{01}^{(L),\phi}(0)
-
\Gamma_{01}^{(L),-\phi}(0)
=
4(-1)^{(L-1)/2}L g^L\sin\phi;
\]

3. the arbitrary-\(K\) fixed-jet nonclosure corollary; and
4. its U0 source-law and resource interpretation.

These are author-side claims only. Independent source and mathematics review
would be required before any novelty or scientific result is awarded.

---

## 3. Exact finite control family

Let

\[
L=2q+1\geq3
\]

be odd. Label the vertices of the cycle \(C_L\) by

\[
0,1,\ldots,L-1.
\]

Fix \(g>0\) and \(\phi\in\mathbb R\). Define the Hermitian matrix
\(H_\phi^{(L)}\) by

\[
(H_\phi)_{r,r+1}
=(H_\phi)_{r+1,r}
=g,
\qquad
0\leq r\leq L-2,
\]

\[
(H_\phi)_{0,L-1}
=g e^{-i\phi},
\qquad
(H_\phi)_{L-1,0}
=g e^{i\phi},
\]

with all remaining entries zero.

Define

\[
U_\phi(\tau)=e^{-i\tau H_\phi}
\]

and the positive column-stochastic endpoint family

\[
\Gamma^\phi_{ij}(\tau)
=
|U_\phi(\tau)_{ij}|^2.
\]

The conjugate member satisfies

\[
H_{-\phi}=H_\phi^*=H_\phi^T.
\]

Therefore:

\[
|H_{-\phi}|=|H_\phi|
\]

entrywise,

\[
\operatorname{spec}(H_{-\phi})
=
\operatorname{spec}(H_\phi),
\]

and

\[
\Gamma^{-\phi}_{ij}(\tau)
=
\Gamma^\phi_{ji}(\tau).
\]

Thus the pair differs, when it differs at all, only in directed probability
transport relative to physically fixed preparation and reader ports.

---

## 4. Lemma CJ-A — walk-pair expansion

Let \(\mathcal W_m(j\to i)\) be the walks of length \(m\) from \(j\) to \(i\)
on \(C_L\). For

\[
W=(v_0=j,v_1,\ldots,v_m=i),
\]

define

\[
w_\phi(W)
=
\prod_{a=1}^m
(H_\phi)_{v_a v_{a-1}}.
\]

Then

\[
(H_\phi^m)_{ij}
=
\sum_{W\in\mathcal W_m(j\to i)}
w_\phi(W).
\]

Writing

\[
\Gamma^\phi_{ij}(\tau)
=
\sum_{r=0}^{\infty}
c_r^\phi(i,j)\tau^r,
\]

the coefficient is

\[
c_r^\phi(i,j)
=
\sum_{m+n=r}
\frac{(-i)^m i^n}{m!\,n!}
\sum_{\substack{
W\in\mathcal W_m(j\to i)\\
W'\in\mathcal W_n(j\to i)
}}
w_\phi(W)\overline{w_\phi(W')}.
\]

### Proof

Expand the exponential:

\[
U_\phi(\tau)_{ij}
=
\sum_{m=0}^{\infty}
\frac{(-i\tau)^m}{m!}
(H_\phi^m)_{ij}.
\]

Multiplication by its complex conjugate and collection of terms with
\(m+n=r\) gives the result. The matrix-power walk expansion is standard.
\(\square\)

### Physical content

A probability coefficient does not inspect one path by itself. It compares
pairs of alternatives with the same endpoints. The phase-sensitive object is
the closed walk obtained by following one alternative and reversing the
other.

---

## 5. Lemma CJ-B — nonzero relative winding costs at least one cycle

For two walks \(W,W'\) with the same endpoints, concatenate \(W\) with the
reverse of \(W'\). The result is a closed walk of length

\[
|W|+|W'|.
\]

If its net winding around \(C_L\) is nonzero, then

\[
|W|+|W'|\geq L.
\]

### Proof

Lift the cycle to its universal cover, the integer line. A closed walk with
winding number \(s\neq0\) lifts to a path whose endpoints differ by \(sL\).
Each edge step changes the lifted coordinate by at most one, so the walk
contains at least \(|s|L\geq L\) edge traversals. \(\square\)

### Corollary

If

\[
|W|+|W'|<L,
\]

then the two alternatives have the same net crossing number of the
distinguished closing edge. Hence

\[
w_\phi(W)\overline{w_\phi(W')}
\]

is independent of the sign of \(\phi\).

This is the precise finite version of “the response cannot see around the
loop before alternatives have enclosed the loop.” It is a path-expansion
fact, not a claim about a particle trajectory in the native ontology.

---

## 6. Theorem CJ-C — pre-winding probability-jet equality

For the full stochastic matrices:

\[
\frac{d^r}{d\tau^r}
\Gamma^\phi(\tau)\bigg|_{\tau=0}
=
\frac{d^r}{d\tau^r}
\Gamma^{-\phi}(\tau)\bigg|_{\tau=0}
\qquad
\text{for every }0\leq r<L.
\]

Equivalently,

\[
\mathcal J_{L-1}(\Gamma^\phi;0)
=
\mathcal J_{L-1}(\Gamma^{-\phi};0).
\]

### Proof

Fix \(i,j\) and a coefficient order \(r<L\). Every term in Lemma CJ-A is a
pair of walks with total length \(r\). Lemma CJ-B says that their relative
closed walk has zero winding. Its closing-edge phase therefore cancels
between \(w_\phi(W)\) and \(\overline{w_\phi(W')}\). The coefficient is
unchanged under \(\phi\mapsto-\phi\). This holds entrywise. \(\square\)

### Strength of the statement

The equality is not merely:

1. equality of the diagonal probabilities;
2. equality of one prepared column;
3. equality of the leading exponent;
4. equality of edge magnitudes; or
5. equality up to relabeling.

It is equality of every entry of every probability derivative strictly below
the cycle length.

---

## 7. Theorem CJ-D — exact first conjugation-odd derivative

Assume

\[
\sin\phi\neq0.
\]

For the directed transition from prepared vertex \(1\) to read vertex \(0\),

\[
\Gamma^\phi_{01}(\tau)
-
\Gamma^{-\phi}_{01}(\tau)
=
\frac{
4(-1)^q g^L\sin\phi
}{
(L-1)!
}
\tau^L
+
O(\tau^{L+1}),
\]

where

\[
q=\frac{L-1}{2}.
\]

Therefore

\[
\boxed{
\frac{d^L}{d\tau^L}
\left[
\Gamma^\phi_{01}(\tau)
-
\Gamma^{-\phi}_{01}(\tau)
\right]_{\tau=0}
=
4(-1)^q L g^L\sin\phi
}.
\]

### Proof

The shortest path from \(1\) to \(0\) is the direct edge:

\[
W_{\rm d}:1\to0,
\qquad
|W_{\rm d}|=1,
\qquad
w_\phi(W_{\rm d})=g.
\]

The other simple path traverses the rest of the cycle:

\[
W_{\rm l}:1\to2\to\cdots\to L-1\to0,
\]

\[
|W_{\rm l}|=L-1,
\qquad
w_\phi(W_{\rm l})
=
g^{L-1}e^{-i\phi}.
\]

At total order \(L\), these are the unique path pair with nonzero relative
winding. Adding a backtrack would increase total length by two. The two
cross terms in Lemma CJ-A give

\[
\frac{2g^L}{(L-1)!}
\operatorname{Re}
\left[
-i(-1)^q e^{i\phi}
\right]
=
\frac{2(-1)^qg^L\sin\phi}{(L-1)!}
\]

in \(c_L^\phi(0,1)\). Replacing \(\phi\) by \(-\phi\) reverses this term.
All zero-winding terms cancel in the difference. Multiplication by \(L!\)
gives the derivative formula. \(\square\)

### Triangle recovery

For \(L=3\), \(q=1\), so

\[
\Gamma^\phi_{01}(\tau)
-
\Gamma^{-\phi}_{01}(\tau)
=
-2g^3\sin\phi\,\tau^3+O(\tau^4),
\]

recovering the triangle witness of the preceding probability-jet packet.

---

## 8. Corollary CJ-E — no fixed finite probability-jet closure

Fix any finite integer \(K\geq0\). Choose an odd

\[
L>K.
\]

Then the pair \(\Gamma^\phi,\Gamma^{-\phi}\):

1. has the same size \(L\);
2. has the same support graph \(C_L\);
3. has the same edge magnitudes and spectrum;
4. has the same full probability jet through order \(K\); and
5. differs as an analytic stochastic family.

Hence there is no single-valued map

\[
\mathcal F_K:
\left(
\mathcal D_{\rm even},
\mathcal J_K(\Gamma;0)
\right)
\longmapsto
\{\Gamma(\tau)\}_{\tau}
\]

that reconstructs both families when
\(\mathcal D_{\rm even}\) contains only conjugation-even descriptors common
to the pair.

### Proof

The common-input statements follow from Section 3 and Theorem CJ-C. The
families differ by Theorem CJ-D. A function has one output on one input, so it
cannot return both distinct laws. \(\square\)

### Differential-closure form

Fix an order \(s\). Consider any deterministic locally unique equation

\[
\Gamma^{(s)}(\tau)
=
F\left(
\tau,
\Gamma(\tau),
\dot\Gamma(\tau),
\ldots,
\Gamma^{(s-1)}(\tau);
\mathcal D_{\rm even}
\right).
\]

Choose odd \(L>s-1\). The conjugate pair has identical initial data through
order \(s-1\) and the same printed descriptor. Local uniqueness forces the
same solution, contradicting Theorem CJ-D.

Therefore no fixed finite differential order closes this entire
sign-reversible family unless the law receives an additional
conjugation-odd physical input or gives up local uniqueness.

### Exact scope

This does not exclude:

1. closure order that grows with \(L\);
2. a richer source state whose dimension grows with the apparatus;
3. a local microscopic rule carrying an independently physical orientation
   field;
4. nonunique dynamics plus a separately stated physical selector;
5. a whole-boundary or whole-program positive law;
6. a law that physically forbids one conjugate control; or
7. a non-differential source law.

---

## 9. Corollary CJ-F — independent-control distinction cost

Take \(M\) disjoint odd-cycle comparator blocks, each of length \(L>K\), with
independently supplied reversible signs

\[
\boldsymbol\epsilon
=
(\epsilon_1,\ldots,\epsilon_M)
\in
\{-1,+1\}^M.
\]

All \(2^M\) members have the same phase-blind structural descriptors and the
same \(K\)-jet. Conditional on physical oriented ports, their order-\(L\)
directed responses reveal the independent signs.

Any deterministic source interface required to predict all these
independently typed settings must therefore admit at least

\[
2^M
\]

distinguishable input/state cases, or at least \(M\) independent binary
distinctions in any finite exact encoding.

### Interpretation

This is not a claim that the universe stores literal digital bits or that the
configuration domain is discrete. It is an operational distinguishability
lower bound. The distinctions may be carried by continuous apparatus fields,
orientable reference systems, source states, or another physical structure.

Supplying a target-derived sign table earns zero U0 source credit. Supplying
independently calibrated reversible controls is legitimate, but the native law
must still explain how those controls generate the complete response.

---

## 10. Gauge, presentation, and reference audit

### 10.1 Edge phases are not separately physical

A diagonal rephasing of the supplied basis redistributes the edge phases.
Only the accumulated loop distinction affects the comparator. The proof was
written in a one-edge gauge for clarity.

This does not authorize a fundamental U(1) connection. It identifies the
gauge-invariant response coordinate already present in the standard-quantum
control.

### 10.2 Conjugate cycles are presentation-related without oriented ports

A reflection of the abstract cycle reverses its orientation and exchanges the
two conjugate descriptions. If no physical preparation, reader, or reference
distinguishes that reflection, the two members are operationally equivalent.

The CJ-D distinction is claimable only when:

1. the source and detector ports are physical;
2. their directed comparison is retained;
3. the sign-reversing intervention is independently executable; and
4. presentation permutations are separated from physical reversal.

This firewall prevents an arbitrary vertex numbering from becoming an arrow
of time or a law-level handedness.

### 10.3 Aharonov--Bohm is inspiration, not inheritance

The magnetic Aharonov--Bohm experiment is a physical example in which
alternative routes carry a loop-sensitive response even where a local force
description along the routes is insufficient. It demonstrates that global
relational response is real physics.

U0 does not inherit electromagnetic potentials, charged particles, spatial
loops, complex amplitudes, or holonomy from that example. A native proposal
must derive or independently type its own physical relational distinction.

---

## 11. Mandatory hostile controls

### Control T — tree

On a tree, every edge-phase assignment is removable by diagonal rephasing.
There is no cycle winding and no conjugation-odd transition response.

**Purpose:** a source rule may not infer hidden loop data where no loop
response exists.

### Control E — even cycle

For even \(L\), the cycle is bipartite. Let \(S\) be \(+1\) on one
bipartition and \(-1\) on the other. Then

\[
SH_\phi S=-H_\phi.
\]

Therefore

\[
S U_\phi(\tau)S
=
U_\phi(-\tau)
=
U_\phi(\tau)^\dagger,
\]

which implies

\[
|U_{\phi,ij}(\tau)|
=
|U_{\phi,ji}(\tau)|.
\]

Since the conjugate member transposes the transition matrix,

\[
\Gamma^{-\phi}(\tau)
=
\Gamma^\phi(\tau)
\]

for the complete family.

**Purpose:** cycle topology alone does not guarantee a directed conjugation
witness. Odd non-bipartite structure is load-bearing.

### Control Z — zero orientation response

If

\[
\sin\phi=0,
\]

the first conjugation-odd coefficient vanishes and the two members are
transition-equivalent.

**Purpose:** a loop is not automatically chiral.

### Control R — unreferenced reflection

If the experiment quotients the orientation-reversing reflection, the pair is
one operational class.

**Purpose:** label order is not physical orientation.

### Control X — explicit physical sign input

If a calibrated intervention supplies a physically verified
conjugation-odd setting \(c=\pm1\), the two experiments no longer have the
same source descriptor.

**Purpose:** CJ-E does not exclude a lawful source response to genuine
physical controls.

### Control H — target Hamiltonian input

If \(H_\phi\), its loop phase, or the full answer family is handed to the
proposed rule, the family is reproduced trivially.

**Purpose:** representation is not source completion.

---

## 12. What “global” means here

The theorem uses “global” in a precise operational sense:

> The distinguishing response compares alternatives whose relative closed
> route winds through the complete cycle.

It does **not** imply:

1. superluminal influence;
2. instantaneous action at a distance;
3. a fundamental spatial topology;
4. a particle traversing both paths as an ontic trajectory;
5. nonlocal hidden variables;
6. a global clock; or
7. failure of local quantum field theory.

A local source law on a richer physical carrier can accumulate and transport
the required relational information. CJ-E says only that the information is
not recoverable from a fixed finite jet of the visible transition kernel plus
descriptors that erase its orientation.

---

## 13. Consequences for the U0 source search

The source search now has a sharper partition.

### Route U1 — fixed finite kernel jet

One fixed finite-order closure acts only on

\[
\Gamma,\dot\Gamma,\ldots,\Gamma^{(K)}.
\]

With conjugation-even source descriptors, this route fails uniformly by
CJ-E. **Closed at the printed class scope.**

### Route U2 — size-growing jet or memory

The source carries enough order/state to resolve cycles as they grow. This is
mathematically open. It must explain:

1. the physical identity of the extra state;
2. how its resource cost scales;
3. why it is not reconstructed from the target answer;
4. how interventions access or alter it; and
5. how genuine divisions treat it.

### Route U3 — independently physical conjugation-odd control

The source takes an oriented apparatus/reference distinction as legitimate
input and generates the response under one invariant rule. This is the most
economical escape for externally reversible controls.

The distinction may not be an uncalibrated sign label or supplied quantum
phase. Its source, reader, transformation law, and reversal operation must be
physical and target-independent.

### Route U4 — local relational carrier

A richer configuration may carry orientation information through local
interactions even though the visible endpoint kernel does not. This route is
open and does not require a nonlocal law. It must pass the U0 source-closure,
memory, composition, and no-equivalent-input gates.

### Route U5 — whole-boundary indivisible law

The law assigns the complete positive response to the typed experiment
without a finite local jet restart. This remains the most directly
Barandes-facing route.

It still must be uniform rather than a per-experiment table, compose at
physical records, resist artificial intermediate division, and generate
held-out controls.

### Route U6 — nonunique local law plus actuality selector

A singular/nonunique law can let identical finite jets depart differently.
But the selector is then additional physics and must be printed. Mathematical
nonuniqueness is not an explanation.

No surviving route is selected by this packet.

---

## 14. Barandes-facing interpretation

Barandes's correspondence permits a quantum system to be represented by an
ordinary-positive indivisible stochastic law with Hilbert structure
secondary. The odd-cycle family is compatible with that representation:
each \(\Gamma^\phi(\tau)\) is ordinary-positive.

The source-completion debt is exposed by the reversible family:

\[
\text{physical control reversal}
\quad\longmapsto\quad
\Gamma^\phi
\leftrightarrow
\Gamma^{-\phi}.
\]

A complete native theory must explain this map without receiving
\(H_\phi\), a wavefunction, an action, or a phase/holonomy answer.

CJ-E does not refute Barandes. It says that a stochastic-law ontology cannot
be completed merely by treating a finite number of initial transition
derivatives as the physical state. The law must know more because the
experiment physically knows more.

That “more” could be:

1. an oriented physical control relation;
2. an independently real source/reference state;
3. a larger relational configuration;
4. an irreducible whole-process law; or
5. new empirically testable physics.

The correspondence alone does not select among these.

---

## 15. Complete-process and intervention wall

The cycle theorem concerns one family of unperturbed endpoint readers. Even a
source that passes CJ-E has not generated a complete quantum process.

It must still predict under the same law:

1. reversal and continuous variation of the physical orientation control;
2. inserted interventions at multiple locations;
3. retained versus erased intermediate records;
4. adaptive choices conditioned on earlier records;
5. alternative preparation/read ports;
6. multiple interacting cycles;
7. tensor/composite experiments rather than disjoint direct sums only;
8. genuine division and nondivision behavior;
9. held-out lengths and coupling strengths; and
10. the full retained transcript distribution.

A table

\[
(L,g,\phi)\mapsto\Gamma^\phi
\]

computed from the target quantum Hamiltonian is a compiler. A native law must
map independently specified physical systems and interventions to these
responses without the answer already present in \(\phi\) as a target quantum
transport table.

---

## 16. Resource and actuality ledger

Any future use of a CJ-E escape must print:

| coordinate | required question |
|---|---|
| source state | what physical object carries the missing distinction? |
| orientation | how is reversal defined without label convention? |
| memory | how much future-relevant state persists across unrecorded seams? |
| scaling | does the carrier/order grow with cycle number or size? |
| intervention | how do controls change the carrier under one law? |
| reader | which physical record detects directed response? |
| division | when may that state be discarded and conditioning restarted? |
| actuality | what configuration or record is actual in one run? |
| calibration | what establishes the control without target recovery? |
| precision | what exact/approximate distinction is physically required? |

The theorem concerns predictive distinguishability, not why one random
outcome occurs. Irreducible stochastic sampling remains allowed.

---

## 17. Forbidden inferences and attack battery

1. **Graph ontology:** calling the comparator cycle the fundamental universe.
2. **Lattice regression:** treating finite vertices as spacetime atoms.
3. **Trajectory import:** reading walk paths as actual particle histories.
4. **Fundamental phase import:** promoting the target complex phase to the
   native beable.
5. **Holonomy by naming:** calling the missing coordinate “relational” while
   supplying the target loop answer.
6. **Time import:** treating \(\tau\) as derived physical time.
7. **Label chirality:** using clockwise vertex numbering as a physical
   orientation.
8. **Even-cycle inflation:** claiming every loop distinguishes conjugates.
9. **Tree inflation:** claiming local edge phases are always physical.
10. **Finite-jet generalization:** extending CJ-E to every enlarged positive
    state or local field theory.
11. **Nonlocality inflation:** inferring superluminal or nonlocal dynamics.
12. **Memory erasure:** omitting an independently evidenced reference carrier
    to manufacture indivisibility.
13. **Target advice:** supplying the sign response or Hamiltonian as a control
    descriptor.
14. **Order-growth concealment:** calling an \(L\)-dependent closure one
    fixed-resource law.
15. **Nonuniqueness as physics:** allowing both departures without an
    actuality/control selector.
16. **Endpoint/process conflation:** treating the unperturbed family as a
    complete intervention law.
17. **Barandes refutation:** presenting a finite-jet class no-go as a no-go
    for indivisible stochastic ontology.
18. **Hilbert promotion:** inferring fundamental Hilbert space because the
    visible probability jet is insufficient.
19. **Nelson repair:** importing diffusion or paths as the missing carrier.
20. **Gravity rescue:** asking MG0 to choose the orientation law.

---

## 18. Falsifiers

The author-side theorem packet fails if:

1. any entry of the conjugate pair differs below order \(L\);
2. the coefficient or sign in Theorem CJ-D is wrong;
3. another conjugation-odd path pair contributes before total length \(L\);
4. the spectrum or entry magnitudes differ between the pair;
5. the even-cycle control distinguishes the conjugate members;
6. the tree control retains gauge-invariant phase response;
7. an inspected primary source already proves the full arbitrary-order
   source-closure theorem and the attribution is not corrected; or
8. the claim is used without physical orientation/reference conditions.

A future native proposal fails this gate if:

1. it uses a fixed finite kernel jet and phase-blind descriptors yet claims
   both reversible odd-cycle responses;
2. its missing sign is fitted after target inspection;
3. its extra state has no physical source or intervention semantics;
4. its resource grows while being reported as constant;
5. its response disappears after restoring an omitted physical reference;
   or
6. it predicts only endpoints and not the held-out complete process.

---

## 19. Outcome ladder

### CJ-L0 — algebra/source failure

The packet is withdrawn or reduced to cited prior art.

### CJ-L1 — bounded odd-cycle theorem

Pre-winding jet equality and the first unequal derivative survive.

### CJ-L2 — uniform fixed-jet source-class obstruction

CJ-L1 survives together with the arbitrary-\(K\), fixed-order closure and
independent-control distinction corollaries.

### CJ-L3 — physical orientation-bearing positive source

One target-blind physical law generates the reversible control family and
complete records. **Not reached.**

### CJ-L4 — scalable complete quantum matter

The same law survives composites, adaptive interventions, Bell/contextual,
identical-particle, and field-theoretic controls. **Not reached.**

### CJ-L5 — common-nomology readiness

The complete matter law supplies a legitimate MG0 input against a distinct
rival. **Not reached.**

Current author-side ceiling:

\[
\boxed{
\mathrm{CJ\!-\!L2\ author\ packet\ only;\ no\ scientific\ award}
}
\]

No independent review, adjudication, empirical evaluation, or official
promotion has occurred.

---

## 20. Next physics question

The theorem rules out one false shortcut and leaves the real source problem:

> What independently physical, presentation-covariant,
> conjugation-odd relational structure can couple to interventions and
> generate directed complete-process response without being a supplied
> quantum phase, action, holonomy, or answer table?

The next author-side investigation should compare, without selecting:

1. orientation carried by an actual reference/source system;
2. orientation generated by a noncommuting intervention grammar;
3. orientation accumulated by a local relational carrier;
4. a direct positive whole-boundary consistency law; and
5. the possibility that no ordinary-positive native law supplies the required
   scalable structure without target-equivalent information.

That comparison must preserve the even-cycle, tree, unreferenced-reflection,
multi-cycle resource, no-equivalent-input, and complete-process controls.
It may not assume a fundamental discrete web, continuum, trajectory, phase,
or spacetime.

The companion reversal-source architecture gate now performs this comparison
at author-side scope. It proves that a covariant positive law plus a
contingent asymmetric source can generate odd response, while the reference
and a noncommuting intervention grammar remain nonselecting. It also retains
empirical interaction-level P/T violation as a distinct control. No native
response rule is thereby constructed.

---

## 21. Authority ledger

\[
\begin{array}{ll}
\text{cycle control} & \text{standard quantum comparator only}\\
\text{pre-winding equality} & \text{exact author-side theorem}\\
\text{first unequal derivative} & \text{exact author-side theorem}\\
\text{fixed finite jet closure} & \text{excluded at printed scope}\\
\text{tree/even-cycle controls} & \text{pass}\\
\text{conjugation-odd distinction} & \text{source routes classified / law absent}\\
\text{native positive source law} & \text{absent}\\
\text{configuration ontology} & \text{unselected}\\
\text{fundamental phase/holonomy} & \text{not inferred}\\
\text{physical time or spacetime} & \text{not inferred}\\
\text{U0-T4 / pin / review} & \text{closed / not authorized}\\
\text{MG0 / gravity result} & \text{none}
\end{array}
\]
