# D34d — predictive state, observable memory and clock status

**Status:** ROUND-1 REPAIR PIN, 2026-07-13. Sections 1–6 were frozen after
D34c's terminal finite typed-DAG compatibility result and before any D34d
executable or numerical receipt. Section 7 records the provisional receipt;
section 8 records its independent rejection and freezes the repair before the
replacement executables. The investigation incorporates the external desired
theorem relayed by the user, but does **not** adopt that theorem as stated.

## 1. The question

The proposed reconciliation is:

> a complete SHARD history law may be Markov after the right state enlargement,
> while the durable record process seen by an observer is generally
> non-Markovian.

There is a true statement nearby, but three different claims must not be
collapsed:

1. remembering the entire past always makes an ordinary history law Markov;
2. a **local, record-carried** predictive state may or may not be sufficient;
3. forgetting that predictive state may make the visible record process
   non-Markovian, but does so only when the projection is not lumpable.

Claim 1 is a representation tautology, not a locality theorem. Claim 2 is the
physical target. Claim 3 is a conditional theorem, not a universal fact.

The quantum D34c object requires a parallel statement in terms of future
instruments/history functionals. Fine-path diagonal probabilities are not a
licensed substitute when alternatives interfere.

## 2. Frozen object types

### 2.1 Classical history law

Let `mu` be a consistent law on timed typed actor histories with filtration
`F_t`. The **history state** is

```text
X_t = the complete marked history through t.
```

Whenever regular conditional laws exist, `X_t` is Markov by construction:
the conditional future given the past depends on `X_t`, because `X_t` *is* the
past. This state is generally unbounded and global. D34d will never label this
result `local Markovization`.

### 2.2 Predictive equivalence and sufficient state

Two pasts are predictively equivalent when they give the same conditional law
for every licensed future experiment:

```text
h ~pred h'  iff  Law(future | h) = Law(future | h').
```

The quotient `[h]_pred` is the minimal predictive state at the level of
behavior. It need not be finite-dimensional, finite-memory, computable, or
locally stored.

A candidate distributed local state `S(h)` earns sufficiency only if

```text
Law(local future | complete past h) = Q(local future | S(h))
```

for every admitted past and local future query. `S` must be carried by the
relevant actor tips, collar/event records or declared boundary factors. It may
not be a hidden copy of the universe history with the word `local` attached.
Remote causally unrelated histories must not change it or its transition law.

### 2.3 Observable record projection

Let `R_t = pi(S_t)` retain only the durable record variables available to the
declared observer. The visible process is Markov exactly when the projection
is lumpable at the claimed width: all hidden states with the same visible
record must induce the same next-visible-state law. Otherwise two pasts can
share the same present record but predict different visible futures; that is
the operational memory witness.

The intended conclusion is therefore:

> observable non-Markovianity is the failure of a declared record projection
> to retain the predictive state.

It is not guaranteed for every projection. Identity projections and genuinely
lumpable coarse grainings are Markov.

### 2.4 Quantum predictive equivalence

For D34c-style quantum histories, equality of ordinary conditional
probabilities is too weak. Two past carrier/history states are predictively
equivalent only if **every allowed future local instrument**, including every
coarse graining that can reveal interference, gives the same future
decoherence functional/operational statistics. The candidate state may be a
density operator, process-tensor memory, boundary functional or an equivalent
record-carried object. D34d does not assume in advance that a classical hidden
Markov chain suffices.

## 3. Four notions currently called time

D34d keeps these separate in every theorem and receipt:

1. **local actor count:** the ordered number of rings/acts on one record wire;
2. **causal order:** the partial order defined by shared-record predecessors;
3. **construction time:** the real parameter of D34b's independent
   exponential clocks;
4. **emergent proper time:** a future physical ruler inferred from records and
   causal geometry, not presently derived.

Auxiliary heap/commit order is a serialization gauge and is not a fifth
physical time. A local ring count is an intrinsic order parameter, not yet a
clock calibrated in seconds. D34b construction time is a valid parameter of
the chosen stochastic model, but its exponential rate and its identification
with physical time remain primitive. A common rescaling of all rates changes
only units; relative actor-dependent rate changes generally change causal-DAG
probabilities and are physical unless an additional gauge theorem proves
otherwise.

## 4. The theorem ladder to decide

### T1 — full-history Markovization

For a standard-Borel history law admitting regular conditionals, the complete
past `X_t` is a Markov state. This theorem is expected to hold and is explicitly
classified as global/trivial.

### T2 — local predictive-state criterion

A SHARD history law admits a Markov realization on a declared distributed
local state `S` **iff** `S` is a sufficient statistic for all licensed local
future experiments and its update closes using only the touched local state
and fresh local noise. This is a characterization, not an existence theorem.

D34d must determine whether the chosen D34b actor law satisfies it. The current
expectation is narrow: the complete live local carrier/tip state plus residual
clock/mark state is sufficient for the constructed exponential-clock process;
memorylessness may remove residual waiting ages. That expectation does not
establish sufficiency for a general SHARD law or for the D34c quantum lift.

### T3 — visible-record lumpability

Given a Markov predictive state `S_t`, the durable projection `R_t=pi(S_t)` is
Markov iff its transition/instrument law is lumpable through `pi` at the stated
initial-law scope. If not, the receipt must exhibit two histories with the same
current durable record and different next-record conditional laws.

The word **generally** may be used only as `not guaranteed / generic under an
explicit parameter family`, never as a theorem that every observable record
process has memory.

### T4 — quantum version

The quantum analogue, if earned, is closure on an operational predictive state
or finite-memory process tensor: all future instrument statistics factor
through that state. An observed record process is quantum-Markov only under the
corresponding instrument-lumpability/conditional-independence condition.
D34d must either build this object for the finite D34c family or state exactly
why the timed/infinite lift is still required.

### T5 — clock-status theorem

D34d will identify which statements are invariant under:

- a common monotone change/rescaling of construction time;
- changes of serializer among linear extensions;
- independent changes of local actor rates;
- replacement of exponential waiting laws by age-dependent renewal laws.

The exponential law's memorylessness is expected to make the current actor
configuration Markov without storing clock age. A non-exponential negative
control should require age/residual-life data in the predictive state. This
would explain a source of apparent memory without declaring exponential clocks
fundamental.

## 5. Exact receipt plan

The first receipt is classical and exact; no stochastic cone campaign starts
inside D34d.

- **P1 — tautology gate:** enumerate a finite non-Markov record process and
  prove that complete histories form a Markov state. Print the state-size
  growth so the construction cannot be narrated as finite/local compression.
- **P2 — predictive quotient gate:** compute future-law equivalence classes
  exactly for finite hidden-state specimens; recover the minimal predictive
  quotient and compare it with proposed record variables.
- **P3 — lumpability gate:** include one strongly lumpable projection and one
  non-lumpable projection. The latter must print two equal present records with
  unequal exact next-record probabilities and a multi-step memory witness.
- **P4 — local-versus-global gate:** construct two disconnected actor
  components. A candidate local state and its future law must be invariant
  under changes in the remote component at fixed local stopping data. A hidden
  universe census/history state is the named negative control.
- **P5 — D34b clock gate:** compare the exponential actor construction with an
  age-dependent renewal variant. Gate the sufficiency of the current actor
  configuration for the exponential model and the necessity/sufficiency of
  adding clock ages in the renewal model. Distinguish fixed construction time,
  fixed local ring count and fixed global event count.
- **P6 — time-gauge gate:** prove serializer invariance on an incomparable
  diamond; show common rate rescaling leaves untimed causal-DAG probabilities
  unchanged; exhibit whether unequal relative rate changes alter an order or
  reception probability.
- **P7 — quantum finite gate:** on the D34c diamond/typed-DAG family, compare
  pasts with the same durable classical record but different retained quantum
  carrier state. An allowed future instrument must distinguish them. Then
  retain the correct carrier/predictive state and gate equality of all future
  instruments in the finite test basis. No diagonal-only shortcut is allowed.
- **P8 — claim scorecard:** separately report full-history Markovization,
  local predictive closure, observed non-lumpability, quantum finite closure
  and clock status. Failure of one cannot be averaged into another.

All discrete probabilities use exact rational/algebraic arithmetic. Any
continuous-time check uses analytic expressions plus at least 100 decimal
digits as regression. Receipts are frozen before execution, rerun under fresh
hash salts, and followed by independent hostile review streams on probability,
quantum history mathematics and locality/clock architecture. New openings are
repaired and delta-reviewed before a terminal noun.

## 6. Claim ceiling

The maximum first-round noun is:

> `PREDICTIVE-STATE / OBSERVABLE-MEMORY / CLOCK-STATUS
> CHARACTERIZATION FOR THE CHOSEN D34b–D34c FAMILY`.

It cannot earn `every SHARD law has a finite local Markov state`, `physical time
is exponential clock time`, `quantum non-Markovianity is classical hidden
memory`, `proper time is derived`, or `the universe law is selected`.

The desired theorem can become a genuine SHARD theorem only after replacing
“appropriately enlarged local state” with a precise record-carried sufficiency
condition and replacing “generally non-Markovian” with the exact failure of a
declared lumpability condition.

## 7. Provisional exact receipts (2026-07-13; hostile review required)

Two dependency-free receipts are green under two fresh hash salts:

- `code/d34d_predictive_clock_exact.py` ->
  `data/d34d_predictive_clock_exact.out`: 7/7, summary SHA-256
  `31e924d568af3bc59f7cd08fbaefe2e6bb1e7c357d1e7951e0312ab94810cbc3`;
- `code/d34d_quantum_predictive_exact.py` ->
  `data/d34d_quantum_predictive_exact.out`: 7/7, summary SHA-256
  `898b8a0039748760d83a151e93abdf6d01fb66888245d4d3626f8e95ac6bcf01`.

These are provisional until the three hostile streams and any required delta
round close.

### 7.1 Classical result

The proposed theorem splits exactly as predicted by the pin.

1. **Full-history Markovization passes but is global/trivial.** In the exact
   non-Markov specimen, using the whole visible word as the state closes the
   next-step law, but its positive state count grows
   `2,3,5,8,13,21` through depths one to six.
2. **The visible-record process can genuinely have memory.** Histories `10`
   and `00` end in the same current record `0`, while their next-`1`
   probabilities are exactly `3/8` and `7/20`. Their posterior predictive
   states are respectively `(1/2,1/2,0)` and `(2/5,3/5,0)`.
3. **Lumpability is the divide.** A separate positive control has a closed
   two-record quotient; the witness fails because its two hidden `record=0`
   states have group rows `(1/2,1/2)` and `(3/4,1/4)`.
4. **Local closure is architectural, not automatic.** An independent remote
   factor sums out of the local transition exactly. By contrast, at fixed
   global event count A's chance to ring changes from `1/2` to `1/4` when the
   remote census changes. This confirms again that global jump count is the
   wrong locality stopping rule.

For the chosen D34b exponential construction, memorylessness removes residual
clock age: the full current distributed actor configuration (live graph/tips,
carrier state and the licensed fresh local mark law) closes the future law. A
uniform-renewal control has next-half-unit ring probability `1/4` at age zero
and `1/2` at age one, so the same live configuration is insufficient unless
clock age is added. Thus Markov versus non-Markov can depend on what the state
retains; it is not an intrinsic label attached to the record noun alone.

### 7.2 Clock verdict

The exponential `t` remains **construction time in the chosen law**. A common
rate rescaling changes units and leaves untimed race probabilities unchanged.
A pathwise increasing relabeling of already realized timestamps preserves
order. Neither fact makes independent relative rate changes gauge: on a shared
wire the exact A-first probability changes from `1/3` to `1/2`. Local ring
ordinal, causal order, construction `t` and emergent proper time therefore
remain distinct. D34d does not derive seconds or a proper-time ruler.

### 7.3 Quantum result and the stronger boundary-state warning

The D34c diamond supplies the quantum non-lumpability witness directly. For a
fixed durable `s`, the coherent path carrier and the path-recorded/dephased
alternative have the same path-basis diagonal. The next H/output instrument is
nevertheless deterministic `o=1-s` in the first case and uniform in the
second. Summing the exact D34c functional gives joint probabilities
`(0,1/2,1/2,0)` versus four `1/4`s.

A real-qubit density matrix is a sufficient predictive state for the declared
isolated real-qubit future algebra: the exact `P0,P1,P+` signature reconstructs
it. But this does **not** generalize to one record's reduced state when an old
factor can return. Two joint carrier/environment states with the same reduced
`I/2` are sent by a later boundary CNOT to certain `P=0` and certain `P=1`.
The predictive state must then retain the joint collar/process memory. A truly
disconnected remote factor, by contrast, traces out of all local future
statistics exactly.

This is the main conceptual advance over the external desired theorem:

> the appropriate Markov state is the minimal operational boundary state that
> screens the licensed future—not necessarily a finite state inside each
> record, and not the whole universe history. Observable non-Markovianity is
> what appears when the chosen record projection fails to retain that boundary
> state.

### 7.4 Provisional noun and live review fronts

**Provisional combined noun:** `PREDICTIVE-STATE / OBSERVABLE-MEMORY /
CLOCK-STATUS CHARACTERIZATION FOR THE CHOSEN D34b–D34c FAMILY`.

The hostile round must attack at least:

- whether the classical witness establishes strong or only initial-law
  non-lumpability and whether the narration keeps them distinct;
- whether the D34b closure claim has retained every changing actor variable
  and uses a genuinely local stopping algebra;
- whether exponential clock memorylessness is being confused with derivation
  or physical time;
- whether `P0,P1,P+` tomography is scoped only to real one-qubit states;
- whether the returning-environment example demands a process tensor/joint
  boundary state rather than being narrated as failure of density matrices;
- whether the D34c decoherence-functional calculation licenses every stated
  probability partition;
- whether any finite-memory/locality language exceeds the receipts.

No terminal theorem is claimed before those reviews and their delta pass.

## 8. Hostile round 1 and the replacement pin (2026-07-13)

### 8.1 Verdict: exact arithmetic survives; the local/Markov width does not

Three independent streams reran the receipts and independently rebuilt their
central calculations:

- probability/history law: `MAJOR REVISION — 0B/5M/3m/2n`;
- quantum/process memory: `MAJOR REVISION — 0B/2M/4m/2n`;
- locality/clock architecture: `REJECT AT STATED WIDTH — 1B/5M/4m/2n`.

Every printed fraction and matrix survived. The receipt files reproduced
byte-for-byte under fresh salts. The combined provisional noun is nevertheless
withdrawn pending repair.

The blocker is architectural. The complete current D34b Harris configuration
is a global state of a locally generated process. Calling that configuration
“distributed” does not prove that one record, or a bounded collar around it,
screens its future. In the actual D34b grammar, B sends an incoming interaction
to its neighbor A at rate `1/4` when `deg(B)=1`; after B births a second
neighbor, the rate is `1/8`, even if A's own tip and private clock state are
unchanged. A's tip alone is therefore not predictive.

Four further distinctions are load-bearing:

1. P2 classified three pure hidden states, not the predictive equivalence
   classes of observed histories. The latter have exactly `2,3,...,13`
   reachable belief states through depths `1..12` in the chosen specimen.
2. Strong lumpability (all initial laws), law-relative/weak Markovity and the
   demonstrated failure for one initial law are different statements.
3. A scalar exponential survival identity does not itself construct the full
   D34b generator or a local stopping filtration. The renewal control proved
   age necessity but not age-augmented sufficiency.
4. The quantum coherent/path-recorded comparison uses two different past
   instrument contexts. It proves durable-record operational insufficiency,
   not non-Markovianity of one fixed quantum process. Rebit tomography is also
   a one-state algebra result, not a multi-time process theorem.

### 8.2 Classical replacement gates — frozen before code

The replacement classical receipt must contain the following independent
gates.

- **R1 — observed-history predictive quotient.** Enumerate every positive
  observed word through depth 12, compute its exact posterior belief, quotient
  by future-law equivalence, and print `2,3,...,13`. Prove that for current
  record zero, belief `(p,1-p,0)` has next-one probability `1/4+p/4`, so the
  distinct beliefs are genuinely predictive classes. Keep hidden state,
  posterior state and durable record as separate rows.
- **R2 — three lumpability scopes.** Gate a strongly lumpable positive
  control; a chain that is not strongly lumpable but is Markov for a declared
  initial law because the offending state is unreachable; and the actual
  uniform-initial witness `3/8 != 7/20`. No unqualified “exact divide” is
  permitted.
- **R3 — the actual ideal D34b state and generator.** Define `Z_t`: active
  Ulam actors, private ring/birth counters, typed adjacency, wire tips/event
  history, eligibility/seal status and any modeled carrier fields. For bounded
  cylinder `f`, gate the support-local generator

  ```text
  Lf(z) = sum_y [
      1/4 (f(B_y z)-f(z))
    + sum_(x in N_y) 1/(4 deg(y)) (f(I_yx z)-f(z))
    + 1/2 (f(N_y z)-f(z)) ].
  ```

  The analytic theorem must attach to the ideal independent Poisson/mark
  product source: independent increments plus local measurable updates make
  `Z_t` a time-homogeneous strong Markov process at physical stopping times.
  The finite Decimal/PRF actor is only an implementation regression.
- **R4 — locality hierarchy, including the counterexample.** Gate the actual
  D34b `deg(B)=1 -> 2` incoming-rate change `1/4 -> 1/8`, passive reception
  without A-ring reset, and disconnected-factor invariance. State the earned
  hierarchy exactly: `Z_t` is global; each generator term has bounded touched
  support; A's tip is insufficient; no fixed finite/bounded all-future collar
  is yet proved. A future finite-horizon/growing-boundary theorem remains an
  open, not an implication of R3.
- **R5 — stopping dictionary.** Separate fixed construction time, A-own-ring
  count, A-wire-event count (including passive receptions), fixed global event
  count and the untimed order skeleton. Carry the terminal D34b locality
  theorem only at its licensed stopping scopes.
- **R6 — renewal sufficiency.** For independent uniform-renewal actors, build
  the age-augmented piecewise-deterministic state. Gate
  `P(R>s | age=a)=S(a+s)/S(a)`, a two-actor residual race, initiator reset,
  newborn age zero and passive-receiver no-reset. Prove conditional closure on
  graph plus the complete age vector; keep local observers' hidden-age belief
  as a separate issue.
- **R7 — time/order transformation table.** Rebuild an actual typed-DAG
  canonicalizer for two incomparable actor events. Gate: serializer orbit
  invariance; common-rate identity `Law_(c lambda)(Z_T)=Law_lambda(Z_(cT))`;
  failure of invariance at fixed numeric `T`; invariance of embedded winner
  order under common scaling; order preservation but homogeneous-law change
  under nonlinear timestamp relabeling; and an explicitly named heterogeneous-
  rate D34b variant with marked shared-wire masses `(1/48,1/24)` versus
  `(1/32,1/32)`.
- **R8 — capacity ledger.** Print bounded event-outcome rank/incidence arity
  separately from unbounded Ulam identifier length, actor degree/edge census,
  connected-boundary width, clock-age vector and posterior-belief complexity.
  No global configuration may be called one finite-capacity record.
- **R9 — scorecard.** The maximum classical noun is `D34b GLOBAL STRONG-
  MARKOV PROCESS WITH SUPPORT-LOCAL GENERATOR + EXACT OBSERVABLE-MEMORY
  CHARACTERIZATION`. A bounded local predictive state remains open unless an
  additional receipt actually constructs it.

### 8.3 Quantum replacement gates — frozen before code

- **U1 — harden the recorded-path functional.** Construct
  `D_rec(h,h')=delta_(p,p')D(h,h')`, then gate normalization, strong positivity
  and its incidence coarse graining. Do not obtain a second experiment by
  merely relabeling the diagonal of the first.
- **U2 — rescope the existing comparison.** Rename it `durable-record
  operational insufficiency across declared past instruments`. It is not the
  fixed-process non-Markov gate.
- **U3 — fixed three-slot causal-break witness.** Use one process with initial
  correlated `P,E` state. The past choices `I_P` and `X_P`, followed by the
  same nonzero middle causal-break outcome `P=0` and the same repreparation
  `P=0`, leave `E=0` and `E=1`; the fixed future `CNOT(E->P)` must give certain
  `P=0` and certain `P=1`. This earns operational non-Markovianity of one
  fixed process.
- **U4 — tomography scope.** Prove algebraically that `P0,P1,P+` reconstruct
  an arbitrary real-symmetric two-level operator. Call this a rebit
  tomographic effect set, not a multi-time instrument or general qubit result.
- **U5 — architecture fork.** Report separately: retaining joint `P,E` makes
  the displayed total update Markov; eliminating E requires a reduced
  multi-time process tensor and exhibits memory by U3. These are alternative
  representations, not synonyms.
- **U6 — remote theorem.** State and gate the analytic tensor/partial-trace
  identity for arbitrary trace-one product remote factors and local effects.
  Declare whether initial cross-component correlations are excluded.
- **U7 — scorecard.** No timed/direct-integral quantum law, universal finite
  memory theorem, or general-instrument finite Markov order may be claimed.

### 8.4 Literature alignment to carry

The repair must explicitly compare its terminology with four primary results:

- Shalizi–Crutchfield causal states: predictive equivalence classes are the
  minimal representation for accurate future prediction;
- Geiger–Temmel lumping: strong `k`-lumpability concerns every initial law and
  must not be confused with a stationary or fixed-law property;
- Pollock et al.'s operational Markov condition: quantum memory requires a
  multi-time/causal-break criterion;
- Taranto et al.'s quantum Markov order: non-Markov processes cannot have
  finite Markov order for every possible instrument, so finite quantum memory
  claims must remain instrument-specific.

After replacement, the same three reviewers must perform delta audits. A
terminal statement requires closure of the blocker and every major finding.
