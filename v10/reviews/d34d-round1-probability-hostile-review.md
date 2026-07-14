# D34d round 1 — independent probability/history-law hostile review

**Target:** baseline commit `0119f4e`, especially
`note-d34d-predictive-state-clock-status.md` section 7,
`code/d34d_predictive_clock_exact.py`, both committed D34d outputs, and the
terminal D34b marked-Harris construction.  **Verdict:** **MAJOR REVISION —
0 BLOCKER / 5 MAJOR / 3 MINOR / 2 NIT.**  No printed exact fraction, matrix
row, receipt digest, or executable verdict was falsified.  The rejection is at
the theorem/gate width: several correct specimens are being used as receipts
for predictive-state and clock-closure statements they do not compute.

## Independent reproduction

I reran the classical executable under fresh `PYTHONHASHSEED=17,99173` and
both D34d executables under fresh salts `41,7727`.  Each run was byte-identical
to its committed `.out` file:

- classical file SHA-256
  `1b75e1628cc5ab09f29592036d0f29a4032ec4cde3dcb3300efa9dbca615f386`,
  summary digest
  `31e924d568af3bc59f7cd08fbaefe2e6bb1e7c357d1e7951e0312ab94810cbc3`;
- quantum file SHA-256
  `46ff97ab93983bd78875df1aef888825695fca7847a62f26cbe977601b7486c7`,
  summary digest
  `898b8a0039748760d83a151e93abdf6d01fb66888245d4d3626f8e95ac6bcf01`.

I independently rebuilt the three-state HMM from its transition matrix rather
than importing the receipt.  The two witness cylinder masses are
`P(10)=1/3` and `P(00)=5/12`; their posteriors are respectively
`(1/2,1/2,0)` and `(2/5,3/5,0)`, and their exact next-`1` probabilities are
`3/8` and `7/20`.  The positive-word counts really are
`2,3,5,8,13,21`.  The uniform-renewal probabilities are also exactly `1/4`
at age zero and `1/2` at age one.  For exponential rates `(1,2)`, the order
law is `(1/3,2/3)`, a common factor cancels, and changing the rates to `(2,2)`
changes the first probability to `1/2`.

Those facts survive.  What follows concerns what they establish.

## MAJOR findings

### M1 — P2 does not recover the predictive quotient defined in the pin

The pin defines predictive equivalence on **pasts**: two observed histories
are equivalent when all conditional future laws agree.  P2 instead computes
future signatures of the three *pure hidden states* `A,B,C`.  Showing that
those pure states are pairwise distinguishable is not the same calculation as
quotienting observed histories or posterior beliefs.

The distinction is load-bearing here.  An independent exact enumeration gives
the following number of reachable posterior beliefs at word depth `n=1..12`:

```text
2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13.
```

At a current visible `0`, the posterior has form `(p,1-p,0)` and the next-`1`
probability is `1/4+p/4`, so distinct reachable `p` values are already
predictively distinct at one future step.  The observed-history predictive
quotient therefore keeps growing in this specimen even though its Bayesian
state has a one-parameter representation.  The printed P2 label “MINIMAL
PREDICTIVE STATE” and the preregistered promise to recover the quotient are not
earned by the pure-state partition.

**Mandatory repair:** quotient positive observed histories, not only hidden
basis states.  Print reachable belief/predictive-class counts through a frozen
depth, prove the one-step injection above, and state separately: (i) the
three-state hidden realization, (ii) the observer-computable posterior
predictive state, and (iii) the durable record projection.  Do not call one
of these the other.

### M2 — strong, weak, and fixed-initial-law lumpability remain conflated

The positive control is strongly lumpable: equal block rows make the projected
chain Markov for every initial distribution.  The negative control is not
strongly lumpable, and the `10/00` calculation separately proves that its
projection is non-Markov for the particular uniform `INITIAL`.  Both are good
results.  They do not license an unqualified “lumpability is the exact divide.”

Strong lumpability is sufficient, and in the usual finite homogeneous setting
is the relevant all-initial-laws criterion.  It is not necessary for a chosen
initial law.  A simple exact countercontrol has `A,B -> 0`, `C -> 1`,

```text
A -> (A,C) = (1/2,1/2)
B -> (B,C) = (3/4,1/4)
C -> A       with probability 1,
```

and initial law `delta_A`.  The partition is not strongly lumpable because
the `A` and `B` block rows differ, but `B` is unreachable and the observed
process is the Markov chain `0 -> (0,1)=(1/2,1/2)`, `1 -> 0`.  More generally,
fixed-initial-law or weak lumpability is a filtered-belief condition, not just
equality of every hidden row inside a block.

**Mandatory repair:** define and gate three scopes separately:

1. strong lumpability / Markovity for every initial law;
2. Markovity or weak lumpability for one declared initial law, checked on every
   reachable filtered belief/history at the frozen horizon (plus an analytic
   closure argument if an all-time claim is made);
3. failure for the actual witness initial law, which the `10/00` pair already
   proves.

The final theorem should say “the visible process is Markov exactly when the
projection is lumpable in the explicitly declared law-relative sense,” not
use strong lumpability as the only meaning of the word.

### M3 — P5 does not prove closure of the D34b actor process

P5 verifies the scalar identity `P(T>a+s | T>a)=P(T>s)` for one exponential,
normalizes uniform `1/k` race rows for `k<=8`, and checks the independent mark
vector.  It never executes or derives the transition kernel of the D34b state
it says is closed.  In particular, it does not carry:

- live/inactive/sealed status and Ulam identities;
- actor ring and birth ordinals;
- changing birth-tree adjacency and eligible-target rows;
- passive receptions, which change carrier/tip state without resetting the
  receiver's clock;
- the filtration and stopping-time scope at which un-rung residual clocks are
  renewed;
- the distinction between the full distributed configuration and a finite
  local boundary sufficient state.

The closure claim is plausible and likely true for the **ideal** D34b source
law: independent rate-one Poisson processes have the strong Markov property,
and fresh product marks can drive the next local update.  But that theorem does
not follow from the executable's scalar regression.  Moreover, “the full
current distributed actor configuration” is a universe-wide state presented
in distributed notation.  It is a locally updated Markov state, not yet the
local predictive compression targeted by T2.  P4 only removes a disconnected
factor; it does not prove screening by a collar inside a connected component.

**Mandatory repair:** define the exact D34b state `Z_t` and its natural
filtration, including every variable needed by the generator.  Prove from the
independent Poisson/mark product law that `Z_t` is a time-homogeneous strong
Markov process at physical stopping times and write its generator/next-event
kernel.  Then make a separate locality statement: either exhibit a declared
record-carried boundary state that screens every licensed regional future, or
narrow the result to a globally distributed, locally updated Markov state.
Do not infer the first statement from disconnected tensor factorization.

### M4 — the preregistered renewal sufficiency half is absent

P5 promised both necessity and sufficiency of adding clock age to the renewal
model.  The two `1/4 != 1/2` values prove necessity of something beyond the
age-forgetting live configuration.  No age-augmented transition law is built,
and sufficiency is not gated.

For an iid renewal law with survival `S`, the needed analytic object is

```text
P(residual > s | current age = a) = S(a+s)/S(a)
```

on reachable `a` with `S(a)>0`.  For multiple actors, the state is the full
age vector together with the actor configuration; ages flow deterministically
between rings, the initiator resets to zero, a newborn starts at zero, and a
passive reception does not reset its receiver.  That gives a piecewise
deterministic Markov state under stated independence assumptions.

**Mandatory repair:** implement or prove that age-augmented kernel, including
competing renewal actors and passive receptions, and gate normalization and
history-independence conditional on the augmented state.  Until then the
receipt earns “age is necessary in this control,” not “renewal closure after
adding age.”

### M5 — P6 declares two of its promised gauge results instead of proving them

The serializer check is a dictionary whose two inputs are manually assigned
the same string.  That is the desired quotient written as data, not an
independent canonicalization of two event histories.  Likewise, a monotone
map applied to three already realized timestamps proves only that a monotone
map preserves order.  It does not prove invariance of the timed history law.

The rate fractions themselves are correct.  The proper common-rescaling
statement for the full continuous-time law is a compensated identity of the
form `Law_{c lambda}(Z_t) = Law_lambda(Z_{ct})`; at fixed numerical time, a
common rate change changes event-count and timed-history distributions.  A
general nonlinear time relabeling turns constant exponential hazards into
time-dependent hazards unless the law is transformed with it.  Only the
untimed order/DAG pushforward is automatically insensitive to timestamp
relabeling.

**Mandatory repair:** reconstruct the incomparable two-event typed DAG from
each serialization with a separately coded canonicalizer and compare the
pushforward masses.  Gate the full common-rate/time-coordinate identity on the
D34b generator (or narrow explicitly to one-shot untimed race order).  State
that arbitrary monotone timestamp relabeling is an order-gauge fact, not a
symmetry of the homogeneous timed measure.

## MINOR findings

### m1 — P4 is a generic product identity, not the preregistered actor specimen

`LOCAL_TRANS tensor REMOTE_TRANS` sums out because the remote rows were chosen
to normalize.  `own_ring_birth=1/4` and the two global race shares are then
hardcoded.  This is correct arithmetic, but it does not construct two D34b
actor components as P4 requested.  The terminal D34b actor coupling already
contains stronger evidence; explicitly inherit and cite that theorem or
rebuild the actor-level factor here.

### m2 — the general history-state theorem needs its measure-theoretic scope

For a standard-Borel path law, a regular conditional future kernel makes the
stopped past a Markov state, up to the usual almost-sure choice of conditional
versions.  Null histories do not acquire canonical conditionals.  If a
time-homogeneous Markov representation is claimed, include the current time or
use a shift-covariant law; otherwise call it time-inhomogeneous.  The finite
word calculation illustrates the theorem but does not prove its full
continuous-time statement.

### m3 — “fresh local mark law” is not itself a state variable

The ideal D34b product law supplies future independent marks; the finite
BLAKE2/Decimal actor reference does not prove iid randomness.  The theorem
should attach to the ideal product source and list the actor counters needed to
index Ulam children/marks.  The deterministic reference remains an
implementation diagnostic, exactly as the terminal D34b review required.

## NIT findings

1. The horizon-`1..4` pure-hidden-state signature loop adds no evidence once
   horizon one separates `A,B,C`; the missing calculation is over reachable
   posterior beliefs.
2. The 100-decimal exponential division is a useful regression but should not
   be described as additional proof beyond the exact analytic survival-law
   identity.

## What survives at reviewed strength

- Complete-history Markovization is a valid global representation tautology
  under the stated regular-conditional assumptions; it does not imply local
  finite memory.
- The exact HMM under the declared uniform initial law is visibly non-first-
  order-Markov: `10` and `00` have the same current record and next-`1`
  probabilities `3/8` and `7/20`.
- The good control is strongly lumpable, and the bad control is not strongly
  lumpable.
- Exponential clocks are age-memoryless; the uniform renewal control proves
  age-forgetting insufficient.
- Common scaling cancels from a one-shot exponential race, and changing
  relative rates can change a shared-order probability.
- The quantum executable is byte-reproducible; this probability review did not
  falsify its exact matrices.  Its operational-width claims belong to the
  quantum hostile stream.

## Exact verdict and repair gate

**REJECT THE PROVISIONAL COMBINED NOUN AT CURRENT WIDTH.**  The present exact
noun is narrower:

> `FINITE CLASSICAL NON-MARKOV / STRONG-LUMPABILITY / CLOCK-AGE WITNESS,
> WITH INHERITED PLAUSIBILITY OF D34b MARKOV CLOSURE`.

A delta pass requires all five major repairs.  In particular, the next version
must not call the pure hidden-state partition the minimal predictive quotient,
must print the strong-versus-initial-law distinction, and must either prove
the D34b state/generator/strong-Markov theorem plus a genuine local screening
state or explicitly confess that the established Markov state is the full
distributed configuration.  No change to the exact `3/8`, `7/20`, `1/4`,
`1/2`, `1/3`, or receipt reproducibility results is requested.
