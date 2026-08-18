# CSF claim-lineage root-cause audit

**Date:** 2026-08-18

**Status:** binding process correction; no frozen CSF artifact is modified.

## Finding

The hostile panel correctly killed
`RECURRENCE-DOCTRINE-MOVES-PHYSICS`. The failure was not that a legitimate
calculation was interpreted too aggressively. The two alleged doctrine
predictions were written directly in the scorer:

```text
identity            -> [1,0]
asymmetric_exchange -> [0,1]
```

The scorer then defined “moves physics” as inequality of those two literals.
No preparation, history maps, kernel, port factorization, effect, or calibrated
probe produced either vector.

The defect class is:

```text
LITERAL-AS-MEASUREMENT + SHARED-PREDICATE-CIRCULARITY
```

It is a provenance/instrument failure, not a false exact-arithmetic result.

## How it passed the pipeline

Five protections were individually green but jointly insufficient:

1. **Fixture neutrality inspected only the JSON fixture.** The answer-like
   vectors lived in the scorer, so the data-only check did not see them.
2. **The doctrine gate checked only literal inequality.** Once the source
   contained two different arrays, that gate could not return the opposite
   scientific answer.
3. **No registered mutant targeted the doctrine prediction.** The recurrence
   mutants changed dictionary/rephase/swap wiring, never an upstream physical
   law whose derived screen fed the doctrine claim.
4. **Comparator, qualifier, and prose shared one Boolean.** The apparent
   independent agreement was one predicate copied through three render paths.
5. **Verification recomputed the surrounding algebra, not claim lineage.** It
   correctly rebuilt context dimensions and kernels but did not ask which
   state/law/observable calculation generated `[1,0]` and `[0,1]`.

This is precisely the difference between a sealed value and a measured value.
Hashing, exact arithmetic, replay, and one-occurrence prose binding can
authenticate a planted statement perfectly.

## Scope of contamination

The defect kills only the doctrine-sensitive qualifier and the associated
sentence. It does not move the fixed-history spectrahedron, JCV kernels,
context dimensions, rich-spectrum cross-moment result, calibrated `1` versus
`9/25` instrument fiber, flag/eraser calculation, or fixed-factor
no-signalling check. Those were independently reconstructed by the panel.

The separate history-individuation failure still kills the CSF primary. This
audit neither weakens nor repairs that adjudication.

## Mandatory forward repair

For every claim of the form “changing doctrine/law/geometry changes a
prediction,” a new unit must publish a claim-lineage row containing:

```text
preparation -> candidate law -> successor/instrument -> calibration/effect
            -> derived probability/distribution -> comparison
```

The two sides must use a common preparation and calibrated observable unless
the changed item is explicitly one of them. Literal arrays may appear as
committed anchors or expected regression values, never as the measured outputs
on which the claim predicate is defined.

At least one falsifier must alter an upstream law/object while holding the
calibration fixed and must move or erase the derived output. Mutating a stored
answer, label, or Boolean is not a scientific falsifier. The receipt must name
the upstream measurement keys consumed by each prediction-bearing claim, and
the verifier must independently rebuild at least one complete lineage.

This requirement is engraved as RUNBOOK E-36. It applies to new units and to
the adjudication of already-frozen, nonterminal candidates. It does not reopen
terminal bytes or authorize alteration of WRC after result exposure.
