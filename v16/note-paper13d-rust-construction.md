# Paper 13D Rust construction freeze

Date: 2026-08-20

Status: **RUST SOURCE GREEN / OFFICIAL ARTIFACTS NOT YET GENERATED**

## 1. Bound authority

The realization authenticates and embeds these immutable scientific
authorities:

| authority | SHA-256 |
|---|---|
| accepted mathematical law | `3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9` |
| terminal mathematical adjudication | `ae2c4ef066335c39a0b8057c897c947b06e4270be67d1ed3ec59bf8d6d0a00c9` |
| Rust realization pin | `f9e710b6f739bc159f741858ebf2993631a823bf23c3dec32eb97a5bbfd83e49` |

No mathematical object was selected, changed, or fitted during construction.
No law parameter, dimension, geometry, metric, desired response, or outcome is
a CLI input.

## 2. Frozen source bytes

| path | SHA-256 | size |
|---|---|---:|
| `v16/rust/p13d_gamma/Cargo.toml` | `0294f5e15e2c28514e1374451bcd59624fdfe889abe78c2b2cafe6a7c656d710` | 19 LF / 262 bytes |
| `v16/rust/p13d_gamma/Cargo.lock` | `5c6ea04a904bd1a03bd049e5bd9e66aff9c10a32a200a19c213e2ae1437f889e` | 7 LF / 154 bytes |
| `v16/rust/p13d_gamma/src/lib.rs` | `779d2e669e9848992c7e8b9d3b210f35150d248ea737359effd59e761e57afcd` | 3,366 LF / 105,342 bytes |
| `v16/rust/p13d_gamma/src/main.rs` | `702cc6c0bb3a643124f30e101de43799bc7f71635ed6e93db4ca674790157a7f` | 37 LF / 1,024 bytes |

The crate has no dependency other than the Rust standard library. It contains
no unsafe block, floating-point type, random-number library, network access,
shell execution, build script, FFI, repository discovery, or generated source.
Cargo's `target/` directory is uncommitted disposable build output.

Toolchain used:

```text
rustc 1.98.0 (88d9e12ae 2026-08-18)
cargo 1.98.0 (797e8a9bc 2026-08-05)
edition 2021
```

## 3. Physical object map

### 3.1 Exact arithmetic and primitives

`Rat` is a normalized checked signed rational over `i128`; a zero denominator
is refused. The scientific code has no floating point. `beta` and `kappa`
implement the frozen thresholds 9 and 49. Direct enumeration gives the exact
`B`, `C`, `B2`, and negative-entry `K=CB^-1` matrices.

The local SHA-256 implementation is receipt infrastructure only and passes the
standard empty, `abc`, and million-`a` vectors. Hashes never replace object
reconstruction or equality.

### 3.2 Boundaries and the Paper 13C failure

The seven atomic boundary species are distinct private Rust types. Validated
constructors are the only creation route. `B1Recorded` derives `r=m`.
`B2Plain` and `B2Recorded` derive `t=h`; no caller-supplied `t` exists.
`B3Recorded` and `B3Erased` instead contain the distinct later field
`t_plus`.

Consequently `Ft` accepts only `B3Recorded`. It cannot be called on a `B2`
value, and the old invariant violation is not representable. The eraser has
the sole type `B2Recorded -> B3Erased`, whereas stable operations have the sole
endomorphism type `B3Recorded -> B3Recorded`.

### 3.3 Typed controls and execution

The `SourceStage`, `MediatorStage`, and `ClosedStage` typestates expose only
the accepted writes. The mediator-stage builder has no source-write method;
the reversed word is covered by a Rust compile-fail documentation test. Exact
right-biased override and every admitted hom-set are separately checked.

`Exec` is a checked reader-free syntax with distinct variants for identity,
primitive `U`, queries, continuations, composition, tensor, n-ary fusion,
stable entry, stable endomorphisms, and erasure. Composition checks exact
source and target objects before evaluation. Conditioning, reading, tensor,
fusion, composition, and division are not conflated.

### 3.4 One global evaluator

`Evaluator::evaluate` is the sole execution route. It constructs the exact
relational packet from the complete source and typed program; uses the frozen
private seed weights; retains complete typed traces; convolves composition;
forms tensor products; draws every n-ary fusion cross pair simultaneously; and
pushes deterministic stable and erased futures forward.

Private seeds, program metadata, readers, hashes, serialization order, history
identifiers, caches, and loop indices occur in no physical trace or
probability. Generic finite recursive constructors realize the all-finite law;
bounded selftests are regression evidence and do not replace the accepted
mathematical induction and normalization proofs.

### 3.5 Point-free quotient and readers

The presentation action implements identity, inverse, semidirect composition,
port action, occurrence transport, and unordered-pair transport. The generic
orbit pushforward sums the mass of every labeled value in a physical class.
The representative-mass counterfeit is an explicit failure control.

Readers are applied only to a fixed physical fiber. A diagnostic reader cannot
enter the stabilizer. Alternative contrasts use the intersection stabilizer;
the exact two-occurrence control has a swap symmetry in one alternative that
is removed by the ordered pair.

### 3.6 Tensor, fusion, futures, and erasure

Independent tensor retains the component family and uses a product law. The
empty tensor is deterministic. Physical fusion is one n-ary generator; it
forgets the partition, carries every internal bond, and draws every unordered
cross-pair bond simultaneously. Zero and one component controls draw no cross
seed. The three-singleton control has three cross pairs and eight exact bond
outcomes; a dropped-pair counterfeit has only four.

Stable words compose exact `Fq`, `Ft`, `Fxy`, and `Fr` operations and their
record-label translations. `Ft` changes only `t_plus`. Erasure is absent from
the stable enum and identifies an explicit positive-support nonempty
cross-record pair while leaving the retained past trace conceptually intact.
The empty carrier has one empty record word and vacuous projector transport.

### 3.7 Cuts and response

The native restart API consumes `B1Plain` or `B1Recorded`, neither of which
contains `q0`. Its unique `K` has negative off-diagonal entries. The positive
enlarged `(m,q0)` route is retained as a non-kill. Primitive `C` and queried
`B2` are computed by different typed experiments and remain unequal.

Both queried frontiers reproduce `B2` on every binary source row in the
bounded census. Record stability and division completeness are tested as
independent properties.

The response tests keep the complete context. At fixed `E`, changing `X`
changes `zY` with unit signed response. Under an actually fair epsilon source,
both `X` alternatives give the fair scalar `zY` law and the coarse response is
zero. This directly enforces the terminal adjudication's scope clause rather
than reproducing the same marginal with a provenance-changing mixture.

## 4. Verification evidence

The release `--selftest` reports:

```text
status          PASS
fidelity groups 22
exact checks    133
failures        0
```

The groups cover the twenty pinned mathematical surfaces, thirteen explicit
semantic regression controls, and three SHA-256 standard vectors. The
semantic controls refuse or distinguish:

1. reverse-stage source writes;
2. conflicting `B2` endpoint invariants;
3. `Ft` applied before the post-endpoint type;
4. erasure admitted into the stable grammar;
5. representative mass;
6. reader-defined physical identity;
7. ordered-fold replacement of n-ary fusion;
8. a dropped cross-pair seed;
9. `q0` smuggled into the native restart state;
10. primitive `C` confused with queried `B2`;
11. one-alternative contrast alignment;
12. fixed-context mediation promoted under fair epsilon; and
13. a nontrivial post-closed-stage hom-set.

Rust verification:

```text
cargo fmt --check                         PASS
cargo clippy --all-targets -- -D warnings PASS
cargo test                               PASS
unit tests                               4/4
compile-fail typestate tests             1/1
release build                            PASS
```

The paired writer test publishes two prepared temporary files, preserves both
bytes on success, injects a collision on the second link, removes the newly
published first path, and preserves the foreign colliding path. Relative,
unknown, missing, and mixed CLI arguments refuse with exit code 2. Neither
`--generate-fresh` nor a fresh interface exists.

Release selftest runtime on the construction machine is approximately 0.01 s.
Canonical stdout SHA-256 is
`c8cc4e9f4749e62f2b7af4b2c8f99d651eeaf124932c7c93f4d533e77b38a80d`.
The verify-only stdout SHA-256 is
`b0ecbc341dded5fd2fc68f024222014687b0a8eef88ace5f0347c6aedec69c5c`.

The selftest stdout is byte-identical in:

- the repository crate directory;
- alien CWD `/private/tmp`; and
- an exact source-only directory with no `.git` and no preexisting `target/`.

## 5. Construction-only defects repaired

Four strictly software-level defects were encountered:

1. Rust ownership required cloning a packet when extracting a marginal from an
   owned enum value.
2. The first stabilizer iterator encoded a filtered-out element as `None` for
   the entire collection; a direct loop now preserves only joint fixers.
3. The initial bond test helper accidentally assigned the same scalar color to
   its nominally unequal packets; the helper now derives color from its bit.
4. Clippy requested an explicit fixed-word SHA block loop instead of a generic
   constant-size chunk iterator.

Two weak tests were strengthened before freeze: the fair-epsilon response is
now generated from the two actual epsilon contexts rather than an equivalent
but provenance-wrong mixture, and eraser exclusion now compares its exact
source and target sorts with the stable endomorphism sort. Paired-publication
rollback and all thirteen semantic counterfeits were then made explicit.

None of these changes altered a mathematical boundary, probability, seed law,
generator, hom-set, action, mark, reader, contrast, tensor, fusion, future,
eraser, division, response, parameter, or outcome.

## 6. Freeze disposition

The Rust source is green and ready for its source-freeze commit. The official
Stage-C result and receipt paths are absent, and `--run` has never been invoked.
Until Stage C, the executable status is `RUST-SOURCE-GREEN-UNOFFICIAL`.

The source confirms fidelity to the already accepted mathematical product. It
does not select the law or actualize a branch. Operational chronology, causal
order, dimension, topology, extensive measure, duration, clock, metric,
connection, curvature, gravity, continuum physics, QFT, particles, and
phenomenology remain unconstructed.
