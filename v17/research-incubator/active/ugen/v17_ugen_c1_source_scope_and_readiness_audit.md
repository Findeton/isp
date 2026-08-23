# ISP v17 — U-Gen C1 source, scope, and readiness audit

**Status:** ACTIVE AUTHOR-SIDE AUDIT / NOT INDEPENDENT REVIEW / NOT A PIN

**Date:** 2026-08-23

**Scientific result awarded:** none
**Authority created:** none

---

## 0. Audit decision

The pair-history mathematics is sufficiently reconstructed to enter the
research incubator as a zero-gain comparator and an exact
diagonal-noncomposition candidate. It is not a native ISP generator and it
does not make the C1 contest ready for official freeze.

The scientific status is:

    C1-A FINITE EXAMPLE:             EXACT AUTHOR-SIDE / REVIEW PENDING
    PAIR-HISTORY COMPILER:           STANDARD QUANTUM REFORMULATION
    HILBERT RECONSTRUCTION:          PRIMARY-SOURCE SUPPORTED
    STRONG-POSITIVITY COMPOSITION:   PRIMARY-SOURCE SUPPORTED WITH CAVEATS
    D-OVER-GAMMA BRIDGE:             NEW CANDIDATE INFERENCE / NOT SOURCE FACT
    ONE ACTUAL FINE HISTORY:         NOT SUPPLIED BY D ALONE
    NATIVE POSITIVE GENERATOR:       ABSENT
    OFFICIAL FREEZE READINESS:       NO

---

## 1. Exact source receipts

The retrieved PDFs used for this author-side audit are:

| ID | Source | Version | Retrieved PDF SHA-256 |
|---|---|---|---|
| S1 | Rafael D. Sorkin, “Quantum Measure Theory and its Interpretation” | arXiv:gr-qc/9507057v2 | ad832414edd26f0d74f090f7a2a200a648d889de4478a0f851dac6aee125ab30 |
| S2 | Stan Gudder, “Hilbert Space Representations of Decoherence Functionals and Quantum Measures” | arXiv:1011.1694v1 | a53fa48a99bf17c6d4e369d284957541353302f31b41e864ac2c5b3d941b0cf0 |
| S3 | Fay Dowker, Steven Johnston, and Rafael D. Sorkin, “Hilbert Spaces from Path Integrals” | arXiv:1002.0589v2 | 9c896c1e707816a975ce31e226557c8a94412d37375be760415a8d44b60f98c3 |
| S4 | Paul Boes and Miguel Navascués, “Composing Decoherence Functionals” | arXiv:1609.09723v3 | 148cdbd14307803a1264c649d51bfd0cca8f792fa8a5cb6e0c42c4d125f1e736 |
| S5 | Fay Dowker and Henry Wilkes, “An argument for strong positivity of the decoherence functional in the path integral approach to the foundations of quantum theory” | arXiv:2011.06120v2 | 84995c515874c00a3db98b596cf63b27ae7e207be21dedf76106a18e53e9fcef |

Canonical source pages:

1. <https://arxiv.org/abs/gr-qc/9507057>
2. <https://arxiv.org/abs/1011.1694>
3. <https://arxiv.org/abs/1002.0589>
4. <https://arxiv.org/abs/1609.09723>
5. <https://arxiv.org/abs/2011.06120>

The hashes identify the downloaded evidence used here. The source PDFs are not
new ISP artifacts and are not assigned programme authority.

---

## 2. Claim-by-source reconstruction

### 2.1 One-history interpretation

S1 proposes a realistic spacetime reading in which reality is one history and
the quantum measure supplies a generalized propensity. Zero-measure events
enter through preclusion.

S1 also explicitly identifies unfinished interpretive tasks, including
conditional preclusion and background-free localization of regions. It does
not justify the stronger claim that a strongly positive decoherence functional
by itself samples one fine history.

**Permitted use:** historical and conceptual support for treating one-history
actuality as a possible additional interpretation.

**Forbidden promotion:** “strong positivity implies a unique actual-history
rule.”

### 2.2 Hilbert representation

S2 proves that a decoherence functional has a spanning vector-valued-measure
representation on a complex Hilbert space. In the finite case the spanning
representation is unique up to isomorphism. It also relates strong positivity
of a quantum measure to Hilbert-space representability.

S3 constructs a history Hilbert space directly from the decoherence
functional and, for the printed standard nonrelativistic quantum-mechanical
cases, relates it naturally to the standard Hilbert space.

**Permitted use:** a strongly positive pair-history law contains Hilbert
structure representationally.

**Forbidden promotion:** “therefore the Hilbert vector is ontic,” or
“history language removes quantum structure.”

### 2.3 Tensor composition and strong positivity

S4 proves, in its finite decoherence-functional setting and under its product
composition rule, that:

1. strongly positive systems compose;
2. weakly positive systems need not compose;
3. the strongly positive set cannot be enlarged while remaining closed under
   the stated composition; and
4. a closed set containing all standard quantum decoherence functionals can
   contain only strongly positive members.

S5 extends the composition analysis to its broader landscape. Its exact
uniqueness theorem is not “tensor closure alone selects strong positivity.”
The load-bearing statement is that the strongly positive class is the unique
class in the printed complex landscape that is both tensor closed and Galois
self-dual. The paper also exhibits a positive-entry tensor-closed class before
the maximality/self-duality condition and notes that the real-only landscape
changes the uniqueness conclusion.

**Permitted use:** product composition supplies nontrivial framework evidence
for strong positivity.

**Forbidden promotion:** “composition derives the actual decoherence
functional,” “strong positivity is the only conceivable positivity
principle,” or “the theorem is independent of the product rule.”

---

## 3. Independent rebuild of Proposition C1-A

On the atomic two-history space define

$$
D_\pm=
\begin{pmatrix}
\frac12&\pm\frac{i}{4}\\
\mp\frac{i}{4}&\frac12
\end{pmatrix}.
$$

Both matrices have trace $1$, determinant $3/16$, and eigenvalues
$3/4,1/4$. Their total entry sum is one. Hence both are normalized and
strongly positive.

For the four events of the two-point algebra,

$$
\mu_\pm(\varnothing)=0,\qquad
\mu_\pm(\{0\})=\mu_\pm(\{1\})=\frac12,\qquad
\mu_\pm(\Omega)=1.
$$

Thus their complete diagonal event functions agree and are ordinary additive.

Fix $E=D_+$ and

$$
F=\{(0,0),(1,1)\}.
$$

Under the standard tensor rule,

$$
\mu_{D_+\otimes E}(F)=\frac38,
\qquad
\mu_{D_-\otimes E}(F)=\frac58.
$$

This proves only:

> the isolated diagonal event function does not determine the composed
> diagonal event function under the fixed product rule.

It does not prove that the product rule is forced, that imaginary orientation
is absolute, or that every positive-history theory lacks composition.

### Relative-gauge check

$D_-$ is the complex conjugate of $D_+$. A simultaneous conjugation of every
system and apparatus may be representational. The example fixes $E=D_+$ and
therefore detects relative conjugation. Any review must preserve this
qualification.

---

## 4. Pair-history compiler audit

For a finite circuit with a reversible dilation, the atomic definition

$$
D_p(h,h')
=\sum_s\omega(s)A_p(h\mid s)\overline{A_p(h'\mid s)}
\delta_{f(h),f(h')}
$$

is a Gram kernel. Strong positivity follows directly. Summing over all paths
with a common final label reconstructs the usual amplitude sum, and unitarity
normalizes the result.

Orthogonal final record sectors decohere, so their diagonal values form an
ordinary probability distribution. Unrecorded internal alternatives need not
decohere and cannot generally be restarted from their individual diagonals.

This is an exact finite-circuit construction. It is not a derivation of
quantum dynamics because the circuit matrices, dilation, tensor rule, source
state, and Born-compatible pairing have already been supplied.

---

## 5. Adaptive Clifford-plus-$T$ checks

The C1 pre-pin held-out values were rebuilt directly.

### 5.1 Sign-sensitive continuation

For $T$ followed by $S^\dagger H$ on $|+\rangle$,

$$
p_0=\frac{2+\sqrt2}{4}.
$$

Replacing $T$ by $T^\dagger$ gives

$$
p_0=\frac{2-\sqrt2}{4}.
$$

### 5.2 Magic-state injection

With

$$
|A\rangle=T|+\rangle,
$$

CNOT from data to ancilla followed by ancilla $Z$ measurement gives:

1. outcome $m=0$: $T|\psi\rangle$;
2. outcome $m=1$: $T^\dagger|\psi\rangle$ up to global phase; and
3. correction $S^m$: $T|\psi\rangle$ in both branches.

Each outcome has probability $1/2$ for every normalized input.

### 5.3 GHZ parity

After applying $T^{\otimes n}$ to $\mathrm{GHZ}_n$, the relative phase is
$e^{in\pi/4}$, so the $X$-parity expectation is $\cos(n\pi/4)$ and

$$
p_{\rm even}(n)=\frac{1+\cos(n\pi/4)}2.
$$

These identities verify the comparator targets. They do not establish a
resource lower bound; the eight-value phase cycle has compact classical
descriptions.

---

## 6. Relationship to Barandes

The preserved Barandes source audit supports:

1. ordinary stochastic laws as native dynamical objects;
2. carrier-relative division and indivisibility;
3. nonunique Hilbert or potential representations; and
4. complete parent laws that need not be generated by multiplying subsystem
   transition matrices.

The audited sources do not identify the native law with a decoherence
functional, do not derive division from decoherence of a history event
algebra, and do not print a universal generator for arbitrary interacting
parents.

Therefore

$$
D\longrightarrow\Gamma_{\rm record}
$$

is a v17 synthesis candidate, not a statement of Barandes' published
ontology. It may illuminate why a record-level $\Gamma$ does not compose, but
it currently makes $D$ the richer nomological input and so does not yet
deliver an ordinary-positive native explanation.

---

## 7. Actuality audit

Three notions must remain separate:

1. positivity of $\mu(A)=D(A,A)$;
2. ordinary probability on a decoherent record algebra; and
3. a law selecting one actual fine history.

The first does not imply the third. The second supplies ordinary laboratory
records only after a licensed decoherent partition is identified. A fine
history ontology requires an additional preclusion, coevent, collapse,
boundary, or other actualization principle.

The present candidate selects none.

---

## 8. Gravity and covariance audit

Histories language is compatible with covariant, all-at-once formulations and
does not require that a Hamiltonian time slicing be fundamental. This is a
real architectural advantage for a future gravity programme.

It is not yet a gravity result. The present package lacks:

1. the physical history space of geometries and matter;
2. diffeomorphism gauge and observables;
3. a well-defined measure or decoherence functional over those histories;
4. Lorentzian causal orientation;
5. an internal clock or scale;
6. a semiclassical Einstein limit;
7. reciprocal matter backreaction; and
8. an empirical quantum-gravity discriminator.

No discrete substrate, lattice, causal set, continuum, or dimension is
selected here.

---

## 9. Explanatory accounting

The pair-history compiler changes the representation of standard quantum
theory and reveals which data the diagonal record law omits. It does not
reduce the independent input list.

Its present score is:

| Coordinate | Status |
|---|---|
| complete finite-process adequacy | pass by construction |
| ordinary final-record probabilities | pass |
| composition data exposed | pass |
| quantum process data derived | no |
| actualization derived | no |
| ontology selected | no |
| empirical prediction | none |
| internal time | none |
| gravity | none |

The exact C1-A example may still be scientifically useful as a compact
noncomposition theorem. The compiler is a zero-gain control.

---

## 10. Readiness blockers

Before an official U-Gen C1 freeze can be recommended, at least one of the
following must exist:

1. one concrete native generator satisfying the entry contract; or
2. one bounded, representation-invariant class theorem whose admitted class
   is narrow enough to review and broad enough to matter physically.

The present packet has neither. The appropriate status is therefore
**author-side prepared but scientifically unentered**, not “inconclusive
result” and not “failed theory.”

---

## 11. Maximum permitted statements

If independently verified later:

1. C1-A may establish diagonal noncomposition at its exact finite product
   scope.
2. The compiler may establish exact equivalence between a strongly positive
   pair-history representation and the supplied finite quantum process.
3. The source theorems may support strong positivity as a
   composition-compatible framework condition.

They cannot establish:

1. a native ISP law;
2. complex amplitudes as matter;
3. one actual fine history;
4. universal Barandes completion;
5. QFT or relativistic locality;
6. spacetime or gravity; or
7. a full theory of reality.
