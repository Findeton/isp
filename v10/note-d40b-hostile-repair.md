# D40b — hostile repair: two probability spaces, one level theorem

**Status:** PINNED BEFORE EXECUTION.  No D40b source or stdout exists at this
commit.  
**Date:** 2026-07-15.  
**Mandate:** `reviews/d40-round1-independent-hostile-review.md`.  
**Frozen parent:** D40 theorem commit `d11ba91ec987e4998ad623f6514216f7dfd53039`.

## 1. Repair target

D40 correctly computed four serial weights but placed only the complete
first-two-global-event pushforward next to the Paper 28 first-relevant-event
square.  D40b must type and gate the two probability spaces separately:

```text
STAR_RELEVANT_SERIAL
  p(idle,birth) = 1/18
  p(birth,idle) = 2/33

STAR_UNORDERED_ACTION_ATOM
  mass = 1/18 + 2/33 = 23/198

GLOBAL_SERIAL_EVENT
  p(idle,birth) = 1/32
  p(birth,idle) = 1/48

GLOBAL_TYPED_DAG_ATOM
  mass = 1/32 + 1/48 = 5/96.
```

The two sums answer different questions.  Their inequality is expected and
cannot be used as a cross-object test.  Within each probability space,
unequal serialization weights are compatible with a normalized unordered
atom because the pushforward adds preimages.  Paper 28's flat action-cocycle
nonmembership remains exact; neither inequality is a probability-law
inconsistency.

## 2. Delta gates

### C0 — locks

Lock the D40 pin, D40 source, D40 complete stdout and hostile review.  Fail on
any mismatch.

### C1 — typed two-space pushforward

Construct the full depth-two projected star cylinder distribution rather than
adding only two hand-entered numbers.  Push every serialized path through an
explicit `STAR_UNORDERED_ACTION_ATOM` map that retains its final canonical star
and unordered action multiset.  Gate that the target atom receives exactly
the two hostile-reviewed paths and mass `23/198`.

Separately construct the complete depth-two embedded global-event law and its
typed causal-DAG pushforward.  Gate identical record IDs, identical final
authenticated store, identical typed DAG and mass `5/96` from exactly the two
serializations.

### C2 — scope

Print and gate:

```text
global object = REGISTERED DEPTH-TWO EMBEDDED-JUMP PUSHFORWARD;
timed Harris cylinder theorem = NOT CLAIMED;
arbitrary-down-set projectivity = NOT CLAIMED;
stationary/infinite completion = NOT CLAIMED.
```

The star object is likewise the registered depth-two projected cylinder, not
an infinite completion.

### C3 — Bell Gram positivity certificate

For every Bell setting and every nonzero coefficient vector in
`{-1,0,1}^4`, gate exactly

```text
c^T G c = ||sum_i c_i v_i||^2 >= 0.
```

This is a finite hostile control under the algebraic Gram proof, not the proof
itself.  The proof is the displayed identity for arbitrary real coefficients.
Keep Gram symmetry and normalization separate.

### C4 — claim-ledger and rendering repair

Rename R9 to `TYPED CORPUS CLAIM LEDGER`.  It checks unique row assignment and
scope bookkeeping only; `universality_theorem=0`.  Paper 29 must justify each
row from its cited antecedent.

Render exact radicals with sign-aware text, specifically
`1/2-1/4*sqrt2` rather than `1/2+-1/4*sqrt2`.

## 3. Closing noun

If all gates pass, the repaired terminal statement is

```text
TWO-SPACE SERIAL-TO-UNORDERED PUSHFORWARD THEOREM;
PAPER 28 FLAT-ACTION NONMEMBERSHIP WITHOUT PROBABILITY INCONSISTENCY;
FINITE BELL GRAM-POSITIVITY CONTROL;
UNRESOLVED D15 DICTIONARY.
```

Paper 29 remains held until an independent closing review confirms the delta.

