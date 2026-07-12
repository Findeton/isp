# D17 hostile review, round 1: independent rebuild and reproducibility

**Referee:** independent clean-room/reproducibility stream  
**Date:** 2026-07-11  
**Verdict:** **MAJOR REVISION — `INCOMPLETE-INVESTIGATION`**  
**Narrow fixed-action state/record nonselection result:** **INDEPENDENTLY CONFIRMED**

The frozen executable reproduces exactly.  Normal and optimized Python both
pass 19/19, have identical stdout, and reproduce every receipt hash.  A
separate standard-library rebuild, without importing D17, confirms the action
phases, coherent cancellation, seal matrix, decoherence matrices, record
probabilities, automorphism weights, both sparse towers after expansion by
implicit zero cylinders, the two conditionals, and the inconsistent control.

The load-bearing finite result is sound: the same two-order domain, action and
record isometry give `(1/2,1/2)` for one supplied preparation and `(1,0)` for
another.  An action that only fixes the phases therefore does not select the
boundary state or the recorded probability law.

The current packet does not yet pass its frozen H7 exactly as written.  H7
requires two inequivalent packets that each pass H0-H6.  The equal tower has
the advertised visible non-Markov comparison, but the delta tower has only
`000`; its `x=1` conditioning event is null, so it cannot exhibit the required
two-positive-past H6 comparison.  This does not refute ordinary nonselection,
but it blocks the stronger protocol claim.  An exact second preparation with
amplitudes `(3/5,4/5)` and tower weights `(9/25,16/25)` repairs this specific
gap while keeping the action, domain and instrument fixed.

## 1. Reproduction and frozen bytes

The following executions were repeated independently:

```bash
python3 v10/code/d17_causal_action_measure_nonselection_exact.py
python3 -O v10/code/d17_causal_action_measure_nonselection_exact.py
python3 v10/code/d17_causal_action_measure_nonselection_exact.py | shasum -a 256
python3 -O v10/code/d17_causal_action_measure_nonselection_exact.py | shasum -a 256
shasum -a 256 v10/code/d17_causal_action_measure_nonselection_exact.py
shasum -a 256 v10/data/d17-causal-action-measure-nonselection-exact.json
```

Both modes end with:

```text
CHECKS PASSED: 19/19
SEMANTIC SHA256: 7fa71590dc6fc08eec118d20974a06276a675cd7bd89b421444375d6da0c9da2
SOURCE SHA256: d71af38afa1a434b992cef2fa37c949a5ee2642b7c133c04ca16dee3e233805d
VERDICT: CAUSAL-ACTION-TO-MEASURE-NONSELECTION
```

The normal and `-O` stdout hashes are both:

```text
b3a70d06ef5726a491919d2188f58776a90f3c0c12c05f177d13f92e073b4c03
```

The remaining authoritative hashes match the receipt:

```text
packet  08cffa34cf2b5b128ded2725299ce5a3dd46abad97164aa5435f3e89abcae0b0
D14     e0db2c65a7305ca92bf19fcaa0384e0d825b1a04a5590c0ca243e6192bebc425
D16     861279c4057d294ded74a5bf601aaaa7a75286d277d44f26213ceb9a1ff48b37
```

There is no Python `assert` or `__debug__`-dependent gate.  The explicit
`check` calls and final check-count and semantic-hash guards survive `-O`.
The generated packet is written only after those guards.

## 2. Independent action and orbit reconstruction

I rebuilt the two strict relations directly as Boolean matrices and counted
open intervals and automorphisms by exhaustive permutations.  For the fixed
action `S=N_0` the results are:

| Order | `N_0` | `(-1)^S` | `|Aut|` |
|---|---:|---:|---:|
| `chain4` | 3 | -1 | 1 |
| `diamond4` | 4 | +1 | 2 |

Thus the phases `(-1,+1)` are correct.  Candidate inverse-automorphism raw
weights are `(1,1/2)`, whose exact normalization is `(2/3,1/3)`.  Uniform
unlabeled weights are `(1/2,1/2)`, so the two conventions really differ.

This numerical orbit comparison is not yet an end-to-end orbit-measure
counterexample.  The source never inserts either `mu_orbit^(1/2)` into the
amplitudes and never propagates the inverse-automorphism choice through the
seal and tower.  In the current exact number field, square roots of `1/3` and
`2/3` are also unavailable; integration requires a field extension or a
different exact convention.  The defensible current claim is that orbit
weighting remains supplied data, not that two complete orbit packets were
executed.

## 3. Coherent cancellation, seal and decoherence

The unrecorded equal-preparation amplitudes are

```text
(-1/sqrt(2), +1/sqrt(2)),
```

so their selected coherent sum is exactly zero.  Rebuilding the specified
`8 x 2` seal gives its only nonzero entries at `(row,column)=(1,0)` and
`(7,1)`.  Consequently `V* V=I_2`; both outputs have collar bit one; and the
two record branches have disjoint support.

The full two-branch decoherence matrices inferred independently are:

```text
D_equal = [[1/2, 0], [0, 1/2]]
D_delta = [[1,   0], [0,   0]]
```

They are Hermitian, positive semidefinite and normalized.  The same seal
object is applied to both preparations.  The action object is immutable and
created once; the same `chain4` and `diamond4` objects are used throughout.
Therefore no hidden change of action, domain or instrument explains the
different record probabilities.

Source check 12 only recomputes the two phases, so its label is broader than
its predicate.  Source inspection and the clean-room rebuild establish the
stronger fact for this version, but the executable should freeze identities
or canonical hashes for the domain and instrument if that fact is meant to
remain receipt-bearing.

The future used here is the identity on the eight-dimensional target.  It is
a valid protected future, but only a minimal durability witness; it does not
test a nontrivial later interaction.

## 4. Boundary-state naming and H0

`equal_boundary_state` and `delta_boundary_state` in the source already
contain the action phases.  They are final amplitudes, not the pre-action
preparations named by H0.  The theorem prose distinguishes these concepts,
and the nonselection logic survives, but the executable does not freeze the
factorization

```text
Psi_boundary * sqrt(mu_orbit) * phase(S)
```

as three separate objects.  A hostile receipt should represent and vary those
factors independently so the action cannot be silently counted twice or
absorbed into `Psi_boundary`.

## 5. Projective towers and exact conditionals

I expanded every omitted binary cylinder to an explicit zero and checked all
parent-child equations.  Both supplied depth-1-to-3 families are normalized
and projective:

```text
equal support: 000 -> 1/2, 101 -> 1/2
delta support: 000 -> 1
```

For the equal tower, both conditioning denominators are `1/2` and:

```text
P(z=1 | x=1,y=0) = 1
P(z=1 | x=0,y=0) = 0
```

The visible current value `y=0` therefore does not determine the next law;
the supplied three-bit distribution is genuinely non-Markov in the visible
bit.  The separately normalized control fails because the depth-two child
mass under parent `(1,)` is zero rather than `1/2`.

The helper `is_projective` is sufficient for these particular sparse tables,
but it is not a general validator: it checks only stored parents, does not
check level normalization, and assumes a missing cylinder has no nonzero
descendants.  Freeze a complete cylinder alphabet or validate support closure
and normalization explicitly.

No induction extends these tables beyond depth three.  Their entries are bit
strings rather than causal orders, and no truncation/extension map connects
them to `chain4`, `diamond4`, or the fixed action.  “Complete recorded history
laws” is therefore too broad; the reproduced object is a pair of supplied
depth-1-to-3 mark-cylinder families compatible with the record weights.

## 6. The strict H7 opening

The frozen H7 antecedent says that both inequivalent packets must pass H0-H6.
The equal tower passes the numerical part of H6 because the two positive
histories `000` and `101` share current visible record zero and have different
next conditionals.  The delta tower has no positive `x=1` history.  Its
corresponding conditional is undefined, not a second non-Markov witness.

Therefore the present pair proves:

```text
same S, Omega and R + different supplied Psi => different recorded P.
```

It does not yet prove the stronger frozen statement:

```text
two distinct packets, each satisfying H0-H6 => different recorded P.
```

This opening has an exact, local repair.  Keep support on `000` and `101`, but
replace the delta preparation with pre-action amplitudes `(3/5,4/5)`.  The
same action and seal give weights `(9/25,16/25)`.  The corresponding tower is
normalized, projective, differs from the equal tower, and retains the same
zero/one non-Markov conditionals because both histories remain positive.
The clean-room rebuild verified every one of those rational identities.

That repair discharges the numerical H7 antecedent only.  H5's all-depth
extension and H6's required local hidden-memory carrier/deletion control still
remain open.

## 7. Findings and required disposition

```text
R1 MAJOR    The delta packet does not pass H6, so the pair does not satisfy
            H7 exactly as frozen.  Replace it with a second two-positive-
            branch exact packet or narrow H7.
R2 MAJOR    The towers are supplied finite bit tables, not action-evaluated
            causal extensions, and no all-depth induction exists.
R3 MAJOR    No local memory carrier or deletion countercontrol realizes H6;
            the table directly encodes the full past.
R4 MODERATE H0's state/measure/action factors are conflated in the amplitude
            variables.
R5 MODERATE Orbit weights are calculated but not propagated end to end.
R6 MODERATE “complete history law” exceeds a depth-three cylinder witness.
R7 MINOR    The projectivity helper under-validates arbitrary sparse tables.
R8 MINOR    The full decoherence matrices and fixed-domain/instrument hashes
            are inferred rather than frozen as explicit receipt fields.
```

## 8. Final decision

**MAJOR REVISION.**  Preserve the narrow result
`CAUSAL-ACTION-TO-MEASURE-NONSELECTION` as an exact finite boundary-state
nonselection theorem: it is independently reproduced and mathematically
correct.  Do not treat the current receipt as closure of frozen H7 or as a
causal, all-depth, locally generated history measure.  The paper's formal
status `INCOMPLETE-INVESTIGATION` and its ceiling—record instrument and towers
supplied, not action-derived—are correct.
