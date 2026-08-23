# ISP v17 — PC5 complete-process and non-Clifford resource displacement

**Status:** ACTIVE AUTHOR-SIDE CANDIDATE / NOT A PIN / NOT REVIEWED
**Date:** 2026-08-23
**Scientific result awarded:** none
**Authority created:** none

---

## 0. Reality question

PC3 found a projective coherent realization of one finite endpoint law. PC4
then constructed a finite ordinary-positive realization of the same entire
endpoint law. The physical lesson is not that either ontology won. It is that
the registered endpoint experiment did not identify the difference.

PC5 asks a stronger, still bounded question:

> When complete transformation equivalences and an unbounded calibrated
> non-Clifford word family are registered, where must a successful
> ordinary-positive account place the missing predictive structure?

The possible answers are not collapsed into “classical” and “quantum.” They
are separated as:

1. a finite functorial positive carrier;
2. a continuous phase-complete positive carrier;
3. transformation or preparation context;
4. hidden irreversible memory;
5. nonuniform whole-word advice;
6. an indivisible whole-program law with no intermediate positive carrier;
7. a noncommutative predictive boundary; or
8. an empirical deviation.

This document constructs an exact obstruction only for item 1, supplies
positive controls for items 2--6, and records what a scalable successor would
still have to prove. It does not select an ontology.

---

## 1. Registered operational packet

### 1.1 Finite tomographic interface

Let the operational system be one qubit. Register the six Pauli eigenstate
preparations

$$
\mathcal P_{\rm P}
=
\{\rho_{a,s}=(I+s\sigma_a)/2:
  a\in\{x,y,z\},\ s\in\{-1,+1\}\}
$$

and the three binary Pauli readers

$$
\mathcal M_{\rm P}=\{M_x,M_y,M_z\}.
$$

This finite packet is tomographically complete for unital qubit channels.
Indeed, the output expectations on the three positive-axis inputs determine
the three columns of the channel's Bloch matrix. Therefore two unitary
channels that agree on every registered preparation and reader are the same
projective unitary channel.

The use of a finite tomographic packet matters. The result below is not won by
registering a continuum of preparations and then observing that a finite
carrier cannot name them.

### 1.2 Calibrated generators

The generator names do not carry the physics. Their complete operational
calibration is fixed by

$$
H=\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix},
\qquad
T=
\begin{pmatrix}
1&0\\
0&e^{i\pi/4}
\end{pmatrix},
$$

and

$$
\mathcal H(\rho)=H\rho H^\dagger,
\qquad
\mathcal T(\rho)=T\rho T^\dagger.
$$

Every finite word in $H$ and $T$ is registered together with its complete
Pauli-tomographic profile. Since

$$
H^{-1}=H,
\qquad
T^{-1}=T^7,
$$

the word grammar contains the operational inverse of every word. No dimension,
geometry, ontology, or complex amplitude is inferred from the names $H$ and
$T$; the matrices merely specify the established comparison experiment.

### 1.3 Complete transformation equivalence

For registered procedures $A$ and $B$, write

$$
A\simeq_{\rm op}B
$$

exactly when every registered preparation, reader, retained record, and future
continuation gives the same probability law. This is an operational quotient,
not an instruction to identify physically different histories before the
record interface is fixed.

---

## 2. Retained and erased implementation records

### 2.1 The eight-state carrier

Use the PC4 cube carrier

$$
\Omega_8=\{(x,y,z):x,y,z\in\{-1,+1\}\}.
$$

The Pauli and Hadamard controls act by

$$
\begin{aligned}
I(x,y,z)&=(x,y,z),\\
X(x,y,z)&=(x,-y,-z),\\
Y(x,y,z)&=(-x,y,-z),\\
Z(x,y,z)&=(-x,-y,z),\\
H(x,y,z)&=(z,-y,x).
\end{aligned}
$$

The parity

$$
\pi(x,y,z)=xyz
$$

is preserved by $I,X,Y,Z$ and reversed by $H$.

### 2.2 Two operationally equal erased channels

Define two trusted random implementations

$$
\mathcal D_1
=
\frac14(\mathcal I+\mathcal X+\mathcal Y+\mathcal Z),
$$

and

$$
\mathcal D_2
=
\mathcal H\circ\mathcal D_1.
$$

For every qubit state,

$$
\mathcal D_1(\rho)=\mathcal D_2(\rho)=I/2.
$$

On the cube carrier, however, the induced kernels differ exactly. From any
$\lambda\in\Omega_8$, $D_1$ is uniform on the four states with parity
$\pi(\lambda)$, whereas $D_2$ is uniform on the four states with parity
$-\pi(\lambda)$.

### 2.3 The typing distinction

There are two different experiments.

**Retained record.** Let the random branch label and its apparatus record be
part of the output instrument. The two implementations then have different
conditional branch states and are not operationally equivalent. A process
ontology may retain their distinct histories without being contextual relative
to this richer experiment.

**Erased record.** Apply a declared erasure that removes the branch record from
the complete registered operational boundary before any future continuation.
The resulting quantum channels are operationally equal. The cube kernels still
differ by hidden parity.

The erased experiment therefore gives a clean classification:

$$
\boxed{
\text{operational descent}
\quad\lor\quad
\text{hidden implementation context}
}
$$

but not an ontology verdict. Requiring the two hidden kernels to be identical
is transformation noncontextuality, an additional invariance principle unless
it is independently derived. Allowing them to differ retains an empirically
idle context coordinate unless some registered future reader can access it.

Even the phrase “complete erasure” must not beg the question. Operational
erasure says that no registered continuation recovers the record. Ontological
erasure would additionally decree that no microscopic trace exists. The latter
is a physical postulate, not a consequence of the channel equality.

---

## 3. Exact non-Clifford infinite-order lemma

The non-Clifford obstruction can be proved without appealing to approximate
universality.

Choose determinant-one representatives

$$
\widetilde H=iH,
\qquad
\widetilde T=e^{-i\pi/8}T,
$$

and set

$$
U=\widetilde H\widetilde T\in SU(2).
$$

Direct calculation gives

$$
\operatorname{tr}U
=
\sqrt2\sin\frac\pi8
=:a,
$$

so

$$
a^2=1-\frac1{\sqrt2}.
$$

The element $a^2$ is not an algebraic integer. It lies in
$\mathbb Q(\sqrt2)$ and its field norm is

$$
\left(1-\frac1{\sqrt2}\right)
\left(1+\frac1{\sqrt2}\right)
=\frac12,
$$

whereas the norm of an algebraic integer in this quadratic field is an
integer. Hence $a$ is not an algebraic integer either.

If the projective class $[U]$ had finite order, the eigenvalues of $U$ would
be roots of unity. Their sum $\operatorname{tr}U=a$ would then be an
algebraic integer, a contradiction.

**Lemma PC5.1.** The projective channel $[HT]$ has infinite order. Therefore
the projective process group generated by the calibrated $H$ and $T$ contains
infinitely many operationally distinct channels.

The finite Pauli preparation/reader packet distinguishes these channels
because it is process-tomographically complete for the registered unital
family.

---

## 4. Finite reversible-positive carrier theorem

### 4.1 Exact admitted class

For $m<\infty$, define a **finite functorial reversible-positive carrier** to
consist of:

1. an ontic set $\Omega_m=\{1,\ldots,m\}$;
2. positive preparation distributions for the registered Pauli preparations;
3. positive response functions for the registered Pauli readers;
4. one column-stochastic matrix $K_g$ for each projective word channel $g$;
5. transformation noncontextuality on the registered complete process
   quotient, so $K_g$ depends on $g$, not its word spelling;
6. exact functorial composition

   $$
   K_{gh}=K_gK_h,
   \qquad
   K_e=I_m;
   $$

7. ontic representation of operational inverses,

   $$
   K_{g^{-1}}K_g=K_gK_{g^{-1}}=I_m;
   $$

8. exact reproduction of the complete registered process profiles.

The inverse condition is substantive. It excludes models that reproduce a
reversible laboratory channel while irreversibly dumping information into an
unregistered memory. Such models remain possible but enter a different,
charged branch.

### 4.2 Stochastic automorphisms

If a stochastic matrix has a stochastic inverse, its affine action is an
automorphism of the probability simplex. It must send extreme points to
extreme points. Therefore it is a permutation matrix.

Consequently every admitted $K_g$ lies in the finite group $S_m$.

### 4.3 Faithfulness from complete calibration

Suppose $K_g=K_h$. Then all registered preparation/reader probabilities after
$g$ and $h$ agree. Tomographic completeness implies that the two unitary
channels agree, hence $g=h$ as projective channels. The map

$$
g\longmapsto K_g
$$

is therefore injective.

### 4.4 The theorem

**Theorem PC5.2 (finite carrier obstruction).** No finite functorial
reversible-positive carrier reproduces the exact unbounded calibrated
$H,T$ process family.

**Proof.** Lemma PC5.1 supplies an infinite projective subgroup. Sections
4.2--4.3 would embed it faithfully into the finite permutation group $S_m$,
which is impossible. QED.

This theorem does **not** say that positivity fails. It says that four jointly
declared properties cannot all remain free:

$$
\boxed{
\text{finite carrier}
+\text{functoriality}
+\text{ontic reversibility}
+\text{process noncontextuality}
}
$$

for the exact unbounded $H,T$ process family.

---

## 5. Positive continuous control

The strongest immediate hostile control is an exact positive model, not a
quantum slogan.

Let the ontic carrier be the unit sphere $S^2$. For a pure qubit state
$|\psi\rangle$ with Bloch vector $w_\psi$, define

$$
\rho(v\mid\psi)
=
\frac1\pi(v\cdot w_\psi)
\Theta(v\cdot w_\psi).
$$

For a rank-one outcome $|\phi\rangle\langle\phi|$, define

$$
\xi_\phi(v)=\Theta(w_\phi\cdot v).
$$

Then

$$
\int_{S^2}\xi_\phi(v)\rho(v\mid\psi)\,d\Omega(v)
=
|\langle\phi\mid\psi\rangle|^2.
$$

Every qubit unitary acts by its ordinary Bloch-sphere rotation, so the ontic
evolution is deterministic, positive, Markovian, and exactly includes $T$.
The model uses two continuous ontic coordinates and carries the complete
orientation needed for the phase-sensitive response family.

This control proves the proper interpretation of Theorem PC5.2:

> the non-Clifford extension destroys the finite reversible carrier, but a
> positive ontology survives by carrying continuous phase-complete predictive
> structure.

For arbitrary instruments and mixed processes, an even more direct positive
control takes the quantum density operator or predictive comb itself as the
ontic state and uses Born response kernels. That construction is exact and
positive, but it simply reifies the standard quantum predictive object. It is
representation, not explanatory compression.

Neither control establishes that a Bloch direction, density matrix, or complex
amplitude is what exists in nature.

---

## 6. Contextual and non-disjoint controls

The single-qubit stabilizer literature does not support one unqualified
sentence saying that “the blowtorch proves transformation contextuality for
every positive ontology.”

Lillystone, Wallman, and Emerson prove a broad obstruction for the complete
single-qubit stabilizer subtheory and show that contextuality can be confined
to transformations. Their operational equivalence is precisely the erased
$D_1/D_2$ control above.

Kocia and Love exhibit a Grassmann model with non-disjoint ontic states and
argue that the blowtorch does not display transformation contextuality there.
They identify the disjoint-state single-simplex premise as the boundary of the
broader no-go.

PC5 therefore treats contextuality as a typed resource coordinate:

$$
R_{\rm ctx}
=
\text{information or structural dependence retained across
operationally equivalent implementations}.
$$

It does not treat the word “contextual” as an automatic synonym for false,
quantum, or empirically distinguishable.

---

## 7. Indivisible whole-program control

For every complete registered program $p$, ordinary quantum theory already
defines a positive distribution over completed records,

$$
\Gamma_p(r)=\Pr_Q(r\mid p).
$$

Such a family can deny that any intermediate ordinary-positive variable is a
future-sufficient restart state. It therefore evades both Theorem PC5.2's
finite Markov carrier and Q-Cut's sufficient-cut premise.

Existence is nevertheless cheap. If $p\mapsto\Gamma_p$ is supplied as an
answer table or if the entire target quantum process is received as state,
the quantum composition law has merely moved into

$$
R_{\rm comp}
\quad\text{or}\quad
R_{\rm unif}.
$$

The constructive U-Gen question remains:

> Does one fixed physical indivisible law generate the complete family from
> independently calibrated local controls, or does it consume the whole
> program and return the already-known quantum answer?

PC5 does not answer that question. It makes the escape explicit enough for a
later constructive contest.

---

## 8. Resource-displacement ledger

| Candidate account | Exact PC3 stabilizer endpoints | Exact unbounded $H,T$ words | Complete-process equivalence | Where the structure resides |
|---|---:|---:|---:|---|
| PC4 six/eight-state carrier | yes | no | not registered | finite control action supplied |
| finite functorial reversible-positive carrier | yes | impossible | descends by premise | theorem PC5.2 |
| finite context-sensitive or hidden-memory model | possible | not excluded | may fail descent | $R_{\rm ctx}$ or $R_{\rm mem}$ |
| continuous Bloch-sphere positive model | yes | yes for pure/unitary/projective packet | contextuality must be audited | continuous phase-complete carrier |
| density-operator/predictive-object ontology | yes | yes | implementation-sensitive unless quotiented | complete quantum predictive object |
| non-disjoint Grassmann model | stabilizer scope | extra structure for $T$ | avoids one disjoint-state no-go | algebraic constraints / higher-order term |
| indivisible completed-record law | yes | yes in principle | no intermediate cut required | whole-program law or oracle risk |
| standard quantum comparator | yes | yes | channel quotient fixed operationally | noncommutative state and composition law |

The anti-laundering rule is:

$$
\Delta R_i<0
\quad\Longrightarrow\quad
\exists j\ne i:\Delta R_j>0
\quad\text{or a proof that the removed information is idle}.
$$

The relevant vector remains

$$
(R_{\rm pred},R_{\rm mem},R_{\rm ctx},R_{\rm comm},
  R_{\rm comp},R_{\rm unif},R_{\rm phys}).
$$

Carrier cardinality, continuous dimension, mutual information, law-description
length, runtime, apparatus size, energy, and spacetime volume are different
coordinates. PC5 does not identify them.

---

## 9. Scalable many-body comparator

Montina proves a relevant but assumption-heavy external theorem. For an
$N$-dimensional Hilbert space, his admitted ontological class includes:

1. positive preparation distributions, with preparation context allowed;
2. positive Markov kernels for every physically attainable unitary, with
   transformation context allowed;
3. compatibility of those kernels with state evolution and sequential
   composition;
4. positive response functions for rank-one projective measurements, with
   measurement context allowed, reproducing the Born rule;
5. disjoint support for orthogonal quantum states; and
6. an additional post-transient support condition, his Property 2, which
   makes support transport time-symmetric on a selected ontic subspace.

Under those assumptions the number $w$ of continuous ontic variables obeys

$$
w\ge 2N-2.
$$

For $n$ qubits, $N=2^n$, giving

$$
w\ge 2^{n+1}-2.
$$

PC5 does not import this as an ISP result for four reasons:

1. Property 2 is an additional support/time-symmetry premise, not bare
   Markovity;
2. the theorem assumes the full all-unitary and all-projective interface;
3. exact reproduction on the countable dense Clifford+$T$ subgroup does not
   imply the all-unitary premise without a continuity bridge; and
4. continuous dimension is not automatically memory bits, energy, precision,
   or physical volume.

It is a strong candidate comparator for a separately reconstructed scalable
gate, not a license to announce exponential physical cost now.

---

## 10. What the physics says at this gate

### Earned author-side mathematics

Conditional on the printed class definition:

1. $HT$ has infinite projective order;
2. no finite functorial, ontically reversible, transformation-noncontextual
   positive carrier reproduces the exact unbounded calibrated word family;
3. a continuous positive carrier reproduces the same single-qubit unitary and
   projective predictions; and
4. erased implementation equivalence locates context but does not by itself
   identify ontology.

### Not earned

PC5 does not establish:

1. that complex amplitudes are ontic;
2. that all positive histories are impossible or expensive;
3. that contextuality alone causes quantum advantage;
4. that Barandes indivisibility is false or sufficient;
5. a many-body resource theorem;
6. a native uniform indivisible generator;
7. a new empirical prediction;
8. QFT, time, locality, spacetime, or gravity.

The strongest reality statement is therefore:

> Finite stabilizer simulations do not settle ontology. Exact phase-complete
> process composition forces a successful positive account either beyond a
> finite reversible noncontextual carrier or into another explicitly charged
> resource branch.

---

## 11. Hostile controls for any successor

Any promotion-bearing successor must include at least:

1. finite endpoint-only PC4 control;
2. finite complete-process carrier control;
3. continuous Bloch/Kochen--Specker positive control;
4. density-operator/predictive-object reification control;
5. retained-record and erased-record transformation mixtures;
6. context-sensitive word-kernel control;
7. hidden irreversible memory control;
8. non-disjoint ontic-state control;
9. whole-program indivisible answer-table control;
10. one fixed uniform generator control;
11. a countable-dense-without-continuity mutant; and
12. a physical-resource claim mutant that substitutes dimension for bits or
    energy.

---

## 12. Next-gate disposition

PC5 is not ready to freeze as an official unit. Its finite theorem is exact,
but the promotion-bearing question is scalable information displacement, not
the fact that eight cube vertices cease to suffice.

The recommended ordering is:

1. **Q-Cut official gate, if separately authorized:** independently test the
   scalable information burden of a positive future-sufficient cut;
2. **PC5 author-side source and scope audit:** preserve the exact finite
   obstruction and positive controls;
3. **U-Gen scalable successor:** either independently reconstruct a
   Montina-type many-body theorem under fully printed assumptions or design a
   different scalable operational resource test; and
4. **U-Gen constructive contest:** require one fixed indivisible law to
   generate held-out complete processes without target-process input.

No automatic official unit, repaired pin, clock, causal-order, spacetime, or
gravity work follows from this document.

---

## 13. Exact primary-source bindings

1. P. Lillystone, J. J. Wallman, and J. Emerson,
   “Contextuality and the Single-Qubit Stabilizer Formalism,”
   arXiv:1802.06121v2,
   <https://arxiv.org/abs/1802.06121v2>.
2. L. Kocia and P. Love, “The Non-Disjoint Ontic States of the Grassmann
   Ontological Model, Transformation Contextuality, and the Single Qubit
   Stabilizer Subtheory,” arXiv:1805.09514v1,
   <https://arxiv.org/abs/1805.09514v1>.
3. L. Kocia and P. Love, “Discrete Wigner Formalism for Qubits and
   Non-Contextuality of Clifford Gates on Qubit Stabilizer States,”
   arXiv:1705.08869v2,
   <https://arxiv.org/abs/1705.08869v2>.
4. A. Montina, “Exponential complexity and ontological theories of quantum
   mechanics,” arXiv:0711.4770v2,
   <https://arxiv.org/abs/0711.4770v2>.

The infinite-order lemma and finite stochastic-automorphism theorem are
proved directly here rather than attributed to those sources.
