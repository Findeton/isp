# CEL Paper 7 hostile review — locality, dynamics, Barandes ontology, and physical scope

Seat: **P — locality, dynamics, Barandes ontology, and physical scope**  
Target: CEL Paper 7 candidate commit `f3c3ef99f1506f01208a670198a91abe27c952d5`  
Independence: I did not read, request, list, summarize, or infer either other CEL report. All scratch work was confined to `/private/tmp/cel-physics-review.HIxRvU`.

## 1. Immutable-target and hash audit

The immutable chain is internally consistent and chronological.

| object | protocol binding / commit | reviewer value | status |
|---|---:|---:|---|
| pin | `83762533fa6dad63acbeb3c13b2db9a63b6533b0ce113a61012d959552fa542d` | same | PASS |
| generic core | `f08b880095e71ac79082d2672ec849dc9ffd1ab66c702a85f2b24165a02aedac` | same | PASS |
| core-freeze note | `01f584c0117a79f61d9dcb2dc352d7ecf291f4176f583882d72c5a13bfd6966c` | same | PASS |
| physical fixture | `8a18a70f1e1b7781806d800c54afd5dcbd10dbac1307db4420bafcb4b57854f2` | same | PASS |
| scorer | `27ee69af161382dfda3de81e1ea4d0edf4d6b4afb8d11d5f30ec7d3e075749c8` | same | PASS |
| fixture-freeze note | `b5bf12b6d8032601ed59a6d8d32d46ea7f4e809c842c3efa7020f3546d4748e7` | same | PASS |
| transcript | `098d6113fb9f3ce0dbf43a28aeec213a5b06235c55556389989e93e1387028f6` | same | PASS |
| receipt | `a2fe34ccbbc8a1049824fd72020da5806e399f7a50a45e9bdf832e7e45a8eeda` | same | PASS |
| Paper 7 | `acf2dafb165d5ceb82bf4bc532b194f760095ce355b0b5ee7c5996df13878f90` | same | PASS |
| candidate verification | `abbc2eba6042a519769986c480931e10accccbea58454df1750453d3a66c7106` | same | PASS |
| candidate commit | `f3c3ef99f1506f01208a670198a91abe27c952d5` | same Git object | PASS |
| verification commit | `15299d1ee6ffca4ede9b9bd0ae86dfe2dee386c1` | same Git object | PASS |

The parent chain is pin `671a257b` → core freeze `3a992852` → fixture/scorer freeze `c737bdb8` → candidate `f3c3ef99` → verification `15299d1e`, with monotonically later commit timestamps. Hashing the candidate paths directly from the candidate Git tree reproduces all three candidate artifact hashes. Hashing the verification note from the verification Git tree reproduces its binding.

A fresh alien-CWD replay reproduced transcript, receipt, and paper byte for byte. A separate Git archive containing only the frozen scorer, core, fixture, and eleven runtime anchors ran without a `.git` directory and reproduced the same three hashes. The receipt contains eight valid payload seals, 44 distinct passing gates, 13 claims, 11 qualifiers, and 15 scope walls. All 41 registered mutants returned exit `1` and wrote no candidate artifact; `--selftest` did likewise, an unknown option returned exit `2`, and an existing target was refused before evaluation.

This establishes artifact integrity. It does not establish the physical interpretation of a gate.

## 2. Independent method and tools

I read `RUNBOOK.md`, the complete frozen CEL hostile protocol, the pin and both freeze notes, the candidate-verification note, Paper 7, the fixture, transcript, receipt, generic core, scorer, the Paper 4 bundle doctrine, and the relevant record definition in v12 Paper 1. I rebuilt the load-bearing finite physics in a standalone exact script, `/private/tmp/cel-physics-review.HIxRvU/independent.py`. That script imports neither `cel_core.py` nor `cel_score.py`; it uses integer and rational arithmetic plus an independent Gaussian-rational type.

The independent rebuild covered the two CNOT order maps, kernels, screens, exchange action, operational-null control, reset channel in both pictures, one- and two-copy record paths, branch retention/coarse-graining, both JCV coefficient families, Stinespring stacks, flag vectors, calibrated ports, an attachment-erasure control, a fixed-factor Bell control, and the exact `7/5` resource witnesses.

Primary literature was checked to type the claims rather than enlarge them:

- Barandes treats the stochastic process in a configuration space while Hilbert-space objects and dilations are representations: Jacob A. Barandes, *Quantum Systems as Indivisible Stochastic Processes*, [arXiv:2507.21192](https://arxiv.org/abs/2507.21192).
- The isometric dilation is imported operator theory, not a CEL derivation of relational ontology: W. F. Stinespring, *Positive Functions on C*-Algebras*, [Proc. AMS 6 (1955) 211–216](https://doi.org/10.1090/S0002-9939-1955-0069403-4). The corresponding measurement-dilation precedent is M. Neumark, *Spectral Functions of a Symmetric Operator*, [Izv. Akad. Nauk SSSR 4 (1940) 277–318](https://www.mathnet.ru/eng/im3893).
- Kraus decompositions describe operations and admit nonunique retained outcomes: K. Kraus, *General State Changes in Quantum Theory*, [Annals of Physics 64 (1971) 311–335](https://doi.org/10.1016/0003-4916(71)90108-4). The same-state/many-ensemble issue and remote preparation are sharpened by L. P. Hughston, R. Jozsa, and W. K. Wootters, [Physics Letters A 183 (1993) 14–18](https://doi.org/10.1016/0375-9601(93)90880-9).
- “Invariant,” “preserved,” “correctable,” and “noiseless” are distinct operational notions: R. Blume-Kohout, H. K. Ng, D. Poulin, and L. Viola, *Information-Preserving Structures*, [arXiv:1006.1358](https://arxiv.org/abs/1006.1358). Exact quantum correction also requires reference-safe coherent recovery, not only separation of two classical sectors: E. Knill and R. Laflamme, [Phys. Rev. A 55 (1997) 900](https://doi.org/10.1103/PhysRevA.55.900).
- The four-square ingredient is classical: J.-L. Lagrange, *Démonstration d’un Théorème d’Arithmétique* (1770), [collected text](https://fr.wikisource.org/wiki/M%C3%A9moires_extraits_des_recueils_de_l%E2%80%99Acad%C3%A9mie_royale_de_Berlin/D%C3%A9monstration_d%E2%80%99un_Th%C3%A9or%C3%A8me_d%E2%80%99Arithm%C3%A9tique). Matrix sum-of-squares precedent includes D. Ž. Djoković, [Linear Algebra and its Applications 14 (1976) 37–40](https://doi.org/10.1016/0024-3795(76)90061-6).
- Ordinary coupling universality comes with substantial Lorentz/gauge/S-matrix structure, not repeated type labels alone; a sharp primary example is S. Weinberg, [Phys. Rev. 135 (1964) B1049](https://doi.org/10.1103/PhysRev.135.B1049). The relevant QED identity is J. C. Ward, [Phys. Rev. 78 (1950) 182](https://doi.org/10.1103/PhysRev.78.182).

## 3. Exact recomputation table

| quantity | candidate value | reviewer value | status |
|---|---:|---:|---|
| frozen artifact hashes | 10 bindings match | 10 match | PASS |
| candidate payload | 44/44 gates; 8 seals; 13 claims | 44 distinct PASS; 8/8 seals; 13 claims | PASS |
| mutation battery | 41/41 refuse without writes | 41/41, exit `1`, no artifact | PASS |
| true off-tree replay | byte-identical | byte-identical; no `.git` | PASS |
| CNOT order endpoints from `100` | `[7,6]` | `[7,6]` | PASS |
| biased/balanced `111` screens | `16/25`, `1/2` | `16/25`, `1/2` | PASS |
| both order kernels complete | yes | diagonal weights sum to `1`; yes on all inputs | PASS |
| exchange-fixed kernels | balanced only | balanced only | PASS |
| identical-history null control | raw unequal, channel equal | raw unequal, channel equal | PASS |
| universality dimension price | `2 -> 1` | `2 -> 1`, caused by adding the declared equation `p=q` | PASS / POSTULATE |
| reset Heisenberg action | diagonal-covariant, record lost | `P0 -> I`, `P1 -> 0`; both sectors map to `0` | PASS |
| relabeling control | recoverable, fixed-projector commutation fails | same | PASS |
| redundant record path | `111 -> 101`; final loss in enlarged grammar | `111 -> 101 -> 100`; semigroup sizes `2`, `4` | PASS |
| retained/discarded identity-flip branch | retained recoverable; coarse channel uniform | same | PASS |
| JCV kernels | both `diag(16/25,9/25)` | same | PASS |
| JCV first-port probabilities | `0 -> 49/625` | first family `(0,1)`; second `(49/625,576/625)` | PASS |
| JCV flag vectors | `(0,1)/(24/25,7/25)` and `(7/25,24/25)/(1,0)` | same | PASS |
| graph-attachment erasure control | not run | delete or change attachment: every channel, stack, kernel, and port probability is identical | **FAIL PHYSICAL WELD** |
| fixed-factor EPR control | outside scope | both retained local random-unitary branches give Bob `I/2`; only ordinary unconditional no-signalling is tested | LIMITED |
| scalar resource witness | `7/5`, no one-row `Q(i)`, two rows | `|1+3i/5|^2+|i/5|^2=7/5` | PASS |
| rank-two witness | minimum three `Q(i)` rows | determinant `7/5` blocks square two-row factor; displayed three-row Gram is exact | PASS |
| registered general constructor | ranks `[2,2,1,2]`, rows `[2,2,1,2]` | proof and registered rows agree | PASS |
| physical number-field resource | claimed only as bookkeeping | one complex row `sqrt(7/5)` exists after field extension; no physical hierarchy is established | REPRESENTATION ONLY |

## 4. Theorem/proof audit

### FATAL-1 — the “relational flag-cell weld” has no operational discriminator

The mathematical dilation is correct. The relational promotion is not.

The scorer computes every process statistic from `histories` and `coefficient_families`. The attachment `['matter','flag']`, the words `pre_cells`/`post_cells`, and the declared graph edge never enter a later transport or probe. `CEL-D3` checks membership and list lengths. `CEL-D4` checks matrix support and a basis permutation. `CEL-D5` then measures a port probability entirely from the matrices. Changing the attachment to a self-loop, deleting it, or deleting the graph reading leaves the full numerical signature unchanged.

This is exactly the distinction Paper 4 made: support across configurations is not spatial adjacency within a configuration. The anonymous-ancilla negative is not a physical negative control; it is the same mathematical kind of object denied two metadata booleans. The four-gate discriminator is absent. Therefore the qualifier `PORT-FIBER-RETYPED-AS-CREATION-COUPLING-DATA`, the qualifier `FLAG-DILATION-WELDED-BUT-ACTUALIZATION-UNBUILT`, and the primary phrase “creation-event layer constructed” are not earned as physical statements.

The strongest registered replacement is already available: `CEL-MATHEMATICAL-LADDER-CONSTRUCTED-BUT-RELATIONAL-FLAG-WELD-UNBUILT`.

### MAJOR-2 — “one creation-event layer” is an interface over three fixtures, not one successor dynamics

The recurrence arm uses fixed three-qubit CNOT circuits. The permanence arm uses separate classical bit grammars. The dilation arm uses `I,Z` histories and a declared flag catalogue. No single packet executes all three, and no map

```text
(relations, geometry, process state) ->
(new relations, new geometry, new process state)
```

selects a rewrite, kernel, coupling, or continuation grammar in one indivisible step. The common vocabulary is useful bookkeeping, but physical unity requires a common law and a cross-arm calibration. CEL supplies neither.

### MAJOR-3 — recurrence propagation is correct; type universality remains the desired law

The nonselection counterexample is valid and valuable: `16/25` and `1/2` are both lawful on the same transports and move a calibrated screen. Spectator naturality, exchange covariance, and shared-token restriction propagate equality only after their axioms or joint law are supplied. The token-disjoint equality is exactly the added equation that cuts dimension `2 -> 1`.

The paper is mostly honest about this. Its analogy to “the same coupling in both laboratories” needs one further boundary: ordinary QFT has a single field/operator algebra over spacetime, Poincaré or generally covariant locality, internal gauge representation, Ward identities, and extensive cross-context calibration. CEL has only repeated event-type labels in an unselected catalogue. Different type dictionaries can therefore pass the finite surface and change future probabilities.

### MAJOR-4 — permanence is a finite classical, grammar-relative recoverability certificate

The reset counterexample correctly kills algebra covariance as a general permanence criterion. The restricted/enlarged semigroup results also check exactly. But the construction certifies two classical sectors under a closed, declared finite grammar. It does not certify coherent quantum information against a reference system, a complete future catalogue, or an unknown law. The enlarged grammar's `mathematical_all=True` survives only because the source bit remains globally distinct while the licensed flag readouts lose the record.

Thus CEL constructs record capacity relative to a grammar. Without catalogue closure and actualization, it does not construct an objective occurred record. This is consistent with v12's definition—mutually exclusive correlated sectors available under declared future dynamics—but it must not be promoted beyond that declared future.

### MAJOR-5 — the EPR/no-signalling debt is untouched

The independent Bell check gives the expected narrow result: applying retained `I` or `X` branches on Alice's half of a Bell pair changes the joint state but leaves Bob's fixed-factor marginal exactly `I/2`; discarding the branch also leaves `I/2`. That is ordinary no-signalling for a local trace-preserving instrument.

It is not the missing test. CEL has no outcome-conditioned remote preparation, no entangled state shared across a changing relational carrier, no definition of Bob's algebra after Alice's rewrite, and no proof covering decomposition-sensitive dynamics. HJW remote ensemble preparation and Gisin's signalling mechanism remain directly relevant if the earlier decomposition-sensitive update is ever composed with this layer; see N. Gisin, [Physics Letters A 143 (1990) 1–2](https://doi.org/10.1016/0375-9601(90)90786-N). The classical flag control proves neither steering-unphrasability nor no-signalling for the desired extension.

### MAJOR-6 — the `2r` theorem is valid mathematics; the resource is not physical

For a PSD Hermitian matrix over `Q(i)`, zero-pivot-safe Hermitian `LDL^dagger` has rational nonnegative pivots; each nonzero pivot is a sum of at most four rational squares and hence two Gaussian norms. The number of nonzero pivots is the rank, so the `2r` row bound follows. The `7/5` and rank-two minimality witnesses are correct at that field.

But the cost disappears after extending scalars: over the complex numbers `7/5=|sqrt(7/5)|^2` is one row. Since CEL explicitly refuses to make `Q(i)` ontic, “minimum flag resources” is not a physical observable. What survives is exact-verifier representation cost. A physical resource hierarchy would require a selected amplitude field, allowed-gate grammar, preparation cost, and calibrated operational comparison.

### Attribution audit

The Stinespring isometry, Kraus nonuniqueness, and the general distinction among invariant/preserved/correctable structures are imported results. CEL's genuine contributions at this scope are the exact fixture joins, the finite recurrence counterexample and dimension price, the declared-grammar recoverability controls, and the explicit elementary `Q(i)` `2r` construction. Naimark/Stinespring dilation alone never ontologizes the ancillary space. The paper currently has no literature section, so this attribution boundary is invisible to a new reader.

## 5. Seat-specific ontology, representation, and locality audit

| proposed object | strongest defensible reading after review | status |
|---|---|---|
| complete configuration | possible ontic state label in a Barandes-style process | candidate; catalogue unselected |
| relational rewrite | typed metadata for a possible successor | not selected and not operational in CEL |
| history transports `V_h` | Hilbert-space representation of candidate histories | representation / law coordinate |
| positive kernel `M` | unconditioned process-law coordinate | physically consequential but unselected |
| port factor `C` | calibrated instrument/unravelling data | representation unless a retained physical record is supplied |
| Stinespring flag | auxiliary dilation factor | not yet a relational cell |
| durable record | distinction recoverable under every word of one declared finite grammar | conditional capacity, not an actualized fact |
| `Q(i)` | exact arithmetic convention | representation, not ontology |
| Hamiltonian | absent; at most a representation of a selected differentiable law | unconstructed |
| spacetime/gravity | no causal, metric, curvature, or geometry-fed observable | unconstructed |

Barandes' ontology is compatible with treating Hilbert space, Kraus operators, and Hamiltonians as secondary representations of an indivisible stochastic law. It does not by itself license calling an ancilla a newly real spatial cell. The ISP extension wants the complete configuration to include a locally changing relation graph. Paper 4 proposed a fixed meta-catalogue of possible graphs with changing realized graph blocks. CEL remains on the fixed-representation side: a declared two-to-four dilation is annotated as creating `flag`, but no selected law chooses that rewrite and no output-graph computation affects a later probe.

The actors `A,B,C` in the recurrence fixture are tensor-factor names, not localized actors in a derived relational geometry. CNOT overlap is algebraic support overlap, not causal proximity. There is no propagation cone, neighbor algebra, metric, energy-momentum response, or calibrated backreaction. Consequently this paper contributes no gravity result and no evidence that the local carrier back-reacts.

The strongest nontechnical ontology is therefore modest: the theory may contain actual complete relational configurations linked by an indivisible stochastic successor law, with records as persistent distinctions. CEL organizes the coordinates such a law must carry and proves several consistency lemmas. It does not supply the successor law, the catalogue, the probabilities, the coupling values, the closed continuation grammar, or the occurrence rule.

## 6. Counterexamples and unrun controls

1. **Graph-erasure control (exact, killing for the physical weld).** Keep both coefficient families and all matrices fixed; delete `rewrite.attachment`, replace it by `flag—flag`, or erase graph metadata entirely. The kernel, complete channel, stacks, supports, and port probabilities remain byte-identical. Only the metadata classifier changes.
2. **Alternative universality dictionaries (already witnessed, not exhausted).** Token-disjoint contexts carrying `16/25` and `1/2` both satisfy completeness and locality. Declaring their labels to denote one type imposes equality; a different catalogue dictionary does not. No held-out physical context selects the dictionary.
3. **EPR fixed-factor control (exact but insufficient).** Both retained random-unitary branches on Alice give Bob marginal `I/2`. This checks ordinary local CPTP no-signalling only. A remote-steering instrument, decomposition-sensitive update, and changing Bob algebra remain unrun.
4. **Field-extension control.** `7/5` needs two rows over `Q(i)` but one over `C`. The registered hierarchy is not invariant under an admitted representation enlargement.
5. **Catalogue-enlargement control.** The paper itself shows a new licensed writer erases the last flag copy. No closure principle prevents further generators, so “permanent” cannot be absolute.
6. **Joint-layer control absent.** No fixture contains a relational rewrite whose own output geometry determines the next kernel, coupling, and graph-dependent probe. Therefore the three arms have not been shown to be one physical layer.
7. **Process-arity and field control absent.** No arbitrary concurrent family, Fock-like carrier, statistics sector, vacuum, or interaction density is constructed. The three CNOT actors do not address the two-to-`n` problem.
8. **Gravity control absent.** No same process is run with and without a relational change while holding non-geometric controls fixed, and no invariant later probe registers a geometry-mediated difference.

## 7. Consequence and scope reclassification

Secure at finite exact scope:

- completeness/locality do not select a kernel across token-disjoint contexts;
- naturality, a licensed symmetry, and restriction of a supplied joint law propagate equality at their respective rungs;
- raw kernels are quotiented only after the complete admitted operational family is fixed;
- diagonal-algebra covariance is weaker than classical record recovery;
- finite declared grammars admit exact all-word recoverability checks and redundancy controls;
- the two JCV instrument families share one unconditioned channel but differ under a retained calibrated port;
- the `Q(i)` Gram construction and its registered minimal-row witnesses are mathematically correct.

Not secured:

- a physically relational created flag;
- one unified creation-event dynamics;
- selected event types, rewrite, kernel, coupling, or grammar;
- objective permanence beyond a closed declared catalogue;
- actualization;
- EPR steering compatibility or changing-factor no-signalling;
- backreaction, gravity, Lorentz invariance, continuum spacetime, QFT, particles/species/statistics, Hamiltonian reconstruction, constants, or deviations.

The decisive successor should be one held-out two-region joint-successor arena. A local event must be selected from the pre-state, create or alter a relational edge, transport the process state, and make a later probe computed from the output graph change. Erasing only the graph must erase that change. The same construction must define Alice and Bob algebras before and after the rewrite and prove all-input unconditional no-signalling while explicitly testing outcome-conditioned steering. Finally, the same event type should recur at symmetry-related sites and predict a held-out fourth context with one coupling; this would begin to select, rather than merely name, interaction universality.

## 8. Grade

**REJECT** the delivered physical headline and its two relational-flag qualifiers. This is not a rejection of the exact recurrence, recoverability, dilation, or number-theory calculations. It is a rejection of promoting their common interface to a constructed physical creation-event layer when the graph can be erased without moving any observable.

Recommended registered disposition:

```text
CEL-MATHEMATICAL-LADDER-CONSTRUCTED-BUT-RELATIONAL-FLAG-WELD-UNBUILT
```

The recurrence, null-quotient, bare-covariance, finite-grammar recoverability, Gaussian-rational-bound, and unselected-dynamics qualifiers survive with the scope corrections above. `PORT-FIBER-RETYPED-AS-CREATION-COUPLING-DATA` and `FLAG-DILATION-WELDED-BUT-ACTUALIZATION-UNBUILT` do not.

## 9. Numbered repairs and kill conditions

1. **KILL the primary relational headline now.** Replace it with the registered mathematical-ladder outcome unless Repair 2 passes. Replacement sentence: “CEL constructs a common finite mathematical interface for recurrence, classical recoverability, and calibrated dilations; it does not yet construct a physically relational creation event.”
2. **REQUIRE a graph-fed discriminator.** Add a later probe derived from the output graph and an erasure/reconstruction control. Kill condition: if erasing attachment/graph metadata while keeping the process matrices fixed leaves every calibrated invariant unchanged, the object remains an ancilla, not geometry.
3. **REQUIRE one joint successor fixture.** Rewrite, process transport, kernel, port factorization, and continuation grammar must be coordinates of one event law in one arena. Three neighboring examples do not establish one layer.
4. **RETYPE the dilation.** Until Repair 2 succeeds, replace “created flag cell/coupling” by “catalogue-annotated Stinespring flag/factorization.” Attribute Stinespring, Kraus, Naimark, IPS, and exact-QEC precedents explicitly.
5. **SCOPE permanence positively.** Replacement sentence: “The registered classical flag partition is recoverable after every word of this finite declared grammar; catalogue enlargement and actualization remain open.” Kill condition: any licensed future word merging the last readable sectors defeats the certificate.
6. **ADD the EPR gate before composing with decomposition-sensitive dynamics.** Construct entanglement, remote steering, and the post-rewrite Bob algebra. Require all-input equality of Bob's unconditioned statistics across Alice settings. Kill condition: any controllable distant marginal movement rejects the dynamics.
7. **PRICE universality honestly and test its dictionary.** Derive event-type identity from a catalogue automorphism/locality relation, then use one parameter to predict a held-out context. Kill condition: two inequivalent type dictionaries passing all admitted controls while moving the held-out probe leave universality declaration-indexed.
8. **RENAME the exact-field result.** Use “Gaussian-rational representation-row cost,” not physical flag-resource cost, until the field and gate grammar are selected and operational. Include the scalar-extension control.
9. **KEEP the fundamental-law absence in the abstract headline.** No next-rewrite law, history kernel law, coupling law, catalogue law, or continuation-grammar law was found. This may not be relegated to the final scope list.
10. **MAKE the successor physics-selective.** The next unit should vary candidate local coupling/rewrite laws under graph-fed probes, symmetry recurrence, spectator composition, and EPR no-signalling, then report the exact surviving law variety or a block. Another classifier over supplied labels will not advance the dynamics.

## 10. Report SHA-256

Normalized report SHA-256:
`fcbbec15fc19bfb07b489cc0a5e0570f182c70214878e1ac5301f01703a8e8cb`.

The normalized digest is computed with the 64 hexadecimal characters in the preceding field replaced by 64 zeroes. The ordinary file SHA-256 after insertion is reported separately to the panel coordinator.
