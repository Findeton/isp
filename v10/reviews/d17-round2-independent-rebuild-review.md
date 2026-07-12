# D17 hostile review, round 2: independent rebuild and reproducibility

**Referee:** independent clean-room/reproducibility stream  
**Date:** 2026-07-11  
**Formal D17 verdict:** **MAJOR REVISION — `INCOMPLETE-INVESTIGATION`**  
**Narrow fixed-action measure-nonselection theorem:** **PASS**

Round two repairs the exact quantum and finite-probability mathematics.  Normal
and optimized execution reproduce 26/26 with identical stdout and all receipt
hashes.  A reconstruction that did not import D17 confirms the explicit
factorization, erasure probabilities `0` and `1/2`, record isometry and Born
weights, the `(9/25,16/25)` packet, normalized inverse-automorphism weights
`(2/3,1/3)`, projectivity through depth 40, both non-Markov conditionals, exact
equality of the equal tower and D14 memory tables through depth three, CPTP
reset completeness, and the reset output.

The narrow theorem is now secure: a fixed action phase function and fixed D14
seal do not select the boundary/orbit packet or the supplied projective mark
law.  The repaired executable still does not join its action cell, causal-order
extensions and memory circuit into one causal-history construction.  In
particular, the checked extension path stops before the size-four
`chain4/diamond4` action domain, and the second positive packet is not run
through the local-memory network.  These are integration defects, not
counterexamples to nonselection.

## 1. Frozen reproduction

The following commands were repeated:

```bash
python3 v10/code/d17_causal_action_measure_nonselection_exact.py
python3 -O v10/code/d17_causal_action_measure_nonselection_exact.py
python3 v10/code/d17_causal_action_measure_nonselection_exact.py | shasum -a 256
python3 -O v10/code/d17_causal_action_measure_nonselection_exact.py | shasum -a 256
shasum -a 256 v10/code/d17_causal_action_measure_nonselection_exact.py
shasum -a 256 v10/data/d17-causal-action-measure-nonselection-exact.json
```

Both direct runs end with:

```text
CHECKS PASSED: 26/26
SEMANTIC SHA256: a5d2cb4dd4b7b065430bcb4aedc7c88daddf1df1ad84c970f1ae3b78cd7ee525
SOURCE SHA256: 305f532548db3734ed6d92896f98ea9803fbcc86a5786a402cfb6cff8a847d42
VERDICT: CAUSAL-ACTION-TO-MEASURE-NONSELECTION
```

Normal and `-O` stdout hashes are identical:

```text
bf5a54311daf639d612857c36cd40acc637f9a4246bd1cdecb816fa74b80b306
```

The remaining current hashes match the receipt:

```text
packet  15cfd44534c4b7de4d66e834a318a00eb666cfaffe7dccb86bc45c2891563cfe
D14     e0db2c65a7305ca92bf19fcaa0384e0d825b1a04a5590c0ca243e6192bebc425
D16     861279c4057d294ded74a5bf601aaaa7a75286d277d44f26213ceb9a1ff48b37
```

No Python `assert` or `__debug__` gate occurs in D17.  The explicit checks,
count guard and semantic-hash guard survive optimization, and the packet is
written only after they pass.

## 2. Factorization, interference and the D14 seal

The source now evaluates three explicit factors:

```text
A_j = boundary_envelope_j * orbit_sqrt_j * phase_j.
```

For `S=N_0`, the independent interval census gives `N_0=(3,4)` on
`(chain4,diamond4)`, hence phases `(-1,+1)`.  The equal envelope and unit raw
orbit factors produce

```text
A_equal = (-1/sqrt(2),+1/sqrt(2)).
```

Its norm is one and its coherent erasure probability is
`|A_0+A_1|^2/2=0`.

I separately rebuilt the `8 x 2` seal.  Its only nonzero cells are `(1,0)` and
`(7,1)`, so `V*V=I`, every supported output has collar bit one, and the two
record branches are orthogonal.  Applying the lifted erasure effect while
leaving the record unread gives

```text
(|A_0|^2+|A_1|^2)/2 = 1/2.
```

Thus the claimed `0` versus `1/2` comparison is exact and uses one Born
evaluation on each experimental arrangement.  The full recorded decoherence
matrix is `diag(1/2,1/2)`.

The code implements the before and after effects as two specialized helper
formulas rather than one operator and its typed lift.  That is a minor audit
weakness; direct matrix reconstruction confirms that the formulas represent
the intended same system effect on the sealed image.

## 3. Second boundary packet and fixed ingredients

The supplied second envelope `(3/5,4/5)` is normalized.  With the same phases,
unit orbit factor and exact same seal it produces

```text
A_second = (-3/5,+4/5),
P(record) = (9/25,16/25).
```

Both alternatives are positive, so both tower conditionals are defined.  The
source creates the action and seal once and reuses the same order objects in
both paths.  The difference cannot be attributed to a changed instrument or
action.

Check 15 itself freezes only the recomputed phase pair; it does not hash or
compare the domain and instrument.  Source inspection establishes reuse in
this revision, but a future receipt should make the full fixed tuple
`(Omega,S,R,types)` explicit instead of relying on object flow.

## 4. Orbit weights reach the record

The independent automorphism census is:

```text
|Aut(chain4)|   = 1
|Aut(diamond4)| = 2.
```

Raw square-root inverse-automorphism factors `(1,1/sqrt(2))` therefore give
record masses `(1,1/2)`, which normalize exactly to `(2/3,1/3)`.  The D17
calculation genuinely propagates these factors through the same seal before
normalization.

The executable uses envelope `(1,1)` for this path while the displayed uniform
path used `(1/sqrt(2),1/sqrt(2))`.  The common envelope scale cancels, so the
numbers remain correct, but the control does not isolate orbit convention with
every other factor literally held fixed.  Reusing the equal envelope with
orbit factors `(1,1/sqrt(2))` gives raw masses `(1/2,1/4)` and the same
normalized `(2/3,1/3)`.  Freeze that direct comparison.  Also retain the
current ceiling: the orbit-weighted result reaches one record partition but
not a projective tower or local-memory continuation.

## 5. Projective towers and validator attack

Both supplied families have positive support:

```text
equal:   000 -> 1/2,   101 -> 1/2
second:  000 -> 9/25,  101 -> 16/25.
```

After depth three, every stored positive cylinder has one child obtained by
appending zero.  I independently generated both families through depth 40;
every level normalized to one and every parent equaled the sum of its
children.  The deterministic rule is a valid induction to arbitrary finite
mark depth.  For either packet:

```text
P(z=1 | x=1,y=0)=1,
P(z=1 | x=0,y=0)=0.
```

The inconsistent normalized depth-two control correctly fails projectivity.

The repaired `is_projective` is adequate on the displayed towers, but hostile
inputs expose four API loopholes:

```text
{2:{(0,0):1}}                    -> accepted despite no depth one
{1:{(2,):1},2:{(2,7):1}}        -> accepted despite nonbinary marks
{}                               -> IndexError rather than False
projective_tower(...,max_depth=2)-> still returns depths 1,2,3
```

Gaps, negative masses and unnormalized levels are rejected correctly.  Require
depth one, validate the mark alphabet, handle the empty mapping, and reject a
requested depth below three or define its truncation semantics.  These bugs do
not affect the current two witnesses.

## 6. Causal-extension reconstruction stops short

The four tested predicates are genuine induced one-element extensions:

```text
root1  -> chain2
root1  -> anti2
chain2 -> chain3
anti2  -> vee3.
```

They can represent the root-to-depth-one and depth-one-to-depth-two transitions
of the mark tower.  The next transition is absent from the receipt:

```text
chain3 -> chain4
vee3   -> diamond4.
```

`chain3 -> chain4` passes with the existing labels.  The existing labeled
diamond does not extend `vee3` in its upper-left submatrix.  A relabeling with
old-to-new permutation `(3,0,1,2)` does pass and preserves the action phase;
in that presentation the newly inserted element is below all three prior
elements.  I verified both facts independently.

Therefore an exact final link exists, but D17 neither constructs nor checks
it.  It also supplies no map from bit histories to orders, no executable
truncation map, and no causal order at depths four through six.  Check 18 is
best read as “two transitions of a possible causal branch have order
examples,” not “the projective branches are realized by causal extensions.”

This is the main remaining overclaim.  The all-depth result is complete for a
supplied mark-cylinder law, not for causal-order growth.  The executable also
never evaluates the fixed action on the extension nodes.  The semantic ceiling
correctly admits that the towers remain supplied rather than action-derived.

## 7. Local memory and reset

Without importing D17, I rebuilt the D14 `X,M,Y,Z` network and compared every
history entry with the equal tower.  The tables agree exactly:

```text
depth 1: 0 -> 1/2, 1 -> 1/2
depth 2: 00 -> 1/2, 10 -> 1/2
depth 3: 000 -> 1/2, 101 -> 1/2
```

The network stores `X` in the carried bit `M`, later copies `M` into `Z`, and
seals visible `X,Y,Z` records sequentially.  It does not inspect a global
history tuple.  The two reset Kraus operators satisfy
`K_0^*K_0+K_1^*K_1=I_16`.  Resetting `M` before the final copy leaves only
density-matrix diagonals 0 and 8, each with mass `1/2`, so both branches end in
`z=0`.  This is a valid local finite-memory and deletion witness.

D17's local-memory call is fixed at half-half.  It is not the second
`(9/25,16/25)` packet used to close strict H7.  I parameterized the same D14
network independently with initial masses `(9/25,16/25)` and obtained exactly
the second tower through depth three, with projectivity intact.  The repair is
therefore mathematically available, but it is not part of the frozen receipt.
If H7 is read literally as requiring both packets to pass the integrated H6
gate, parameterize and execute both memory packets.

Finally, `M` is a local carrier only inside the standalone D14 four-bit
circuit.  It is not typed as a boundary or collar of any D16 causal order.
That missing identification is why the formal interacting-click-law problem
remains open.

## 8. Finding ledger

```text
C1 MAJOR    The action/record cell, extension skeleton and D14 memory circuit
            remain three separate compatibility witnesses; no integrated
            causal-history record packet exists.
C2 MAJOR    Check 18 stops before chain4/diamond4 and supplies no history-order
            map, causal truncation or all-depth causal extensions.
C3 MODERATE The second H7 packet is not executed through the local-memory H6
            network, although an exact parameterized repair was verified.
C4 MODERATE Orbit factors reach a record but are not varied with the exact
            same envelope in source and do not reach a tower.
C5 MODERATE “complete recorded history laws” is correct only for supplied
            mark cylinders, not causal-order histories.
C6 MINOR    The tower validator accepts missing depth one and nonbinary marks,
            crashes on empty input, and mishandles max_depth below three.
C7 MINOR    The fixed-domain/instrument check and common erasure operator are
            established by inspection rather than frozen directly.
```

## 9. Decision

**PASS** the exact finite subresult
`CAUSAL-ACTION-TO-MEASURE-NONSELECTION`: factorization, interference change,
record probabilities, positive-support boundary nonselection, orbit-to-record
weighting, projective mark induction and finite local-memory/reset compatibility
all survive independent reconstruction.

**MAJOR REVISION** remains necessary before calling the tower a causal-order
history measure or the packet an interacting click law.  Preserve
`INCOMPLETE-INVESTIGATION`, narrow source check 20 to “distinct supplied
projective mark-cylinder families,” and integrate one typed causal-order,
record, extension and memory packet before another closure claim.
