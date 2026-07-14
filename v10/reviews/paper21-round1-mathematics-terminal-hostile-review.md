# Paper 21 — mathematics terminal hostile review

**Target:** commit `afbd2ba`,
`relativistic-isp-v10-paper21-local-generators-do-not-imply-local-memory.md`.
**Disposition:** **ACCEPT / TERMINAL-CLEAN — 0 BLOCKER / 0 MAJOR / 0 MINOR /
0 NIT.**  The paper is mathematically consistent with the clean D34d evidence,
reproduces its exact numbers and hashes, and does not turn support-local
generation into a bounded local-memory theorem.

## 1. Audit method and reproduction

I checked the paper against:

- the repaired classical and quantum executables and committed outputs;
- `note-d34d-predictive-state-clock-status.md` through its terminal status;
- the original three hostile reports and every probability, locality/clock,
  and quantum delta;
- the terminal D34b nonexplosive Harris-law result and D34c finite typed-DAG
  result;
- the cited primary literature on causal states, strong lumpability, renewal
  prediction, operational quantum Markovity, and instrument-specific quantum
  Markov order.

Fresh runs under `PYTHONHASHSEED=67,65537` are byte-identical to the committed
receipts:

- classical output SHA-256
  `912394a45eb76e3cf3d36ed51310f44f7f51f0e2c0d9162b97d42015feb6b16b`,
  `13/13`, summary SHA-256
  `9f9e59954bd1710e70c27d1fa6c5b285c50eec096dae21d433c04201092ac282`;
- quantum output SHA-256
  `e1990fe3a4dfbc44c83b4b49216df44ad9462dcb410c9c24c19dc4144c3884d1`,
  `10/10`, summary SHA-256
  `cc496ff94d360c34ffb5f52b2e4ba57f342378d3807198a3a0f5d9ff01c4dce0`.

The paper's receipt table copies the gate counts, summary hashes, and final
review dispositions exactly.

## 2. State hierarchy and full-history Markovization

Sections 1–2 preserve all distinctions forced by the hostile round:

1. complete past `X_t`;
2. complete current generative configuration `Z_t`;
3. behavioral predictive equivalence class `[h]_pred`;
4. a candidate region/collar state `B_A(h)`;
5. the observer's record projection.

The full-history statement is correctly conditional on regular conditional
future laws. Null histories require a chosen version, and the current time is
retained when needed. The paper calls this construction global and generally
unbounded; it never presents it as local Markovization.

Predictive equivalence is used in its standard behavioral sense: pasts are
identified when every licensed future conditional agrees. “Minimal” means the
quotient by that operational equivalence, not a claim of finite dimension,
bounded storage, computability, or realization inside one record. Section 2.4
then gives the actual screening equation a collar would have to satisfy.

## 3. The D34b generator and strong-Markov theorem

### 3.1 Generator correctness

For each active unsealed actor `y`, the displayed generator has rates

```text
birth:                         1/4,
interaction with x in E_y:    1/(4 |E_y|),
idle:                          1/2.
```

The interaction row sums to `1/4`, so every actor contributes total intensity
one. `E_y` is explicitly the eligible **unsealed** neighbor set; sealed actors
are excluded as initiators and targets. This matches the final P8 repair and
the exact `R--A--B` control, where R has no row and `A->B` remains `1/4`.

Each update reads the initiating actor's adjacency/eligibility data and changes
only the initiating wire plus a new child or named target. The total embedded
race still has a global normalization if one asks “which event is next,” but
the law is not defined through a universe-wide opportunity denominator. The
paper's phrase “support-local actor terms” is therefore correct and does not
mean bounded read size or bounded predictive memory.

### 3.2 Strong-Markov proof

Theorem 1 is valid at its stated scope. The ideal source preassigns independent
rate-one Poisson clocks and independent mark streams to Ulam addresses and
activates an address at birth. The terminal D34b theorem supplies
nonexplosion: every bounded construction-time interval contains finitely many
live actors and marked events almost surely. Consequently the generator has
finite total rate along every realized finite-time configuration.

At a stopping time of the **complete construction-time filtration**, the
independent-increment/strong-Markov property of the active Poisson sources and
the untouched product law of future marks restore the same source law,
independently of the stopped past. Newborn addresses carry independent source
coordinates. Since each update is a measurable function of `Z_t` and the
fresh mark, the resulting nonexplosive pure-jump configuration process is
time-homogeneous strong Markov.

The proof correctly attaches to the ideal product source. It does not infer
iid randomness from the finite keyed-stream/Decimal implementation. It also
does not call construction time proper time or a relativistic clock.

### 3.3 The global/local boundary is honest

The paper repeatedly says that `Z_t` is the configuration of the entire
constructed universe. Calling its fields distributed does not make the state
record-local. The established hierarchy is exactly the reviewed one:

```text
global strong-Markov configuration
+ support-local generator terms
+ disconnected-factor locality
!= bounded predictive state inside one actor record.
```

No sentence upgrades this result to finite local memory, finite collar width,
or foliation/proper-time independence.

## 4. Proposition 2 and the locality obstruction

The one-record counterexample is exact. When B has only A as an eligible
neighbor,

```text
rate(B -> A) = 1 x 1/4 x 1 = 1/4.
```

After B births an additional eligible child, while A's tip, private ring
ordinal, and private exponential clock state remain unchanged,

```text
rate(B -> A) = 1 x 1/4 x 1/2 = 1/8.
```

Therefore A's private actor state does not determine the law of A's next wire
event. This is a sufficiency counterexample, not evidence of action at a
distance: the missing degree datum is stored at the adjacent B actor.

The passive-reception accounting is also correct. An incoming `i(B,A)`
creates one A-wire event and predecessor while consuming no A ring, yielding
`A-own/A-wire/global = 0/1/1`. The paper therefore keeps actor-own ring count,
wire-event count, causal order, global event count, and construction time
separate.

The listed future possibilities are appropriately conditional. The paper does
not claim that the whole connected component is always necessary, that every
finite collar fails, or that no screening theorem can exist; it states that no
fixed bounded all-future collar has yet been proved.

## 5. Predictive beliefs and lumpability

The HMM rows and uniform initial law match the receipt. Independent arithmetic
gives

```text
belief(10) = (1/2,1/2,0),   P(next 1 | 10) = 3/8,
belief(00) = (2/5,3/5,0),   P(next 1 | 00) = 7/20.
```

Both histories have positive mass and the same latest visible record, so
`3/8 != 7/20` is a genuine violation of first-order Markovity for the declared
initial law.

The paper does not confuse the three hidden labels with the observer's
predictive quotient. Its exact depth-`1..12` posterior-class counts are
`2,3,...,13`. At visible zero, `next-one=1/4+p/4` is injective in posterior
`(p,1-p,0)`, proving that those distinct beliefs are distinct predictive
classes. The paper also discloses the compact one-parameter representation,
so proliferation of reachable values is not misreported as growing vector
dimension.

The lumpability scopes are correct:

- strong lumpability supplies first-order Markovity for every initial law in
  the finite homogeneous control;
- it is not necessary for one chosen law, as shown by the closed reachable
  A/C sector from `delta_A`;
- the uniform-initial specimen actually fails Markovity via `10/00`.

The final “if and only if” is stated in law-relative predictive-sufficiency
language, not as an assertion that strong lumpability is necessary for every
fixed initial law. “Generally non-Markovian” is explicitly rejected as a
universal claim.

## 6. Construction-clock mathematics

Every clock identity is correct and properly scoped.

- Exponential survival obeys `S(a+s)/S(a)=S(s)`, so residual age is omitted
  from the chosen unit-rate configuration state.
- The uniform-`[0,2]` renewal control has next-half-unit ring probabilities
  `1/4` at age zero and `1/2` at age one.
- For two independent residual supports of lengths two and one, the exact
  winner law is `(1/4,3/4)`.
- Graph plus the complete age vector closes the declared renewal control as a
  piecewise-deterministic Markov process: surviving ages advance, an
  initiator resets, a newborn starts at zero, and a passive receiver does not
  reset.

The common-rate table distinguishes all transformations that the baseline
blurred. At fixed numeric `T`, common scaling changes the law. With the horizon
transformed, the full identity is

```text
Law_(c lambda)(Z_T) = Law_lambda(Z_(cT)).
```

It follows pathwise by dividing every preassigned wait by `c`, preserving all
marks and Ulam addresses, and inducting through births. The exact nontrivial
coupling `(1,2) -> (1/2,1)` includes birth and passive reception, so this is
not inferred from a zero-ring cylinder alone. Nonlinear timestamp relabeling
is correctly limited to order preservation; homogeneous exponential hazards
change.

The heterogeneous marked shared-wire masses are correct:

```text
rates (1,2): (1/16)(1/3,2/3) = (1/48,1/24),
rates (2,2): (1/16)(1/2,1/2) = (1/32,1/32).
```

The paper names this a variant and does not pretend that relative rates were
derived by D34b.

## 7. Quantum mathematics and scope

Although the primary assignment is the classical theorem, I checked that the
paper's combined conclusion does not borrow an unreviewed quantum statement.

The D34c functional splits into four disjoint `2x2` rank-one Gram blocks, so it
is strongly positive with rank four. Coherent path incidence gives
`(0,1/2,1/2,0)`. Masking unequal path values gives the independently
constructed recorded-path functional `I_8/8`, with four durable `1/4` cells.
The paper correctly calls their comparison durable-record insufficiency across
different past instrument contexts, not non-Markovity of one fixed process.

The separate causal-break witness is correct. From

```text
rho_PE = (|00><00| + |11><11|)/2,
```

past operations `I_P` and `X_P`, followed by the same nonzero `P=0` outcome,
discard, and `P=0` repreparation, leave conditional joint states `|00><00|`
and `|01><01|`. The outcome probability is `1/2` in both cases and the reduced
middle P state is `P0` in both cases. The same future `CNOT(E->P)` gives P0 and
P1 with certainty. This one fixed process therefore violates the operational
causal-break Markov condition.

Retaining joint PE makes the displayed total finite update Markov; eliminating
E yields reduced multi-time memory. The paper limits `P0,P1,P+` tomography to
one real-symmetric two-level operator, excludes the complex Y component, and
does not infer a universal finite quantum Markov order or timed quantum
history law.

## 8. Capacity, literature, and open-result ledger

The capacity ledger matches D34c/D34d. Uniformly bounded resources are only:

```text
fresh event-outcome rank = 6,
immediate event incidence in/out arity <= 2.
```

The paper explicitly leaves Ulam identifier length, actor degree, total
configuration size, boundary width, age-vector dimension, and posterior
complexity unbounded or unproved. Thus it does not infer bounded actor memory
from bounded event factors.

Primary-source checks support the attributions:

- Shalizi–Crutchfield identify causal-state representations as minimal for
  accurate prediction;
- Geiger–Temmel define strong `k`-lumpability through `k`th-order Markovity for
  every starting distribution;
- Marzen–Crutchfield analyze minimal predictive causal states for discrete
  renewal processes;
- Pollock et al. give an operational necessary-and-sufficient Markov condition
  for multi-time quantum processes;
- Taranto et al. prove that no non-Markov quantum process has finite Markov
  order with respect to every possible instrument.

The paper claims none of those abstract structures as original. Its stated
SHARD-specific contribution is limited to their exact application to the
chosen D34b/D34c family.

The closing open ledger is complete: rate/operation selection, dynamic
adjacency and component joining, the timed D34b–D34c operator-valued measure,
an intrinsic profinite quantum extension, cone/dimension recovery, and the
relation of construction time to proper time all remain open.

## 9. External opening: stems, active collars, and the profinite spectrum

The proposed canonical-state opening does not change the verdict, but it is an
important object-typing check. Three constructions must not be identified:

1. A **whole stem** is an ancestor-closed realized past (or, in the v9
   spectrum, a finite down-set occurrence type answered by a completed
   history). It contains settled historical structure, much of which may be
   irrelevant to a declared future query.
2. An **active collar/boundary** is the current interface through which the
   licensed future of a region can still couple to the rest. It is a proposed
   statistic of the current configuration, not automatically the whole stem
   and not automatically bounded.
3. A **predictive equivalence class** is law- and experiment-relative: two
   pasts are identified only when their conditional laws agree for every
   licensed future experiment. It is a quotient by future behavior, not an
   ancestor-closure operation or a topological completion.

Paper 21 states this correctly. `X_t`, `Z_t`, `[h]_pred`, and `B_A(h)` are
separate objects; the collar earns canonical predictive status only if the
screening equation in section 2.4 is proved. Proposition 2 shows that A's tip
alone fails that test. The paper leaves open whether the right representative
is a growing collar, a belief over a collar, a connected component, or some
smaller law-relative quotient. It does not assume that the canonical state
must live on one record.

No connection to the v9 profinite stem spectrum is claimed or presently
earned. V9 Paper 7's stem spectrum is the Stone spectrum of the Boolean
algebra generated by covariant stem-occurrence questions; equivalently, its
covtree tower refines exact-rank stem signatures. That compact observable
space hosts covariant measures and forgets distinctions inside stem-equivalent
fibers. It is not by itself:

- a current active boundary of a growing Harris configuration;
- the physical next-record filtration;
- a law-relative predictive quotient;
- a proof that future conditionals factor through finite stem data.

Indeed, the same stem-spectrum point can have multiple completed-history lifts
on rogue fibers, while predictive equivalence depends on the chosen law and
future experiment algebra. Conversely, two distinct stem signatures could in
principle induce the same future conditional under a special law. A real
bridge would have to push the D34b law to a declared stem/covtree filtration,
disintegrate future extensions there, and prove that some active-collar or
stem-signature statistic is sufficient. D34d performs none of those steps.

Paper 21's only profinite statement is that an intrinsic profinite quantum
extension remains open. That is the correct ceiling; it neither consumes nor
misattributes the v9 stem-spectrum theorem.

## 10. Final disposition

Paper 21 does not exceed the clean evidence. Its terminal noun is exact:

> **D34d GLOBAL-MARKOV / LOCAL-GENERATOR / OBSERVABLE-MEMORY
> CHARACTERIZATION.**

At reviewed strength this means:

- the selected static-adjacency D34b law is strong Markov on its complete
  global Harris configuration;
- its generator is a sum of support-local actor terms;
- record projections can be Markov or non-Markov according to explicitly
  scoped predictive sufficiency/lumpability;
- the finite quantum specimen has operational memory and is Markovized by
  retaining its joint boundary state;
- no bounded local predictive collar, physical proper time, timed quantum
  law, or unique universe rule follows.

**ACCEPT / TERMINAL-CLEAN — 0B / 0M / 0m / 0n.** No mandatory paper edit or
scientific repair remains.
