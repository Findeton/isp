# Paper 21 round 5 — boundary/locality target closing delta

**Target:** commit `befb10c`, audited without qualification against the two
minor findings and one nit in
`paper21-round4-boundary-locality-target-final-delta.md`, followed by a fresh
regression pass over all of repaired section 10.

**Exact verdict:** **DELTA-CLEAN / UNQUALIFIED CLOSURE — 0 BLOCKER / 0 MAJOR /
0 MINOR / 0 NIT.**

The carrier-class outcome, whole-component/global distinction, candidate
D34b-to-v9 map gates and per-branch verdict tuple are all repaired exactly.
The repairs introduce no new boundary, locality, clock, stopping, NSE,
capacity or causal-meaning overclaim. The boundary/locality side of the D34e
target is ready to freeze.

This is a prose-only target delta. I did not rerun the frozen D34d executables:
`befb10c` changes no accepted theorem, probability, matrix, receipt or output
hash.

## 1. Round-4 m1 — carrier-class and whole/global outcomes: CLOSED

The former universal-looking label

```text
NO RECORD-CARRIED EXACT REALIZATION
```

has been replaced by

```text
NO EXACT REALIZATION IN THE DECLARED CARRIER CLASS.
```

The criterion quantifies over every member of the frozen physical carrier
class `C`, not merely the tested finite candidate list. Universal
nonrealizability language is explicitly reserved for a theorem over the full
physically admitted record-carrier class. Candidate-list failure remains the
strictly weaker `CANDIDATE-CLASS OBSTRUCTION` outcome.

The previous combined `WHOLE-COMPONENT/GLOBAL ONLY` label is also split:

- `WHOLE-COMPONENT ONLY` requires necessity of the complete connected-
  component state at the declared scope and excludes irrelevant disconnected
  global factors;
- `GLOBAL ONLY` requires a theorem that the connected component is
  insufficient and that the declared complete global state is necessary.

Thus the emitted verdict now says which physical width is required. A
distributed component-sized carrier is no longer silently conflated with a
state containing disconnected factors. The all-future growing-carrier row
also explicitly excludes either necessity theorem, so first-applicable
ordering does not hide a whole/global result behind a generic growing-width
pass.

**Disposition:** closed without remainder.

## 2. Round-4 m2 — candidate `u` and bridge gate zero: CLOSED

Section 10.5 now types

```text
u = candidate mark-forgetting/causet map.
```

It cannot be used in the posterior pushforward until all four required gates
are established:

1. forgetting marks/types sends the completed D34b event/wire order into the
   past-finite completed-causet domain used by v9;
2. the map is well defined under the declared event/Ulam relabeling gauge;
3. the map is Borel measurable under the chosen D34b and v9 history codings;
4. the conditional completion law admits the stated pushforward through it.

Failure refuses this online-to-v9 bridge branch rather than passive prediction
itself. The notation therefore no longer supplies the main domain/codomain
bridge by assumption.

The neighboring profinite discipline remains intact. A current finite past is
not assigned one future-known spectrum point; its candidate adapted datum is a
posterior measure over completions. Completed-observable factorization,
online-predictive factorization and construction of an adapted inverse limit
remain three separate claims. A marked carrier may be called profinite only
after the required finite inverse-limit/Stone structure is established.

**Disposition:** closed without remainder.

## 3. Round-4 nit — verdicts are indexed per frozen branch: CLOSED

Section 10.8 now freezes every decision branch as

```text
(mu,A,Q,I,S,C),
```

with `I` omitted passively. The first-applicable rule operates only within
that branch, and each theorem label additionally says `A.S.` or `POINTWISE`.
An undefined operational input therefore cannot preempt a licensed passive
result, and changing law, region, question, instruments, stopping algebra or
carrier class cannot be hidden inside one verdict.

The almost-sure branch uses one common full-measure reachable domain for the
licensed family; the pointwise alternative uses every legal reachable state.
Pre-stop interventions require their controlled past law or a declared
dominating measure rather than passive `mu` by default. These qualifications
make the branch tuple operational rather than merely decorative.

**Disposition:** closed without remainder.

## 4. Fresh section-10 boundary/locality regression pass

### 4.1 Boundary and causal meaning: PASS

The target remains a **predictive record-DAG boundary**. “Causal” is explicitly
limited to the record/wire DAG and is not promoted to a spacetime light cone,
Lorentz covariance, finite propagation speed or proper time. Construction
covariance remains gauge invariance under alternative serializations of
disjoint incomparable record-DAG updates at the same stopping scope.

No graph neighborhood, stem class, current record or fixed shell is assumed
to realize the predictive quotient before the screening and recursive-closure
proofs.

### 4.2 Clock, stopping and recursive closure: PASS

The frozen stopping scopes remain distinct:

- fixed construction time;
- A-own-ring count;
- A-wire-event count, including passive receptions.

Global event depth remains only an auxiliary enumeration and locality-negative
control. The recursive update continues to include elapsed time,
survival/no-event information, renewal-age flow, passive and cross-boundary
inputs, externally initiated events, and touched or created boundary records.
An embedded event-chain candidate must disclose exactly which waiting-time
data it discards.

No new text converts the auxiliary construction clock into record proper time
or a spacetime coordinate.

### 4.3 Screening, NSE and D5 ownership: PASS

Predictive omission while a sealed record persists is still separate from
physical deletion/compression. Only the latter invokes an independent
NSE/isometric-carrier theorem preserving all protected distinguishability.
No query-relative screening equality is promoted to global evidence erasure.

D5 messages remain conditional carrier candidates. A physical factor cover,
typed scopes and values, interface embeddings and exactly-once ownership must
be constructed or supplied and audited before contraction earns any
record-native or causal-boundary interpretation.

### 4.4 Capacity and locality resources: PASS

The required ledger still separates graph radius, actor/record count,
open-port count, finite-state count where finite, continuous dimension and
precision, unbounded fields, identifier cost and the independently typed
quantum widths. Fixed radius is not treated as bounded capacity under
unbounded incident degree. Finite per-click content is not promoted to a
uniform boundary-memory theorem.

### 4.5 Finite audit and promotion scope: PASS

Finite computation earns only `D(N,H,Q,I,S)`-sufficiency. Current-size and
future-horizon promotion still require distinct induction/closure and
limit/stabilization theorems. Candidate obstruction, declared-class
exclusion, finite-domain survival, bounded all-future realization and growing
all-future realization remain distinct outcomes.

No finite enumeration is allowed to produce a bounded-collar, all-size or
all-future headline.

### 4.6 Status ceiling: PASS

The repaired section still ends at

> **D34e TARGET IDENTIFIED; PREDICTIVE RECORD-DAG BOUNDARY UNCONSTRUCTED.**

Nothing in `befb10c` converts the target architecture into a derived physical
boundary, a local interactive click law, a v9 profinite realization or a
spacetime locality theorem. Paper 21's D34d result and its receipts are not
reopened.

## 5. Exact closing ledger

| Audit item | Disposition |
|---|---|
| Carrier-class exclusion label matches theorem quantifier | **PASS** |
| Candidate-list obstruction remains weaker | **PASS** |
| Whole-component and global necessity emitted separately | **PASS** |
| Candidate `u` is not assumed to exist | **PASS** |
| Domain, gauge, measurability and pushforward gates present | **PASS** |
| Bridge failure does not refuse passive prediction | **PASS** |
| Verdict frozen per `(mu,A,Q,I,S,C)` branch | **PASS** |
| Passive and operational outcomes cannot preempt one another | **PASS** |
| `A.S.` and `POINTWISE` domains are labeled | **PASS** |
| Record-DAG causality not promoted to spacetime locality | **PASS** |
| Clock/no-event/passive-crossing closure preserved | **PASS** |
| Screening remains distinct from NSE erasure | **PASS** |
| D5 physical cover and ownership remain gated | **PASS** |
| Fixed radius remains distinct from bounded capacity | **PASS** |
| Finite cells do not earn all-future promotion | **PASS** |
| Fresh §10 boundary/locality regression | **NONE FOUND** |

The exact terminal count is therefore:

> **0B / 0M / 0m / 0n.**

No further boundary/locality target repair is required before freezing D34e.
This closes the specification audit only; it does not claim that the boundary
has been constructed.
