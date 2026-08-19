# RFB hostile review — Seat P: locality, causality, physical content, and forward theory

Status: **FROZEN INDEPENDENT HOSTILE REPORT**.

I read the frozen RFB protocol completely and reviewed only the immutable
candidate, its named antecedents, primary literature, and independent exact
scratch calculations under `/private/tmp`. I did not read, list, request,
summarize, or infer any sibling RFB report. I made no candidate or git mutation.

## 1. Grade and recommended primary

**Grade: ACCEPT-WITH-FIXES.**

The fixed-factor quantum-information result is correct. The exact Bell state has
Bob marginal `I/2`; Alice's Z and X measurements remotely prepare distinct HJW
ensembles with that same average; and every fixed, affine, trace-preserving local
channel on Alice leaves Bob's unconditioned marginal invariant. I also applied
the delivered classical instrument and coherent dilation, a natural exact
hybrid-tag realization, and natural write-only/active-feedback unitaries to the
HJW preparations. After Alice's outcomes are summed, every such fixed Bob map
gives the same complete Bob output for Z and X. Conditional steering remains,
as it should.

The primary is too broad. The advertised `14 x 13` matrix contains `182` cells,
but `173` are populated by the default
`UNTOUCHED-BY-REGISTERED-SURFACE`, only `9` contain nondefault row-level
content, and the impose/drop aggregate ranges over only `11` named compound
assays. An exact changed-object mutant can promote an unassayed cell to a false
`FORCED` statement while all `49` gates and the frozen primary still pass. The
paper renders only the eleven-row joint table, not the full matrix. This is a
mapping of local registered forcing cells, not of the forcing boundary.

My recommended primary is therefore:

```text
RFB-LOCAL-FORCING-CELLS-MAPPED
```

This wording is a review narrowing, not a newly licensed frozen outcome. A
scientific repair requires a new candidate generation and full replay.

## 2. Frozen target and source reconciliation

The immutable target hashes independently reproduce:

| object | SHA-256 |
|---|---|
| `v16/note-rfb-pin.md` | `acc2cca5b46b4512a3b1298ec45623a621539da83691bebb6c4ab2dc8a431bc2` |
| `v16/code/rfb_core.py` | `7d0a787d108ac16229dc6819a81f74f7b80203eaefa71d28f30f1f31b27e9ada` |
| `v16/code/rfb_fixture.json` | `f3557b3400584d01984c6a4f38d40744c9e2cf2f0e36c7c4aa225b045e5bd362` |
| `v16/code/rfb_score.py` | `4a2c9590e1d64f9e40c6e5828d132b9b746aa8938e18aee95a484caabc8c87ff` |
| `v16/code/rfb_output.txt` | `a7ebef77a507bac62c64fa594ed539902ed7a333fe5c77a677a4aad1f124aace` |
| `v16/code/rfb_receipt.json` | `e8cefe5b28d343fe76fdad89283a02c8c2f477243bbc7455b83324a0fe7a4659` |
| `v16/paper-10-record-feedback-boundary.md` | `360b4e861add1a5eac0b09296fe0e52438787697aa22097801f0e43cc2c2a5f4` |
| `v16/note-rfb-candidate-verification.md` | `9dc606172278d7595531603e4a3bc272d227cf665f297fc4ed16ea1ae3178531` |

Removing `content_sha256` from the canonical receipt and hashing the remaining
payload gives
`5d63d8df0d8e1b94b9374c8bea452ab95985ba440432d931cbf16722438321b2`,
exactly its embedded seal. Its transcript and paper seals equal the immutable
artifact hashes above.

## 3. Independent Bell and HJW reconstruction

I used exact rational arithmetic and no RFB/QSF imports. The joint state was

```text
rho_AB = 1/2 [[1,0,0,1],
              [0,0,0,0],
              [0,0,0,0],
              [1,0,0,1]].
```

It is trace one and

```text
Tr_A rho_AB = I_B/2.
```

Alice's two complete projective instruments give Bob the conditional ensembles

```text
Z: {1/2, |0><0|}, {1/2, |1><1|}
X: {1/2, |+><+|}, {1/2, |-><-|}.
```

I derived these rows by applying the Alice projectors to `rho_AB` and taking the
partial trace; they were not entered as answers. Both averages are exactly
`I/2`, while the sets of conditional states differ. Thus:

- equality of the unconditioned marginal is established;
- steering is also established;
- equality of the marginal does not mean equality conditional on Alice's
  outcome; and
- a conditional difference is not a communication channel unless Alice's
  outcome is supplied or the unconditioned Bob law moves.

For any trace-preserving Alice channel with Kraus operators `A_i`,

```text
Tr_A sum_i (A_i tensor I) rho_AB (A_i^dagger tensor I)
  = Tr_A rho_AB.
```

This is the general fixed-factor theorem. The scorer's four channels are
examples, not the reason it is true. A trace amplifier violates the premise and
moves the unnormalized marginal, exactly as the drop control reports.

## 4. The feedback-family test the candidate does not itself execute

The locality arm does not compose the record-mode objects with HJW preparations.
It applies generic Alice-side identity, dephasing, and bit-flip channels to the
Bell state. Names such as `classical-dephase` and `hybrid-dephase` do not weld
those channels to the classical instrument, coherent dilation, partial tag, or
reader/writer constructions elsewhere in the scorer. The HJW gate itself checks
only that the two ensemble averages agree before any feedback law is applied.

The missing computation can nevertheless be done where the maps are typed:

1. The delivered classical ports

   ```text
   K0 = [[1,0],[0,0]],  K1 = [[0,1],[0,0]]
   ```

   obey `K0^dagger K0 + K1^dagger K1 = I`. Retaining the orthogonal port flag,
   the complete matter-plus-flag output is byte-identical for the Z and X HJW
   ensembles.
2. The delivered coherent reset dilation has reached isometry
   `|0> -> |0>|0>`, `|1> -> |0>|1>`. Its complete retained output is likewise
   identical for Z and X.
3. A natural exact partial-tag isometry

   ```text
   |0> -> |0>|0>,
   |1> -> |1>(w|0> + c|1>),  w^2+c^2=1
   ```

   realizes the three visibility rows `(w,c)=(0,1),(3/5,4/5),(1,0)` and gives
   plus probabilities `1/2,4/5,1`. Its complete output is identical for the two
   HJW ensembles at every `w` because it is one fixed linear isometry.
4. Initializing a local record and applying the delivered matter-controls-record
   permutation, with or without the natural record-controls-matter reader, also
   gives identical complete Bob outputs for Z and X.

These exact controls support fixed-factor safety for the affine realizations.
They do **not** create the one common long-time feedback process that the
candidate does not define. In particular, the hybrid visibility row is a
one-input tag construction, and the reader/writer row is a neighboring unitary
construction. A relational attachment, common event law, multi-step retained
record, and changing subsystem algebra remain absent.

The detector is not blind. As a deliberately decomposition-sensitive control,
assign a Bob record-bit probability to a pure input by

```text
p(record=1 | rho) = 4 rho_00 rho_11.
```

The Z ensemble gives `0`, the X ensemble gives `1`, despite their common
density operator: exact record TV `1`. This is not a lawful RFB affine family;
it verifies the mandatory kill condition and shows exactly what a future ontic
feedback completion must exclude.

The fixed-factor disposition is therefore:

```text
PHRASABLE-NO-SIGNALLING-PROVED
[FIXED 2 x 2 FACTORIZATION; AFFINE LOCAL MAPS; UNCONDITIONED BOB LAW]
```

The relational/dynamic-factorization disposition is separately:

```text
UNPHRASABLE-BECAUSE-COMPOSITE-DYNAMICS-UNBUILT.
```

It is incompleteness, not safety.

## 5. Locality and causal scope

The fixture contains no distance, graph support, contact relation, light cone,
or evolving factorization. “Alice” and “Bob” are declared tensor factors of a
two-qubit matrix. Consequently the result establishes algebraic marginal
invariance, not spacelike separation or Lorentz causality.

A changing-factorization theorem would have to define at least:

- the complete relational composite state;
- which evolving subalgebra is Bob after birth, merge, or split;
- a graph-derived separation/contact condition;
- the allowed local instruments on those changing algebras;
- Alice-outcome-unconditioned Bob records, carrier availability, event rates,
  and local geometry at every pre-contact window; and
- a positive theorem over every allowed preparation and instrument, not only
  one Bell/HJW fixture.

An exact scope-metadata mutant changed the fixture text to “changing
factorization after graph birth, merge, or split,” updated only its self-hash,
and passed all `49` gates while executing the same `2 x 2` partial trace. This
does not contradict the paper, which keeps the wall. It proves that the scorer
does not type dynamic factorization and that changing the prose field cannot
promote the theorem.

Actualization is also external. An operational record protocol requires actual
Alice and Bob outcomes. Refusing actualization makes the model incomplete; it
does not turn a marginal calculation into an explanation of outcomes.

## 6. Chirality: exact formula, missing physical calibration

The exact chirality table is reproduced:

```text
q=2: 0, 1
q=3: 1/4, 1, 1/4
q=4: 1/2, 1, 1/2, 0.
```

But the scorer obtains it by evaluating

```text
p_r(k) = (1 + Re exp(2 pi i (k-r)/q))/2
```

at the hard-coded reference `r=1`. It does not construct the reference arm,
complex seed, reader action, common boundary, or calibrated port that would
connect this number to the feedback dynamics.

The distinction is relational to that oriented reference:

```text
p_r(k) = p_{-r}(-k).
```

If the reference is averaged because no orientation is physically available,
the probability is exactly `1/2` for every charge at `q=2,3,4`, and opposite
charges are indistinguishable. Changing the hard-coded reference from `r=1` to
`r=0` makes the frozen chirality gate refuse at its named surface.

Therefore `RFB-G-R-CHIRALITY` survives only as an exact formula relative to a
declared biased phase reference. It is an operational calibration only after a
physical reference preparation and readout are built and their joint gauge
covariance is demonstrated. As delivered, it is a typed literal unconnected to
the feedback process.

## 7. Why the forcing-boundary primary must narrow

The exact matrix audit is:

| quantity | count |
|---|---:|
| assumption rows | `14` |
| freedom columns | `13` |
| full cells | `182` |
| default `UNTOUCHED` cells | `173` |
| nondefault cells | `9` |
| named joint impose/drop assays | `11` |

`all_impose_drop_measured` quantifies over the eleven `joint_findings`, not over
the 182 matrix cells. Several compound findings correspond to row-level entries,
and the full matrix is never rendered into the paper. A default says “this unit
did not assay the cell”; it is not evidence that the assumptions fail to
constrain that freedom.

The decisive changed-object test altered only

```text
A-DISJOINT-LOCALITY x actualization
```

from default `UNTOUCHED` to the scientifically false
`FORCED-BY-A-DISJOINT-LOCALITY`. All `49` gates passed and the primary remained
`RFB-FORCING-BOUNDARY-MAPPED`. The changed receipt is internally sealed. Thus
the result machinery does not bind the advertised full boundary to the
measurements.

What survives is useful and exact: the eleven registered local assays and their
named return-on-drop controls. What dies is the global verb “mapped.”

## 8. Outcome reachability and comparator independence

`RFB-G-OUTCOME-REACHABILITY` evaluates `derive_primary` on four manually chosen
Boolean triples. It constructs no process that is blocked, inconsistent, or
unfinished. It proves that four strings are reachable in a software truth
table, not that the scientific outcomes are physically feasible.

`RFB-G-PRIMARY` is not an independent scientific reconstruction. Both functions
consume the same three flags; one uses ordered conditionals and the other an
equivalent eight-row lookup table. Replacing the entire “independent” function
by the literal call

```text
return derive_primary(flags)
```

passes all `49` gates and reproduces the primary. This changed-object survivor
kills the independence claim while leaving the local measurements untouched.

These two gates should be renamed as code-path totality and implementation
agreement unless actual alternative physical fixtures and an independently
derived scientific comparator are supplied.

## 9. Mandatory-kill disposition

| mandatory kill | result |
|---|---|
| calibrated remote-setting dependence | The nonlinear record control gives exact TV `1`, so the detector is live. No delivered/natural affine fixed-factor feedback map signals. A future ontic family would be killed by one such row. |
| graph-free or memory-only replacement | The delivered implementation itself is graph-free: rational matrices, permutations, finite functions, and metadata reproduce every result. Any relational or geometric reading is killed; the paper correctly declines one. |
| physically unentered cell counted as mapped | Triggered. `173/182` cells are defaults, and an unassayed-cell promotion survives all gates. The primary is narrowed. |
| QFT/GR/particle/Hamiltonian/continuum inference | No such inference appears in the candidate result. The explicit walls survive. Any later promotion from this fixture would be a major violation. |

## 10. Primary-literature audit

The literature is used as precedent rather than evidence for RFB, which is the
correct type.

- Arrighi and Martiel's [Quantum Causal Graph Dynamics](https://arxiv.org/abs/1607.06700)
  supplies a causal/localizability framework on superposed time-varying graphs,
  but its stated structure theorem assumes a vertex-preserving unitary. The pin's
  qualification is accurate.
- Arrighi, Durbec, and Emmanuel's
  [size-varying reversible causal graph dynamics](https://arxiv.org/abs/1805.10330)
  obtains local reversible creation/destruction in three relaxed classical
  settings; it is not RFB's quantum back-reacting law.
- Arrighi, Durbec, and Wilson's
  [Quantum networks theory](https://arxiv.org/abs/2110.10587) already permits
  coherent node merge, split, and reconnection and develops logical partitions
  with consistency/comprehension. The candidate correctly refuses to claim
  quantum size-change kinematics as new.
- Arrighi, Christodoulou, and Durbec's
  [graph-superposition/covariance paper](https://arxiv.org/abs/2010.13579)
  explicitly uses node names for branch alignment and treats renamings as
  coordinate changes. This supports a naming/covariance requirement, not any RFB
  graph result.
- Behr and Sobocinski's
  [rule-algebra paper](https://arxiv.org/abs/1807.00785) proves associative DPO
  rule composition along overlaps. Hawkins, Markopoulou, and Sahlmann's
  [Quantum Causal Histories](https://arxiv.org/abs/hep-th/0302111) uses CP maps on
  a supplied causal pre-spacetime. Both are precedents; neither selects RFB's law.
- Gudder's [Hilbert representation theorem](https://arxiv.org/abs/1011.1694)
  supports the strong-positivity/representation statement, while Dowker,
  Johnston, and Surya's
  [extension analysis](https://arxiv.org/abs/1007.2725) warns that finite
  decoherence functionals need not extend to the full event sigma algebra.
- Barandes' [indivisible-stochastic formulation](https://arxiv.org/abs/2507.21192)
  supports treating indivisible stochastic laws as primary and Hilbert objects as
  secondary. It does not provide ISP's graph-generated, size-changing,
  record-stable successor.
- Process tensors are established operational machinery for memory-bearing
  multi-time processes, as in
  [Pollock et al.](https://arxiv.org/abs/1512.00589); process matrices are
  established indefinite-order machinery, as in
  [Oreshkov, Costa, and Brukner](https://arxiv.org/abs/1105.4464). RFB supplies no
  witness requiring either promotion.
- The HJW use is faithful to
  [Hughston, Jozsa, and Wootters](https://doi.org/10.1016/0375-9601(93)90880-9):
  the Z and X ensembles are distinct realizations of one density operator.

The forward statement “substantial kinematics exists; the synthesis is
unbuilt” survives this audit. Nothing here derives QFT, GR, particles, a
Hamiltonian, constants, or an empirical deviation.

## 11. Integrity, replay, and mutant audit

The immutable target path set is clean. I constructed a minimal off-tree source
tree containing only the scorer's frozen runtime/read set; it contains no
`.git`. Invoked from the alien CWD `/private/tmp`, it reproduced byte-identical
artifacts:

```text
transcript a7ebef77a507bac62c64fa594ed539902ed7a333fe5c77a677a4aad1f124aace
receipt    e8cefe5b28d343fe76fdad89283a02c8c2f477243bbc7455b83324a0fe7a4659
paper      360b4e861add1a5eac0b09296fe0e52438787697aa22097801f0e43cc2c2a5f4
```

All `39` frozen mutants were run in that true off-tree tree. Every mutant
returned code one at its declared upstream gate and produced no output, receipt,
or paper. The exact mutant-ledger payload hashes to
`a070edf529b764a0f294ab4cd99a14de2635a9199077cdd3aa8bc8e36b390701`.

Unknown argv returns code two; `--selftest` returns zero. A second clean run
refuses existing artifacts. Moving only the generated receipt aside and rerunning
also refuses because the transcript and paper survive; restoring the receipt
recovers the byte-identical set. This checks partial-artifact/no-overwrite
behavior without destructive deletion.

The three required seat-specific changed-object classes, plus one scope control,
are:

| changed object | result | identifying SHA-256 |
|---|---|---|
| unassayed matrix cell promoted to false `FORCED` | **escaped** all 49 gates; primary unchanged | scorer `c182697b2bde921c7d8d5db96b5b3154085389464ea209dc32d4dcc91367ccc5`; receipt `1d55bb6808fe46647a1613e1d51cc319293fd5d99221052bda37f6dc9581b6f6` |
| alleged independent comparator collapsed to `derive_primary` | **escaped** all 49 gates; primary unchanged | scorer `b3df1eea7e989d4774222d88b951f2868c1f64ce040c66e95a51dc771a368716`; receipt `4d0d21499fb5dd96b4029f33b973ec92525bdd0ec7fb01d6073c19362cd7187d` |
| phase reference changed from `r=1` to `r=0` | refused at `RFB-G-R-CHIRALITY`; proves reference is load-bearing | scorer `42192073cef2606b4b1ba1c15c7a2598e670b510859c505354c523b7c3dc6d49` |
| scope metadata promoted to changing factorization | **escaped** all 49 gates while retaining the same 2x2 calculation | scorer `6f4909ef15365b6405d91d26f9222a47aefa4e9a777d85bf9815353dcd23fa79`; receipt `5a0144394486f88076f9bd61e20c8b8b9d83de06009cfb9ca5864360929673a8` |

The independent physics payload—including Bell/HJW rows, feedback outputs,
nonlinear TV-1 detector, chirality quotient, and matrix counts—hashes to
`25af2beced4ea8b8a1cefbd970fd053372aa558d9860ae16eb133473bac4d65c`.

## 12. Ordered repairs

1. **NARROW the primary** to `RFB-LOCAL-FORCING-CELLS-MAPPED`. Do not use the
   global verb until every claimed cell is assay-bound or explicitly typed as
   unassayed rather than scientifically untouched.
2. **RENDER and seal the full matrix.** Gate every nondefault entry against a
   named impose/drop result; gate the default count and coordinates; add an
   unassayed-cell content mutant. The current joint table is not the matrix.
3. **RETYPE default cells.** Use `UNASSAYED-BY-THIS-UNIT` unless an actual
   assumption-drop census establishes `UNTOUCHED-BY-REGISTERED-SURFACE`.
4. **DEMOTE outcome reachability** to software-path totality until separate
   physical fixtures instantiate blocked, inconsistent, and unfinished cases.
5. **REPLACE the primary comparator** with a reconstruction from independently
   measured scientific predicates. A second encoding of the same three flags is
   not independent.
6. **WELD locality to feedback.** Apply each genuinely common classical,
   coherent, hybrid, decoherence-only, and active event map to both HJW ensembles;
   retain every local record port; sum Alice outcomes; compare every calibrated
   Bob grain. Where no common map exists, emit `UNPHRASABLE`, not `SAFE`.
7. **RENDER the general fixed-factor theorem.** Separate unconditional CPTP
   invariance from trace-nonincreasing postselection, steering conditional on
   Alice outcomes, and decomposition-sensitive nonlinear controls.
8. **TYPE the scope in code.** A locality gate must refuse changing-factorization
   language unless the relational composite, evolving Bob algebra, separation,
   and every-window theorem are actually constructed.
9. **CALIBRATE chirality physically.** Supply the oriented reference state,
   reader action, common-boundary port, and joint gauge transformation. Otherwise
   demote chirality to a formula at a declared reference.
10. **ADD the four Seat-P mutants** above to the repaired surface, including the
    TV-1 decomposition-sensitive detector as the causal kill control.
11. **KEEP the dynamic-factorization branch explicitly incomplete.** Fixed-factor
    marginal invariance cannot answer “who is Bob?” after birth, merge, or split.
12. **PRESERVE every forward scope wall and literature type.** Network,
    histories, process-tensor, process-matrix, and Barandes machinery are
    precedents, not RFB results.

## 13. Protocol-final schema

grade:
`ACCEPT-WITH-FIXES`

recommended primary:
`RFB-LOCAL-FORCING-CELLS-MAPPED`

exact claims surviving:
Bell/HJW construction; fixed-factor unconditioned marginal invariance for
affine CPTP local maps; exact no-signal outputs for the delivered/natural
fixed-factor feedback realizations; conditional steering; the reference-relative
chirality table; eleven local impose/drop assays; all scope walls; artifact and
mutant integrity.

claims killed or narrowed:
`RFB-FORCING-BOUNDARY-MAPPED`; physical outcome reachability; scientific
independence of the primary comparator; chirality as an already calibrated
feedback observable; any safety claim for a relational/changing factorization;
any geometric, QFT, GR, particle, Hamiltonian, continuum, or empirical reading.

new counterexample hashes:
independent physics `25af2beced4ea8b8a1cefbd970fd053372aa558d9860ae16eb133473bac4d65c`;
all-mutant ledger `a070edf529b764a0f294ab4cd99a14de2635a9199077cdd3aa8bc8e36b390701`;
unassayed-cell receipt `1d55bb6808fe46647a1613e1d51cc319293fd5d99221052bda37f6dc9581b6f6`;
comparator-collapse receipt `4d0d21499fb5dd96b4029f33b973ec92525bdd0ec7fb01d6073c19362cd7187d`;
dynamic-scope receipt `5a0144394486f88076f9bd61e20c8b8b9d83de06009cfb9ca5864360929673a8`;
chirality-reference source `42192073cef2606b4b1ba1c15c7a2598e670b510859c505354c523b7c3dc6d49`;
normalized report SHA-256
`cbdd067689246cc2be99d0cc5e231e6ab612b876572c065cded28eb1dc35a6a4`;
ordinary final-file SHA-256 is reported out of band to the coordinator because
embedding it would change the bytes being digested. The normalized digest is
computed with the preceding 64-character report field replaced by zeroes.

scope walls:
fixed tensor factor only; no spacetime separation; no relational composite; no
dynamic subsystem algebra; no graph/geometry; no catalogue/division/
actualization derivation; no indefinite-order witness; no QFT/GR/continuum;
no particles/species; no Hamiltonian/energy/constants; no empirical prediction.

ordered repairs:
1 primary narrowing; 2 full-matrix sealing; 3 `UNASSAYED` retyping; 4 physical
outcome fixtures; 5 independent comparator; 6 feedback/HJW weld; 7 generic
fixed-factor theorem; 8 code-enforced causal scope; 9 physical chirality
reference; 10 Seat-P mutants; 11 dynamic-factorization incompleteness; 12 scope
and literature preservation.
