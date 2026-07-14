# D34d round 1 — probability/history-law hostile delta review

**Repair target:** commit `b92b82b`.  **Baseline:** probability hostile review
of `0119f4e`, verdict `0B/5M/3m/2n`.  **Delta verdict:** **DELTA-CLEAN —
0 BLOCKER / 0 MAJOR / 0 MINOR / 0 NIT.**  All five mandatory repairs and all
three minor findings are closed.  The two former nits are either removed or
properly subordinated.  I found no new probability-theory blocker or major.

## Reproduction and independent checks

I ran both repaired receipts under fresh `PYTHONHASHSEED=53,104729`.  Every
run was byte-identical to the committed output:

- classical file SHA-256
  `43aa03a459bd05509998e0f770a97ed726982ab28fdcdbaf0735aadae3c4891c`,
  summary SHA-256
  `9f9e59954bd1710e70c27d1fa6c5b285c50eec096dae21d433c04201092ac282`;
- quantum file SHA-256
  `e1990fe3a4dfbc44c83b4b49216df44ad9462dcb410c9c24c19dc4144c3884d1`,
  summary SHA-256
  `cc496ff94d360c34ffb5f52b2e4ba57f342378d3807198a3a0f5d9ff01c4dce0`.

I independently rebuilt the repaired classical calculations rather than
importing the receipt.  The results agree:

- reachable observed-history posterior counts through depths `1..12` are
  exactly `2,3,4,5,6,7,8,9,10,11,12,13`;
- at visible zero, posterior `(p,1-p,0)` has next-one probability
  `1/4+p/4`, so the distinct beliefs are genuinely distinct predictive
  classes;
- the strong positive control has block rows
  `(2/3,1/3),(2/3,1/3),(1/2,1/2)`;
- the law-relative countercontrol has hidden block rows
  `(1/2,1/2),(3/4,1/4),(1,0)`, while the offending `B` state is unreachable
  from `delta_A` because both `A->B` and `C->B` are zero;
- the original uniform-initial process still has the exact fixed-law failure
  `P(1 next | 10)=3/8 != 7/20=P(1 next | 00)`;
- uniform-renewal survival gives the single-clock `1/4` versus `1/2`
  witness and the two-age residual race `(0,1) -> (1/4,3/4)`;
- the D34b incoming rate really changes `B->A: 1/4 -> 1/8` when B gains a
  second neighbor, while A's own state is unchanged;
- the marked heterogeneous shared-wire masses are exactly
  `(1/48,1/24)` and `(1/32,1/32)`.

## Finding-by-finding delta

### M1 — observed-history predictive quotient: CLOSED

P2 now computes posteriors of every positive observed word, deduplicates those
beliefs, and prints the exact depth profile `2..13`.  The one-step formula
`1/4+p/4` proves injectivity within the visible-zero sector, while the
visible-one sector is the singleton hidden state `C`.  Hidden ontic state,
observer posterior state, and durable record are explicitly separated.  The
old pure-hidden-state signature loop remains only as a separately labeled
ledger and no longer carries the quotient claim.

### M2 — strong versus law-relative lumpability: CLOSED

P3 now contains three distinct claims:

1. a strongly lumpable chain, hence a Markov projection for every initial
   law;
2. a chain that is not strongly lumpable but is Markov from `delta_A` because
   `B` is unreachable and the visible symbol identifies `A` versus `C` on the
   reachable class;
3. the actual uniform-initial non-Markov witness `3/8 != 7/20`.

The second result is all-time, not merely a finite probe: rows from the
reachable set `{A,C}` have zero entry into B, so that set is closed and each
visible block has one reachable hidden state.  The note no longer uses
unqualified strong lumpability as a necessary fixed-law condition.

### M3 — D34b state/generator/strong-Markov width: CLOSED

P8 defines the complete global configuration `Z_t`, including active Ulam
actors, ring/birth ordinals, adjacency and eligibility, wire tips/events, and
modeled carrier fields.  Its exact event-rate inventory is the D34b generator:
each active actor contributes birth `1/4`, neighbor interactions totaling
`1/4`, and idle `1/2`.  On the four-actor seed every actor row is one and total
intensity is four.

The analytic theorem is now attached to the **ideal** source rather than the
finite PRF reference.  The terminal D34b result already supplies nonexplosion;
independent Poisson increments, independent future marks, measurable current-
state updates and finite total rate on finite configurations give the standard
time-homogeneous strong-Markov pure-jump process at physical stopping times.
The Decimal/BLAKE reference is correctly kept outside that probability proof.

Most importantly, the locality width is no longer hidden.  P9 demonstrates
that A's tip/private state does not determine its incoming law, because a
change at B sends `B->A` from `1/4` to `1/8`.  The earned statement is exactly
`global Markov state + support-local generator terms + disconnected-factor
locality`; a bounded all-future record/collar state remains open.  This is the
distinction the first review required.

### M4 — renewal age sufficiency: CLOSED

P10 supplies the missing age-augmented kernel.  For reachable age `a`, the
residual survival law is `S(a+s)/S(a)`.  The two-actor race is normalized and
depends only on the current age vector; elapsed time advances all surviving
ages, the initiator resets, a newborn starts at zero, and a passive receiver
does not reset.  With independent renewal durations and fresh marks, those
rules are the piecewise-deterministic Markov closure of the complete global
graph-plus-age process.  The note separately warns that an observer lacking
neighbor ages needs a belief over them.  It does not promote global age-vector
closure to bounded local memory.

### M5 — serializer and time transformation proof: CLOSED

P11 builds actual D34b event states in both orders and canonicalizes the
physical typed DAG.  Disjoint A/P operations agree after serialization is
erased; shared-wire A/B orders differ through their predecessor incidence.
The former hardcoded two-string declaration is no longer the repair gate.

The time table now carries all required scopes:

- common rate scaling preserves the embedded winner/order law;
- it changes the distribution at fixed numeric construction time;
- the compensated full-generator identity is
  `Law_(c lambda)(Z_T)=Law_lambda(Z_(cT))`;
- a nonlinear timestamp map preserves a realized order but changes the
  homogeneous exponential law;
- relative actor rates change a physical shared-wire split in an explicitly
  named heterogeneous variant.

The no-ring exponential cells are sufficient exact witnesses for fixed-time
failure, while the full compensated identity follows analytically from
scaling the complete generator `L -> cL`.

## Former minor and nit findings

- **Generic product control:** closed by P9's actual D34b disconnected actor
  comparison; P4 is retained only as an elementary precursor.
- **History-state theorem scope:** the generic statement remains conditioned
  on standard-Borel regular conditionals and is called global/trivial.  The
  new time-homogeneous/strong-Markov claim is made only for the ideal D34b
  process with its Poisson source and physical stopping filtration.
- **Fresh marks/source typing:** closed.  The theorem uses ideal independent
  mark streams and includes the actor counters; it makes no iid claim about
  deterministic BLAKE coordinates.
- **Pure hidden signatures:** now supplementary; observed pasts carry P2.
- **Decimal exponential arithmetic:** consistently labeled a regression of
  the analytic identity, not an independent proof.

One implementation-scope point is worth preserving but is not a delta defect:
the reachable chosen D34b exemplar is the static no-sealing active graph (the
event-inert sealed root was already suppressed in the terminal exact oracle).
If future work introduces dynamic sealing, `d34b_rates` must filter eligibility
again and the generator theorem must be rerun.  No present claim extends to
that different grammar.

## Claim ceiling

The repaired ceiling is accurate:

> **D34d GLOBAL-MARKOV / LOCAL-GENERATOR / OBSERVABLE-MEMORY
> CHARACTERIZATION:** the chosen classical D34b law is strong Markov on its
> complete global configuration and has support-local generator terms; visible
> record processes are Markov or non-Markov under the explicitly law-scoped
> sufficiency/lumpability condition; the separate finite quantum exhibit is
> evaluated by the quantum hostile stream.

The classical receipt does **not** claim a bounded local predictive state,
physical proper time, derived rates, a timed quantum direct integral, or a
universal SHARD Markovization theorem.  The capacity ledger explicitly marks
Ulam identities, actor degree, global state size, collar width, renewal-age
width and belief complexity as nonuniform or open.

## Final delta verdict

**DELTA-CLEAN.**  The exact HMM, lumpability, D34b generator, age-augmented
renewal and time-transformation results are correct at their repaired scopes.
The central scientific answer is now honest: the selected D34b universe has a
global strong-Markov configuration generated by local event terms, but D34d
has not derived a bounded predictive state carried by each individual record.
No mandatory probability repair remains before terminal synthesis, subject to
the independent quantum and locality/architecture delta verdicts.
