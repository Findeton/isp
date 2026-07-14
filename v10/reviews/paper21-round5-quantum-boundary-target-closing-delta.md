# Paper 21 round 5 — quantum-boundary target closing delta

**Target:** commit `befb10c`, audited without qualification against the two
minor findings and one nit in
`paper21-round4-quantum-boundary-target-final-delta.md`, followed by a fresh
regression check of repaired §10.

**Exact verdict:** **DELTA-CLEAN — 0 BLOCKER / 0 MAJOR / 0 MINOR / 0 NIT.**

The common-domain quantifier, outcome-resolved quantum-update types and width
definitions are all repaired exactly.  The repairs introduce no fresh quantum,
operational, measure-theoretic or profinite overclaim.  The quantum side of the
Paper 21 D34e target is ready to freeze.

## 1. Round-4 finding disposition

### m1 — common almost-sure operational domain: CLOSED

The old statement could be read as allowing a different exceptional null set
for each licensed instrument.  Section 10.2 now freezes one common
`mu`-full reachable set `H_0` and requires

```text
K^I_(tau,A)(h,.) = Kbar^I_(tau,A)(B_A(h),.)
    for every h in H_0 and every licensed I.
```

This is the required simultaneous quantifier order.  The text also supplies
the two correct routes to that common domain:

- finite or countable determining instrument/query families permit
  intersection of full-measure sets;
- uncountable families require a jointly regular version or a determining
  subfamily plus an extension theorem.

The pointwise alternative is separately typed on every legal reachable state,
and every theorem/verdict must say `A.S.` or `POINTWISE`.  Section 10.4 repeats
the same domain distinction in the screening gate, and §10.8 carries it into
the outcome labels.  Thus the repair is not a local notation patch followed by
an inconsistent theorem statement.

The adjacent regression is also closed: when an intervention precedes the
conditioning stop, §10.1 requires the controlled past law or a declared
dominating measure rather than passive `mu`.  No operational branch now gains
its conditioning domain from an unlicensed passive-law substitution.

### m2 — outcome-resolved instrument branches: CLOSED

Section 10.6 now distinguishes all three update types required by the hostile
review:

```text
deterministic encoder/update
    completely positive, trace preserving and causal;

outcome-resolved instrument branch
    completely positive and trace nonincreasing;

sum over outcome branches
    trace preserving and causal.
```

It further states that a normalized conditional update is derived by
conditioning and is not asserted to be a linear channel.  Ports, trace/link
conventions and the use of subnormalized boundary states must be fixed.  This
is the correct typing for the paper's durable outcome words and adaptive
instrument scope.

No occurrence elsewhere in §10 re-promotes an outcome-conditioned normalized
map to a channel.

### n1 — carrier, ancilla-memory and cut widths: CLOSED

The three primary widths are now defined as

```text
d_carrier = minimum Hilbert dimension over record-native retained carriers
            subject to declared ownership constraints;
d_op      = real or complex span dimension of conditional operational
            boundary functionals;
chi_cut   = operator-Schmidt rank of the conditional-comb Choi operator under
            one explicitly named tensor bipartition.
```

The possible ancilla-memory minimum is explicitly over the declared
**unrestricted comb/process realizations**, in contrast to the record-native,
ownership-constrained `d_carrier`.  “Bond rank” is reserved for a separately
declared tensor-network convention.  Density-operator rank and channel
Choi/Kraus rank remain separately named and cannot substitute for any of these
without a theorem.

The former ambiguity between two apparently identical “minimal memory
dimensions” is therefore gone, and the algebraic meaning of `chi_cut` is
fixed.

## 2. Fresh §10 regression audit

### Operational quotient and carrier factorization: PASS

- Passive prediction and controlled intervention remain different supplied
  inputs.
- Predictive equivalence still compares every licensed typed instrument and
  durable outcome, with adaptive choices and entangled-ancilla scope declared.
- Probabilities still arise from contraction with a supplied conditional
  process/decoherence object, never fine-history diagonals.
- The quotient remains law-, region-, query-, instrument- and
  stopping-relative.
- Sufficiency, exact minimality and physical record-native realization remain
  separate claims.

### Quantum consistency ledger: PASS

The edit leaves the four independent consistency layers intact:

1. finite `D_n`: normalization, Hermiticity and strong positivity;
2. tower: exact restriction/incidence projectivity;
3. conditional comb: Choi positivity, causal trace constraints and compatible
   named marginals;
4. physical update realization: the correctly typed CP/trace/causality gates
   audited above.

Strong positivity is not attributed to a restriction map.  Projectivity does
not stand in for complete positivity or comb causality.

### Auxiliary witness scope: PASS

The `P,E` construction remains explicitly a negative control showing that a
reduced one-time state can fail.  It neither constructs a SHARD boundary nor
proves that the D34b–D34c law requires a process-memory carrier.

### Quantum-profinite nonclaim: PASS

The profinite section remains a list of bridge gates, not a quantum extension
theorem.  It separates completed-history factorization, posterior online
factorization and construction of a new compatible inverse system.  It does
not claim that:

- finite strong positivity and projectivity automatically extend to an
  infinite quantum history object;
- operational responses are continuous in the v9 stem topology;
- quantum marks, ports or combs factor through finite stem partitions;
- the profinite topology selects the law, instruments or physical carrier.

The new mark-forgetting gates and topology language strengthen that refusal;
they do not smuggle in a quantum bridge.

### Claim strength and outcome classes: PASS

The repaired target still says **boundary unconstructed**.  Finite enumeration
earns only registered-domain sufficiency; arbitrary-size and arbitrary-horizon
promotion require separate theorems.  The quantum width ledger is diagnostic,
not evidence that a bounded carrier exists.  No edit alters Paper 21's D34d
theorems or its finite receipts.

## 3. Closing disposition

| Closing audit item | Disposition |
|---|---|
| One common `H_0` for all licensed instruments | **PASS** |
| Uncountable-family/common-version gate | **PASS** |
| Pre-stop intervention past-law typing | **PASS** |
| Deterministic update CPTP/causal | **PASS** |
| Outcome branches CP trace-nonincreasing | **PASS** |
| Branch sum trace-preserving/causal | **PASS** |
| Normalized conditioning not called a channel | **PASS** |
| Record-native `d_carrier` distinguished from ancilla memory | **PASS** |
| `chi_cut` fixed by Choi bipartition | **PASS** |
| Prior positivity/projectivity/comb gates preserved | **PASS** |
| Typed operational equivalence preserved | **PASS** |
| `P,E` negative-control scope preserved | **PASS** |
| No profinite quantum extension claimed | **PASS** |
| Fresh §10 regression | **NONE FOUND** |

The exact closing count is therefore:

> **0B / 0M / 0m / 0n.**

No further quantum-boundary text repair is required before freezing the D34e
investigation.  This closes only the target specification; it does not claim
that the predictive record-DAG boundary, its quantum process carrier or its
profinite realization has been constructed.
