# D34d round 1 — quantum-process hostile review

**Frozen target:** commit `0119f4e`, especially
`v10/code/d34d_quantum_predictive_exact.py`, its committed output, and
`note-d34d-predictive-state-clock-status.md` §§2.4, 4/T4, 5/P7 and 7.3.
The classical/clock receipt is outside this stream except where the quantum
text borrows its Markov/lumpability language.

**Verdict:** **MAJOR REVISION** — the exact D34c diamond reconstruction, its
licensed coherent and path-recorded probabilities, the rebit tomography
identity, and the returning-boundary counterexample all survive independent
rebuild.  The central quantum narration nevertheless crosses two boundaries:
it calls a failure of record-state sufficiency a quantum non-Markov witness,
and it calls state tomography a multi-time predictive-closure result.  Those
are not equivalent without a fixed process tensor and an operational causal
break.

**Counts:** **0 BLOCKER / 2 MAJOR / 4 MINOR / 2 NIT**.

## 1. Independent reproduction

I reran the frozen D34d receipt without editing the tree:

```text
PYTHONHASHSEED=271828 python3 v10/code/d34d_quantum_predictive_exact.py
PYTHONHASHSEED=314159 python3 -O v10/code/d34d_quantum_predictive_exact.py
```

Both runs exit zero, print 7/7, and reproduce

```text
898b8a0039748760d83a151e93abdf6d01fb66888245d4d3626f8e95ac6bcf01
```

exactly.  I also reran the parent D34c receipt with
`PYTHONHASHSEED=161803` under `python3 -O`; it exits zero and reproduces all
14/14 gates.  The D34d program uses exact `Fraction` arithmetic throughout;
I found no float, tolerance, random draw, external dependency or
hash-iteration dependence.

## 2. Independent mathematical rebuild

### 2.1 D34c diamond functional — confirmed

Ordering the fine histories as `(s,p,o)`, the nonzero part of the functional
is four disjoint path blocks.  For fixed `(s,o)`,

```text
D_(s,o) = (1/8) [[1, eta], [eta, 1]],
eta = (-1)^(1+s+o).
```

Thus `(s,o)=(0,0),(1,1)` have the minus block and `(0,1),(1,0)` the plus
block.  Each block has eigenvalues `(1/4,0)`, so the full matrix is Hermitian,
strongly positive and rank four.  Its total incidence sum is one.

Summing both path amplitudes inside each durable `(s,o)` event gives

```text
P_coh(0,0), P_coh(0,1), P_coh(1,0), P_coh(1,1)
  = 0, 1/2, 1/2, 0.
```

The four durable events are mutually decoherent because different `(s,o)`
blocks have zero cross terms.  In the separately path-recorded experiment,
the receiver makes `p=0` and `p=1` orthogonal, so
`D_rec(h,h')=delta_(p,p') D(h,h')`; its durable probabilities are four
`1/4`s.  These are licensed probabilities, but they belong to two different
operational functionals.  They are not two readings of the same undecorated
fine-path diagonal.

### 2.2 Carrier witness — confirmed with a narrower meaning

Conditioning on `s`, the unrecorded path carrier is `|->` for `s=0` and
`|+>` for `s=1`; the support-excluded path receiver reduces the path carrier
to `I/2`.  Both have Z diagonal `(1/2,1/2)`.  A subsequent H and Z readout
therefore gives

```text
coherent:   o = 1-s with certainty,
recorded:   P(o=0)=P(o=1)=1/2.
```

This exactly proves that the declared durable record `s` and even the pair
`(s, Z-diagonal-of-P)` are not sufficient for predictions across those two
preparation/intervention contexts.  It does not yet prove that a fixed
multi-time quantum process is non-Markovian.

### 2.3 Real-qubit tomography identity — confirmed

For an arbitrary real symmetric two-level operator

```text
rho = [[a,b],[b,c]],
```

the three separately sampled effects give

```text
p0=a,  p1=c,  p+=(a+c+2b)/2,
b=p+-(p0+p1)/2.
```

Hence `P0,P1,P+` are informationally complete for the real-symmetric
two-level operator space.  This is a universal algebraic identity, stronger
than the program's six-state regression.  It is not informationally complete
for a complex qubit because it has no Y-sensitive effect.

### 2.4 Returning boundary — confirmed

The two exact joint states

```text
rho_corr = 1/2 (|00><00| + |11><11|),
rho_anti = 1/2 (|01><01| + |10><10|)
```

both reduce to `I/2` on P.  `CNOT(E->P)` sends their P reductions to `P0`
and `P1`, respectively.  Therefore the reduced state on P is not sufficient
when E may return.  Retaining the joint `P,E` boundary state is sufficient
for this specimen.  The calculation alone does not decide whether E should
be retained as local boundary state or eliminated into a process tensor.

## 3. Major findings

### M1 — Q3/Q7 do not establish quantum non-Markovianity of one process

Q3 compares a coherent past with a path-recorded/dephased past.  Those are
different prior instrument contexts: one appends an orthogonal path receiver
and the other does not.  Their equality on the projected record `s` and their
different future H/output statistics show that `s` is **not an operationally
sufficient state across the admitted contexts**.  That is a valid and useful
result.

It is not by itself an operational quantum-Markov test.  The standard
process-tensor condition asks whether, after a causal break blocks information
flow through the present system, future statistics remain dependent on past
instruments.  D34d constructs neither a multi-slot process tensor nor a causal
break.  It also does not exhibit two record histories generated under one
fixed instrument schedule with the same current visible record and different
future record laws.  Consequently the phrases

```text
QUANTUM OBSERVABLE NON-LUMPABILITY
durable classical shadow can be non-Markov because it omits coherence
D34c diamond supplies the quantum non-lumpability witness directly
```

are wider than Q2/Q3.  Classical strong lumpability is a property of a fixed
transition kernel; changing the past instrument cannot be silently treated as
choosing another hidden state of that kernel.  The relevant operational
quantum distinction is described by the causal-break/process-tensor criterion
of [Pollock et al., *Operational Markov Condition for Quantum
Processes*](https://arxiv.org/abs/1801.09811).

**Required repair — either route is acceptable:**

1. re-label Q3 and §7.3 as `DURABLE-RECORD OPERATIONAL INSUFFICIENCY ACROSS
   DECLARED PAST INSTRUMENTS`, and explicitly leave quantum Markovianity open;
   or
2. build a fixed three-slot process/comb and an exact causal-break witness.
   The current Q5 states already suggest the test: generate `rho_corr` and
   `rho_anti` through two allowed past instruments of one process; at the
   middle slot select the same nonzero P-measurement outcome and reprepare the
   same P state; then let E return through `CNOT(E->P)`.  If the future remains
   `P0` versus `P1`, with every conditioning probability printed, that is a
   genuine operational memory witness.  The process and allowed instrument
   family must be stated once and held fixed.

### M2 — Q4 proves state tomography, not multi-time predictive closure

The exact formula in §2.3 proves that a present real density matrix is
identifiable from three terminal-effect settings.  It does not by itself prove
that the density matrix screens the complete past from **all future
instruments**.  That stronger statement additionally requires the future law
to be a fixed sequence of CP instruments acting only on this carrier and fresh
uncorrelated ancillas.  If an old factor can return, Q5 itself proves that the
reduced carrier state fails.

The program never defines the claimed “declared real one-qubit future
instrument algebra”; `EFFECTS=(P0,P1,PPLUS)` is a test set of terminal effects,
not a normalized instrument and not a set of multi-time transformations.  It
tests injectivity on six selected states, not equality of future combs for two
different pasts with the same retained state.  Thus the headline
`FINITE OPERATIONAL PREDICTIVE CLOSURE` and P7's requested “all future
instruments” gate are not earned as written.

**Required repair:** define one of the following objects and use its correct
noun.

- For the narrow result, declare the isolated **rebit terminal-effect
  algebra** `span_R{P0,P1,P+}` and prove the symbolic reconstruction identity
  for arbitrary `[[a,b],[b,c]]`.  Call this tomographic completeness, not
  process closure.
- For predictive closure, declare the full future instrument/comb family,
  prove that every allowed future statistic factors through the retained
  boundary object, and gate operational equality for paired histories.  If
  returning factors are excluded, state the fresh-product/no-return
  hypothesis.  If they are included, the predictive object must be the joint
  boundary state or a process tensor, not P's reduced density matrix.

## 4. Minor findings

### m1 — The recorded-path probability is not independently fail-closed in D34d

`coarse_probability(..., False)` merely sums the diagonal of the coherent D.
That number becomes a licensed probability only because D34c separately
constructed the support-excluded orthogonal path receiver and proved the
masked functional.  D34d's prose says recording/dephasing, so the number is
right, but its own gate does not construct or test `D_rec`.

**Repair:** build `D_rec[i][j]=D[i][j]` iff `p_i=p_j`, gate its Gram/PSD and
normalization properties, and incidence-coarse that functional.  Rename the
helper so diagonal selection is never called a coarse probability of D.

### m2 — Joint boundary state and process tensor are alternatives, not synonyms

Q5 proves exactly that a larger joint `P,E` boundary state is required if E
can return.  If that enlarged state is retained, the total `P,E` evolution is
an ordinary closed Markov update.  A process tensor is the appropriate reduced
description when E is omitted and arbitrary interventions on P across several
times are admitted.  The repeated phrase `joint boundary/process memory`
leaves this architectural choice unresolved.

**Repair:** print two separate scorecard rows: `(a)` joint-boundary
sufficiency with E retained; `(b)` reduced-process memory after E is eliminated,
which remains open until the causal-break/process-tensor gate in M1 is built.

### m3 — Q6 proves a sampled product-factor control, not the stated universal

The code tests `rho_local tensor rho_remote` for 3 local states, 4 remote
states and 3 local effects, plus commuting X permutations.  The narration says
“every normalized remote factor” and “all declared local future
probabilities.”  Those universal statements follow analytically for arbitrary
trace-one product factors, but not from the finite sample as gated.  Initially
correlated local/remote states are not product factors; their correct retained
object is the local reduced state while the components remain forever
disconnected.

**Repair:** either label Q6 a finite regression or add the algebraic partial-
trace theorem for arbitrary normalized sigma and arbitrary local effect/map.
State explicitly whether initial cross-component correlations are forbidden.

### m4 — “Real qubit” must stay a rebit scope condition everywhere

The three-effect signature cannot recover the imaginary off-diagonal/Y
component of a general qubit.  D34c's displayed circuit and tested states are
real, so no present number fails.  But any later complex phase gate or general
qubit input leaves the Q4 state representation incomplete.

**Repair:** use `rebit` or `real-symmetric carrier sector` consistently, and
make expansion to the complex qubit algebra an explicit open requiring one
Y-sensitive setting and complex carrier arithmetic.

## 5. Nits

1. Q1's `rank` variable is incremented once per presumed block rather than
   row-reducing D.  The determinant-zero/nonzero-trace checks do logically
   imply rank one per disjoint block, so the answer four is valid; rename it
   `rank_from_block_proof` or compute it directly.
2. `P0,P1,P+` are three effects sampled in separate settings, not one
   three-outcome instrument because they do not sum to identity.  The prose
   should say “tomographic effect set.”

## 6. Claim-by-claim disposition

| Claim | Disposition |
|---|---|
| Exact reproducibility under fresh salts/optimization | **PASS** |
| D34c signed 8x8 functional, Hermiticity, normalization, rank four and strong positivity | **PASS** |
| Coherent durable `(s,o)` probabilities `(0,1/2,1/2,0)` | **PASS**, licensed decoherent partition |
| Path-recorded durable probabilities four `1/4`s | **PASS from D34c parent**, harden D34d gate per m1 |
| Same durable `s`/Z diagonal but different H-output laws | **PASS** |
| Durable `s` is not an operationally sufficient predictive state across the two contexts | **PASS** |
| Fixed observed quantum record process is non-Markov / non-lumpable | **NOT ESTABLISHED — M1** |
| `P0,P1,P+` are informationally complete for real-symmetric two-level states | **PASS analytically** |
| Six tested states establish all-state tomography | **Regression only**; universal identity is available |
| Rebit density matrix closes all declared multi-time future instruments | **NOT ESTABLISHED — M2** |
| Reduced P state fails if correlated E can return | **PASS** |
| Joint P,E boundary state suffices for the displayed return interaction | **PASS** |
| Q5 establishes a process-tensor memory witness | **NOT YET — M1/m2** |
| Forever disconnected product factor is irrelevant to local effects | **PASS**, sampled plus elementary theorem |
| Arbitrary correlated remote/process locality theorem | **NOT GATED — m3** |
| Timed/direct-integral quantum law, infinite memory bound, universal SHARD Markov theorem | Correctly **NOT CLAIMED** |

## 7. Adjudicated claim ceiling

At baseline `0119f4e`, the strongest quantum wording fully supported is:

> **FINITE D34c DURABLE-RECORD INSUFFICIENCY AND REBIT BOUNDARY-STATE
> CHARACTERIZATION:** the exact diamond functional has licensed coherent and
> path-recorded durable statistics that differ; the durable classical record
> does not retain the rebit coherence needed to predict the declared H/output
> test; real-symmetric one-carrier states are tomographically determined by
> `P0,P1,P+`; and a reduced carrier state is insufficient if a correlated
> boundary factor can return, while the displayed joint boundary state is
> sufficient.  A fixed multi-time process-tensor Markov/non-Markov theorem is
> not yet established.

The combined D34d classical result may still say that **its classical visible
specimen** is non-Markov by exact failure of lumpability.  The quantum stream
must not borrow that noun until M1 is repaired.  Once M1 is narrowed or supplied
with the exact causal-break witness and M2 distinguishes tomography from
process closure, this stream can move directly to delta review; the D34c
matrix, fractions and Q5 boundary calculation do not need reopening.
