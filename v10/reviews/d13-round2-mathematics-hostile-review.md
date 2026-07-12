# D13 hostile round-2 mathematics review

**Date:** 2026-07-11  
**Verdict:** **PASS AT THE NARROWED FINITE-KERNEL SCOPE**  
**D13 protocol verdict:** correctly remains `INCOMPLETE-INVESTIGATION`  
**Proved theorem:** `FINITE-LOCAL-UNITARY-KERNEL-NONUNIQUENESS-PROVED`  
**New fatal or major opening:** none

## Executive decision

The repaired D13 artifacts answer the round-one review honestly.  The SymPy
program has been replaced by a dependency-free exact receipt.  The universal
category/functor theorem has been withdrawn, the path-integral sewing claim is
conditional, amplitude polar coordinates are no longer called evidence or
holonomy without extra hypotheses, covariance is restricted to endpoint
unitary frames, the scalar-field example is restricted to a sector where a
`2 -> 2` amplitude exists, and the protocol verdict is now the required
`INCOMPLETE-INVESTIGATION`.

The 21-check program genuinely expands the finite witness.  It adds an exact
interference cell, a disjoint-laboratory no-signalling cell, a Kraus channel,
a declared seal/record/live-collar isometry, persistence under a system-only
future algebra, and a visible non-Markov history law.  The fixed-interval
iSWAP pair remains operationally inequivalent.

Two receipt labels remain slightly stronger than their implementation.  The
“reversible hidden-memory circuit” is represented in code by its exact
two-history measure rather than explicit reversible gate matrices.  The
“Born-once” check proves that accidental double-squaring would change `1/2` to
`1/4`; it does not trace an independent end-to-end probability pipeline.  Both
are minor scope repairs.  Neither affects the nonuniqueness theorem or the
formal incomplete verdict.

## Frozen artifacts and exact reproduction

```text
96a51b2e00759931db7ae208698d064542aaebfaf61dce7d3d0b32e812131802  note-d13-round1-opening-repairs.md
b11f8ffce91d803d991afe294be95e156a79461094edb833c8cf723743d8cb39  code/d13_finite_kernel_no_go_exact.py
825e94f287e607f1b9d62cc5c7a5394ddbbd39aac8a796660febe62a4e7bb9dc  note-d13-maximal-action-theorem.md
77309f48136b8036365157509e9d27f1032e2a602398a70d9598544b3592f77e  relativistic-isp-v10-paper14-the-action-behind-the-records.md
06226a2bd93a3314fe74aaefe1d2a26b2869197dad77f2fa4c1177673e9e753d  code/d13_corpus_action_inventory.py
e03cea4a1940a3a274e7dc5499b39c4932a8e334ff09945265480836f7dc3fe4  data/d13-finite-kernel-no-go-exact.json
31e0ddbf3d32f066ec657327c0b0824352cf80b2f92953ae176bd0ec87429ab9  data/d13-corpus-action-inventory.json
```

The kernel receipt ran successfully under default normal and optimized Python.
Both stdout streams and both JSON outputs were byte-identical:

```text
checks                         = 21/21
semantic SHA-256               = 4eb19b0eb34bdc9cd910029cb3d4c22bb47d8d847e0fe12353a7b5eac69f2852
normal/-O stdout SHA-256       = 587f768d8f5b7c59b3858c4275b17273a41c7fbd9a28e80dd6c5e14add369fca
generated JSON SHA-256         = e03cea4a1940a3a274e7dc5499b39c4932a8e334ff09945265480836f7dc3fe4
reported source SHA-256        = b11f8ffce91d803d991afe294be95e156a79461094edb833c8cf723743d8cb39
```

The antecedent inventory also reproduced under normal and optimized Python:

```text
Markdown files                 = 524
broad-relevant files           = 501
antecedent corpus SHA-256      = 51d19c00e979ecfb796aba2c34e810cfbe3bd00586e8703c1ce54c7826877c6e
normal/-O stdout SHA-256       = 34a498085240c2504d5e780e95f66a63548bf3edb49af3ae3d57c01ef41505f7
generated inventory SHA-256    = 31e0ddbf3d32f066ec657327c0b0824352cf80b2f92953ae176bd0ec87429ab9
checks                         = 5/5
```

The inventory is correctly described as high-recall indexing rather than an
automatic interpretation engine.  D13 self-files are excluded from the frozen
antecedent stream, so adding D13 reviews does not move the corpus hash.

## M1–M12 adjudication

### M1 — false same-support wording

**CLOSED.**

The repaired notes say that the candidates share the ambient four-dimensional
carrier, types, ownership grammar, and allowed outcome labels, but not positive
prediction support.  The exact zero of half-iSWAP is disclosed.  This is the
correct distinction.

### M2 — interval/reparameterization ambiguity

**CLOSED.**

The theorem, JSON scope, executable labels, and Paper 14 all freeze one
operational diamond interval/evidence slab and forbid reparameterizing it
between candidates.  On the fixed preparation/effect,

$$
p_{\pi/4}=\frac12,\qquad p_{\pi/2}=0.
$$

Although `U_(pi/4)^2=U_(pi/2)`, one quarter kernel and one half kernel are not
the same map on this fixed interval.  Their eigenvalue ratios differ, and the
fixed experiment distinguishes them, so unitary conjugation, global phase, or
probability-preserving record relabeling cannot identify them.

The result proves angle/coupling nonselection conditional on the fixed
interval.  It does not determine the evidence-to-proper-time conversion, and
the paper does not claim that it does.

### M3 — undefined universal category

**CLOSED BY WITHDRAWAL.**

The boundary-amplitude construction is now explicitly a candidate bridge.
The note says D13 has not defined or proved a symmetric monoidal category of
all sealed diamonds, its presentation quotient, or a universal sewing theorem.
No `Hilb/CP` theorem remains.

### M4 — formal path-integral overread

**CLOSED BY NARROWING.**

General sewing is conditional on a supplied well-defined regional action.  The
repairs explicitly name edge modes, boundary charges, ghosts, corner terms,
anomalies, regulators, and theory-specific sewing measures.  The only exact
gluing result claimed by the executable is the finite matrix identity
`U_(pi/4)^2=U_(pi/2)`.

### M5 — non-Markovity was not executed

**CLOSED for compatibility; minor executable-label qualification.**

The supplied history measure is

$$
P(0,0,0)=\frac12,\qquad P(1,0,1)=\frac12.
$$

Therefore

$$
P(Z=1\mid Y=0,X=1)=1,
\qquad
P(Z=1\mid Y=0,X=0)=0,
$$

while `Y=0` in both branches.  The visible process violates first-order
Markovity exactly.  This is a probability on trajectories, not an inference
from one-time marginals.

A reversible enlarged realization exists: initialize a fair `X`, copy it by
CNOT into a zero memory, leave a zero `Y`, and later copy the memory into zero
`Z`.  On the initialized subspace it produces exactly the displayed histories,
and the system-plus-memory circuit is reversible/Markov.

The code itself hard-codes the two history masses and evaluates the
conditionals; it does not construct the CNOT matrices or audit the enlarged
state.  Rename the receipt cell “exact visible non-Markov history with a stated
reversible dilation,” or add those matrices.  The theorem now claims only that
the amplitude architecture **permits** non-Markov visible records, so the
mathematical opening is closed.

### M6 — polar quotient and zeros

**CLOSED.**

The repaired theorem fixes the positive reference, amplitude normalization,
and global phase before asserting coordinates.  It states that otherwise
common additive constants remain and that zeros require a separate support
field.  This is the correct scalar polar decomposition scope.

### M7 — evidence/holonomy conflation

**CLOSED.**

The notes now call the formula only an atomwise polar representation of a
supplied scalar amplitude.  They require a normalized positive record law plus
evidence gluing/survival before calling the modulus coordinate RN/KL evidence,
and transports, loops, gauge action, and cocycle laws before calling the phase
sealed holonomy.  They also preserve coherent summation before probability
readout.

### M8 — covariance overread

**CLOSED BY EXACT SCOPE.**

The executable verifies independent input/output **unitary endpoint-frame**
covariance for the fixed instrument probability.  Paper 14 explicitly says
this is not Lorentz or diffeomorphism covariance and keeps A6 open.  The
disjoint schedule computation is likewise identified as one finite cell; the
broader schedule statement is inherited from D12 only under its explicit
disjointness/adjacent-swap hypotheses.

### M9 — pointer orthogonality was not durability

**CLOSED within the declared future algebra.**

The repaired isometry is

$$
|j\rangle\mapsto
|j\rangle_{\rm system}|j\rangle_{\rm record}|1\rangle_{\rm live\ collar}.
$$

Its columns are orthonormal, the record branches are exclusive, and the collar
is live with probability one.  Later licensed kernels act as
`U_system tensor I_record tensor I_collar`; they cannot mix record sectors.
Consequently every sector norm, and hence the record distribution, is
invariant under the entire declared system-only unitary algebra.  The code
checks one nontrivial later unitary cell, while the tensor-factor structure
proves the general statement at that scope.

This is valid finite permanence and repeat-read semantics.  It does not derive
the pointer instrument or justify why nature's future algebra excludes record
rewrites.  The repaired paper says both explicitly.

### M10 — A4 subgates were absent

**CLOSED as finite cells; universal A4 correctly remains open.**

The new receipt verifies:

- coherent `H H` return probability `1` versus the inserted-record/dephased
  probability `1/2`;
- invariance of the second Bell marginal under a local unitary on the first
  qubit;
- Kraus completeness for computational dephasing;
- normalized positive dephased output;
- entangling capacity, unitarity, and normalized pointer probabilities.

The “Born weight is read once” check is only

```text
p = 1/2 and p*p != p.
```

It demonstrates that double-squaring is detectable (`1/4 != 1/2`) but does not
audit an independent end-to-end implementation in which a Born weight could be
inserted twice.  This label should say “double-squaring would change the exact
prediction.”  Since the paper calls these finite subgates and leaves universal
A4 open, no theorem-level opening remains.

### M11 — overbroad `phi^4` strengthening

**CLOSED.**

The continuum family is now restricted to a real scalar perturbative EFT on
Minkowski or a suitable asymptotically flat background, with fixed vacuum,
asymptotic states, field normalization and renormalization convention, no
symmetry forbidding `phi^4`, and distinct small positive renormalized
couplings.  In that sector the quartic term leaves the classical differential
principal part and Minkowski cone unchanged and changes the connected
`2 -> 2` amplitude.  The notes explicitly deny a generic curved-spacetime
S-matrix and deny that arbitrary higher derivatives preserve the principal
part.

### M12 — incorrect protocol verdict

**CLOSED.**

Every repaired artifact now distinguishes:

```text
proved:  FINITE-LOCAL-UNITARY-KERNEL-NONUNIQUENESS-PROVED
formal D13 protocol verdict:  INCOMPLETE-INVESTIGATION
```

The gate table keeps A1, general A2–A6, architecture universality, fields,
couplings, units, empirical selection, spacetime holdouts, and hostile closure
open.  The candidate-class adjudication says explicitly that the A–H census is
not a proof that all generalized actions reduce to the amplitude schema.

This is exactly the grade demanded by the frozen protocol.

## Independent check of the 21 exact cells

No algebraic failure was found:

1. both iSWAP members are unitary;
2. `X_ex` commutes with number and exchange;
3. the exact square identity holds;
4. tensor-disjoint cells commute;
5. the overlap control does not commute;
6. endpoint basis transport preserves the trace probability;
7. the seal/birth columns are orthonormal;
8. record branches have masses `(0,1/2,1/2,0)`;
9. those masses normalize;
10. both gates have concurrence one witnesses;
11. the fixed-interval prediction pair is `(1/2,0)`;
12. coherent and inserted-record path rules differ as claimed;
13. the Bell marginal no-signalling cell is exact;
14. projective Kraus operators are complete;
15. the dephased `|+>` state is `diag(1/2,1/2)`;
16. double-squaring changes the half probability;
17–18. the untouched record register preserves distribution and readout;
19. the collar register is certainly live;
20. the visible history conditionals are `1` and `0`;
21. the frozen count and semantic receipt agree.

## Inventory assessment

The repaired inventory does what it claims:

- scans Markdown in V1–V10;
- excludes D13-named V10 files and Paper 14 from the antecedent boundary;
- hashes path and bytes in deterministic order;
- records every category count, heading, and matched scope-guard line;
- freezes file count, broad-relevant count, and corpus stream hash;
- reproduces byte-identically under `-O`.

The category regex is intentionally broad—`selector` alone will make many
files relevant—so 501/524 is not evidence that 501 papers contain a serious
action theorem.  The prose correctly calls it high-recall inventory rather
than semantic proof.  The human ledger remains responsible for interpretation.

## New residual ledger

```text
R2-1  MINOR  Code stores the non-Markov history table but does not execute the stated reversible CNOT dilation.
R2-2  MINOR  Born-once cell proves p^2 != p, not an end-to-end no-double-Born pipeline audit.
R2-3  MINOR  Retained obsolete SymPy script/JSON should be labeled superseded in-file or archived to avoid receipt ambiguity.
```

No residual is fatal or major.  R2-1 and R2-2 require label precision only;
the underlying probability identities are correct.  R2-3 concerns provenance:
the repaired notes consistently point to the new standard-library receipt, but
the old JSON still contains its former broader verdict.

## Final verdict

**PASS the repaired mathematics at the finite-kernel scope.**  All M1–M12
findings are closed by implementation or explicit withdrawal, the 21-check and
inventory receipts reproduce exactly, and the operational nonuniqueness
theorem is valid.  Preserve `INCOMPLETE-INVESTIGATION` as D13's formal protocol
verdict.  Nothing in this round derives a universal action, record ontology,
Lorentz/diffeomorphism gauge, physical-unit bridge, or geometry holdout.
