# D40b round-two independent review

**Verdict:** `0 BLOCKERS / 1 MAJOR / 1 MINOR / 0 NIT`; promotion withheld.  
**Frozen repair commit:** `25e44e5`.  
**Source SHA-256:**
`892fc4e445b29bcc56aec8e1622d4bc84e527a511e0daf74ee3ead71d82ea68e`.  
**Complete-output SHA-256:**
`30c943f876201ce1e36ae89808c9427b4e611d13804a460d110c921e13ab1508`.  
**Date:** 2026-07-15.

The probability-space major from round one is mathematically closed.  The
new star pushforward is `23/198`; the separate global typed-DAG pushforward is
`5/96`; both normalize and both target atoms have exactly two serial
preimages.  Promotion is withheld only because the executable does not lock
all code it imports and one descriptive census is not an exact gate.

## 1. Reproduction

Fresh runs under `PYTHONHASHSEED=19` and `101` exit zero, are byte-identical to
the committed stdout and reproduce complete-output hash

```text
30c943f876201ce1e36ae89808c9427b4e611d13804a460d110c921e13ab1508.
```

Independent arithmetic confirms

```text
1/18 + 2/33 = 23/198,
1/32 + 1/48 = 5/96.
```

The target star paths have the same unordered canonical actions and final
canonical star.  The target global paths have the same event-ID set, final
authenticated store and typed causal-DAG atom.  The two namespaces are
distinct.  The 320 Bell quadratic-form controls are exact and the sign-aware
radical rendering is correct.

## 2. MAJOR — transitive runtime antecedents are not checked

D40b C0 locks its pin, the D40 pin/source/output and round-one review.  It then
imports D40, which in turn imports the live D34c and D39b implementations and
their dependencies.  Importing D40 does not execute D40's
`lock_and_type_checks()`.  A changed runtime dependency could therefore feed
D40b's new calculations while all five C0 hashes still pass.

This is a receipt-integrity major, not a mathematical counterexample.  The
focused delta must execute D40's twelve antecedent locks (and seven level
constructors), or directly lock every transitive runtime source it consumes.
It should also lock D40b source and complete output before claiming closure.

## 3. MINOR — exact census values are printed but not gated

C2 reports

```text
star serial paths       28
star unordered atoms    17
global serial paths     44
global typed DAG atoms  40
global merges            4,
```

but passes whenever each value is merely positive.  Those counts are now
used in the receipt note and README, so the closure delta must gate the exact
tuple `(28,17,44,40,4)`, as well as the three unclaimed-scope zeros.

## 4. Findings closed from round one

- The two probability spaces have separate constructors and exact sums.
- The complete global object is scoped to the registered depth-two embedded
  jump pushforward.
- Bell Gram positivity has both the arbitrary-coefficient algebraic identity
  and 320/320 finite hostile controls.
- R9 is a typed claim ledger with `universality_theorem=0`.
- Negative-radical text is repaired.

A tiny D40c provenance/census delta should close this review.  No D40b theorem
or number otherwise requires change.  Paper 29 remains held.

