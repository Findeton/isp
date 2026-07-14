# Paper 21 round 1 — quantum/literature terminal hostile review

**Frozen target:** commit `afbd2ba`, especially paper 21 §§2, 7, 9–12 and
the D34c/D34d receipt dependencies it consumes.

**Verdict:** **PASS WITH MINOR TERMINAL-DOCUMENT REPAIRS**.

**Counts:** **0 BLOCKER / 0 MAJOR / 2 MINOR / 3 NIT**.

The D34c functional, licensed probability partitions, fixed-process
causal-break witness, boundary-state Markovization and rebit/process-tensor
scope are all correct.  The paper's quantum claim ceiling is accepted.  The
remaining work is provenance and precision: add the omitted D34c dependency
to the terminal evidence table, stop grouping the generic auxiliary `P,E`
causal-break specimen under the “exact D34b/D34c mapping,” and tighten three
small phrases.

## 1. Independent reproduction and manifest cross-check

I ran both quantum dependencies from the frozen tree:

```text
PYTHONHASHSEED=262147 python3 -O v10/code/d34d_quantum_predictive_exact.py
PYTHONHASHSEED=524309 python3 -O v10/code/d34c_nse_quantum_history_exact.py
```

Results:

- D34d: 10/10, exact summary SHA-256
  `cc496ff94d360c34ffb5f52b2e4ba57f342378d3807198a3a0f5d9ff01c4dce0`;
- D34c: 14/14, committed output file SHA-256
  `9ce73a693b41f765eff163749ef769ca0cb4ce856ead66d690a63a20331a731a`.

The D34d review chain ends unqualified `DELTA-CLEAN — 0B/0M/0m/0n` in
`d34d-round3-quantum-text-final-delta.md`.  D34c LEDGER #171 is terminal at
the finite typed-DAG width: its quantum-mathematics and NSE/seal deltas are
clean; the architecture delta accepted the core with small representation
corrections, all of which were applied in the terminal commit before the
`9ce73...` output.  No timed operator-valued D34b–D34c law was approved.

## 2. D34c functional and licensed probabilities

Paper 21 reproduces the exact D34c formula

```text
D((s,p,o),(s',p',o'))
 = (1/8) delta_(s,s') delta_(o,o')
   (-1)^[p(1+s+o)+p'(1+s'+o')].
```

For fixed `(s,o)`, its path block is

```text
(1/8) [[1,eta],[eta,1]],  eta=(-1)^(1+s+o),
```

with eigenvalues `(1/4,0)`.  The four disjoint blocks make D rank four,
Hermitian, normalized and strongly positive.

The coherent durable `(s,o)` partition is decoherent because D has no cross
terms between different durable cells.  Incidence-summing the two path
alternatives gives

```text
(P_00,P_01,P_10,P_11)=(0,1/2,1/2,0).
```

The support-excluded orthogonal path receiver defines a **different**
functional,

```text
D_rec=delta_(p,p')D=I_8/8,
```

which is normalized and strongly positive and gives four durable `1/4`s.
Paper 21 correctly keeps the two experiments separate.  It never reads the
fine diagonal of the coherent D as a probability partition without the
receiver/dephasing construction.  The coherent/dephased H-output comparison
is also correctly scoped as durable-record insufficiency across two declared
past instrument contexts, not one-process non-Markovianity.

**Disposition:** exact and licensed; no finding.

## 3. Fixed three-slot causal-break witness

The paper's single process starts from

```text
rho_PE=diag(1/2,0,0,1/2).
```

Past `I_P` leaves this state correlated; past `X_P` produces
`diag(0,1/2,1/2,0)`.  Selecting the same middle `P=0` outcome has probability
`1/2` in both cases.  Discarding P and repreparing `P0` leaves conditional
joint states `|00><00|` and `|01><01|`, both with reduced P state `P0`.  The
same future `CNOT(E->P)` then produces local `P0` and `P1` with certainty.

Thus a fixed process retains past-instrument dependence after a genuine
causal break.  One allowed witness is enough to violate the operational Markov
condition.  This matches the criterion of Pollock et al., [*Operational Markov
Condition for Quantum Processes*](https://arxiv.org/abs/1801.09811).  It is no
longer the rejected inference from coherent-versus-recorded model contexts.

**Disposition:** Proposition 3 is mathematically sound at its declared finite
width; no finding.

## 4. Boundary-state Markovization and process-tensor scope

Paper 21 makes the correct architectural fork:

- retain E: the current joint `P,E` density operator distinguishes the two
  middle histories and closes under the declared controlled operations;
- eliminate E: the identical reduced P state does not determine the future,
  so a reduced multi-time process description carries memory.

The paper does not say that one record's reduced density matrix is sufficient.
Nor does its `P0,P1,P+` calculation reconstruct a process tensor: it is
explicitly a tomographic effect set for one real-symmetric two-level state.
The missing Y-sensitive setting and general complex-qubit closure are refused.
The finite witness is not upgraded to universal finite quantum Markov order,
consistent with Taranto et al., [*Quantum Markov
Order*](https://arxiv.org/abs/1805.11341) and [*The Structure of Quantum
Stochastic Processes with Finite Markov
Order*](https://arxiv.org/abs/1810.10809).

**Disposition:** correct scope; no finding.

## 5. Predictive boundary and the profinite-stem opening

The external opening is handled correctly in the body.  Paper 21 first defines
the canonical **law-relative behavioral quotient** `[h]_pred` by equality of
all licensed future laws (§2.3).  Only afterward does it ask whether that
quotient has a state representation carried on a record/collar/boundary
(§2.4).  It does not identify “canonical predictive state” with one record or
assume a bounded collar.

Quantumly, the analogous predictive object may be a joint boundary state when
the boundary is retained or a process tensor/comb when it is eliminated.  The
paper states this, rather than placing an independent qubit beside each actor
and calling it sufficient.

No connection to the v9 profinite stem spectrum is earned or claimed.  Section
9 explicitly leaves an intrinsic profinite quantum extension open.  D34d has
not shown that predictive equivalence is continuous in the stem topology,
respects every finite-stem cylinder, or factors to a quotient of the profinite
completion.  Those would be additional theorems.

**Disposition:** the non-claim is correct.  Nit n3 below would make the open
and the possible nonexistence of a record-carried realization still clearer.

## 6. Literature and priority audit

The primary-source attributions are accurate:

- Shalizi–Crutchfield establish causal-state predictive equivalence and
  minimality;
- Geiger–Temmel distinguish strong all-initial-law lumpability from narrower
  law-relative behavior;
- Marzen–Crutchfield study renewal predictive states and elapsed-age memory;
- Pollock et al. supply the causal-break operational Markov condition;
- Taranto et al. establish instrument dependence of finite quantum Markov
  order.

Paper 21 correctly says those structures are prior art.  One subsequent
priority sentence is too broad, however: its auxiliary `P,E` causal-break
example is a generic diagnostic implementation of the established
process-tensor criterion, not an exact construction inside the D34b actor law
or D34c typed-DAG history functional.  That is m2 below.

## 7. Findings

### m1 — the “terminal evidence base” omits the D34c dependency

Section 7 consumes the D34c functional, orthogonal receiver and real carrier
construction; §8 consumes D34c's six-state event factor and incidence-arity
result.  Yet §11 lists only the D34d executables and D34d delta streams.

This is not a false number, but it makes the terminal provenance table
incomplete.  A reader cannot recover the parent 14/14 receipt or its terminal
review boundary from the table that calls itself the evidence base.

**Required repair:** add at least:

```text
d34c_nse_quantum_history_exact.py | 14/14,
output SHA-256 9ce73a693b41f765eff163749ef769ca0cb4ce856ead66d690a63a20331a731a
D34c terminal three-stream disposition | LEDGER #171;
finite typed-DAG compatibility accepted, timed quantum lift not accepted
```

If individual reviews are listed, distinguish the quantum/NSE clean deltas
from the architecture core-clean delta whose small corrections were applied
in the terminal commit.

### m2 — the generic causal-break witness is not an “exact D34b/D34c mapping”

Section 10 says the SHARD-specific contribution is “the exact mapping to
D34b/D34c,” and includes “the fixed finite boundary-memory construction” in
that list.  But Proposition 3 is transparently introduced elsewhere as a
**separate** fixed `P,E` process.  Its correlated initial state and three-slot
instrument sequence are not generated by the D34b scheduler, embedded in a
D34c typed actor DAG, or derived from the D34c diamond functional.

The example validly demonstrates the architecture, but its generic exact
instantiation is not a SHARD-specific priority claim.

**Required repair:** split the sentence:

```text
The SHARD-specific contributions are the D34b generator and rate obstruction,
the clock/stopping and capacity ledgers, and the exact D34c durable-record
bridge. Proposition 3 is a diagnostic instantiation of the standard
causal-break criterion; no novelty or completed D34b-D34c embedding is claimed
for that auxiliary process.
```

### n1 — state the ordering of the coherent probability vector

`P(s,o)=(0,1/2,1/2,0)` is correct but its tuple order is implicit.  Write
`(P_00,P_01,P_10,P_11)` once.

### n2 — make the instrument sequence the witness, not a qualified process noun

Proposition 3 says the process is “operationally non-Markovian for the declared
instrument sequence.”  The intended statement is clearer as:

> the declared instrument sequence witnesses operational non-Markovianity of
> this fixed finite process.

This keeps process non-Markovianity as the violated causal-break property and
the displayed instruments as its witness.  It does not change the result.

### n3 — the final open should not presuppose a record-carried realization

The final question asks for “the smallest record-carried ... state,” although
the body correctly leaves existence open.  Replace it by:

> determine whether the law-relative predictive quotient admits a
> record-carried boundary/process representation; if so, characterize the
> smallest such representation and whether its width is bounded.

Optionally append that no factorization through the v9 profinite stem spectrum
has been proved.  This is a clarification, not a new prerequisite for paper
21's result.

## 8. Claim-by-claim terminal disposition

| Paper claim | Disposition |
|---|---|
| D34c formula, rank four, strong positivity | **PASS** |
| Coherent durable law `(0,1/2,1/2,0)` | **PASS**, licensed decoherent partition |
| Recorded-path `D_rec=I_8/8` and four `1/4`s | **PASS**, distinct functional |
| Cross-context durable-record insufficiency | **PASS**, not called fixed-process memory |
| Fixed three-slot causal-break witness | **PASS** |
| Joint-boundary Markovization | **PASS** for the declared finite controlled process |
| Eliminated-boundary reduced process memory | **PASS** |
| Rebit effect tomography | **PASS**, no complex/process-tensor widening |
| Universal finite quantum Markov order | Correctly **NOT CLAIMED** |
| D34c timed/direct-integral quantum history law | Correctly **NOT CLAIMED** |
| Canonical predictive quotient is one record/bounded collar | Correctly **NOT CLAIMED** |
| Predictive quotient factors through v9 profinite stems | Correctly **NOT CLAIMED / OPEN** |
| Literature attributions | **PASS** |
| Q8 auxiliary witness as D34b/D34c-specific contribution | **REPAIR m2** |
| Terminal quantum evidence manifest | **INCOMPLETE m1** |

## 9. Adjudicated ceiling

The paper's scientific endpoint is accepted:

> **D34d GLOBAL-MARKOV / LOCAL-GENERATOR / OBSERVABLE-MEMORY
> CHARACTERIZATION**, with a **finite fixed-process quantum-memory witness and
> rebit boundary-state characterization**.

It remains conditional on the chosen D34b/D34c family and does not derive a
bounded predictive collar, timed quantum history law, profinite-stem
factorization, physical proper time or unique universe rule.

After m1 and m2 repair provenance/priority and the three nits are cleaned, this
quantum/literature stream can move directly to a textual delta.  No executable,
matrix or causal-break calculation needs reopening.
