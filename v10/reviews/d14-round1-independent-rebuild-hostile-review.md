# D14 hostile review, round 1: independent clean-room rebuild and reproducibility

**Referee:** independent clean-room/reproducibility stream  
**Date:** 2026-07-11  
**Verdict:** **MAJOR REVISION — CURRENT PROTOCOL VERDICT `INCOMPLETE-INVESTIGATION`**

The frozen executable is exactly reproducible.  It passes 30/30 under normal
and optimized Python with byte-identical stdout; its source, local arithmetic
dependency, generated packet, semantic payload, and stdout hashes all match
the pre-review receipt.  The category/coherence, interference, finite frame,
history-projectivity, memory, and no-signalling witness calculations are real
exact calculations rather than floating-point or `assert` artifacts.

The advertised theorem nevertheless does not yet pass its frozen protocol.
Two promised type/countercontrol claims are directly false in the executable
API: a record-overwrite map is successfully constructed and composed, and a
seal-like map without a collar successfully feeds later dynamics.  The
reported “overwrite rejected” check only observes that the already accepted
map fails a diagnostic predicate.  The history proof also appends an
orthogonal whole-history register mathematically but does not construct the
corresponding sequential local protected instruments inside `FSDiam`.

There are two claim-manifest failures.  The construction begins with supplied
kernels and supplied record instruments, while the physical-action-to-kernel
dictionary is explicitly left open; the proved object is therefore a
kernel/instrument-to-record-history bridge, not yet an action-to-record bridge.
And the executable and pre-review receipt emit the positive verdict even
though the protocol defines that verdict to require B12 hostile closure,
which by status has not occurred.

These are load-bearing but repairable openings.  The exact finite algebra
survives; the present theorem name, protected-category implementation, and
protocol verdict do not.

## 1. Frozen artifacts and exact reproduction

### Commands

From `/Users/felixrobles/workspace/isp` I ran:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 v10/code/d14_action_record_bridge_exact.py
PYTHONDONTWRITEBYTECODE=1 python3 -O v10/code/d14_action_record_bridge_exact.py
PYTHONDONTWRITEBYTECODE=1 python3 v10/code/d14_action_record_bridge_exact.py | shasum -a 256
PYTHONDONTWRITEBYTECODE=1 python3 -O v10/code/d14_action_record_bridge_exact.py | shasum -a 256
shasum -a 256 v10/code/d14_action_record_bridge_exact.py
shasum -a 256 v10/code/d13_finite_kernel_no_go_exact.py
shasum -a 256 v10/data/d14-action-record-bridge-exact.json
```

### Results

Both direct executions printed the same 30 labels, ending in:

```text
PASS 030: pre-final exact check count is frozen
CHECKS PASSED: 30/30
SEMANTIC SHA256: 3a1c766d1f82986f667b1897b817f44b51250db204659503592f545ce9807490
SOURCE SHA256: 287c47f8cee8593956918b62f1c4786506b2af6dd5d9e5568acea73e7051c84f
DEPENDENCY SHA256: 1ea9969cb3e61b805e031ea7b3b025e3a1f88b56e268337824c6a6abcba1cf45
VERDICT: FINITE-ACTION-TO-RECORD-BRIDGE-PROVED
```

The complete stdout hashes were byte-identical:

```text
normal  05edee685a6905408d331cb3546db4edbc2bdaeae6fd154d6f0ec8d2bc80bdbe
-O      05edee685a6905408d331cb3546db4edbc2bdaeae6fd154d6f0ec8d2bc80bdbe
```

Current file hashes were:

```text
287c47f8cee8593956918b62f1c4786506b2af6dd5d9e5568acea73e7051c84f  D14 source
1ea9969cb3e61b805e031ea7b3b025e3a1f88b56e268337824c6a6abcba1cf45  D13 arithmetic dependency
9217316b6a98b3b8d42920214933c1d5832137abeb72fedee65a7fbcffc51c5f  generated D14 JSON
```

I independently rebuilt the canonical semantic object from the JSON keys
`schema`, `scope`, `arithmetic`, `checks_passed`, `history_depths`,
`nonmarkov`, and `verdict`, serialized it with sorted compact JSON exactly as
the source does, and obtained:

```text
3a1c766d1f82986f667b1897b817f44b51250db204659503592f545ce9807490
```

Every frozen hash in `d14-pre-review-receipt.md` is therefore accurate.

## 2. Runtime, optimization, dependencies, and output provenance

The D14 source contains no Python `assert` statement, no `__debug__` branch,
and no optimization-dependent gate.  Its `check` routine uses an explicit
conditional followed by `raise AssertionError`, so `python3 -O` does not
remove it.  The explicit check-count and semantic-hash gates likewise use
ordinary conditionals.  This explains, and the reruns confirm, normal/`-O`
identity.

Direct imports are Python standard-library modules plus the local
`d13_finite_kernel_no_go_exact.py`.  That dependency itself imports only the
standard library.  D14 hashes the exact sibling dependency before its first
substantive category cell.  I found no undeclared third-party package,
network read, environment input, random seed, clock, locale, or numerical
precision dependency.

The phrase “dependency-free executable” in Paper 15 is not literal: D14 has a
declared, hash-locked local source dependency.  “No third-party dependency”
would be exact wording.  This is editorial, not a reproducibility failure.

The program writes its JSON only after all 30 checks and the frozen semantic
hash pass.  No check reads that JSON.  Re-running regenerates the same packet
hash, so the proof is not authenticated by reading its own output.  The
packet and full-stdout hashes are external receipt claims rather than internal
gates, but both independently match.

## 3. Independent exact reconstruction

I wrote a scratch reconstruction using only `dataclasses` and
`fractions.Fraction`, with a fresh implementation of `Q(sqrt(2))`, matrix
multiplication, sequential projective branches, and the two-CNOT memory
permutation.  It did not import D14 until after its positive calculations.

Command:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 /tmp/d14_cleanroom_rebuild.py
```

Independent output included:

```text
independent interference 1 1/2
independent history/projectivity [1, 1, 1]
independent memory visible histories (0, 0, 0) (1, 0, 1)
```

Thus the following substantive witness claims reconstruct independently:

- coherent `H-H` evolution returns probability one while insertion of the
  intermediate computational record gives one half;
- the supplied projective-instrument witness normalizes at depths 1, 2, and
  3 and its child sums equal each parent cylinder;
- the reversible memory map sends the two input branches to visible histories
  `(0,0,0)` and `(1,0,1)`, giving the printed deterministic conditionals.

The free strict symmetric-monoidal evaluation theorem and the adjacent-swap
connectivity of finite linear extensions are standard and the paper's finite
proof is mathematically adequate at the explicitly free-category scope.
Nothing in this review refutes those algebraic results.

## 4. Fatal and major opening ledger

### O1 — protected record overwrite is accepted, not rejected

**Severity:** critical for B0/B5 and the durable-record theorem.  
**Status:** open.

`Port.sealed` is stored but neither `Mor.__post_init__`, `compose`, nor
`tensor` enforces it.  The source itself constructs `overwrite_mor` as a valid
`Mor`.  Check 22 then tests only

```python
not preserves_record(overwrite_mor, 1, 1)
```

and prints `sealed-record overwrite control is rejected`.  No rejection has
occurred.

My direct API probe constructed a two-level sealed-record flip and composed it
with an identity:

```text
overwrite Mor constructed overwrite_probe
overwrite composes True
preserves_record diagnostic False
```

This contradicts protocol B0 (“attempts to overwrite sealed records must be
rejected”), the B5 countercontrol, the theorem note's “rejected by the
protected type rule”, and Paper 15's “explicit record-flip control is
rejected”.

**Required repair:** define the licensed protected morphism category in code,
validate generator admission against sealed input/output ownership, and make
construction or composition of the flip raise.  Then prove that identity,
composition, tensor, symmetry, controlled read, and fresh-output extension
preserve the licensed class.  Merely renaming `preserves_record` to a
diagnostic is insufficient for the current theorem.

### O2 — omitting the live collar does not prevent continuation

**Severity:** major for B5 and mandatory countercontrol 5.  
**Status:** open; counterexample executed.

The code proves that its chosen seal writes collar value `1`.  It does not
prove the frozen countercontrol “omitting a live collar prevents
continuation.”  `FSDiam` has no opportunity rule requiring a live collar for
a later generator.

I constructed an isometric seal-like map `S -> S tensor R` with no collar,
then a later system-only map `S tensor R -> S tensor R`.  `compose` accepted
the continuation:

```text
no-collar continuation constructed True
```

Paper 15's statement that a record without a collar is terminal is therefore
not a property of the implemented category.

**Required repair:** type event opportunities so only a declared live-collar
token can authorize the relevant continuation, then execute a negative
no-collar composition test.  Alternatively withdraw terminality and mandatory
countercontrol 5, leaving the collar as carried but not causally necessary.

### O3 — the proved map begins after the action-to-kernel bridge

**Severity:** major claim-scope and manifest error.  
**Status:** open.

The frozen source data are typed carriers, supplied matrices, a supplied
boundary state, and a supplied record instrument/protected algebra.  There is
no action functional, path measure, gauge quotient, boundary measure, or map
from `exp(iS)` to those matrices.  Paper 15 section 12 explicitly lists

```text
physical field configurations and regional action
  -> finite boundary carriers and gluing measure
  -> typed local diamond grammar and kernels
```

as a missing dictionary.  Consequently D14 currently proves a finite
**supplied-kernel-and-instrument-to-record-history** bridge.  It does not yet
prove the filenames, title, semantic verdict, and theorem name
`FINITE-ACTION-TO-RECORD-BRIDGE-PROVED` literally.

**Required repair:** either narrow the title, theorem, packet schema/verdict,
and manuscript claims to the object actually proved, or construct one
nontrivial action-to-kernel/gluing-measure example with gauge/boundary data and
carry it through the record bridge.  B10's honest primitive list must control
the headline.

### O4 — positive protocol verdict is premature before B12

**Severity:** major manifest/status failure.  
**Status:** open by definition.

The protocol defines the positive verdict to require “B0–B10 and B12 pass”
and defines `INCOMPLETE-INVESTIGATION` when a promised review is missing.  The
theorem note and Paper 15 are explicitly `pre-hostile-review`; the receipt is
explicitly `pre-review`; and this is the first clean-room hostile review.
Nevertheless the JSON, stdout, abstract, theorem, and receipt already state
the positive protocol verdict.

Even absent O1–O3, B12 cannot be true before hostile closure.  At this round's
state the formal protocol verdict is `INCOMPLETE-INVESTIGATION`.

**Required repair:** distinguish a candidate/executable theorem label from
the formal protocol verdict and promote only after all three hostile streams
close.  Do not hash a future B12 outcome into a pre-review semantic packet.

### O5 — history records are appended globally rather than executed locally

**Severity:** major proof/construction gap for B5–B7 and “without a global
clock”.  
**Status:** open, though a standard repair is available.

`recorded_branch(history, u, initial)` first computes the complete system
class operator, constructs a basis vector whose dimension is `2**depth`, and
tensors the final system branch with that whole-history label.  No sequential
record generator inside `FSDiam` produces this growing protected string, and
the separate four-level B5 seal is never composed with the two-level B6/B7
history process.

Orthogonalizing completed histories makes the off-diagonal check true by
construction.  The intended local theorem can be valid, but it needs the
missing construction: for each complete instrument, build the local
Stinespring/isometry

```text
W |psi> = sum_z M_z |psi> tensor |z>_fresh-record,
```

prove `W^dagger W=I`, compose these generators through depths 1–3, and recover
the same class-operator strings and projective cylinders by tracing only the
licensed carriers.  This would show that the orthogonal history register is
accumulated locally rather than written after the entire history is known.

## 5. Secondary openings and weak checks

### O6 — only half of memory countercontrol 6 is executed

The memory check traces/sums over the hidden bit and really obtains visible
non-Markov conditionals.  But the mandatory countercontrol also says deleting
the memory changes the process.  No reset/deletion channel or comparison law
is executed or proved.  Add a control that resets/traces-and-reprepares `M`
before `M -> Z`; it should change the `(1,0,1)` branch to `z=0`.

### O7 — the positivity and disintegration predicates are weaker than labels

Check 24 tests `p.im == 0` and `p.re.a >= 0`, but does not test the
`sqrt(2)` coefficient `p.re.b` or implement the sign of a general `Q2`
element.  Its `p.norm2() == p.re*p.re` clause is automatic once the imaginary
part is zero.  The current witness values are independently verified rational
nonnegative numbers, so the result is true; the executable predicate is still
too weak for its label.  Assert `p.re.b == 0` for this witness or implement an
exact quadratic-field sign test.

Check 27 computes the intended cylinder ratio but asserts only that the
rational coefficient lies between zero and one.  It omits zero imaginary and
quadratic coefficients and does not freeze the actual value.  For this
witness the exact result is `1/2`; assert it directly.

### O8 — countercontrol 7 is chiefly definitional

The code checks equality of two schedules for one disjoint diagram, and the
paper supplies the general adjacent-swap proof.  Because schedule labels are
not data in `Mor`, their observational absence is defined rather than
independently attacked.  This is acceptable for a free-category theorem but
must remain explicitly conditional: it does not prove that every physical
diamond theory's construction labels are gauge.

## 6. B0–B12 evidence audit

| Gate | Evidence | Round-1 result |
|---|---|---|
| B0 typed category | typed dimensions reject one mismatch; sealed flag unenforced | **fail** |
| B1 coherence | exact units, associativity, interchange, symmetry cells plus free-SMC proof | pass at frozen free scope |
| B2 order gauge | one nontrivial schedule cell plus adequate finite adjacent-swap proof | pass conditionally |
| B3 coherent gluing | `1` vs `1/2`, row-normalization control, explicit internal sum | pass |
| B4 frames | exact internal unitary cancellation, probability and one `SL(2,C)` cone cell | pass at finite stated scope |
| B5 records/birth | isometry/read/persistence witness; overwrite and no-collar rules fail | **fail** |
| B6 decoherence | exact orthogonal-string calculation; local sequential realization missing | **incomplete** |
| B7 projectivity | depths 1–3 exact; completeness induction sound | pass conditional on complete instruments |
| B8 memory | exact unitary visible non-Markov cell; deletion control absent | partial |
| B9 locality | interchange plus one exact Bell marginal; continuum scope withheld | pass at finite scope |
| B10 action scope | primitive list honest, but title/verdict outrun it | **fail claim manifest** |
| B11 handoff | missing action/region/instrument/units dictionary explicitly listed; holdout withheld | pass |
| B12 hostile closure | round 1 has major open findings; other streams not yet closed | **fail/currently open** |

## 7. Mandatory countercontrol audit

| Countercontrol | Result |
|---|---|
| ill-typed boundary gluing | pass |
| sealed-record overwrite rejected | **fail: accepted, then diagnosed** |
| intermediate record changes interference | pass |
| local row normalization changes composition | pass |
| omitted collar prevents continuation | **fail: explicit continuation constructed** |
| hidden-memory marginal is visibly non-Markov | pass |
| deleting memory changes process | missing |
| global schedule label absent from evaluated map | conditional/theoretical pass |

## 8. Claim, filenames, and status determination

The filenames and headlines consistently say “action-to-record”, but the
mathematical input begins at supplied finite kernels and a supplied record
instrument.  This consistency of naming does not make the name accurate.  The
pre-review status labels are otherwise honest: protocol frozen, theorem
pre-hostile, paper draft, and receipt pre-review.  Their embedded positive
verdict is the inconsistent part because the protocol reserves it for B12
closure.

The defensible round-1 result is:

```text
EXACT FINITE FREE-SMC KERNEL EVALUATION          = REPRODUCED
FINITE INTERFERENCE/FRAME/HISTORY/MEMORY CELLS  = REPRODUCED
PROTECTED RECORD MORPHISM CATEGORY              = NOT IMPLEMENTED
LIVE-COLLAR NECESSITY                           = REFUTED IN CURRENT API
LOCAL SEQUENTIAL HISTORY-RECORD CONSTRUCTION    = INCOMPLETE
ACTION-TO-KERNEL DICTIONARY                     = OPEN
B12 HOSTILE CLOSURE                             = OPEN
FORMAL D14 PROTOCOL VERDICT                     = INCOMPLETE-INVESTIGATION
```

## 9. Final verdict

**MAJOR REVISION.**  Preserve the exact algebraic cells and the standard
free-category evaluation theorem.  Before round 2, repair or withdraw the
protected-overwrite and collar countercontrols, locally realize the sequential
history instrument, execute memory deletion, strengthen the two weak numeric
predicates, narrow “action-to-record” to the proved kernel/instrument bridge
unless an actual action-to-kernel map is added, and keep the formal verdict
`INCOMPLETE-INVESTIGATION` until B12 truly closes.

`git diff --check` passed before this review was written.  No primary D14 file
was edited by this referee.

