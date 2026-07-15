# D40b exact repair receipt

**Status:** focused repair candidate, `PASS 5/5`; independent closing review
open.  Paper 29 remains held.  
**Date:** 2026-07-15.  
**Pin:** `note-d40b-hostile-repair.md`, committed before source at `b7dc713`.  
**Source:** `code/d40b_probability_space_repair_exact.py`.  
**Stdout:** `data/d40b_probability_space_repair_exact.out`.

## 1. Frozen values

```text
source_sha256           = 892fc4e445b29bcc56aec8e1622d4bc84e527a511e0daf74ee3ead71d82ea68e
stdout_body_sha256      = 9aadc4930236bf38fb86cc0aa6632bb2f80971869c4334f34559246c465e949c
internal_science_sha256 = 8e39b18e2039482e36db5351cd892d2225b74a9fd9d95433a0233aa43e258b68
complete_stdout_sha256  = 30c943f876201ce1e36ae89808c9427b4e611d13804a460d110c921e13ab1508
```

The committed stdout is byte-identical to a fresh zero-exit run.

## 2. Major closure

D40b constructs two distinct sum types and pushes the complete registered
depth-two laws, rather than substituting one pair of serial paths for the
other.

For the Paper 28 projected first-relevant-event star law:

```text
serialized paths             28
unordered action atoms       17
target serial preimages        2
target serial weights     1/18, 2/33
target unordered mass      23/198.
```

For the complete first-two-global-event embedded jump law:

```text
serialized paths             44
typed causal-DAG atoms       40
serial merges                 4
target serial preimages       2
target serial weights     1/32, 1/48
target typed-DAG mass        5/96.
```

Both pushforwards normalize exactly.  Within each object the target atom is
the sum of its two serialization preimages.  `23/198` and `5/96` are not
supposed to agree, because silent omitted events distinguish the projected
first-relevant-event law from the complete first-two-global-event law.

The repaired conclusion is exact:

```text
Paper 28's chosen star kernel is not in the registered flat action-cocycle
variety.  That nonmembership is not a probability inconsistency: the
unordered law sums, rather than equates, serialization weights.
```

## 3. Minor closure

The global object is now named only as the registered depth-two embedded-jump
typed-DAG pushforward.  No timed Harris-cylinder theorem, arbitrary-down-set
projectivity or stationary/infinite completion is inferred.

The Bell Gram construction is supplemented by 320/320 exact controls over all
nonzero coefficient vectors in `{-1,0,1}^4` across four settings.  Every case
checks

```text
c^T G c = ||sum_i c_i v_i||^2 >= 0.
```

The arbitrary-real-coefficient proof is the same Gram identity; the finite
controls are hostile examples, not its logical replacement.

R9 is renamed a typed corpus claim ledger.  Its twelve rows are uniquely
assigned, while `universality_theorem=0`; Paper 29 must justify the placements
from antecedent theorems.  Exact rendering now prints
`1/2-1/4*sqrt2`.

## 4. Closing scope

```text
TWO-SPACE SERIAL-TO-UNORDERED PUSHFORWARD THEOREM;
PAPER 28 FLAT-ACTION NONMEMBERSHIP WITHOUT PROBABILITY INCONSISTENCY;
FINITE BELL GRAM-POSITIVITY CONTROL;
UNRESOLVED D15 DICTIONARY.
```

Independent closing review must rederive both sums, verify the two constructor
namespaces, reproduce all 320 Gram controls and confirm the fixed-depth and
claim-ledger wording before Paper 29 begins.
