# Paper 13D Rust realization pin

Date: 2026-08-20

Status: **FROZEN IMPLEMENTATION CONTRACT / PHYSICS IMMUTABLE**

## 1. Authority and purpose

This pin authorizes one clean Rust realization of the terminally accepted
Paper 13D mathematical law. It does not reopen, repair, tune, extend, select,
or reinterpret that law.

The binding mathematical corpus is:

| artifact | commit | SHA-256 |
|---|---|---|
| physics pin | `a20c52a` | `722dc3bfe528fc3a52f2d2f5afcaba2c7858250e63d24439e43d0a17ab5c049e` |
| mathematical law | `efe9d97` | `3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9` |
| construction certificate | `efe9d97` | `93f1e84444d60365fe729d73058dae1f3dede63a87bf1663d4865511255b50bb` |
| hostile protocol | `04f503e` | `4754f89b01c7975ef79de2d9465e54304bbcf2d6e02b942f9957062a63c9eba3` |
| category review | `0c2bd7e` | `190f6ea125b0d8319714f74cd104ad3b6464fce7c816f08eb2d597ecb8cf64d9` |
| probability review | `c2c9743` | `4110f2149c3a424104bd526433314c5370431674ace1e097d9782f9eaf26ed4c` |
| physics review | `f4a367c` | `60eaff32be938006e84df124986e3ae4f72c60399380316b7a14b67034676647` |
| terminal adjudication | `a8cc45e` | `ae2c4ef066335c39a0b8057c897c947b06e4270be67d1ed3ec59bf8d6d0a00c9` |

The adjudicated mathematical product is fixed:

```text
referent    P13D-POINT-FREE-EXECUTABLE-GAMMA-CONSTRUCTED
law         P13D-ONE-TYPED-EXECUTABLE-GAMMA-CONSTRUCTED
experiment  P13D-TYPED-EXPERIMENT-CATEGORY-CONSTRUCTED
nondivision P13D-NATIVE-B1-CUT-NONDIVISIBLE
record      P13D-TYPED-STABLE-FUTURE-CATEGORY-CONSTRUCTED
eraser      P13D-EXECUTABLE-ERASER-CONTROL-CONSTRUCTED
division    P13D-COMPLETE-DIVISION-FRONTIERS-CONSTRUCTED
size        P13D-VARYING-SIZE-COVARIANT-FAMILY-CONSTRUCTED
response    P13D-RECIPROCAL-RELATIONAL-RESPONSE-CONSTRUCTED
actuality   P13D-ACTUALIZATION-UNCONSTRUCTED
```

The implementation is evidence of faithful executable realization. Runtime
tests do not replace the all-finite mathematical proofs and cannot promote a
new scientific coordinate.

## 2. Exact path whitelist

### Stage A — this pin

- `v16/note-paper13d-rust-implementation-pin.md`
- `v16/LOG.md`
- `STATUS.md`

No Rust source may exist before the Stage-A commit.

### Stage B — source construction and freeze

- `v16/rust/p13d_gamma/Cargo.toml`
- `v16/rust/p13d_gamma/Cargo.lock`
- `v16/rust/p13d_gamma/src/lib.rs`
- `v16/rust/p13d_gamma/src/main.rs`
- `v16/note-paper13d-rust-construction.md`
- `v16/LOG.md`
- `STATUS.md`

Cargo's local `target/` directory is disposable build output and must remain
ignored and uncommitted. No fixture, cached scientific object, Python helper,
generated source, or vendored dependency is authorized.

### Stage C — official artifacts, only after source freeze

- `v16/paper13d-rust-result.json`
- `v16/paper13d-rust-receipt.json`
- `v16/LOG.md`
- `STATUS.md`

No Stage-C path may exist during Stage B. Official generation is one
transactional run against the exact frozen source.

No other path is authorized by this pin.

## 3. Toolchain and dependency policy

The crate shall use stable Rust and the 2021 edition. It shall use the Rust
standard library only. This avoids a network-resolved dependency graph and
makes the realization independently buildable from the committed bytes plus a
standard toolchain.

`Cargo.lock` is committed. Unsafe Rust, build scripts, procedural macros,
foreign-function calls, shell execution, environment-dependent scientific
branches, system time, randomness, network access, and repository discovery
are prohibited.

If a local SHA-256 implementation is used for receipts, it must pass the empty
string, `abc`, and one-million-`a` standard vectors. Hashes are evidence only;
no digest may substitute for rebuilding or comparing a mathematical object.

## 4. Representation contract

### 4.1 Exact arithmetic

All probabilities use a normalized signed rational type backed by checked
integers. Construction rejects zero denominators and overflow. Equality is
mathematical equality after sign and greatest-common-divisor normalization.
There are no floating-point values anywhere in scientific objects, tests,
results, or receipts.

The exact constants are immutable:

```text
R  = [[3/5,-4/5],[4/5,3/5]]
B  = [[9/25,16/25],[16/25,9/25]]
C  = [[49/625,576/625],[576/625,49/625]]
B2 = [[337/625,288/625],[288/625,337/625]]
K  = [[351/175,-176/175],[-176/175,351/175]]
```

No parameter, coefficient, threshold, seed distribution, response target,
dimension, or geometry field may be supplied by a CLI flag or edited after a
test result is known.

### 4.2 Finite carriers and presentation action

Occurrences use explicit stable identifiers internal to one presented value;
physical comparison is under the complete finite-set presentation groupoid,
not identifier equality. Port swaps act on every declared X/Y-typed field and
fix scalar fields exactly as in the law. Unordered pairs have a canonical
endpoint representation.

The groupoid implementation shall provide identity, inverse, semidirect
composition, action on every boundary and trace, and exhaustive finite
orbit/pushforward utilities for the bounded verification census. It shall sum
all orbit mass. Selecting one representative's mass is forbidden.

Readers are separate functions over an already constructed physical fiber.
They are absent from stabilizers, orbit construction, and physical-history
identity. A landmark may orient a reader only when it is a typed physical mark.

### 4.3 Boundary invariants by construction

Use distinct Rust types for:

- `B0`, `B1Plain`, `B1Recorded`, `B2Plain`, `B2Recorded`,
  `B3Recorded`, and `B3Erased`;
- formal tensor boundaries retaining component partitions; and
- fused atomic boundaries without that partition.

Fields are private. Validated constructors are the only creation path.
`B1Recorded` derives `r=m`. `B2Plain` and `B2Recorded` derive `t=h`; callers
cannot inject a conflicting `t`. `B3Recorded` and `B3Erased` contain a distinct
`t_plus` with no equality invariant. A later toggle is definable only on
`B3Recorded`.

The empty occurrence carrier is supported. Its unique record word is empty
and all projector statements are vacuous. Claims about two nontrivial sectors
must require a nonempty carrier.

### 4.4 Typed controls and execution

The control category shall use Rust typestates for `Source`, `Mediator`, and
`Closed`. Only the frozen hom-sets have constructors and composition methods.
Right-biased override is associative. A mediator-stage write followed by a
source-stage write must be unrepresentable as a typed composition, not parsed
and rejected after evaluation. Compile-fail documentation or an equivalent
compile-time witness must cover that negative case.

The execution syntax is separate from control syntax. A checked free
symmetric-monoidal AST shall distinguish identity, primitive `U`, queried
`Q0/Qr`, continuation `D/Rc`, composition, independent tensor, simultaneous
fusion, stable entry, stable endomorphisms, and eraser. Composition constructors
compare exact boundary objects/sorts before any probability calculation.

Categorical composition, conditioning, reader pushforward, independent tensor,
physical fusion, and division factorization remain distinct APIs.

### 4.5 One evaluator

One structural evaluator consumes a well-typed execution AST and a complete
source argument and returns an exact finite distribution over complete typed
traces. Atomic seed laws are the frozen fair source bits, `eta` weights
`16/25,9/25`, uniform `[25]` occurrence seeds, and uniform `[25]` unordered-pair
seeds. Private seeds never appear in a trace.

The evaluator must implement exactly:

- the frozen relational packet equations;
- `beta` and `kappa` with thresholds 9 and 49;
- endpoint bond threshold 16 for unequal colors and 9 for equal colors;
- convolution for composition while retaining the shared typed boundary;
- product for independent tensor;
- one simultaneous unordered cross-pair draw set for n-ary fusion; and
- deterministic pushforward for stable maps and eraser.

No observational factorization, cached transition table, alternative evaluator,
history identifier, execution-loop index, reader name, or serialized order may
enter a probability.

## 5. Future, erasure, division, and response

### 5.1 Stable future

`entry` has the sole type `B2Recorded -> B3Recorded`. Stable endomorphisms
act only on `B3Recorded`:

- `Fq(A)` toggles `q_plus`;
- `Ft(A)` toggles `t_plus`;
- `Fxy(A)` swaps every X/Y-typed packet field and fixes scalar color, bonds,
  and record;
- `Fr(A)` toggles record bits and returns the exact induced label transport.

The stable-word evaluator accepts arbitrary finite words in the generated
monoid. Projector transport is checked generatorwise and by compositional
label transport. The implementation may test bounded words as regression
evidence but shall state that arbitrary word length is covered by the accepted
induction theorem, not exhaustive execution.

### 5.2 Eraser

`erase_record` has the sole type `B2Recorded -> B3Erased`. It drops the record
and preserves the other declared fields. It is an execution generator but is
absent from the stable-word enum and stable category constructors.

The positive-support erasure witness must construct two reachable nonempty
source values differing only in record and show equal erased targets. It must
not claim that every syntactically legal relational packet has positive mass,
that all past statistical correlation vanishes, or that the retained trace is
rewritten.

### 5.3 Native cut and complete divisions

The native `B1` restart test consumes exactly the declared `m` carrier and
reconstructs the unique candidate `C B^{-1}`. Its negative entries establish
only the frozen cut-relative result. A positive enlarged `(m,q0)` restart is a
mandatory non-kill.

Complete queried `B1Plain` and `B1Recorded` frontiers must pass equal-boundary
future sufficiency and direct-versus-cut equality on every admitted value in
the bounded exact census. Their endpoint law is `B2`, not `C`. The primitive
`U` path is a different experiment. Stable record and complete division are
stored and tested as independent booleans.

### 5.4 Response

Contrast construction takes an ordered pair of complete experiments, aligns
them with the intersection stabilizer, and returns the complete signed
point-free response before applying coarse readers. Fixed-context and
tautological-context rows are both retained. The unit `X -> zY` mediation
coordinate is positive at fixed `E`; its coarse scalar response under fair
tautological epsilon is zero.

Response means relational counterfactual sensitivity only. The code and
artifacts may not label it causal direction, chronology, geometry,
backreaction, energy transfer, or gravity.

## 6. Mandatory fidelity suite

`cargo test` and `--selftest` must complete the following independent groups.
Each group reports a name, exact check count, and pass/fail; a single failure
returns nonzero.

1. rational normalization, checked arithmetic, and exact matrices;
2. `beta/kappa` counts and `B/C/B2/K` reconstruction;
3. all control hom-sets, identity, override, and associativity;
4. boundary constructor invariants and illegal-target refusal;
5. execution source/target typing and trace retention;
6. relational mechanism truth equations and context-indexed response;
7. bond law for equal/unequal colors;
8. normalized primitive, continuation, composition, tensor, and fusion laws;
9. presentation identity/inverse/composition/action and orbit-mass pushforward;
10. reader independence, landmark orientation, and coarse-reader cancellation;
11. alternative-dependent contrast intersection stabilizer;
12. tensor unit/braiding/product and tensor-versus-fusion separation;
13. zero-, one-, two-, and three-component simultaneous fusion plus deletion;
14. stable entry, every future generator, composition, and record-label transport;
15. executable reachable erasure and stable-grammar exclusion;
16. native restart negativity and enlarged-carrier positive non-kill;
17. complete queried divisions, primitive unqueried nondivision, and the four
    stable-record/complete-division combinations;
18. empty/nonempty carrier behavior, finite-set covariance, and deletion;
19. all registered signed response controls, including cancellation and
    fixed-versus-tautological mediation; and
20. permanent-wall and no-award assertions.

The source shall include at least these semantic regression mutations as test
functions or local altered objects, never as alternate production laws:

- reverse a stage write;
- set a conflicting `t` on a `B2` boundary;
- apply `Ft` to `B2Recorded`;
- include erasure in the stable word grammar;
- use representative mass instead of orbit pushforward;
- put a diagnostic reader in the stabilizer;
- replace simultaneous fusion with an ordered fold;
- drop one cross-pair seed;
- smuggle `q0` into the native restart state;
- confuse primitive `C` with queried `B2`;
- align a contrast with only one alternative's stabilizer; and
- claim fixed-context mediation in the fair tautological row.

These controls defend fidelity. Their labels, counts, or hashes are not
scientific inputs.

## 7. Determinism, CLI, and transactions

The binary accepts exactly:

```text
p13d-gamma --selftest
p13d-gamma --verify-only
p13d-gamma --run RESULT_PATH RECEIPT_PATH
```

Unknown, duplicate, mixed, missing, relative output, identical output, or
extra arguments fail before scientific evaluation. `--selftest` and
`--verify-only` write no file. `--run` accepts only the two exact Stage-C
absolute paths and refuses if either already exists.

Canonical JSON uses UTF-8, lexicographically ordered object keys, exact
rationals encoded as canonical strings, no insignificant whitespace, and one
final LF. Root, alien-CWD, and true source-only/no-`.git` executions must be
byte-identical.

Official publication is paired and transactional: build both complete byte
arrays in memory; create two unpredictable same-directory temporary files with
create-new semantics; write, flush, and `sync_all`; atomically publish the
result, then the receipt; on any failure remove only the temporary or newly
published path created by this invocation. Existing paths are never removed or
overwritten. The receipt binds source, Cargo files, mathematical corpus,
normalized result, every check group, and every promotive object.

## 8. Code-only repair boundary

Without reopening physics, Stage B may repair:

- ownership, borrowing, lifetimes, moves, and clone placement;
- compiler, formatter, lint, module, and visibility errors;
- integer-overflow handling that preserves exact supported values;
- deterministic serialization and SHA implementation defects;
- CLI parsing, path validation, paired publication, cleanup, and rollback;
- allocation, streaming, memory, and runtime problems;
- diagnostics and test harness organization; and
- platform-neutral filesystem behavior.

Every repair must preserve all accepted mathematical objects and canonical
scientific bytes. The construction note records the defect and exact repair.
No sequence of software repairs creates authority to alter physics.

A change to a boundary, invariant, probability, threshold, seed law,
generator, hom-set, group action, mark, reader, contrast, tensor, fusion,
future map, eraser, division argument, response definition, parameter, or
outcome is semantic. On the first such necessity, stop without a successor and
ask the user. There is no automatic Paper 13E or implementation-repair chain.

## 9. Freeze and acceptance gates

Stage B freezes only if:

- the exact mathematical hashes in Section 1 authenticate;
- no unauthorized path or dependency exists;
- `cargo fmt --check`, `cargo test`, and a release `--selftest` pass;
- every mandatory group and semantic regression control passes;
- root, alien-CWD, and true source-only runs are byte-identical;
- source and construction-note hashes, sizes, toolchain, runtime, and check
  counts are recorded; and
- every result coordinate remains explicitly mathematical-accepted but
  implementation-unofficial until Stage C.

Stage C is allowed only after the Stage-B source commit. Its official run must
use the exact frozen source and commit the two artifacts together with their
hashes. A successful Rust realization confirms faithful execution of the
accepted Paper 13D law. It does not select the law, actualize a branch, or open
chronology, dimension, geometry, metric, curvature, gravity, continuum, or QFT.
