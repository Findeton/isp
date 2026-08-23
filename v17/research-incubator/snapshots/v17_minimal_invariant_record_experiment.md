# PRIVATE EXPERIMENT DESIGN — minimal invariant relational record

Date: 2026-08-23

Status: **EXPOSED DEVELOPMENT DESIGN / NO DATA / NO OFFICIAL UNIT**

This is a deliberately minimal laboratory calibration of the invariant-record
theorem. It is not a microscopic ontology, clock model, spacetime model, or new
quantum law. If used in an official cycle, its complete design and predictions
must enter the contamination ledger as already exposed.

## 1. Physical question

Can a quantum apparatus record an invariant relational bit while preserving
coherence between alternatives that have the same invariant value, even though a
record of one raw coordinate destroys that coherence?

Ordinary quantum mechanics predicts yes. The experiment would validate the
operational construction and its resource accounting, not select an ontology.

## 2. Minimal carrier and symmetry

Use three system qubits with computational labels

$$
(q,a,b)\in\mathbb Z_2^3.
$$

The nontrivial group element $g=1$ acts by

$$
(q,a,b)\longmapsto(q,a\oplus q,b\oplus1).
$$

On qubits this is the unitary

$$
U_g=\operatorname{CNOT}_{q\to a}X_b.
$$

The raw coordinate $a$ is transformed differently in the $q=0$ and $q=1$
sectors. A classical pointer that attempts to transform as a copy of $a$ therefore
meets the center-preservation obstruction when $q$ remains coherent.

The relative sector permutations on the raw $a$ bit generate the transitive
$\mathbb Z_2$ action, so the minimal represented common algebra of that pointer is
$M_2(\mathbb C)$ with scalar center. In the joint raw $(a,b)$ algebra the relative
action flips $a$ and leaves $b$ fixed, giving $M_2(\mathbb C)\otimes\mathcal D_b$.
Thus $a$ becomes quantum memory while $b$ remains a transformable classical
coordinate. The invariant-y instrument creates a new classical output; $y$ is not
silently reclassified as an old central raw variable.

Here this is a registered laboratory symmetry action, not an assertion of
fundamental gauge redundancy. The source below is deliberately asymmetric under
$U_g$ and therefore consumes a calibrated preparation/reference resource. That
resource must be printed. A genuinely gauge-constrained implementation would need
a separately constructed invariant source or relational encoding and may not
silently reuse the same preparation.

Define instead

$$
y=a\oplus qb.
$$

Then

$$
y'=a\oplus q\oplus q(b\oplus1)=a\oplus qb=y,
$$

so $y$ is invariant.

The b qubit is functioning as the physical reference used to relationalize the
raw a coordinate. Thus this is simultaneously an invariant-output construction
and a reference-assisted construction. Those are overlapping physical features,
not rival interpretations. The reference preparation, control, and disturbance
must remain in the resource ledger.

## 3. Coherent source with two invariant fibers

Define

$$
|\phi_0\rangle
=\frac{|000\rangle+|111\rangle}{\sqrt2},
$$

and

$$
|\phi_1\rangle
=\frac{|010\rangle+|101\rangle}{\sqrt2},
$$

where the bit order is $(q,a,b)$. The first state lies wholly in the $y=0$
fiber; the second lies wholly in the $y=1$ fiber. Within each fiber the two terms
have opposite raw $a$ values.

The full calibration source is

$$
|\Psi\rangle
=\frac{|\phi_0\rangle+|\phi_1\rangle}{\sqrt2}.
$$

This source contains both within-fiber and cross-fiber coherence, allowing the two
effects to be tested separately.

It is not invariant under $U_g$. That is acceptable for the operational covariance
test only because the preparation asymmetry is declared as a resource. Add a
twirled-source control and refuse any claim of a gauge-physical state unless the
complete preparation descends through the gauge constraint.

## 4. Invariant-record circuit

Append a record qubit $r$ in $|0\rangle$. Compute

$$
r\leftarrow r\oplus a\oplus qb
$$

using

1. `CNOT(a -> r)`;
2. `TOFFOLI(q,b -> r)`.

This is a global joint instrument on the declared qubit register. A hardware
implementation must print its interaction graph, mediator modes, routing, and
gate decomposition. It is not a local measurement merely because the logical
registers have separate names, and it supplies no emergent locality.

The resulting unitary is

$$
V_y=\sum_{q,a,b}|qab\rangle\langle qab|\otimes X_r^{a\oplus qb}.
$$

Because $y$ is invariant,

$$
[V_y,U_g\otimes I_r]=0.
$$

No intermediate arithmetic bit is exposed. The only pointer value is the
completed invariant.

## 5. Exact registered predictions

### 5.1 Invariant arm

Conditioned on $r=y$, the system state is exactly $|\phi_y\rangle$. Therefore the
within-fiber interference reader

$$
F_y^+=|\phi_y\rangle\langle\phi_y|
$$

has probability one.

If the record is read nonselectively, cross-fiber coherence is removed. The
retained system state is

$$
\rho_y=\frac12|\phi_0\rangle\langle\phi_0|
+\frac12|\phi_1\rangle\langle\phi_1|.
$$

Hence the original-source reader has

$$
\langle\Psi|\rho_y|\Psi\rangle=\frac12.
$$

Thus the record destroys exactly the coherence between distinct recorded values
and preserves exactly the coherence inside each value.

### 5.2 Raw-coordinate arm

Run this arm separately on the preregistered preparations $|\phi_0\rangle$ and
$|\phi_1\rangle$. The value $y$ is therefore preparation provenance, not a
postselected outcome or a second simultaneous record. Copy $a$ to a pointer and
take the complete nonselective output. Within either $y$ fiber, the two
alternatives have opposite $a$. The system state becomes an equal incoherent
mixture and

$$
\Pr(F_y^+\mid \phi_y,\text{raw }a\text{ recorded})=\frac12.
$$

The raw arm therefore pays for which-sector information with loss of the
within-fiber interference that the invariant arm preserves. If a future design
uses $|\Psi\rangle$ and concurrently records $y$, that is a different, enlarged
instrument and must be frozen separately.

### 5.3 Coherent eraser arm

Again prepare $|\phi_y\rangle$ with $y$ carried only as preparation provenance.
Premeasure $a$ into a quantum memory but reverse the exact premeasurement before
any irreversible amplification. In the ideal circuit the memory returns to its
ready state and

$$
\Pr(F_y^+\mid \phi_y,\text{raw premeasurement uncomputed})=1.
$$

This is reversible uncomputation, not destruction of an actual classical fact.

### 5.4 Redundant invariant arm

After computing $y$ into $r$, copy the orthogonal record bit into $m$ disjoint
fragment qubits. A complete nonselective measurement or one inaccessible
orthogonal register yields a broadcast classical record. Every fragment reader
agrees on $y$, while the system retains the exact $|\phi_y\rangle$ coherence
conditional on that value.

### 5.5 Boundary-by-boundary feature product

The same apparatus changes type across its own stages:

| Boundary | I invariant output | C controller classicalized | N quantum memory | R physical reference | Objective broadcast |
|---|---|---|---|---|---|
| prepared source | no output yet | no | no | yes: b is prepared | no |
| coherent $V_y$ premeasurement | invariant interaction | no | yes: r remains coherent | yes | no |
| complete nonselective y instrument | yes | no: q coherence survives within y | retained only inside y blocks | yes | no |
| redundant-fragment boundary | yes | no | no exposed incompatible r reader | yes | yes operationally |

This table is why I/C/N/R must not be treated as exclusive ontologies. A single
physical process can carry different feature values at different complete
boundaries.

## 6. Imperfect-record extension

Replace the orthogonal record states by pure states with overlap $c$. With equal
priors, the exact registered relations are

$$
\mathcal V=|c|,
\qquad
\mathcal D=\sqrt{1-|c|^2},
\qquad
\mathcal D^2+\mathcal V^2=1.
$$

For $m$ conditionally independent fragments, $c\mapsto c^m$. Correlated
fragments, leakage, unequal priors, and mixed pointer states are separate controls
and do not obey this equality automatically.

## 7. Required tomography

The minimal data package must estimate:

1. preparation fidelity for $|\Psi\rangle$, $|\phi_0\rangle$, and
   $|\phi_1\rangle$;
2. process fidelity or a sufficient witness for $U_g$ and $V_y$;
3. invariance error $\|[V_y,U_g\otimes I]\|$ in a frozen operational norm;
4. conditional $F_y^+$ probabilities in invariant, raw, and eraser arms;
5. the cross-fiber $|\Psi\rangle$ reader after invariant recording;
6. fragment agreement and pairwise read disturbance;
7. leakage of $q$ or raw $a$ into the invariant pointer and fragments;
8. drift and crosstalk over calibration and held-out runs.
9. the asymmetric-source resource and a separately analyzed $U_g$-twirled source
   control.

The norm, confidence procedure, calibration split, held-out split, exclusion rules,
and stopping rule must be frozen before data.

## 8. Failure meanings

- Failure of the invariant commutator identifies an apparatus/control error or an
  incorrectly modeled symmetry.
- Loss of within-fiber coherence beyond the preregistered noise model identifies
  leakage or an unmodeled measurement channel.
- Failure of the raw arm to lose coherence identifies an incomplete raw record,
  not a violation of complementarity.
- Fragment disagreement identifies failed broadcast structure.
- Agreement with all quantum predictions validates the operational theorem in the
  registered domain; it does not support a unique ontology.
- A reproducible deviation from the complete quantum instrument predictions would
  be scientifically significant only after independent replication and a frozen
  alternative model.

## 9. Nonclaims

This calibration does not establish:

- that $q,a,b$ are fundamental variables;
- that nature is discrete;
- that $y$ is time;
- that the displayed $\mathbb Z_2$ action is a gauge symmetry of the universe;
- that the invariant is uniquely selected;
- that redundant records produce one actual outcome;
- that a stable record is either an admitted Barandes conditioning division or a
  strong screening boundary under a selected path realizer;
- that circuit order is emergent chronology;
- locality, spacetime, dimension, signature, metric, or gravity;
- a Barandes configuration space or indivisible stochastic law.

It also does not show that the noncentral raw coordinates are unreal. A future
native lift could assign definite configuration values to them while reproducing
the operational interference statistics through one indivisible parent endpoint
law. Such a lift would have to use the same native configuration, endpoint law,
apparatus, reference, and observation map in the invariant, raw, eraser, and
redundant-reader arms; it cannot be inferred from the present Hilbert instrument.
A probability law over unrecorded intermediate configurations would require an
additional selected realizer.

## 10. Present status

```text
DESIGN:                 EXPOSED-PRIVATE
STANDARD-QM-PREDICTION: DERIVED-ANALYTICALLY
HARDWARE-PLATFORM:      UNSELECTED
NOISE-MODEL:            UNFROZEN
DATA:                   NONE
EMPIRICAL-RESULT:       UNTESTED
ONTOLOGY:               UNSELECTED
NATIVE-PROCESS-LIFT:     UNCONSTRUCTED
OFFICIAL-CYCLE:         NOT-AUTHORIZED
```
