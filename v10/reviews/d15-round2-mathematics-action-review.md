# D15 round-2 mathematics/action repair review

**Date:** 2026-07-11  
**Reviewer:** independent mathematics/action/EFT referee  
**Verdict:** **MINOR REVISION**  
**Exact finite dictionary:** **PASS at conditional nongravitational scope**  
**Formal D15 status:** correctly remains `INCOMPLETE-INVESTIGATION`

## Decision

All round-one major defects in the finite matrix-to-D14 construction are
substantially repaired.

- The Hadamard kernel is explicitly a phase plus a supplied vertex measure.
- The CNOT support zeros follow from an exact `Z2` multiplier sum.
- The seal is composed through D14 `Obj`/`Port`/`Mor` objects from environment
  injection, CNOT, explicit record commit and live-collar emission.
- A future system action is admitted by D14 and preserves the record.
- The memory permutation is built inside D15 rather than imported from D13.
- A fixed-dictionary closed experiment distinguishes the base and
  phase-modified kernels by probabilities `1` and `1/2`.
- The EFT note now includes `xi_H H^dagger H R`, operator equivalences,
  curvature power counting, leading matter sectors, neutrino alternatives and
  a materially improved coefficient ledger.

The remaining defects are narrower.  Every D14 port is ownerless, so the
system/environment interaction does not exercise the locality/join admission
required by S6.  The memory cell freezes only two support entries, not the
advertised non-Markov conditionals, and `cnot_four` reimplements the truth
table instead of embedding the already-derived multiplier kernel.  “Bell
record” still names a correlation with no record instrument, and the nongauge
status of the qubit toy is not an explicit quotient/edge-mode ledger.

The EFT ledger closes the normal-form objections at schematic scope, but it is
not a numerical EFT packet: no definite scheme/scale, truncation order,
regulator or sector cutoff is selected.  The primary acknowledges this and
retains `INCOMPLETE-INVESTIGATION`, so it is a remaining protocol task rather
than a contradiction.

## Frozen artifacts and reproduction

```text
78af9ed95a1ab5e27aa5edea2104c8f834688a1a1b3a06c6ef271b35afdb045a  code/d15_regulated_action_dictionary_exact.py
d4ea94c6b727aa9ec7e20cad1304ad019e4711ffc1512d0f90532d75e01b3777  data/d15-regulated-action-dictionary-exact.json
64dd46878392b1d134087ed51f5a9cf2384b48df86c7ab35bdd5d034f2397b17  note-d15-maximal-low-energy-action.md
99be0212ca2e0afb7dd837dfdcc5b8ab3c189d6e9356e306070e876bfdf6f070  note-d15-eft-action-parameter-ledger.md
c307569de38099e6217c869611d7f9c06b4eb3235c38a1ba788ef3f1a021a8e4  note-d15-uv-survivor-audit.md
b882b04f4e9873458e26317a0d8315a582743f60801642e447ca5b81e645cf19  data/d15-regulated-dictionary-pre-review-receipt.md
```

Independent normal and optimized execution produced:

```text
checks                         = 26/26
normal stdout SHA-256          = 89bef6673905ceac8506cd2a6e9624a3265a31e087f7a69ead0f3d8a59152384
optimized stdout SHA-256       = 89bef6673905ceac8506cd2a6e9624a3265a31e087f7a69ead0f3d8a59152384
semantic SHA-256               = f739c75352b8099b85836b4b7c471d131a173491217156e9d3da7d658ca1f1e3
source SHA-256                 = 78af9ed95a1ab5e27aa5edea2104c8f834688a1a1b3a06c6ef271b35afdb045a
packet SHA-256                 = d4ea94c6b727aa9ec7e20cad1304ad019e4711ffc1512d0f90532d75e01b3777
D13 arithmetic dependency      = 1ea9969cb3e61b805e031ea7b3b025e3a1f88b56e268337824c6a6abcba1cf45
D14 bridge dependency          = e0db2c65a7305ca92bf19fcaa0384e0d825b1a04a5590c0ca243e6192bebc425
```

The receipt agrees.  Normal and optimized stdout are byte-identical, and no
Python `assert` supplies a gate.

## Round-one opening disposition

```text
M1  CLOSED       supplied Hadamard measure is explicit; no action-only
                 normalization is claimed.
M2  CLOSED       auxiliary Z2 sums derive both CNOT deltas.
M3  CLOSED FOR S4 CARRIER; PARTIAL FOR S6
                 actual D14 objects are used, but ownership/join provenance
                 is not instantiated.
M4  CLOSED       D14 protection applies; hostile record flip is rejected.
M5  CLOSED AT SCHEMATIC NORMAL-FORM SCOPE
                 xi_H, mixed terms, equivalences and power counting added.
M6  SUBSTANTIALLY CLOSED
                 matter and coefficient classes are now explicit; numerical
                 scheme/scale/truncation remains future work.
M7  PARTIAL      memory is local to D15, but duplicates the truth table and
                 does not freeze the two non-Markov conditionals.
N1  OPEN/MINOR   “Bell record” remains inaccurate.
N2  OPEN/MINOR   the trivial nongauge quotient and absence of edge modes are
                 not explicitly entered in the toy ledger.
```

## 1. Action, measure and support

### Hadamard

The revised check says that a local phase plus supplied vertex measure yields

```math
K_H(b,a)=2^{-1/2}(-1)^{ab}.
```

The two ingredients are visible directly: `(-1)^(ab)` is the phase and
`2^(-1/2)` is supplied measure/normalization.  Unitarity follows exactly.  The
repair no longer claims that `S_H=pi ab` fixes the magnitude.

For future auditability, `S_H` and `mu_H` could be separate packet fields, but
the formula and narrowed wording close the mathematical overclaim.

### CNOT

The revised kernel evaluates

```math
{1\over2}\sum_{\lambda_c=0}^1(-1)^{\lambda_c(b_c\oplus a_c)}
{1\over2}\sum_{\lambda_t=0}^1(-1)^{\lambda_t(b_t\oplus a_t\oplus a_c)}.
```

Each factor is one when its constraint vanishes and zero otherwise, giving

```math
\delta_{b_c,a_c}\delta_{b_t,a_t\oplus a_c}.
```

The exact receipt compares this result with the CNOT permutation.  This closes
the objection that the zeros were merely written into the matrix and called
an action.  The multiplier measure and choice of constraints remain supplied,
as expected for a construction rather than a selector.

## 2. Actual D14 integration

`d14_seal_from_action` constructs

```text
system
  -> system tensor fresh-environment-|0>
  -> CNOT-action(system,environment)
  -> system tensor protected-record
  -> system tensor protected-record tensor live-collar.
```

Every arrow is a D14 `Mor`, and D14 `compose` produces the seal.  Its matrix
equals the direct seal matrix.  Its target contains a sealed record with
persistent `record_id="R"` and a collar.

The later future morphism carries protected correspondence `((1,1),)` and
preserves the record.  My hostile construction of

```math
I_S\otimes X_R\otimes I_C
```

on the same target is rejected with

```text
ValueError: protected record overwrite.
```

The old raw-array overwrite counterexample therefore no longer applies.  The
built-in D15 receipt should freeze this rejection directly, but the hash-locked
D14 constructor already enforces it, so this is not a mathematical blocker.

### Explicit commit remains conditional ontology

`environment-to-protected-record` is an identity matrix between differently
interpreted ports.  It is not derived from the CNOT phase action.  The paper
now calls it an explicit commit and says that the environment/record
interpretation, pointer basis, split and initial state remain supplied.  That
is honest S5 grading.

The finite theorem is therefore

```text
supplied action/measure/support + supplied state/split/commit/collar
  -> admitted D14 protected record cell.
```

It is not autonomous record selection, and the revised primary no longer says
that it is.

## 3. Remaining ownership/join opening

Every port in the D14 chain has `owner=None`.  The CNOT system/environment
interaction consequently passes primitive admission without testing whether
two separate components are entitled to join.

This does not invalidate the matrix or protected record.  It means the witness
closes S4's typed carrier requirement but not S6's owned locality/provenance
requirement.

The repair must choose one ontology:

1. If system and environment belong to one local component, assign every port
   a common owner such as `owner="lab"`.
2. If they begin as distinct components, assign distinct owners and give CNOT
   an explicit join entitlement, while grading its origin as supplied.

Add a negative unentitled-join control.  Do not leave ports ownerless while
describing the cell as an ownership audit.

## 4. Bell, decoherence and memory

The Bell calculations remain exact:

```text
CNOT(H tensor I)|00> = (|00>+|11>)/sqrt(2);
both local marginals = I/2;
same computational-basis probability = 1;
one local-unitary no-signalling marginal.
```

The source still labels the third result “Bell record,” although no D14 record
is created in that subtest.  Rename it “Bell-state same-basis correlation.”
It is not a CHSH or self-testing result.

The environment trace gives exact Z-basis dephasing once the split, state and
interaction are supplied.  The revised primary correctly calls this a
conditional environment-decoherence instance of S5.

### Memory hardening

The memory matrix is now composed locally as

```text
CNOT X->M;
CNOT M->Z.
```

Its support is `0000` and `1101`, each with mass `1/2`.  I independently
computed

```text
P(Z=1 | Y=0,X=1)=1,
P(Z=1 | Y=0,X=0)=0.
```

These are true but not frozen.  The executable checks only two diagonal
entries.  Also, `cnot_four` rewrites the truth table instead of embedding the
already-derived `cnot_action_kernel`; the multiplier action and memory helper
could diverge without a failed check.

Embed the computed four-by-four CNOT on the declared factor pair, compare that
embedding with `cnot_four`, and freeze both conditionals.  This is regression
strengthening, not a counterexample to the current result.

## 5. Fixed-frame action distinction

The repair fixes the external state, final readout and downstream `H`:

```text
base H then H:                  P(out=0)=1;
phase-modified P H then H:      P(out=0)=1/2.
```

This distinguishes the kernels under one shared boundary dictionary.  It is
frame-conditional in the correct sense: co-transforming the neighboring
region from `H` to `H P^dagger` restores probability one.  Hence it does not
prove invariant inequivalence of complete UV actions modulo all boundary
dictionaries.  The revised prose uses it only to show that the finite
dictionary does not select one local action, which it supports.

## 6. EFT normal form and parameter ledger

The new ledger repairs the main mathematical omissions:

- `xi_H H^dagger H R` appears at leading curved-space order;
- mixed matter-curvature operators enter the higher tower;
- operator lists are quotiented by integration by parts, identities, leading
  equations of motion, perturbative field redefinitions and topological
  densities at fixed topology;
- the four-dimensional curvature-squared redundancy is stated;
- gauge, fermion, Higgs, Yukawa and theta sectors are displayed;
- neutrino mass is assigned to the Weinberg operator or extra fields; and
- coefficients are divided into conventions, symmetry-related vertices,
  measured running parameters, bounded Wilson coefficients, state data and
  record/coarse-graining data.

This suffices for the claimed schematic operator normal form.  It does not
make the numerical action unique, and the ledger says so.

The domain is parametrized by

```math
E/\Lambda_{cut}\ll1,
\qquad |R|/\Lambda_{cut}^2\ll1,
```

with an order-`N` omitted-operator estimate.  No particular `N`, regulator,
scheme, reference scale or sector cutoff is frozen.  Before a numerical
empirical verdict, add a concrete packet specifying basis/truncation,
scheme/scale, regulator/matching prescription, numerical domain, coefficient
uncertainties and truncation remainder.

That missing packet is compatible with `INCOMPLETE-INVESTIGATION`; it would be
an overclaim only if the schematic ledger were presented as a precision fit.

## 7. UV survivor scope

The UV audit now includes `EFT4`, `BDQ`, `ASQ`, `SFQ` and `PRIM` and separates
survival from selection.  It explicitly says no two complete UV packets have
been exhibited, so it does not claim `FUNDAMENTAL-NONSELECTION-PROVED`.

The weaker statement that current infrared evidence does not uniquely select
a UV completion is supported.  S10 remains open, and keeping the V9 holdout
closed is the correct S9 decision.

## Gate disposition

```text
S0  PARTIAL       schematic domain/power counting supplied; concrete scheme,
                  regulator, scale and truncation packet absent.
S1  PASS          conditional leading normal-form scope only.
S2  PASS          leading sectors and schematic higher tower.
S3  PASS          parameter-class ledger; concrete fit ledger remains open.
S4  PASS          one finite conditional nongravitational dictionary enters
                  D14; EFT4/gravity dictionary remains formal.
S5  PASS          honest conditional grading; autonomous records not derived.
S6  OPEN/PARTIAL  no owner/join entitlement in the D15 D14 cell; diagram
                  generation and entitlement origin remain unselected.
S7  PASS          assumption/recovery ledger, not emergence.
S8  OPEN          no complete frozen empirical model-selection receipt.
S9  PASS          untouched V9 holdout remains closed.
S10 OPEN          no two complete matched UV packets; no no-go claimed.
S11 OPEN          hostile closure is not complete.
```

## Required round-three hardenings

1. Assign explicit owners to the D14 packet and add the corresponding
   same-component or join-entitlement control.
2. Freeze D15 record-flip rejection directly.
3. Embed the derived CNOT kernel in the memory circuit and freeze both
   non-Markov conditionals.
4. Rename “Bell record” to “Bell-state same-basis correlation.”
5. State that the finite toy has identity gauge quotient, unit gauge-fixing
   factor and no gauge edge modes.
6. Keep the schematic EFT result separate from a future numerical
   scheme/scale/truncation packet.

## Final verdict

**MINOR REVISION.**  The round-one mathematical blockers in the finite
action/measure/support-to-D14 chain are repaired, and all 26 checks reproduce.
The remaining code changes are small but worthwhile: ownership, direct
overwrite regression, memory conditional closure and two scope labels.  The
EFT repairs are adequate at schematic scope; numerical EFT and empirical/UV
selection remain deliberately open.  Preserve `INCOMPLETE-INVESTIGATION`
while applying these hardenings.
