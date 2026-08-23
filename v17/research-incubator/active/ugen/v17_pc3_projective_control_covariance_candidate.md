# ISP v17 — PC3 projective control-covariance candidate

**Status:** ACTIVE AUTHOR-SIDE MATHEMATICS / NOT A PIN / NOT REVIEWED
**Date:** 2026-08-23
**Scientific result awarded:** none
**Authority created:** none

This candidate asks whether independently typed control symmetries can select
the composition data left free by positive primitive endpoints.

It produces a positive mathematical result inside one declared coherent
projective-covariance class. It does not derive that class from ordinary
positive stochastic principles.

---

## 1. Physical procedure packet

Use one boundary type with configuration set

$$
\mathcal C=\{0,1\}.
$$

There are two reversible physical procedure labels:

$$
b
\qquad\text{and}\qquad
r.
$$

Their isolated configuration transition matrices are

$$
G_b
=
G
=
\frac12
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix},
\qquad
G_r
=
I_2.
$$

Thus \(b\) is balanced in the registered configuration basis, while \(r\)
preserves each configuration when used alone. These positive endpoints do
not specify their common-continuation behavior.

The only reader in the core mathematical packet is the complete final
configuration reader. A retained configuration reader inserted between
primitives is a separate division control.

---

## 2. Independently typed control group

Let the classical control procedures carry the finite presentation

$$
\mathcal O
=
\langle b,r
\mid
b^2=e,\;
r^4=e,\;
(br)^3=e
\rangle.
$$

This is the \((2,4,3)\) spherical triangle presentation of the
orientation-preserving octahedral group, of order \(24\).

The relations are to be interpreted as relations among externally registered
control procedures—for example, apparatus orientations—not as quantum
probabilities learned from the system under test.

That distinction is binding. If \((br)^3=e\) is inferred from the same final
configuration return experiment it is later said to predict, then the
construction is calibration, not explanation.

No chronology or spacetime is derived from the word order. It is supplied
laboratory procedure composition.

---

## 3. Candidate covariance bridge

A coherent projective bridge assigns fixed unitaries

$$
B,R\in U(2)
$$

to the two procedures such that

$$
q(B)=G,
\qquad
q(R)=I_2,
\qquad
q(U)=|U|^{\odot2},
$$

and the control relations hold projectively:

$$
B^2\propto I_2,
\qquad
R^4\propto I_2,
\qquad
(BR)^3\propto I_2.
$$

Equivalently, the classes \([B],[R]\in PU(2)\) define a representation of
\(\mathcal O\).

For a word

$$
w=g_m\cdots g_1,
\qquad g_j\in\{b,r\},
$$

\(g_1\) is executed first and \(g_m\) last.

The coherent completed-record law is

$$
\Gamma_w^{\mathrm{coh}}
=
q(G_m\cdots G_1),
$$

where \(G_j=B,R,\) or \(R^{-1}\) according to the letter.

This one multiplication rule applies at every word length. No word-indexed
response table is allowed inside this candidate class.

---

## 4. Gauge and operational equivalence

### 4.1 Scalar lift gauge

Multiplying \(B\) or \(R\) by a scalar phase changes no completed
configuration probability and does not change the projective relations.

### 4.2 Boundary rephasing

A diagonal unitary

$$
D=\operatorname{diag}(e^{i\alpha},e^{i\beta})
$$

acts simultaneously as

$$
B\longmapsto DBD^{-1},
\qquad
R\longmapsto DRD^{-1}.
$$

The preparations and readers transform consistently, so all registered
probabilities are unchanged.

### 4.3 Complex conjugation

The pairs

$$
(B,R)
\qquad\text{and}\qquad
(\overline B,\overline R)
$$

produce complex-conjugate word matrices. Their entrywise modulus squares
agree for every word. They are therefore operationally equivalent at the
registered configuration interface, whether or not a future enlarged
experiment treats antiunitary conjugation as gauge.

The theorem below claims uniqueness of the positive word law, not uniqueness
of an ontic amplitude presentation.

---

## 5. Classification theorem

### Proposition A — unique positive projective-covariant word law

Every coherent projective bridge satisfying the PC3 packet is, modulo scalar
phases and diagonal boundary rephasing, represented by

$$
B=H
=
\frac1{\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix},
\qquad
R=R_{\pm}
=
\begin{pmatrix}
1&0\\
0&\pm i
\end{pmatrix}.
$$

The two signs are complex conjugates and generate the same positive
completed-word law:

$$
q\!\left(w(H,R_+)\right)
=
q\!\left(w(H,R_-)\right)
$$

for every registered word \(w\).

Consequently the endpoint packet plus the projective control-covariance
bridge selects one positive word law inside this coherent class.

---

## 6. Proof

### 6.1 Normalize the balanced involution

Because \(B^2\propto I_2\), multiply \(B\) by a scalar phase so that

$$
B^2=I_2.
$$

Unitarity then gives

$$
B=B^{-1}=B^\dagger.
$$

The flat endpoint \(q(B)=G\) excludes \(B=\pm I_2\), so the two eigenvalues
are \(+1\) and \(-1\), and \(\operatorname{tr}B=0\). Hence

$$
B
=
\frac1{\sqrt2}
\begin{pmatrix}
\epsilon&e^{-i\eta}\\
e^{i\eta}&-\epsilon
\end{pmatrix},
\qquad
\epsilon\in\{+1,-1\}.
$$

A scalar sign and one diagonal boundary rephasing set
\(\epsilon=+1\) and \(\eta=0\). Thus \(B\) is gauge-represented by \(H\).

### 6.2 Normalize the configuration-preserving generator

The condition \(q(R)=I_2\) with fixed configuration labels forces \(R\) to be
diagonal. Removing a scalar phase gives

$$
R
=
\begin{pmatrix}
1&0\\
0&z
\end{pmatrix},
\qquad
|z|=1.
$$

Diagonal boundary rephasing commutes with \(R\), so the relative phase \(z\)
is not removed by the allowed boundary gauge.

### 6.3 Apply the mixed projective relation

Set

$$
A=HR.
$$

Then

$$
\operatorname{tr}A
=
\frac{1-z}{\sqrt2},
\qquad
\det A=-z.
$$

Cayley--Hamilton gives

$$
A^3
=
\left((\operatorname{tr}A)^2-\det A\right)A
-
(\operatorname{tr}A)(\det A)I_2.
$$

The matrix \(A\) is not scalar. Therefore \(A^3\propto I_2\) exactly when

$$
(\operatorname{tr}A)^2=\det A.
$$

Substitution yields

$$
\frac{(1-z)^2}{2}=-z,
$$

or

$$
1+z^2=0.
$$

Hence

$$
z=+i
\qquad\text{or}\qquad
z=-i.
$$

The relation \(R^4\propto I_2\) is then automatic. For the two cases,

$$
(HR_+)^3=e^{i\pi/4}I_2,
\qquad
(HR_-)^3=e^{-i\pi/4}I_2.
$$

### 6.4 Positive operational uniqueness

\(H\) is real and \(R_-=\overline{R_+}\). Every word matrix for the minus
choice is therefore the complex conjugate of the corresponding plus word
matrix, up to scalar phases. Entrywise modulus squares agree. This proves
Proposition A.

---

## 7. Exhaustive prediction battery

The author-side witness words were inspected while designing this candidate.
They receive no blind held-out evidential status.

For any future official freeze, use a prediction-independent exhaustive
battery:

1. order the alphabet by \(b<r\);
2. choose the shortlex least word representing each element of
   \(\mathcal O\);
3. include all \(24\) group elements;
4. mark only the identity and primitive endpoint experiments as calibration;
   and
5. treat every other canonical element as a prediction target.

Because the battery is exhaustive, no favorable separator can be selected
after construction.

### Proposition B — complete positive outcome census

For the selected projective coherent word law, the \(24\) canonical control
elements give:

$$
\begin{array}{c|c}
\text{positive endpoint}&\text{number of control elements}\\
\hline
I_2&4\\
X&4\\
G&16
\end{array}
$$

#### Proof

Conjugation by \(H\) and \(R_+\) permutes the six oriented Pauli axes

$$
\{\pm X,\pm Y,\pm Z\}
$$

as the full orientation-preserving octahedral group. The action is transitive,
and the stabilizer of an oriented axis has order \(24/6=4\).

If a control element maps \(+Z\) to \(+Z\), its configuration transition is
\(I_2\). If it maps \(+Z\) to \(-Z\), its transition is \(X\). The four
equatorial targets \(+X,-X,+Y,-Y\) give the balanced law \(G\), with four
control elements for each target. Thus the counts are \(4,4,16\).
\(\square\)

### 7.1 Transparent design witness

One illustrative nonprimitive word is

$$
w_\star=br^2b.
$$

For either selected lift,

$$
R_\pm^2=Z,
\qquad
HZH=X,
$$

so

$$
\Gamma_{w_\star}^{\mathrm{coh}}=X.
$$

This word is a displayed algebraic witness only. It was not blind and cannot
be promoted independently of the exhaustive battery.

---

## 8. Hostile controls

### 8.1 Markov positive composition

Composing the positive primitive endpoints gives

$$
G_b=G,
\qquad
G_r=I_2.
$$

For the witness,

$$
G I_2^2 G=G.
$$

The coherent prediction is \(X\), so for configuration input \(0\) the
total-variation separation is \(1/2\).

More fundamentally, no group homomorphism

$$
\rho:\mathcal O\longrightarrow\mathsf{Stoch}_2
$$

can satisfy \(\rho(b)=G\). Every group image must have a stochastic inverse,
whereas \(G\) is singular. Thus ordinary two-state Markov composition cannot
represent the reversible control group with this endpoint packet.

This is carrier-relative. A larger hidden carrier is a different model.

### 8.2 Measured-boundary control

Insert and retain a complete configuration reader after every primitive.
Then the operational law is the product of the isolated positive kernels.
Every word containing \(b\) yields \(G\); words containing only \(r\) yield
\(I_2\).

In particular, the measured version of \(w_\star\) yields \(G\), not \(X\).
The separator therefore depends on an unmeasured composition boundary.

### 8.3 Alternative coherent controls

The choices

$$
R_0=I_2,
\qquad
R_\pi=Z
$$

share the isolated endpoint \(q(R)=I_2\), obey \(R^4=I_2\), and can be used
with \(B=H\). They fail the mixed projective relation

$$
(BR)^3\propto I_2.
$$

For both alternatives,

$$
q(BR^2B)=I_2,
$$

not \(X\). The mixed control relation is doing real selection work inside the
coherent class.

### 8.4 Direct indivisible whole-law control

Because \(\mathcal O\) has only \(24\) elements, a direct positive law can
assign an arbitrary stochastic matrix \(K_g\) to every group element, subject
only to

$$
K_e=I_2,
\qquad
K_b=G,
\qquad
K_r=I_2.
$$

Depending on the group element rather than the spelling of its word makes all
control relations well typed. Yet the remaining \(21\) matrices can still be
chosen independently, including \(K_{w_\star}=I_2\), \(G\), or \(X\).

This is one finite uniform direct law, but it is a charged group-indexed
response table. The abstract control relations alone do not select its
continuation probabilities.

The projective coherent bridge gains predictive compression by supplying a
functorial multiplication structure. Whether an ordinary-positive
indivisible principle can generate the same structure natively remains open.

### 8.5 Enlarged-carrier control

A larger configuration carrier can carry a permutation representation of
\(\mathcal O\), with the two observed configurations obtained by
coarse-graining. Such a construction is not ruled out.

It must charge:

1. the carrier and its preparation;
2. the coarse-graining map;
3. inaccessible state information;
4. the group action;
5. physical memory and precision; and
6. why the observed endpoint packet has the required form.

### 8.6 Real-representation control

The selected complex representation can be embedded into a larger real
orthogonal representation. Therefore explicit complex syntax is not an
ontology discriminator. The invariant result is the positive word law and
its input dependency, not the spelling of its lift.

---

## 9. What the candidate establishes

If independently accepted later, the candidate would establish:

1. positive primitive endpoints \(G\) and \(I_2\) do not select their word
   laws;
2. a typed projective representation of the octahedral control group selects
   a unique positive word law within the two-state coherent class;
3. the two complex-conjugate lifts are operationally identical at the
   registered configuration interface;
4. the selected law predicts an exhaustive \(4/4/16\) endpoint census;
5. two-state Markov composition cannot realize the reversible control
   packet;
6. retained intermediate records remove the separator; and
7. unrestricted positive whole laws remain nonunique unless the functorial
   composition structure is added.

---

## 10. What remains unearned

The central explanatory debt is the covariance bridge itself:

$$
\text{classical control group}
\longrightarrow
PU(2)\text{ process action}.
$$

Known quantum mechanics and Wigner-style symmetry arguments motivate such a
bridge. The present endpoint packet does not derive it.

The candidate does not establish:

1. that projective unitaries are ontic;
2. that every physical control symmetry acts projectively on a two-state
   carrier;
3. a native Barandes composition generator;
4. a lower bound against every enlarged positive carrier;
5. tensor or interacting-parent composition;
6. adaptive instruments or process tensors;
7. a non-Clifford resource;
8. universal quantum theory;
9. internal time or causal order;
10. QFT, spacetime, or gravity; or
11. an official v17 result.

---

## 11. Source-faithful Barandes interpretation

A complete Barandes model may supply every

$$
\Gamma_g,
\qquad g\in\mathcal O,
$$

as fixed transition-law data. PC3 does not contradict that representation.

Barandes' published dynamical-symmetry condition asks which transformations
leave an already specified transition matrix invariant, up to
Schur--Hadamard gauge. PC3 asks the converse generative question: whether a
physical control symmetry plus a bounded endpoint packet determines the
transition family.

The projective coherent answer is positive only because the candidate adds a
map into \(PU(2)\). A stochastic-native successor must either derive an
equivalent map, construct a different positive generator with the same
exhaustive predictions, or expose the extra nomological data it requires.

---

## 12. Present disposition

    ENDPOINT PACKET:                    FIXED AUTHOR-SIDE
    CONTROL GROUP:                      EXACT FINITE PRESENTATION
    PROJECTIVE COHERENT CLASSIFICATION: PROVED AUTHOR-SIDE
    POSITIVE WORD-LAW UNIQUENESS:       PROVED AUTHOR-SIDE
    EXHAUSTIVE 24-ELEMENT BATTERY:       DEFINED / NOT RUN AS EXPERIMENT
    MARKOV TWO-STATE CONTROL:           EXACT NO-GO
    DIRECT WHOLE-LAW CONTROL:           NONUNIQUE
    COVARIANCE BRIDGE ORIGIN:           OPEN
    PIN / REVIEW / RESULT:              NONE
