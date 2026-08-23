# ISP v17 — PC2 balanced composition-seam classification

**Status:** ACTIVE AUTHOR-SIDE MATHEMATICS / NOT A PIN / NOT REVIEWED
**Date:** 2026-08-23
**Scientific result awarded:** none
**Authority created:** none

This note answers the smallest exact version of the composition-lift question
left open by E-Comp. E-Comp proves that positive endpoint data do not inherit
coherent multiplication. The present note identifies the complete gluing
coordinates for a chain of balanced two-state unitary lifts and then asks what
those coordinates mean operationally.

The result is deliberately conditional. It starts inside a coherent unitary
lift class. It does not derive that class from ordinary-positive stochastic
principles, make amplitudes ontic, or select a law of nature.

---

## 1. Registered packet

Let

$$
G=\frac12
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix},
\qquad
H=\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix},
$$

and define

$$
q:U(2)\longrightarrow\mathsf{Stoch}_2,
\qquad
q(U)=|U|^{\odot2}.
$$

Let $\mathcal D_2\subset U(2)$ be the diagonal unitary group and let

$$
\mathcal F_G=\{U\in U(2):q(U)=G\}
$$

be the balanced flat fiber. A chain

$$
U_m\cdots U_2U_1,
\qquad U_j\in\mathcal F_G,
$$

has no configuration record at an internal boundary. Only its initial and
final configuration are read. An actual intermediate reader is treated
separately in Section 7.

The question is not whether a coherent lift exists. It is:

> After endpoint rephasings are removed, which additional data determine the
> positive final law $q(U_m\cdots U_1)$?

---

## 2. The flat-fiber normal form

### Proposition A — exact order-two flat fiber

$$
\boxed{\mathcal F_G=\mathcal D_2H\mathcal D_2.}
$$

#### Proof

Every $U\in\mathcal F_G$ can be written

$$
U=\frac1{\sqrt2}
\begin{pmatrix}
e^{ia}&e^{ib}\\
e^{ic}&e^{id}
\end{pmatrix}.
$$

Column orthogonality gives

$$
e^{i(b-a)}+e^{i(d-c)}=0,
$$

or equivalently

$$
a+d-b-c\equiv\pi\pmod{2\pi}.
$$

Set

$$
L=\operatorname{diag}(e^{ia},e^{ic}),
\qquad
R=\operatorname{diag}(1,e^{i(b-a)}).
$$

The orthogonality relation then gives $U=LHR$. The reverse inclusion follows
because diagonal unitaries alter only row and column phases, so
$q(LHR)=q(H)=G$. Therefore
$\mathcal F_G=\mathcal D_2H\mathcal D_2$.

If $LHR=L'HR'$ with all four side matrices diagonal unitary, the two
factorizations differ only by redistribution of a scalar phase between the
left and right factors. Thus their relative diagonal phases agree. $\square$

This is proved here directly. Higher-dimensional complex Hadamard
classification is not imported into the result.

---

## 3. Seam normal form

Choose a flat-fiber decomposition

$$
U_j=L_jHR_j
$$

for each operation. Define the internal seam matrices

$$
S_j=R_{j+1}L_j\in\mathcal D_2,
\qquad 1\le j<m.
$$

### Proposition B — complete seam factorization

For every balanced chain,

$$
U_m\cdots U_1
=
L_mH S_{m-1}H\cdots S_2H S_1H R_1,
$$

and therefore

$$
\boxed{
q(U_m\cdots U_1)
=
q(H S_{m-1}H\cdots S_1H).
}
$$

Conversely, every sequence

$$
(S_1,\ldots,S_{m-1})\in\mathcal D_2^{m-1}
$$

is realized by balanced lifts, for example by taking

$$
U_1=H,
\qquad
U_{j+1}=HS_j.
$$

#### Proof

The product identity follows by associating the adjacent diagonal factors
$R_{j+1}L_j$. For all diagonal unitaries $D_L,D_R$,

$$
q(D_LAD_R)=q(A),
$$

so the external factors $L_m$ and $R_1$ disappear from the positive endpoint
law. The displayed converse has $q(U_j)=G$ for every $j$ and produces the
requested seams by direct multiplication. $\square$

Each $S_j$ has only one nontrivial relative phase after its scalar phase is
removed. Write a representative as

$$
S_{\phi_j}
=
\operatorname{diag}
\left(e^{i\phi_j/2},e^{-i\phi_j/2}\right).
$$

The tuple $(\phi_1,\ldots,\phi_{m-1})$ is a complete sufficient coordinate
for the positive endpoint of this balanced coherent chain. This statement
does **not** claim that the tuple is a minimal physical resource or that the
map from tuples to one chosen final endpoint is injective.

---

## 4. Gauge audit

There are three different notions that must not be conflated.

### 4.1 Decomposition redundancy

Replacing

$$
L_j\mapsto z_jL_j,
\qquad
R_j\mapsto z_j^{-1}R_j,
\qquad |z_j|=1,
$$

does not change $U_j$. It multiplies an adjacent $S_j$ only by a scalar, so
the seam's relative phase is unchanged.

### 4.2 Internal basis rephasing

At the boundary between $U_j$ and $U_{j+1}$, let $D\in\mathcal D_2$ and make
the consistent replacement

$$
U_j\mapsto DU_j,
\qquad
U_{j+1}\mapsto U_{j+1}D^{-1}.
$$

The total product is unchanged. In the normal form, the two inserted factors
cancel inside $R_{j+1}L_j$, so the seam is unchanged. A phase attached only
to one isolated lift is therefore not the invariant content of the theorem.

### 4.3 Operational composition data

Changing the relative seam while keeping every isolated endpoint equal to
$G$ can change a completed-record probability. Such changes are not gauge
copies of one complete experiment. They are different composition laws
compatible with the incomplete endpoint packet.

The physically safe conclusion is:

> The invariant missing datum is relational gluing information at an
> unmeasured composition boundary, not an absolute phase assigned to one
> operation.

This does not make the seam ontic. Complete process calibration relative to a
shared laboratory reference can supply the same information empirically.

---

## 5. Homogeneous repeated operation

Now require the same lift $U=LHR$ at every step. Its constant seam is

$$
S=RL.
$$

After removing its scalar phase, take $S=S_\phi$. The complete unmeasured
block law is

$$
\Gamma_0^{\rm coh}=I_2,
\qquad
\Gamma_m^{\rm coh}(\phi)
=
q\!\left(H(S_\phi H)^{m-1}\right)
\quad(m\ge1).
$$

At depth two,

$$
HS_\phi H
=
\begin{pmatrix}
\cos(\phi/2)&i\sin(\phi/2)\\
i\sin(\phi/2)&\cos(\phi/2)
\end{pmatrix},
$$

and hence

$$
\Gamma_2^{\rm coh}(\phi)
=
\begin{pmatrix}
x&1-x\\
1-x&x
\end{pmatrix},
\qquad
x=\cos^2(\phi/2).
$$

### Proposition C — exact homogeneous positive classifier

Within the homogeneous balanced-unitary subclass, the scalar

$$
x=(\Gamma_2)_{00}\in[0,1]
$$

is necessary and sufficient to determine the entire positive sequence

$$
(\Gamma_m)_{m\ge0}.
$$

#### Proof

If two laws have the same $x$, their phases obey

$$
\psi\equiv\phi
\quad\text{or}\quad
\psi\equiv-\phi
\pmod{2\pi}.
$$

The first choice changes at most scalar phases. Under the second choice,
$S_\psi=\overline{S_\phi}$, and $H$ is real. The complete amplitude product
is therefore complex conjugated, leaving every modulus square unchanged.
Thus all $\Gamma_m$ agree. Necessity follows because the complete sequence
contains $\Gamma_2$. $\square$

This is a classification after the coherent homogeneous law class has been
declared. It is not a derivation of that class from the one-step endpoint.

---

## 6. Exact controls

### 6.1 Hadamard and alternative coherent endpoints

For $\phi=0$,

$$
x=1,
\qquad
\Gamma_2=I_2.
$$

For $\phi=\pi$,

$$
x=0,
\qquad
\Gamma_2=X.
$$

These reproduce the two coherent separators in E-Comp at the level of their
positive repeated-block laws.

### 6.2 A delayed separator

For $\phi=\pi/2$,

$$
\Gamma_1=G,
\qquad
\Gamma_2=G,
\qquad
\Gamma_3=I_2.
$$

To verify the last identity, set $A=S_{\pi/2}H$. Then

$$
\operatorname{tr}A=i,
\qquad
\det A=-1,
$$

so Cayley--Hamilton gives $A^2=iA+I_2$. Consequently
$HA^2=iHS_{\pi/2}H+H$ is diagonal with unit-modulus diagonal entries, and its
modulus-square matrix is $I_2$.

The Markov completion has

$$
\Gamma_m^{\rm M}=G
\qquad(m\ge1).
$$

Thus one coherent law can agree with the Markov law at calibration depths one
and two yet disagree maximally at depth three. Agreement on one extra depth
does not create a composition principle.

### 6.3 Carrier-relative nondivision

For the two-state intermediate configuration carrier,

$$
\det\Gamma_2^{\rm coh}=2x-1.
$$

If $x\ne1/2$, $\Gamma_2$ has rank two. No stochastic $K$ can satisfy

$$
\Gamma_2=KG,
$$

because $KG$ has rank at most one. If $x=1/2$, depth two equals $G$, but the
depth-three control above gives $I_2$, which again cannot factor through $G$.

Therefore every member of the homogeneous balanced-unitary completion class
is nondivisible at depth two or three relative to this carrier. Nondivision
does not select the member of the class.

No claim is made against a larger hidden carrier or a different typed
intermediate object.

---

## 7. Actual record insertion

Insert a complete configuration reader at an internal boundary and retain its
outcome. Under the declared coherent measurement control, conditioning on
that record starts a new block from the observed configuration. Every next
one-step endpoint is $G$, and the seam across the measured boundary no longer
affects any recorded probability.

This is the operational difference between:

1. an unmeasured gluing boundary carrying coherent composition data; and
2. a physical division at which a complete record is made.

It is a control using the registered measurement semantics. It is not a
universal derivation of decoherence from positivity, consciousness, or an
unspecified environment.

---

## 8. Finite calibration does not select an unrestricted block law

Let $\mathsf B^+$ be the permissive class of effectively presented sequences

$$
(\Gamma_m)_{m\ge0},
\qquad
\Gamma_0=I_2,
$$

with every $\Gamma_m$ a normalized positive endpoint matrix for a final-only
block experiment. No composition, analyticity, or finite-order recurrence is
assumed.

### Proposition D — finite-prefix underdetermination

For every $\Gamma\in\mathsf B^+$ and every finite $N$, there is another
$\widetilde\Gamma\in\mathsf B^+$ such that

$$
\widetilde\Gamma_m=\Gamma_m
\quad(0\le m\le N),
\qquad
\widetilde\Gamma_{N+1}\ne\Gamma_{N+1}.
$$

#### Proof

Choose any normalized positive matrix $B\ne\Gamma_{N+1}$ and define one
finite evaluator that calls the original evaluator except at the fixed input
$m=N+1$, where it returns $B$. The result remains effective, positive, and
normalized in the printed final-only block grammar. $\square$

This proposition is intentionally weak but important. A finite calibration
prefix selects an infinite law only after a structural class has been added.
Homogeneous unitary composition is one such class; Markov composition,
finite-memory recurrence, or a native stochastic whole-law principle would
be others. Choosing the structural class is physical input, not a consequence
of endpoint positivity.

---

## 9. What has actually been learned

The two-state balanced case supports four exact conclusions.

1. Every coherent lift of the balanced endpoint is $LHR$.
2. External row and column phases are gauge at the completed endpoint.
3. Sequential behavior depends on relative seam data that the isolated
   positive endpoints do not contain.
4. In the homogeneous coherent subclass, one two-step scalar $x$ classifies
   the entire positive repeated-block sequence, but the subclass itself is an
   additional premise.

The result sharpens “the phases went somewhere” into a typed statement:

$$
\boxed{
\text{isolated positive endpoints}
+\text{unmeasured wiring}
\not\Rightarrow
\text{complete composition law};
\quad
\text{a seam rule is additional input.}
}
$$

The open physical question is why nature uses its observed seam/composition
rule, whether that rule follows from a deeper operational principle, and
whether an ordinary-positive indivisible theory can state it without merely
re-encoding the quantum process law.

---

## 10. Literature boundary

The order-two normal form and every calculation used here are proved in this
note. Complex Hadamard matrices provide the broader mathematical setting:

- Wojciech Tadej and Karol Życzkowski, *A concise guide to complex Hadamard
  matrices*, Open Systems & Information Dynamics **13** (2006), arXiv
  `quant-ph/0512154`.

Operational reconstructions of finite-dimensional quantum theory show that
composition becomes physically informative only together with a larger set
of operational postulates; they do not make the present endpoint packet
sufficient:

- Giulio Chiribella, Giacomo Mauro D'Ariano, and Paolo Perinotti,
  *Informational derivation of quantum theory*, Physical Review A **84**
  (2011), arXiv `1011.6451`.

Reconstructions of complex probability calculus from experimental
composition rules likewise begin with additional operational symmetry and
combination assumptions:

- Philip Goyal, Kevin H. Knuth, and John Skilling, *Origin of complex quantum
  amplitudes and Feynman's rules*, Physical Review A **81** (2010), arXiv
  `0907.0909`.

These references are context, not load-bearing premises of Propositions A--D.

---

## 11. Scope ceiling

### Candidate result, if independently accepted later

An exact classification of the gluing coordinates for balanced two-state
unitary lifts, plus homogeneous positive-sequence classification and explicit
nondivision/nonselection controls.

### Not established

1. a derivation or selection of complex amplitudes;
2. amplitude or seam ontology;
3. a universal composition classifier for all stochastic laws;
4. the higher-dimensional complex-Hadamard fiber;
5. tensor products, entangling operations, adaptive instruments, or process
   tensors;
6. a physical memory, energy, precision, or communication lower bound;
7. a refutation of a complete fixed Barandes law;
8. internal time, causal locality, QFT, spacetime, or gravity; or
9. any official v17 theorem, pin, paper, or promotion.

---

## 12. Present disposition

```text
EXACT PC2 ALGEBRA:                   AUTHOR-SIDE COMPLETE
GAUGE/SEAM DISTINCTION:             PRINTED
HOMOGENEOUS POSITIVE CLASSIFIER:    PRINTED
MARKOV / DELAYED-SEPARATION CONTROL: PRINTED
CARRIER-RELATIVE NONDIVISION:       PRINTED
FINITE-PREFIX WALL:                 PRINTED AT WEAK BLOCK-LAW SCOPE
HIGHER-D / TENSOR / ADAPTIVE LIFT:  OPEN
PHYSICAL SELECTION PRINCIPLE:       OPEN
PIN FROZEN:                         NO
INDEPENDENT REVIEW:                 NONE AUTHORIZED
SCIENTIFIC RESULT:                  NONE
```
