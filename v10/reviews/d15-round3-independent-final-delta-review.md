# D15 hostile review, round 3: independent final-delta audit

**Referee:** independent clean-room focused stream  
**Date:** 2026-07-11  
**Verdict:** **PASS AT THE FINITE REGULATED-DICTIONARY WITNESS SCOPE**  
**Formal D15 status:** **`INCOMPLETE-INVESTIGATION`**

The final D15 delta is real and reproducible.  The authoritative executable
passes 28/28 under normal and optimized Python with byte-identical stdout.
Source, generated packet, semantic payload, D13 arithmetic dependency, and
D14 bridge dependency all match the updated receipt.

The four focused repairs pass independent probes:

1. every source and target port in the finite dictionary has owner `cell-A`;
2. the action-derived record is sealed, owned by `cell-A`, has persistent id
   `R`, and a direct D14 record flip raises;
3. the four-bit CNOT placement takes the supplied two-bit CNOT matrix as an
   argument—passing identity instead produces identity rather than the memory
   copy—and the composed memory has exact visible support `000/101`;
4. summing the hidden memory explicitly gives
   `P(z=1|y=0,x=1)=1` and `P(z=1|y=0,x=0)=0`.

The working theorem now states the finite regulator and gauge ledger exactly:
the regulator is the printed finite binary sum, the gauge group/quotient are
trivial, the basis and vertex normalization are fixed, all ports share one
owner, no cross-component join occurs, and phases are dimensionless.  It
therefore continues to withhold metres, seconds, `G`, gravity, continuum
covariance, `3+1`, and every V9 holdout.

No focused clean-room opening remains against the finite witness.  This PASS
does not promote it into a complete D15 action packet.

## 1. Reproduction

### Commands

```bash
PYTHONDONTWRITEBYTECODE=1 python3 v10/code/d15_regulated_action_dictionary_exact.py
PYTHONDONTWRITEBYTECODE=1 python3 -O v10/code/d15_regulated_action_dictionary_exact.py
PYTHONDONTWRITEBYTECODE=1 python3 v10/code/d15_regulated_action_dictionary_exact.py | shasum -a 256
PYTHONDONTWRITEBYTECODE=1 python3 -O v10/code/d15_regulated_action_dictionary_exact.py | shasum -a 256
shasum -a 256 v10/code/d15_regulated_action_dictionary_exact.py
shasum -a 256 v10/data/d15-regulated-action-dictionary-exact.json
shasum -a 256 v10/code/d13_finite_kernel_no_go_exact.py
shasum -a 256 v10/code/d14_action_record_bridge_exact.py
```

Both direct runs completed with the same 28 labels and ended in:

```text
PASS 028: pre-final exact check count is frozen
CHECKS PASSED: 28/28
SEMANTIC SHA256: 12f73918e7876a2f423d1d4596163e787f52ac50332f2d59bb941c0381f499fe
SOURCE SHA256: 9f539129d5712d28b86d89637248a0fe3b60678fcc29fcddf2e5e675aa8fb4b9
VERDICT: REGULATED-ACTION-DICTIONARY-WITNESS-PASSED
```

Full stdout hashes:

```text
normal  06c5ab5d6455942e14835814914a57f0cc6dad4a4f30997bc504d04153446408
-O      06c5ab5d6455942e14835814914a57f0cc6dad4a4f30997bc504d04153446408
```

Current authoritative hashes:

```text
9f539129d5712d28b86d89637248a0fe3b60678fcc29fcddf2e5e675aa8fb4b9  D15 source
b9bc2fc3a2c8dc9342d985df55f2298db182e8cf0a0e97fc22fd8de5fa2d3b41  D15 packet
12f73918e7876a2f423d1d4596163e787f52ac50332f2d59bb941c0381f499fe  semantic payload
1ea9969cb3e61b805e031ea7b3b025e3a1f88b56e268337824c6a6abcba1cf45  D13 dependency
e0db2c65a7305ca92bf19fcaa0384e0d825b1a04a5590c0ca243e6192bebc425  D14 dependency
```

I independently selected and compactly serialized the semantic fields and
reproduced `12f73918...`.  Every value in
`d15-regulated-dictionary-pre-review-receipt.md` matches current bytes.

No Python `assert`, optimization-dependent branch, floating arithmetic,
random source, or self-read packet supplies a gate.

## 2. Independent delta probes

Command:

```bash
PYTHONDONTWRITEBYTECODE=1 python3 /tmp/d15_round3_delta_probes.py
```

Relevant output:

```text
owners ('cell-A','cell-A','cell-A','cell-A')
record identity True cell-A R
direct flip rejected protected record overwrite
kernel-dependent placement True True
full visible support {(0,0,0): 1/2, (1,0,1): 1/2}
full conditional p1/p0 1 0
D15 ROUND3 DELTA PROBES COMPLETE
```

The probe constructs fresh objects and recomputes the full marginal over the
hidden memory; it does not merely inspect the executable's PASS strings.

## 3. Owned single-component packet

The D14 objects are now:

```text
system       owner=cell-A
environment  owner=cell-A
record       owner=cell-A, sealed=True, record_id=R
collar       owner=cell-A
```

The composed seal has only one source component and one target component.  It
does not exercise or silently create a cross-component join.  The finite S6
claim is therefore exactly a one-owned-cell construction; the general
join-entitlement origin remains open.

The executable also constructs the raw middle-bit flip against the actual D14
seal target.  D14 rejects it with `protected record overwrite`.  This is a
direct negative gate, not an inferred persistence claim.

## 4. Memory built from the action kernel

`cnot_four(two_bit_kernel,control,target)` now embeds the matrix passed to it.
For each four-bit input it extracts the selected two-bit input, applies every
nonzero entry of the supplied kernel, and writes the resulting selected bits
back into the four-bit output.

Two placements compose:

```text
CNOT X -> M,
CNOT M -> Z.
```

Passing the action-derived CNOT gives the memory permutation; passing the
two-bit identity gives the 16-dimensional identity.  Thus the memory is
load-bearingly connected to the D15 action kernel rather than a parallel truth
table or D13 import.

## 5. Full visible non-Markov reconstruction

The source's compressed `x=1` ratio divides the only supported `x=1,y=0,z=1`
mass by itself.  To guard against a vacuous conditional, I independently
summed every hidden-memory value for all eight visible histories.

The only nonzero masses are:

```text
P(x=0,y=0,z=0)=1/2,
P(x=1,y=0,z=1)=1/2.
```

Consequently the complete denominators give:

```text
P(z=1|y=0,x=1)=1,
P(z=1|y=0,x=0)=0.
```

This is genuinely non-Markov in the visible variables because the common
current value `y=0` does not screen off the earlier `x` record.

As a nonblocking readability hardening, a future source revision could compute
these full hidden-memory sums directly rather than the compressed diagonal
ratios.  The independent result shows no current mathematical gap.

## 6. Regulator, gauge, and unit ledger

The working theorem explicitly records for this witness:

```text
regulator                finite binary boundary/history sum;
gauge group/quotient     trivial;
boundary basis           fixed;
vertex normalization     fixed supplied measure;
component ownership      one owner, cell-A;
cross-component joins    none exercised;
action phases            dimensionless.
```

This resolves the former ambiguity about whether the toy carried unprinted
gauge fixing, edge modes, or continuum regulator data.  It does not turn a
trivial gauge group into a gauge/gravity construction.

The same paragraph explicitly says there is no metre/second/`G` bridge and
that the witness is not a discretization of EFT4 or gravity.  The semantic
packet retains the ceiling “does not select nature's action or establish
generally covariant gravity.”

## 7. Receipt and claim consistency

The current documents agree:

```text
executable witness  REGULATED-ACTION-DICTIONARY-WITNESS-PASSED
formal D15 verdict  INCOMPLETE-INVESTIGATION
scope               finite Z2/qubit regional action; nongravitational
```

The updated receipt freezes all requested hashes and 28/28.  The working
theorem calls the finite S4 instance closed and S5 conditional.  The UV audit
still treats every UV candidate as incomplete, distinguishes survival from
selection, and leaves the V9 holdout closed.

## 8. Final focused disposition

| Delta | Independent result |
|---|---|
| 28/28 normal and `-O` | pass, byte-identical |
| source/packet/semantic/dependencies | exact |
| all D14 packet ports owned by `cell-A` | pass |
| cross-component join absent | pass at one-cell scope |
| direct protected record flip | rejected |
| four-bit memory uses supplied two-bit CNOT | pass |
| identity-kernel negative control | produces identity |
| full visible support | `000/101`, each `1/2` |
| exact non-Markov conditionals | `1/0` |
| trivial regulator/gauge ledger | explicit and consistent |
| general covariance/gravity promotion | correctly refused |

**Round-3 independent final-delta verdict: PASS at the finite regulated-action
dictionary witness scope.  Formal D15 remains `INCOMPLETE-INVESTIGATION`.**

`git diff --check` passed before this review was written.  No primary D15 file
was edited by this referee.

