# Independent hostile review of OVG — operator, representation, and instrument seat

Date: 2026-08-18  
Seat: O — operator algebra, instruments, and representation  
Target: v16 Paper 5, `Overlap Gram/instrument varieties, coherent ports, and arity`  
Verdict: **ACCEPT-WITH-FIXES**

## 1. Immutable-target and hash audit

I audited the immutable candidate at
`bb0f13aedadc354068ea2bcc08478bcd8c43ded1` and the verification at
`22da1143cfdea19cea4a29f2b942677a02c0c110`.  I read the full runbook,
frozen pin, generic-core freeze, physical-fixture/refusal/repair freeze,
generic core, data-only fixture, repaired scorer, transcript, receipt,
generated Paper 5, candidate verification, and the antecedent objects named
by the pin.  I did not read or consult another OVG review.

The frozen hashes reproduce byte-for-byte:

| object | protocol SHA-256 | observed |
|---|---|---|
| pin | `286e681a05b7346226f4f3f381036b2b6bc07d809c93c2ac352d9f71a0f44c40` | equal |
| generic core | `7b17a138dc45f564a5180fca81bdb4620aaa570514d090d8a5c45f0f22d985bf` | equal |
| physical fixture | `7b7658492a49c77f6c9ee3e0a2031d5121c627aad5ae6630e21940a68c92b133` | equal |
| repaired scorer | `75cc0e7279ee93a60bfa520eecb4ea37fcde49b3d9e9f7298d98031396628844` | equal |
| refusal/repair freeze | `d44fd66678fe16ce85c2c9780142583a111776108b87788b734833419c9a3b34` | equal |
| transcript | `48cf0fdecc43b1d148c97bac936a879cbbcf14daddfccd6e597014017155fe7f` | equal |
| receipt | `4ba954430acd0772da62c8df16b2c6b08bca9e76fd7b25d3b5b72fcc43ce2852` | equal |
| Paper 5 | `89a6ad8b10b97351d71a499ebbb36b2cf5a89f32d5ec9d005f9b4a68dab16b31` | equal |
| candidate verification | `12774e1a2d9d72d147a67e066679bc6e376e29f4acecc453f3d164ce19ba37e5` | equal |

The chronology is genuine.  The generic core predates the physical fixture;
the fixture/scorer freeze predates all result paths; the first invocation
refused without artifacts because a frozen prose token crossed a Markdown
line; and the only repaired source operation normalizes whitespace for anchor
comparison.  Hash checking, fixture bytes, equations, gates, classifiers,
mutants, and renderers did not change.

I extracted the exact candidate runtime set with `git archive` into
`/private/tmp/ovg_operator_replay`, which contains no `.git`, and ran it from
`/private/tmp`.  It regenerated transcript, receipt, and paper at the three
hashes above.  The 32 gate rows reconcile, all 12 claims occur once, every
payload seal recomputes, and the mutation-name and expected-gate sets are
equal.  I independently invoked all 30 frozen mutants.  Each changed its
registered measured field, exited `1` at the bound gate, emitted no traceback,
and wrote zero artifacts.

The exactness audit is also clean for the registered paths.  The core and
scorer ASTs contain no float literals, the fixture contains no float, and all
Gaussian-rational construction paths used here coerce through `Fraction`.

## 2. Independent method and tools

I did not import the candidate core or scorer for the mathematical
reconstruction.  I wrote a separate standard-library exact implementation at
`/private/tmp/ovg_operator_independent.py`, using my own Gaussian-rational and
matrix routines.  It constructs the permutation operators from bit actions,
computes adjoints and class-map residuals directly, row-reduces the real
operator constraints over `Fraction`, and compares channels on a complete
matrix-unit basis.

I separately proved the general identities on paper rather than extrapolating
from the bounded `Q(i)` coefficient census.  The replay and mutation runs
authenticate the delivery; the independent implementation and proofs audit
the inference.

## 3. Exact recomputation table

| object | candidate value | independent value | status |
|---|---:|---:|---|
| `A^dagger B` for the two CNOT orders | `CNOT(A->C)` | exact same 8-by-8 permutation | PASS |
| relative operator scalar? | no | no; spectrum `+1` (6), `-1` (2) | PASS |
| `(3/5,4/5)` single-port residual | nonzero | `(24/25) CNOT(A->C)` | PASS |
| nonzero entries in that residual | 8 | 8 | PASS |
| `(3/5,4i/5)` residual | zero | zero matrix | PASS |
| parity-port residual | zero | zero for arbitrary common-boundary isometries | PASS |
| phase ranks, five rows | `[1,1,2,2,3]` | `[1,1,2,2,3]` | PASS |
| phase nullities | `[2,2,1,1,0]` | `[2,2,1,1,0]` | PASS |
| nonnormal overlap | `[[0,3/5],[0,0]]` | exact same | PASS |
| nonnormal constraint rank/nullity | `3/0` | `3/0` | PASS |
| nonnormal parity ports | complete | complete | PASS |
| Pauli-triad embedded law | `p^2+q^2=1` | exact operator identity | PASS |
| registered triad rows/screens | `3/2` | three rows, two distinct parameter points and screens | PASS with wording note |
| real/imaginary two-port channels | equal | equal on all four matrix units | PASS |
| calibrated first-port maps | different | different on a matrix-unit witness | PASS |
| dark-now/future-reactivated | zero/nonzero | `0`, then `diag(0,2)` | PASS |
| CNOT order factorization words | `5,5` through length 4 | same; each includes a length-2 word | PASS |
| Toffoli CNOT-only obstruction | nonlinear witness `(2,4)` | exact `F_2` nonlinearity | PASS |
| spectator marginal | `I/2 -> I/2` | same | PASS |
| amplifier marginal | `2I` | same | PASS |
| extra unregistered three-port split | not run | complete for all inputs | NEW CONTROL |

The five phase certificates are adequate at these finite rows.  Each relative
operator is unitary; its declared distinct phases annihilate it; and the trace
moments through dimension minus one fix the multiplicities by the Vandermonde
system.  The certificate is not merely a numerical eigenvalue count.

## 4. Theorem and proof audit

### 4.1 General two-history instrument equation

For `K_j=a_j A+b_j B`, with common-boundary isometries `A,B` and
`Omega=A^dagger B`, direct expansion gives

$$
\sum_jK_j^\dagger K_j
=S I+C\Omega+\overline C\Omega^\dagger,
$$

where

$$
S=\sum_j(|a_j|^2+|b_j|^2),\qquad
C=\sum_j\overline{a_j}b_j.
$$

The candidate's formula is exact.  It is an operator identity and therefore
normalizes every input, not just the displayed preparation.

For one port, put `z=conjugate(a)b` and
`c=1-|a|^2-|b|^2`.  If `Omega` is unitary, diagonalization reduces the full
operator equation to

$$
2\operatorname{Re}(z e^{i\phi_k})=c
$$

for every distinct eigenphase.  In coordinates `(Re z, Im z, c)`, one phase
gives one independent row, two distinct phases give two independent rows,
and three distinct phase points force rank three because a line intersects
the unit circle in at most two points.  Hence the nullities `2,1,0` are a
theorem over `C`, not an inference from the bounded `Q(i)` scan.

The coefficient-lifting step also works, but should be stated explicitly.  A
nonzero formal solution has `z != 0`.  Scale it by a sufficiently small real
`t`.  Required squared magnitudes `x=|a|^2,y=|b|^2` are roots of

$$
X^2-(1-tc)X+t^2|z|^2=0.
$$

For sufficiently small nonzero `t`, the sum is positive and the discriminant
is positive, so both roots are positive; their phases can realize
`conjugate(a)b=tz`.  Thus formal directions lift to actual nonzero complex
coefficients.  They need not lift inside `Q(i)`, and the paper correctly
separates the complex theorem from its finite rational witnesses.

For exactly two distinct phases,

$$
\arg z=-\frac{\phi_1+\phi_2}{2}\pmod\pi.
$$

The sign and modulo convention are correct.  This constrains the phase of the
product `conjugate(a)b` relative to the phase frame of `Omega`; it does not
select either magnitude.

Scalar `Omega=e^{i phi}I` is a degeneracy, not a counterexample: for square
unitaries it implies `B=e^{i phi}A`, so the two maps are projectively one
operator history.  Distinct configuration-event names require an additional
record/event-algebra calibration, exactly as the paper cautions.

### 4.2 Parity ports and larger port families

For any two common-boundary isometries,

$$
K_+=(A+B)/2,\qquad K_-=(A-B)/2
$$

satisfy

$$
K_+^\dagger K_++K_-^\dagger K_-
=\tfrac12(A^\dagger A+B^\dagger B)=I.
$$

This is a universal mathematical existence theorem at the stated isometry
scope.  It does not survive arbitrary contractions: `A=I,B=0`, for example,
gives total effect `I/2`.  Additional ports or another completion may repair
such cases, so the candidate's strata are not a classifier for non-isometric
history families.

My unregistered control splits the `+` parity port into two proportional
record outcomes with factors `3/5` and `4/5`, leaving the `-` port unchanged.
The resulting three-port family is still exactly complete.  Thus parity ports
are one factorization, never a selected or exhaustive port law.

### 4.3 Nonnormal and three-history rows

For the dimension-changing pair,

$$
\Omega=\begin{pmatrix}0&3/5\\0&0\end{pmatrix}.
$$

The equation `z Omega+conjugate(z) Omega^dagger=cI` forces `c=0` from the
diagonal and `z=0` from the off-diagonal.  Its real rank is three and nullity
zero.  No spectral shortcut was used; the candidate handles this correctly.

For `(I,X,Z)`, the displayed ports obey

$$
\frac{p^2}{4}(I+X)^\dagger(I+X)
+\frac{p^2}{4}(I-X)^\dagger(I-X)+q^2Z^\dagger Z
=(p^2+q^2)I.
$$

This constructs a positive-dimensional embedded subvariety.  The machine's
three registered rows contain a repeated `(3/5,4/5)` ratio, so they are only
two distinct rational parameter points.  That does not harm the analytic
circle or the law-nonselection witness, but “three rows” must not be read as
three distinct solutions.

The general Gram formula does specify the full **implicit** coefficient
variety at each supplied finite history family: the coefficient of each
monomial `conjugate(c_jh)c_jk` is exactly `G_hk`.  It does not compute
irreducible components, dimensions, singular strata, or physical moduli after
representation quotient.  Therefore the primary word “constructed” is
defensible only in the paper's own explicit sense “implicit equations
constructed,” not “variety classified or solved.”

## 5. Representation and ontology audit

### 5.1 History phases and port unravellings

An independent history rephasing

$$
A\mapsto e^{i\alpha}A,\quad B\mapsto e^{i\beta}B,
$$

combined with inverse coefficient rephasing leaves every `K_j` unchanged.
It sends

$$
\Omega\mapsto e^{i(\beta-\alpha)}\Omega,qquad
z\mapsto e^{i(\alpha-\beta)}z,
$$

so the invariant is `z Omega`, not the absolute phase of either factor.  The
two-phase theorem is gauge-covariant.  `SINGLE-PORT-PHASE-CONSTRAINED` must
never be paraphrased as an absolute weight phase or exchange-statistics rule.

More generally, if `C` is the port-by-history coefficient matrix, unconditioned
completeness and the channel depend on a left port-unitary only through
`C^dagger C`.  Such a rotation is Kraus/unravelling gauge after ports are
forgotten.  With a calibrated record algebra, its individual branch CP maps
are observable and it is a different instrument unless the calibration is
transported as well.

The real and imaginary port families demonstrate precisely this distinction:
their unconditioned channels agree on a full matrix-unit basis, but their
first branch superoperators differ.  The candidate has not implemented a
physical record calibration, so “operationally different” is conditional on
the declared port labels being record-individuated.  Independent
law-nonselection is nevertheless already witnessed by the Pauli-triad family,
whose calibrated screens and unconditioned maps move with `(p,q)`.

### 5.2 CP, affinity, ancillas, and no-signalling

Each port map `rho -> K_j rho K_j^dagger` is completely positive and affine.
The operator identity `sum_j K_j^dagger K_j=I` makes the unconditioned map
trace preserving, including after tensoring with an arbitrary ancilla.  It
therefore implies, for every bipartite input on a fixed factorization,

$$
\operatorname{Tr}_A[(\Phi_A\otimes I_B)(\rho_{AB})]
=\operatorname{Tr}_A\rho_{AB}.
$$

The candidate's one Bell-like spectator state is a correct regression and its
amplifier is a correct negative control; the more general fixed-factor
unconditioned theorem follows from completeness.  This says nothing about
outcome-conditioned steering, remote selection of a decomposition, a changing
definition of Bob, or a carrier-rewrite factorization.  Those remain open.

### 5.3 What is and is not relationally typed

The CNOT histories are exact fixed-carrier circuit maps with actor-support
labels.  The token rewrite critical pairs are a separate fixture.  No bundle
map identifies a CNOT history with one of those graph rewrites, and no output
relation changes the later operator probe.  Equal matrix dimensions supply a
common operator codomain; they do not derive a relational common future.

Accordingly, OVG constructs an overlap **operator/instrument** problem for
declared event-labelled histories.  It does not yet construct coherent
backreacting relational geometry.  The canonical flag dilation is likewise a
mathematical Stinespring isometry.  Assigning its factor to actor `B` is
catalogue metadata, not a local implementation or durable record.  The frozen
finding already contains this refusal and should retain it verbatim.

## 6. Counterexamples and unrun controls

1. **Three-port refinement (new exact control).** Splitting one parity port
   into two proportional ports gives a complete three-port instrument.  Port
   count and factorization are not selected.
2. **Non-isometric boundary (scope counterexample).** `A=I,B=0` makes the
   advertised parity pair total to `I/2`, so the universal parity theorem must
   retain “common-boundary isometries.”
3. **History-phase gauge (representation control).** Covariantly rephasing a
   history and its coefficients changes the displayed `Omega` and coefficient
   phases but no class map or observable.  Only `z Omega` and calibrated loop
   data are physical.
4. **Port-unitary control.** A unitary rotation of unobserved ports changes the
   Kraus list while preserving the channel.  It becomes physical only when a
   fixed record algebra calibrates the ports.
5. **Relational-weld control still unrun.** Couple the two CNOT orders to
   genuinely different relational rewrites, transport both to a law-generated
   common future, and require the same Gram completeness there.  Without this,
   “typed relational overlap” is a declaration rather than a joint successor.

None refutes the exact spectral theorem.  They locate its representation and
typing boundaries.

## 7. Consequence and scope reclassification

| statement | reviewer classification |
|---|---|
| finite Gram coefficient equations | theorem/constructed implicitly |
| CNOT complex-weight counterexample | exact finite-fixture fact |
| one/two/three-phase theorem | theorem for two square unitary histories over `C` |
| two-phase weight phase | gauge-covariant relative constraint, magnitudes free |
| parity ports | universal existence for common-boundary isometries |
| Pauli-triad freedom | positive-dimensional embedded subvariety; law unselected |
| real/imaginary ports | same channel, conditionally distinct calibrated instruments |
| local flag | mathematical dilation plus declared catalogue placement only |
| primitive arity | joint support does not imply it; Toffoli obstruction is grammar-relative |
| causal nonseparability | untested |
| fixed-spectator no-signalling | theorem for unconditioned fixed-factor TP maps |
| steering/changing Bob | open |
| relational backreaction | not constructed |
| all-`n`, Hamiltonian, fields, particles, QFT/GR deviation | not established |

Proposed machine-word disposition, in frozen order:

1. preserve `OVG-GRAM-INSTRUMENT-VARIETY-CONSTRUCTED` only with “implicit
   finite-history equations; no component/moduli classification” attached;
2. preserve `SINGLE-PORT-PHASE-CONSTRAINED`, explicitly gauge-relational;
3. preserve `MULTIPORT-COHERENCE-EXISTS-BUT-PORT-LAW-UNSELECTED`, with physical
   port individuation conditional on a record calibration;
4. preserve `LOCAL-FLAG-KINEMATICALLY-PERMITTED-BUT-IMPLEMENTATION-UNSELECTED`;
5. preserve `COMPOSITE-SUPPORT-DOES-NOT-FORCE-PRIMITIVE-ARITY`;
6. preserve `CAUSAL-NONSEPARABILITY-UNTESTED`; and
7. preserve `OVERLAP-LAW-UNSELECTED` at the finite operator fixture.

## 8. Grade

**ACCEPT-WITH-FIXES.**

No exact counterexample to the central operator theorem exists in the tested
scope; I independently proved it.  The refutation of the earlier real-weight
no-go is decisive, parity ports are exactly complete, the nonnormal row is
handled by the full operator equation, and the paper refuses the major causal,
arity, gravity, and QFT promotions.

The fixes are scope and representation fixes, not a mathematical kill.  The
candidate must keep “variety constructed” at implicit-equation grade, stop a
duplicate rational row from reading as a third distinct point, and distinguish
event-labelled fixed-carrier circuits from a relationally welded successor.

## 9. Numbered repairs and kill conditions

1. **Narrow the primary.** Everywhere attach: “the exact implicit Gram
   equations and positive-dimensional witnesses are constructed at finite
   supplied history families; irreducible components and physical moduli are
   not classified.”  Kill the primary if “constructed” is used to mean a
   solved/global variety.
2. **Make phase covariance explicit.** State the simultaneous history and
   coefficient rephasing law and identify `z Omega` as invariant.  Kill any
   exchange-statistics, curvature, Hamiltonian, or absolute-weight-phase
   paraphrase.
3. **Correct the triad count.** Say “three registered rows, two distinct
   rational parameter points and screens,” while retaining the analytic
   positive-dimensional family.
4. **Condition instrument distinctness.** The real/imaginary branch maps are
   physically distinct only after ports are calibrated as record outcomes;
   before that, their common channel admits Kraus rotations.
5. **Preserve the isometry quantifier.** Parity completeness is not a theorem
   for arbitrary contractions or differently typed codomains.
6. **Demote relational wording.** Describe the CNOT result as an exact
   fixed-carrier event-labelled operator overlap.  A graph/operator bundle and
   law-generated common future are required before calling it relational
   backreaction.
7. **Retain every refusal.** Local flag implementation and permanence,
   changing-factor steering, causal nonseparability, arbitrary-`n`
   composition, a selected overlap law, Hamiltonian reconstruction, fields,
   particles, gravity, and QFT/GR deviations remain unproved.

These bounded changes are the smallest repair set.  Any repair that changes
candidate bytes or strengthens a finding before joint adjudication violates
the frozen protocol.

## 10. Report SHA-256

The canonical SHA-256 of this report, computed after replacing the 64
hexadecimal characters on the next line by 64 ASCII zeroes, is:

`b346b88c88dfa4715265c2c7cca05b01665d99bec8d751a1220ab6db30cdae63`
