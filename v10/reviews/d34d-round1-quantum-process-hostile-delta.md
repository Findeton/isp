# D34d round 1 — quantum/process hostile delta review

**Repaired target:** commit `b92b82b`, reviewed strictly against every finding
in `d34d-round1-quantum-process-hostile-review.md`.

**Verdict:** **SUBSTANTIVELY DELTA-CLEAN; TWO NITS REMAIN**.

**Counts:** **0 BLOCKER / 0 MAJOR / 0 MINOR / 2 NIT**.

The repaired receipt now keeps four different statements separate:

1. coherent versus path-recorded D34c contexts prove durable-record
   operational insufficiency across past instruments;
2. a new fixed three-slot process independently proves operational
   non-Markovianity through a causal break;
3. `P0,P1,P+` provide only single-time rebit tomography;
4. retaining E as joint boundary state and eliminating E into a reduced
   multi-time process are alternative architectures.

No round-one quantum claim blocker, major, or minor survives.

## 1. Fresh reproduction

I ran:

```text
PYTHONHASHSEED=57721 python3 v10/code/d34d_quantum_predictive_exact.py
PYTHONHASHSEED=65537 python3 -O v10/code/d34d_quantum_predictive_exact.py
PYTHONHASHSEED=104729 python3 -O v10/code/d34c_nse_quantum_history_exact.py
```

Both D34d executions exit zero, print 10/10, and reproduce

```text
cc496ff94d360c34ffb5f52b2e4ba57f342378d3807198a3a0f5d9ff01c4dce0
```

exactly.  The parent D34c receipt independently reproduces 14/14.  I found no
float, tolerance, stochastic gate, external dependency or hash-order effect.

## 2. Independent exact rebuilds

### 2.1 Recorded-path functional

The coherent functional has four `(s,o)` path blocks

```text
(1/8) [[1, eta], [eta, 1]],  eta=(-1)^(1+s+o).
```

The orthogonal path receiver imposes `delta_(p,p')`.  Because D is already
zero unless `(s,o)=(s',o')`, equality of `s,o,p` means equality of the complete
fine history.  Therefore

```text
D_rec = I_8 / 8.
```

It is Hermitian, normalized under incidence (`sum D_rec=1`), strongly
positive, rank eight, and gives each durable `(s,o)` cell
`1/8+1/8=1/4`.  This independently confirms Q1 and closes round-one m1.  The
coherent probabilities remain `(0,1/2,1/2,0)` and belong to the distinct
coherent functional; the repaired text no longer treats diagonal selection as
another coarse reading of that same experiment.

### 2.2 Fixed three-slot causal-break process

Use basis `|P,E>=|00>,|01>,|10>,|11>` and one fixed initial state

```text
rho_corr = diag(1/2,0,0,1/2).
```

The allowed past choices give

```text
I_P: rho_corr,
X_P: rho_anti = diag(0,1/2,1/2,0).
```

The same middle causal break selects `P=0`, discards P, and reprepares `P0`.
The selected outcome has probability `1/2` in both cases.  Its normalized
joint outputs are

```text
I_P history: |00><00|,
X_P history: |01><01|.
```

Both reduce to the identical present system state `P0`.  The same future
`CNOT(E->P)` fixes `|00>` and maps `|01>` to `|11>`, producing certain future
`P0` versus certain future `P1`.  Thus future statistics depend on the past
instrument after the system-carried information has been broken and the same
system state reprepared.  Q8 is a valid operational non-Markov witness inside
one fixed process, not the old cross-model inference.

### 2.3 Tomography and boundary fork

For arbitrary real-symmetric

```text
rho=[[a,b],[b,c]],
```

the effect signature is

```text
(p0,p1,p+)=(a,c,(a+c+2b)/2),
b=p+-(p0+p1)/2.
```

Q4 now calls this exactly what it is: a rebit tomographic effect set.  It
explicitly refuses multi-time process closure and general complex-qubit
tomography.  Round-one M2 and m4 are closed.

At the middle cut above, the two joint `P,E` states differ while their reduced
P states coincide.  Keeping `P,E` therefore supplies a closed joint-state
update; eliminating E produces a reduced multi-time memory problem.  Q9 and
§9.3 report those as alternatives, not synonyms.  Round-one m2 is closed.

### 2.4 Remote product theorem

For arbitrary local `rho`, local effect `F`, and trace-one remote product
factor `sigma`,

```text
Tr_E(rho tensor sigma)=rho Tr(sigma)=rho,
Tr[(F tensor I)(rho tensor sigma)]=Tr(F rho) Tr(sigma)=Tr(F rho).
```

This proves the universal product-factor statement carried by Q9; the generic
rational matrix is a regression, not the proof.  The repaired text explicitly
excludes initially correlated or returning factors from that product theorem.
Round-one m3 is closed.

## 3. Round-one finding ledger

| Round-one finding | Delta disposition |
|---|---|
| M1: cross-context difference called one-process quantum non-Markovianity | **CLOSED** — Q3 rescoped; independent Q8 fixed-process causal break added |
| M2: tomography called multi-time predictive closure | **CLOSED** — Q4 is rebit state tomography only |
| m1: recorded probability not fail-closed through `D_rec` | **CLOSED** — `D_rec=delta_(p,p')D=I_8/8` constructed and gated |
| m2: joint boundary and process tensor conflated | **CLOSED** — Q9/§9.3 separate retained-E and eliminated-E architectures |
| m3: finite remote sample narrated as universal theorem | **CLOSED** — exact tensor/partial-trace identity stated; product scope explicit |
| m4: real-qubit scope might silently widen | **CLOSED** — rebit/real-symmetric restriction and complex-qubit open explicit |
| n1: rank accumulator is a presumed-block count | **OPEN NIT** — unchanged |
| n2: tomographic effects called one instrument | **CLOSED** — now consistently an effect set |

## 4. Remaining nits

### n1 — rank certification remains indirectly named

Q1 still sets `rank=0` and increments it once for each of the four presumed
blocks.  The simultaneously gated zero determinant and positive trace prove
each disjoint block has rank one, so `rank=4` is mathematically correct and no
claim fails.  Rename this value `rank_from_block_proof`, or compute row rank,
so the receipt does not look like an independent rank calculation.

### n2 — stale Q3 lumpability names survive below the repaired headline

The printed Q3 statement is now correct, but its source comment still says
`operational/instrument lumpability` and its Boolean is named
`quantum_lumpability_fails`.  This is exactly the terminology the repair
rightly removed from the claim: the coherent and recorded cases are distinct
past instrument contexts, not hidden states of one fixed transition kernel.
Rename the Boolean to something such as
`record_projection_operationally_insufficient` and update the comment.

These are nomenclature/certificate nits only.  They do not require a new
mathematical gate or reopen any result.

## 5. Claim ceiling

The repaired maximum quantum noun is accepted:

> **FINITE FIXED-PROCESS QUANTUM MEMORY + REBIT BOUNDARY-STATE
> CHARACTERIZATION.**

The combined D34d noun is also safe on this stream: it speaks of a finite
fixed-process causal-break witness that is Markovized by retaining the joint
boundary state.  It does not claim the absent timed D34b–D34c operator-valued
law, universal finite Markov order, general complex-qubit closure, bounded
SHARD memory, or a derived physical law.

After the two source-level naming nits are cleaned, the quantum/process delta
can be recorded as `0B/0M/0m/0n DELTA-CLEAN` without rerunning any conceptual
opening.
