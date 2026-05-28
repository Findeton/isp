# Minimal Enriched ISP Data For Relativistic QFT Reconstruction

Author: Felix Robles Elvira

V3 Paper 1 draft

Date: 2026-05-17

Status: Hardened theorem-level pass. This paper defines the allowed data
layers for V3 QFT reconstruction, formalizes the enriched datum and forgetful
map, proves conservativity over bare ISP stochastic kernels, states the
minimality/no-go theorem forced by V2 Papers 6, 9, and 10, and adds explicit
admissibility criteria for later V3 imports.

## 1. Purpose

The point of this paper is not to add ordinary Hilbert-space QFT as a hidden
primitive. The point is to say exactly which extra structures must be declared
when bare endpoint stochastic kernels are too coarse to carry phase-sensitive,
local-algebraic, or signed metric information.

The V2 ledger forces this move.

1. V2 Paper 6 shows that Markovized Gamma-only component shadows do not
   reconstruct phase-sensitive quantum behavior. A whole-process kernel can
   recover the correct circuit law, but only if the whole process or the
   relevant division/record structure is declared.
2. V2 Paper 9 shows that the successful free-QFT match is not Gamma-only. It
   uses lift, polarization, CAR, and local-net data.
3. V2 Paper 10 shows that the present Born-squared `Gamma` rule cannot recover
   the full signed inverse spatial metric. It can see diagonal/signless metric
   remnants, but full signed metric data require an enriched principal-symbol
   or Clifford datum.

Thus V3 begins with a strict enriched-data interface:

```text
bare stochastic ISP data
+ declared whole-process/record/instrument data
+ declared representation/local-net/principal-symbol data when needed
-> possible QFT reconstruction theorem.
```

The interface is conservative: forgetting enrichment must return the original
ISP kernel architecture. It may not create hidden Markov divisibility, hidden
field algebras, hidden phases, or hidden geometry.

## 2. Barandes-Aligned Ontological Rule

The primitive object is an indivisible stochastic process: a finite or
projective family of whole-process transition laws between actual
configuration/record events.

The following are allowed only as declared structures.

1. **Division events.** A claim that a process factors through an intermediate
   time, region, or apparatus record is a physical assertion, not a default
   algebraic move.
2. **Whole-process kernels.** A coherent operation is represented by the
   stochastic transition law of the whole operation, not by multiplying
   unrecorded component shadows.
3. **Operational instruments.** A measurement is a family of record-labelled
   stochastic operations. Raw comparison maps are not observables.
4. **Representation lifts.** Hilbert, GNS, CAR, CCR, Clifford, and local-net
   structures are representational enrichments unless explicitly derived from
   operational data.

This is the Barandes-compatible posture: Hilbert-space ingredients are not
ontological beables by default. They are powerful representation data for an
indivisible stochastic process when the stochastic/operational structure
supports them.

### Lift-Class Boundary

Any later theorem using phases above a fixed stochastic kernel must specify
its lift class. In particular, an arbitrary Schur-Hadamard entrywise rephasing
of an amplitude lift preserves the endpoint probabilities
`Gamma=|Theta|^2`, but it does not generally preserve unitarity, circuit
realizability, locality, or physical gauge equivalence. Therefore entropy,
gauge, and reconstruction claims must distinguish:

1. arbitrary `Gamma`-lifts;
2. unistochastic or unitary lifts;
3. circuit-realizable lifts;
4. physical gauge equivalence in a declared representation layer.

Forgetting this distinction turns a representation convention into a hidden
physical claim, so it is forbidden by the enriched-data interface.

## 3. Bare ISP Data

A bare finite/projective ISP datum consists of the following.

### Definition 3.1: projective stochastic kernel datum

Let `A` be a directed set of regulators. For each `a in A`, let `X_a` be a
finite configuration set and let

```math
\Delta(X_a)=\{p:X_a\to[0,1]\mid \sum_xp_x=1\}
```

be the simplex of probability states.

For `b\succeq a`, let

```math
P_{ab}:\Delta(X_b)\to\Delta(X_a)
```

be a column-stochastic projection map, with

```math
P_{aa}=I,\qquad P_{ac}=P_{ab}P_{bc}.
```

For each declared whole operation `O` at regulator `a`, let

```math
\Gamma_a[O]:\Delta(X_a)\to\Delta(X_a)
```

be a column-stochastic endpoint kernel.

The datum is projectively compatible on an operation class `\mathcal O` if

```math
P_{ab}\Gamma_b[O_b]
=
\Gamma_a[O_a]P_{ab}+R_{ab}[O],
```

with exact `R_{ab}=0` or an explicitly controlled residual.

### Definition 3.2: comparison maps and exchange defects

Given a reference operation `O_0` whose kernel is invertible on a declared
tested affine domain, define the algebraic comparison map

```math
J_a[O]:=\Gamma_a[O]\Gamma_a[O_0]^{-1}.
```

For two localized operation families `R,S`, define the exchange defect

```math
E_a[R,S]
:=
J_a[R]J_a[S]J_a[R]^{-1}J_a[S]^{-1},
```

whenever the displayed inverses exist on the tested domain.

These are algebraic relative-dynamics maps. They are not automatically
stochastic kernels, instruments, effects, or observables.

### Definition 3.3: Gamma-equivalence

Two microscopic descriptions `M` and `M'` are Gamma-equivalent on a declared
operation class `\mathcal O` if they induce the same projective stochastic data:

```math
X_a=X'_a,\qquad
P_{ab}=P'_{ab},\qquad
\Gamma_a[O]=\Gamma'_a[O]
```

for all tested `a,b,O`, up to the declared gauge/relabeling convention.

Any reconstruction rule that takes only bare ISP data as input must be constant
on Gamma-equivalence classes.

### Definition 3.4: bare ISP tuple

A **bare ISP datum** is the tuple

```math
\mathfrak D^\Gamma
=
\Bigl(
A,\{X_a\}_{a\in A},
\{P_{ab}\}_{b\succeq a},
\mathcal O,
\{\Gamma_a[O]\}_{a,O},
\mathcal T_\Gamma,
\mathcal G_\Gamma
\Bigr).
```

Here:

1. `A` is the regulator directed set.
2. `X_a` are finite configuration spaces.
3. `P_{ab}` are projective stochastic coarse-grainings.
4. `\mathcal O` is the declared operation class. Its elements are
   whole-process operations unless a division/record structure is explicitly
   supplied elsewhere.
5. `\Gamma_a[O]` are endpoint stochastic kernels.
6. `\mathcal T_\Gamma` is the tested domain ledger: reference kernels,
   invertibility domains, comparison maps, exchange defects, and residual
   estimates actually used in the theorem.
7. `\mathcal G_\Gamma` is the declared gauge/relabeling convention.

All Gamma-level claims must be functions of this tuple alone.

## 4. Enriched ISP Data Layers

An enriched ISP datum is a bare ISP datum plus some explicitly declared layers.
No later V3 theorem may use a layer that is not named in its hypotheses.

### Definition 4.1: enriched ISP tuple

An **enriched ISP datum** is the tuple

```math
\mathfrak D^{\rm enr}
=
\Bigl(
\mathfrak D^\Gamma,
\mathsf W,
\mathsf I,
\mathsf E,
\mathsf H,
\mathsf F,
\mathsf N,
\mathsf S,
\mathsf C,
\mathcal A_{\rm adm}
\Bigr).
```

The entries are typed as follows.

| Symbol | Layer | Meaning |
| --- | --- | --- |
| `\mathfrak D^\Gamma` | M0 | Bare projective stochastic ISP datum. |
| `\mathsf W` | E0 | Whole-process operation and division-event ledger. |
| `\mathsf I` | E1 | Record-labelled instruments. |
| `\mathsf E` | E2 | Operational effect systems. |
| `\mathsf H` | E3 | Hilbert/GNS lift and readout map, if used. |
| `\mathsf F` | E4 | CAR/CCR or other field algebra representation, if used. |
| `\mathsf N` | E5 | Operational or algebraic local net, if used. |
| `\mathsf S` | E6 | Clifford/principal-symbol/metric-sign data, if used. |
| `\mathsf C` | E7 | Covariance representation or asymptotic covariance data, if used. |
| `\mathcal A_{\rm adm}` | audit | Admissibility certificates for every nonempty enrichment layer. |

Any layer may be empty. A theorem is Gamma-level only when all entries beyond
`\mathfrak D^\Gamma` are unused in its hypotheses and proof.

The **forgetful map**

```math
F_\Gamma:\mathfrak D^{\rm enr}\longmapsto\mathfrak D^\Gamma
```

discards every non-Gamma layer. It is part of the definition that
`F_\Gamma` does not add operations, records, local regions, field generators,
or factorization claims.

### Layer E0: whole-process operation family

The operation class `\mathcal O` must specify which operations are indivisible
whole processes and which, if any, have declared division events.

For a coherent circuit, the allowed primitive is

```math
\Gamma_a[O_{\rm whole}],
```

not an undeclared product of component shadows.

### Layer E1: record and instrument structure

An instrument for operation `O` is a finite family

```math
\{\mathcal I_a^r[O]\}_{r\in\mathcal R_O}
```

of positive maps such that

```math
\sum_{r\in\mathcal R_O}\mathcal I_a^r[O]=\Gamma_a[O].
```

The label `r` is a physical record. If a claimed intermediate record is not in
`\mathcal R_O`, the process is not divisible through that record.

### Layer E2: operational effect system

For each tested region or apparatus context `C`, an effect system is a convex
set

```math
\mathsf E_a(C)\subseteq [0,1]^{X_a}
```

closed under the declared coarse-grainings. This layer is needed when a theorem
speaks about measurements, local observables, or empirical probabilities beyond
raw endpoint transitions.

### Layer E3: Hilbert or GNS lift

A Hilbert/GNS lift is a tuple

```math
(\mathcal H_a,\rho_a,\{U_a[O]\}_{O\in\mathcal O},Q_a)
```

where `Q_a` is the declared probability readout and

```math
\Gamma_a[O]_{xy}=Q_a(U_a[O];x,y)
```

for the tested operations. In the usual Born-squared case,

```math
Q_a(U;x,y)=|U_{xy}|^2.
```

The lift is not determined by one endpoint kernel unless a theorem proves
uniqueness in the tested class.

### Layer E4: CAR/CCR field representation

A QFT reconstruction theorem may add a field algebra layer, such as a CAR or
CCR algebra `\mathfrak A_a`, a state `\omega_a`, and local generators
`\psi_a(f)`, but this must be declared as enriched representation data.

For CAR:

```math
\{\psi_a(f),\psi_a(g)^*\}=\langle f,g\rangle_a I,\qquad
\{\psi_a(f),\psi_a(g)\}=0.
```

### Layer E5: local net

A local-net layer assigns to each finite region or continuum test region `O`
an effect system or algebra:

```math
O\mapsto\mathsf E_a(O)
\quad\hbox{or}\quad
O\mapsto\mathfrak A_a(O),
```

with declared isotony, locality, covariance, and projective refinement
properties. This layer is not inferred from bare transition matrices alone.

### Layer E6: Clifford/principal-symbol data

For metric-sensitive relativistic QFT, a principal-symbol layer may specify
matrices or operators `\gamma^i(x)` satisfying

```math
{1\over2}\{\gamma^i(x),\gamma^j(x)\}=h^{ij}(x)I.
```

This recovers signed metric coefficients, including off-diagonal signs, but it
is enriched metric data. It is not Gamma-level metric reconstruction.

### Layer E7: covariance representation

A Lorentz/Poincare covariance layer specifies a representation or asymptotic
representation `U(g)` acting on the enriched local-net or field data, with a
declared relation to projective finite kernels.

Finite-regulator exact covariance is not assumed unless proved.

## 5. Forced-Enrichment Ledger From V2

The following ledger is now a theorem-level constraint on V3.

| Source | Obstruction | Enrichment forced |
| --- | --- | --- |
| V2 Paper 6 | Markovized Gamma-only component shadows lose phase-sensitive coherent composition. | Whole-process kernels, declared division/record events, or coherent lift data. |
| V2 Paper 6 | Finite local-net reconstruction is not determined by endpoint kernels alone. | Operational effect systems, instruments, preparation/effect frames, residual bounds. |
| V2 Papers 7-9 | Free Dirac/CAR QFT matching uses lift, polarization, CAR, local net, and sampled boost data. | Hilbert/GNS, CAR, vacuum/polarization, local-net, and covariance layers. |
| V2 Paper 10 | Born-squared `Gamma` is invariant under a sign-flip that reverses signed off-diagonal metric data. | Clifford/principal-symbol or equivalent signed orientation data. |

The positive reading is important: these are not failures of ISP. They are
failure modes of pretending that a single layer, `Gamma`, carries every
structure of QFT. A Barandes-style stochastic theory is allowed to use richer
whole-process and record data. It must simply declare them.

The forced-enrichment map is therefore:

| Target structure | Minimal non-Gamma datum | Why it is minimal |
| --- | --- | --- |
| Phase-sensitive coherent transformations | `\mathsf W` whole-process kernels, or `\mathsf H` coherent lift/readout data | Component endpoint shadows can be phase-blind; the whole operation or a coherent parameterization must be supplied. |
| Measurement records and finite operational local effects | `\mathsf I` instruments and `\mathsf E` effects | A raw stochastic kernel gives endpoint probabilities, not a record-labelled measurement context or local effect system. |
| Free Dirac/CAR QFT matching | `\mathsf H`, `\mathsf F`, `\mathsf N`, and usually `\mathsf C` | The CAR algebra, vacuum/polarization, local net, and covariance action are not functions of one endpoint transition matrix. |
| Signed metric coefficients | `\mathsf S` Clifford/principal-symbol or equivalent signed orientation data | Born-squared `Gamma` can identify signless invariants while losing oriented frame signs. |

This table should be read as a lower-bound table, not a preferred ontology.
For example, if a future theorem reconstructs CAR data operationally from a
richer family of instruments and whole-process kernels, it may replace
`\mathsf F` as an input. But until such a theorem exists, any paper using CAR
has imported a representation-enriched layer.

## 6. Theorem 6.1: Conservativity Of Enrichment

Let

```math
\mathfrak D^{\rm enr}
=
\Bigl(
\mathfrak D^\Gamma,
\mathsf W,\mathsf I,\mathsf E,\mathsf H,
\mathsf F,\mathsf N,\mathsf S,\mathsf C,
\mathcal A_{\rm adm}
\Bigr)
```

be an enriched ISP datum in the sense of Definition 4.1. Let

```math
F_\Gamma(\mathfrak D^{\rm enr})=\mathfrak D^\Gamma
```

be the forgetful map that discards instruments, effects, lifts, field algebras,
local nets, principal symbols, covariance representations, and admissibility
certificates, retaining the bare projective stochastic tuple

```math
\mathfrak D^\Gamma
=
\Bigl(
A,\{X_a\},\{P_{ab}\},\mathcal O,\{\Gamma_a[O]\},
\mathcal T_\Gamma,\mathcal G_\Gamma
\Bigr).
```

Then:

1. `F_\Gamma` preserves all declared whole-process endpoint kernels.
2. `F_\Gamma` preserves projective compatibility residuals for endpoint kernels.
3. If comparison maps and exchange defects are defined from endpoint kernels,
   then `F_\Gamma` preserves their algebraic values wherever the inverses exist.
4. `F_\Gamma` does not create any new division event or Markov factorization.
5. Any theorem whose conclusion is expressible entirely in bare `Gamma`,
   `J`, `E`, and projective residuals remains a bare ISP theorem after
   forgetting enrichment.

### Proof

Items 1 and 2 are immediate from the definition of `F_\Gamma`: the endpoint
kernels, projective maps, and residual ledger `\mathcal T_\Gamma` are retained
unchanged.

For item 3, comparison maps are functions only of retained endpoint kernels:

```math
J_a[O]=\Gamma_a[O]\Gamma_a[O_0]^{-1}.
```

Thus any inverse that exists before forgetting enrichment still has the same
matrix value after forgetting. The same holds for

```math
E_a[R,S]=J_a[R]J_a[S]J_a[R]^{-1}J_a[S]^{-1}.
```

Item 4 is the key Barandes point. `F_\Gamma` discards structure; it does not add
records. A factorization through an intermediate event is present only if that
event was already declared in the enriched instrument/record layer and then
retained as a declared whole-process operation in the bare operation class. No
undetected intermediate slice becomes physical by forgetting data.

Item 5 follows because the theorem's hypotheses and conclusions use only
objects fixed by items 1 through 3.

Therefore enrichment is conservative over the stochastic kernel architecture.
It can add representation power, but it does not rewrite the underlying
indivisible stochastic process into a Markov chain.

## 7. Theorem 7.1: Minimality And No-Go For Gamma-Only QFT Reconstruction

Call a reconstruction rule `R` Gamma-only if it is a function of the bare ISP
datum `\mathfrak D^\Gamma` and is invariant under Gamma-equivalence.

No Gamma-only reconstruction rule can, on the V2 tested classes, reconstruct all
of the following structures:

1. phase-sensitive coherent interferometry;
2. a CAR/local-net free-QFT representation with its vacuum/polarization data;
3. signed off-diagonal metric coefficients for the Born-squared Dirac metric
   benchmark.

Consequently any V3 theorem claiming full relativistic QFT reconstruction must
include at least one non-Gamma enrichment layer among whole-process operation
families, declared records/instruments, Hilbert/GNS lifts, CAR/CCR data,
local-net data, covariance data, or Clifford/principal-symbol data.

### Proof

The proof is by obstruction witnesses.

**Phase witness.** In the two-path/Mach-Zehnder benchmark of V2 Paper 6, the
component stochastic shadows of `H` and `D_\phi` do not determine the output
law of the coherent whole operation `H D_\phi H`. Markovized multiplication of
the component shadows gives a phase-independent `50/50` prediction, while the
whole coherent operation gives

```math
P_\phi(0|0)=\cos^2(\phi/2),
\qquad
P_\phi(1|0)=\sin^2(\phi/2).
```

Thus a Gamma-only component rule cannot reconstruct phase-sensitive coherent
composition. The Barandes-compatible repair is not to multiply hidden
subprocesses, but to supply the whole-process kernel or declared division/record
structure.

**QFT representation witness.** V2 Papers 7-9 match the free massive `1+1D`
Dirac/CAR benchmark only after supplying lift, polarization, CAR, local-net,
and sampled covariance data. Endpoint kernels alone do not determine the CAR
field algebra, the vacuum sector, or the spacetime local net. Therefore a
Gamma-only rule cannot claim the full free-QFT representation proved there.

**Metric witness.** V2 Paper 10 gives an all-order sign-ambiguity no-go for the
present Born-squared rule. A sign-flipped frame produces the same endpoint
`Gamma` data, comparison maps, logarithms, and exchange loops, while the target
off-diagonal metric coefficient `h^{12}` changes sign. Any Gamma-only rule is
constant on these two Gamma-equivalent inputs, so it cannot return the correct
signed metric for both.

The three witnesses are independent. Each blocks a different QFT structure:
coherent phase, local field representation, and signed metric orientation.
Hence full relativistic QFT reconstruction cannot be Gamma-only on the V2
tested classes.

## 8. Concrete Witness Examples

The previous theorem is abstract. The following three witnesses are the
minimal examples later V3 papers should keep in view.

### 8.1 Phase witness: two-path coherent circuit

Let

```math
H={1\over\sqrt2}
\begin{pmatrix}
1&1\\
1&-1
\end{pmatrix},
\qquad
D_\phi=
\begin{pmatrix}
1&0\\
0&e^{i\phi}
\end{pmatrix}.
```

The component Born-squared shadows are

```math
\Gamma(H)
=
{1\over2}
\begin{pmatrix}
1&1\\
1&1
\end{pmatrix},
\qquad
\Gamma(D_\phi)=I,
```

independent of `\phi`. If one falsely composes unrecorded component shadows as
a Markov chain, the output is always `50/50`.

The coherent whole operation is

```math
U_\phi=HD_\phi H,
```

and its whole-process kernel is

```math
\Gamma(U_\phi)
=
\begin{pmatrix}
\cos^2(\phi/2)&\sin^2(\phi/2)\\
\sin^2(\phi/2)&\cos^2(\phi/2)
\end{pmatrix}.
```

Thus the minimal admissible repair is either:

```text
declare Gamma(U_phi) as the whole-process kernel,
```

or supply a coherent representation layer that determines the family
`U_\phi`. What is not allowed is to multiply the phase-blind component shadows
and call the result ISP.

### 8.2 QFT witness: free Dirac/CAR local net

The V2 free-QFT match requires more than endpoint transition probabilities. It
uses a one-particle lift, a positive-energy/polarization choice, a CAR field
algebra, a vacuum state, time evolution, and local-net assignments.

The local CAR relation

```math
\{\psi(f),\psi(g)^*\}=\langle f,g\rangle I
```

and the spacetime local-net assignment

```math
O\mapsto\mathfrak A(O)
```

are not determined by the bare endpoint kernel alone. They are exactly the
kind of enriched representation data that must be declared, reconstructed from
a richer operational family, or explicitly left outside scope.

This witness forces `\mathsf F` and `\mathsf N` for QFT matching claims. It may
also force `\mathsf H` and `\mathsf C` when the theorem speaks about dynamics,
vacuum, spectrum, or Lorentz covariance.

### 8.3 Metric witness: signed off-diagonal ambiguity

In the Paper 10 `2+1D` Dirac benchmark, choose a constant frame `E` and the
sign-flipped frame

```math
\widetilde E_A^{\ 1}=E_A^{\ 1},
\qquad
\widetilde E_A^{\ 2}=-E_A^{\ 2}.
```

The diagonal metric entries are unchanged, but the signed off-diagonal entry
changes sign:

```math
\widetilde h^{11}=h^{11},
\qquad
\widetilde h^{22}=h^{22},
\qquad
\widetilde h^{12}=-h^{12}.
```

For the present Born-squared rule, the two frame choices produce identical
`Gamma`-level data, comparison maps, logarithms, and exchange loops. A
Gamma-only reconstruction rule must therefore return the same `C^{12}` for
both, while the target signed metric requires opposite signs.

The minimal repair is not to rename this Gamma-level recovery. The repair is to
declare signed principal-symbol data, for example

```math
{1\over2}\{\gamma^i,\gamma^j\}=h^{ij}I,
```

or to prove a future operational theorem that reconstructs the same signed
orientation information from admissible records/instruments.

## 9. The Minimal Enriched ISP Data Package

The minimal V3 package is not one fixed Hilbert-space formalism. It is a typed
interface. A theorem imports only the types it needs.

### Package M0: stochastic base

Every V3 theorem starts with:

```text
(X_a, P_ab, Gamma_a[O], operation class O)
```

with whole-process operations declared.

### Package M1: operational records

Needed for measurement, detector, local-effect, and empirical claims:

```text
record labels, instruments I_a^r[O], effect systems E_a(C).
```

### Package M2: coherent representation

Needed for phase-sensitive coherent transformations when whole-process
stochastic kernels are not enough to parameterize the family:

```text
Hilbert/GNS lift, phase/circuit family, readout map Q_a.
```

### Package M3: field/QFT representation

Needed for QFT matching:

```text
CAR/CCR algebra, vacuum or state, local field generators, local net.
```

### Package M4: relativistic geometry/covariance

Needed for Lorentz and metric claims:

```text
covariance representation, Clifford/principal-symbol data, metric coefficient
ledger.
```

A theorem is Gamma-level only if it uses M0 alone. It is operational if it uses
M0 and M1. It is representation-enriched if it uses M2, M3, or M4.

## 10. V3 Import Contract

Every later V3 paper must begin with an import box using the following form.

```text
Gamma-level imports:
- finite/projective stochastic kernels;
- projective maps;
- comparison maps and exchange defects;
- declared whole-process operation class.

Operational imports:
- records/instruments/effects used by the theorem;
- detector or local-net operational assumptions.

Representation-enriched imports:
- Hilbert/GNS lift, if used;
- phase/circuit family, if used;
- CAR/CCR field algebra, if used;
- local net, if used;
- covariance representation, if used;
- Clifford/principal-symbol/metric data, if used.

Forbidden:
- composing undeclared component kernels as if the process were Markov
  divisible;
- calling raw comparison maps observables;
- calling enriched metric recovery Gamma-level metric recovery;
- treating finite-regulator covariance as exact continuum Lorentz covariance
  unless proved.
```

This contract is the main practical output of Paper 1. It tells Papers 2-10
what they are allowed to assume.

## 11. Admissibility Criterion For Enrichment

An enrichment layer is not admissible merely because it is mathematically
convenient. It is admissible only if it passes the following test.

### Definition 11.1: admissible enrichment

Let `\mathsf X` be one of the non-Gamma layers

```math
\mathsf W,\mathsf I,\mathsf E,\mathsf H,\mathsf F,\mathsf N,\mathsf S,
\mathsf C.
```

The layer `\mathsf X` is **admissible for a theorem `T`** if the theorem states
a certificate in `\mathcal A_{\rm adm}` containing:

1. **Typed declaration.** The theorem names the layer and the exact data it
   imports.
2. **Forcing reason.** The theorem identifies whether the layer is needed for
   phase/interference, records/effects, QFT algebra/locality, covariance, or
   signed metric data.
3. **Conservativity.** Forgetting the layer by `F_\Gamma` leaves the bare ISP
   kernels, projective maps, comparison maps, and exchange defects unchanged.
4. **No hidden divisibility.** The layer does not license composition through
   undeclared intermediate kernels or records.
5. **Operational or representational status.** The theorem says whether the
   layer is an operational datum, a representation datum, or a structure
   reconstructed from other declared data.
6. **Non-uniqueness ledger.** If the layer is not uniquely determined by
   `\mathfrak D^\Gamma`, the theorem says so.

If any item fails, the theorem may still be mathematically useful, but it is
not an ISP reconstruction theorem from the declared data. It is a standard QFT
or Hilbert-space theorem with an ISP-style stochastic shadow.

### Proposition 11.2: admissibility blocks hidden QFT imports

Suppose a V3 theorem uses an enriched datum and satisfies Definition 11.1 for
every non-Gamma layer it imports. Then the theorem cannot be misread as a
Gamma-only reconstruction theorem unless all imported non-Gamma layers are
empty or are explicitly reconstructed from Gamma-level data inside the theorem.

Proof. By typed declaration, every non-Gamma object appears in
`\mathcal A_{\rm adm}`. By conservativity, forgetting it returns the bare
stochastic datum. By the non-uniqueness ledger, any missing uniqueness from
bare `Gamma` is visible. Therefore the theorem's input layer is explicit. If a
claim remains after forgetting all non-Gamma layers, it is Gamma-level. If it
does not, it is enriched or operational, not Gamma-only. `square`

The admissibility criterion is deliberately strict. It protects the central
Barandes idea: the stochastic process is primary, and representation tools are
allowed only when their status is clear.

## 12. Barandes Compliance Audit

The paper is Barandes-aligned if it satisfies the following audit.

1. **Whole processes first.** The base datum is a whole-process endpoint law,
   not a chain of hidden intermediate Markov steps.
2. **Division events are physical.** A factorization is allowed only when the
   record/division structure is declared.
3. **Hilbert space is representational.** Hilbert, CAR, Fock, local-net, and
   Clifford data are useful representation layers, not automatic ontology.
4. **Measurement is operational.** Measurements are stochastic instruments with
   records, not collapses of a primitive wavefunction.
5. **No fake Gamma omniscience.** Endpoint probabilities do not by themselves
   determine all phases, local observables, QFT algebras, or signed metric
   coefficients.
6. **Conservative forgetting.** Removing enrichment returns the stochastic ISP
   datum and does not create new subprocesses.

This is also the Einstein-style conceptual discipline of the paper: identify
which quantities are operationally or geometrically meaningful, state which
structures are primitive, and refuse to infer unobserved structure from
notation.

## 13. Current Verdict

V3 Paper 1 establishes the rules of the game for the next sequence.

The honest conclusion is:

```text
Bare Gamma is not enough for full relativistic QFT.
Enrichment is allowed only when typed, declared, and conservative.
The next QFT reconstruction theorem must say exactly which layer supplies each
phase, record, local algebra, covariance, and metric datum.
```

This does not weaken ISP. It makes the ISP reconstruction program precise
enough to be falsifiable. If later papers can reconstruct standard QFT from the
minimal package, the reconstruction is meaningful. If they cannot, the no-go
will say exactly which structure remains external.
