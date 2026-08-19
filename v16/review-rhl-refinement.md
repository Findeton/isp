# RHL Paper 11 hostile review — Seat M (point-free mathematics, refinement, and extension)

**Seat:** M only.  
**Target candidate:** `b84225f0e5692b06708966e6e7028bb4e19a7adc`.  
**Frozen protocol commit:** `67e911dc663473d120de7347c1663028ff5f26bc`.  
**Mutual-blindness statement:** I did not read, list, request, or infer either sibling RHL report. I did not read an external scratchpad. The two audit programs cited below are my own independent `/private/tmp` work. I modified no candidate, pin, source, scorer, receipt, verification note, ledger, or status file.

## 1. Verdict

**Grade: REJECT.**

Theorem 1 is a correct algebraic-colimit theorem, including for noninjective comparison maps, degenerate strongly positive forms, arbitrary directed index sets, and cofinal subsystems. It needs no point set, graph atom, global slice, or tick. The finite presentation controls also reproduce exactly and extend cleanly to a third presentation.

The claimed scientific primary nevertheless does not survive this seat. There are two independent reasons.

1. The candidate does not construct the causal mereology required by R1. It supplies a symmetric monoidal category whose objects are boundary types and whose arrows are fillings, then says that containment, overlap, boundary, and causal precedence are used. Those relations and their compatibility axioms are not defined. A coherent point-free completion can be written, and I give one below, but that is a repair supplied by this review rather than part of the frozen candidate.
2. More decisively for Theorem 1's interpretation, the comparison maps are prediction-carrying data. I construct two inequivalent, exactly compatible comparison systems on the same three local spaces and the same three local functionals. A marked cross term is `1` in one and `0` in the other; the dimensions of the intersections of the marked presentation images are respectively `2` and `1`. Descent therefore removes a choice of representative only **after** a comparison doctrine has been declared. It does not select that doctrine.

The strict highest surviving registered primary is therefore:

```text
RHL-BLOCKED-AT-POINT-FREE-REFERENT
```

If an adjudicator elects to count the paper's primitive phrase “bounded relational filling” as a completed R1 referent despite the missing mereological axioms, the strongest conditional result is still only:

```text
RHL-BLOCKED-AT-REFINEMENT-CONSISTENCY
```

The delivered primary `RHL-REGIONAL-QUANTUM-LAW-CONSTRUCTED-BUT-GEOMETRY-UNENTERED` is not supported at this seat. The no-point/no-tick idea remains mathematically viable; the objection is missing and unselected structure, not a reappearance of hidden spacetime points.

## 2. Immutable target and chronology audit

All immutable bytes match the protocol. The current branch had moved beyond the candidate commit during review, so I reviewed the frozen bytes rather than treating current `HEAD` as the target.

| immutable object | observed SHA-256 | protocol SHA-256 | result |
|---|---|---|---|
| `v16/note-rhl-pin.md` | `1d0df95fb074a688160e1a4554976268643e35835ef46b1d4918b90ee23505ee` | same | pass |
| `v16/code/rhl_core.py` | `032ede336c8cf23b168e018ecd0748e0467d1ca25cb2b44ae750ae320ae9ba8a` | same | pass |
| `v16/code/rhl_core_output.txt` | `c56c8e3dece8357d3af0e39ea2459b8a29b6fd58bc3ffc99e5ba1cabe85adafb` | same | pass |
| `v16/code/rhl_core_receipt.json` | `cfd7f243c96f29b303d7c0ef6c283b40be3994b3f6eb1945a801f0677903e060` | same | pass |
| `v16/code/rhl_regulator.py` | `d6d520a6a43451a889bfc40e2dd8df2f9afc08f032c202c3d8c206c02b4a3db9` | same | pass |
| `v16/code/rhl_regulator_output.txt` | `1f020e41989007048cf2d864f966b90184e332622230f26028c8e90225befb68` | same | pass |
| `v16/code/rhl_regulator_receipt.json` | `cea302918c101c7b2bd5973167776baa587681f4b83b8ebff041e38e0bfee944` | same | pass |
| `v16/code/rhl_score.py` | `b2f1f780d5b907b628adcd4994ac5d6eeb2d2a5abb78783d0a18c06e6582e1c2` | same | pass |
| `v16/code/rhl_output.txt` | `5ce9002848affabf91ea7ec46690465ba2d444738fb9beb68f891accd085fdaf` | same | pass |
| `v16/code/rhl_receipt.json` | `77528f648954ee30ea36bc69785d5646fc73ca2ef145127bd39e1753638eca98` | same | pass |
| `v16/paper-11-unsliced-regional-history-law.md` | `423f3cb56f6e0ccdd54ef59cfa0454509d14c005136e375307bb441133cac384` | same | pass |
| `v16/note-rhl-candidate-verification.md` | `2a7de79764bd92174ceefbc3d64d3fab8c99fb7267edcdf1ee5b458195578f2b` | same | pass |
| `v16/note-rhl-hostile-protocol.md` | `6d960c53e2fd65506da2b0970351b382e55775f13c3fbf8f613be2a3fcad6427` | frozen review protocol | pass |

## 3. Ontology, law, and representation audit

| candidate noun | proper type | Seat-M finding |
|---|---|---|
| one actual compatible web of durable relational facts | proposed ontology | Coherent as an ontological postulate; not derived by the mathematical construction. |
| bounded region | intended ontic/mereological referent | Only described as a “part” of that web. “Part,” “bounded,” and the region operations are not formally supplied. |
| containment, overlap, causal precedence | intended point-free kinematics | Named but not defined in `Reg`; their compatibility is not proved. |
| boundary type and gluing | intended interfaces/composition | Source, target, and categorical composition are named coherently at the abstract SMC level, but no boundary operation from regions to interfaces is constructed. |
| `Reg` | law-domain schema | A syntactically valid category type, not yet the candidate's promised causal mereology. |
| `D_Σ` | law data | A regional decoherence functional once supplied. Strong positivity and compatibility constrain it but do not select it. |
| `I_M`, `V_i`, `J_ji`, `D_i` | representation plus comparison doctrine | `V_i` and matrices are representations. The `J_ji` are not automatically gauge: on fed, marked propositions they determine physical comparisons and can move predictions. |
| algebraic colimit and GNS/Hilbert quotient | representation | Correctly representational. Neither is spacetime ontology. |
| finite matrices, row counts, loop indices | regulator/receipt | Never needed as physical atoms or ticks. |
| representational refinement | vertical comparison operation, if properly typed | Correct semantic intent, but the candidate has no common categorical type system that prevents it from being confused with physical evolution. |
| ontic extension | physical history morphism | Correct semantic intent; durability requires a record/recovery condition beyond a size-changing isometry. |
| actualization | postulate | Correctly left as a postulate. Nothing in Theorem 1 derives it. |

No proof step in the algebraic descent theorem requires an underlying point set or preferred temporal order. The no-point/no-tick mandatory kill therefore does **not** fire. What fails is the stronger word “constructed”: the abstract nouns have not yet been assembled into the causal-site/bordism-like structure the pin itself requires.

## 4. Point-free regional kinematics: a coherent minimum, and what is absent

A point-free construction does not require a set of spacetime points. A sufficient minimum can be given entirely algebraically.

1. Take a class `R` of bounded regions with a zero region `0` and a parthood order `A ≤ B`. Require finite joins when a bounded union is licensed. No atoms or preferred generators are assumed.
2. Define overlap without points by

   ```text
   A ⋈ B  iff  there exists C != 0 with C ≤ A and C ≤ B.
   ```

   Disjointness is the negation of this relation. Meets may be added, but are not necessary for the definition.
3. Add a strict transitive causal precedence relation `A ≺ B`, compatible with parthood: shrinking either causally ordered region preserves the order whenever the result is nonzero. Add the required union-compatibility axioms explicitly. This is causal-site-style data, not a derived metric.
4. Add an interface category `Bnd`, a boundary assignment for composable regions, and a partial gluing operation along matching interfaces. Gluing must be associative up to specified boundary-preserving isomorphism and must respect causal order.
5. Use disjoint/spacelike juxtaposition as the symmetric monoidal product. Do not identify arbitrary set union with tensor product.
6. Type representational refinements as vertical arrows over the same physical region and ontic fillings/extensions as horizontal arrows between physical boundaries. Commuting squares express calibration/pullback compatibility. A double category, fibration, or equivalent two-arrow construction is enough; one undifferentiated arrow class is not.

These axioms are mutually coherent and contain no point set, lattice spacing, graph atom, or global tick. Abstract atomless region algebras and causal sites provide consistency models. But they are not in the candidate. The frozen text defines objects, filling arrows, gluing, and disjoint juxtaposition, then merely says that containment, overlap, boundary, and causal precedence are “used.” In particular:

- containment is not a morphism or order in `Reg`;
- overlap cannot be recovered from an arbitrary symmetric monoidal category;
- causal precedence is absent from the data and axioms;
- a boundary type is an object, but no operation assigns it to a bounded part of the actual web;
- the free-SMC existence paragraph chooses abstract generators and their maps but does not show that they form the required causal mereology or that the generator catalogue is nondeclarative.

Thus the frozen object is a consistent **schema for a point-free law domain**, not a constructed point-free regional kinematics. This is a referent/typing block, not evidence for hidden points.

## 5. Theorem 1: independent proof audit

Let `I` be an arbitrary directed poset, let `J_ji : V_i -> V_j` be coherent linear maps, and let the Hermitian positive-semidefinite forms `D_i` satisfy

```text
D_j(J_ji x, J_ji y) = D_i(x,y).
```

No injectivity is needed.

### 5.1 Algebraic colimit and well-defined form

Form the usual equivalence classes of pairs `(i,x)`, where `(i,x) ~ (j,y)` if some `k ≥ i,j` satisfies `J_ki x = J_kj y`. Directedness and coherence make this an equivalence relation. For two classes, choose `k ≥ i,j` and set

```text
D([i,x],[j,y]) = D_k(J_ki x, J_kj y).
```

If `l` is another common upper bound, directedness provides `m ≥ k,l`; compatibility pulls both candidate values to the same value in `D_m`. If either representative is changed, first choose a stage witnessing that equivalence and then a common upper bound with the other representative. The same compatibility argument gives equality. Sesquilinearity and Hermiticity descend.

### 5.2 Finite-list strong positivity

For any finite set of colimit classes and coefficients, directedness supplies one stage receiving every representative. The colimit quadratic form is exactly the corresponding quadratic form for that stage, hence nonnegative. This proves strong positivity at the claimed finite-list scope; no finite matrix census is being promoted to the theorem.

### 5.3 Noninjective maps and null quotient

If `J_ji x = 0`, compatibility gives `D_i(x,x)=D_j(0,0)=0`. Positivity then implies `D_i(x,y)=0` for every `y` (equivalently, apply the Cauchy–Schwarz inequality for a positive-semidefinite Hermitian form). A comparison map may therefore kill only a `D_i`-null direction. With positive-definite `D_i`, every compatible `J_ji` is automatically injective.

The GNS quotient is consequently well typed: the null radical

```text
N = {x in colim V_i : D(x,x)=0}
```

is orthogonal to the entire colimit, and `D` descends to `V/N`. Completion, if desired, remains representational.

The exact noninjective control was

```text
J : C^2 -> C,       J(x,y)=x,
D_1 = [1],          D_0 = diag(1,0).
```

It obeys `J† D_1 J = D_0`; the killed second direction is null. Replacing `D_0` by `I_2` gives the changed-object control `J†D_1J = diag(1,0) != I_2`, so compatibility fails exactly.

### 5.4 Cofinality

If `I'` is cofinal in `I`, every `I`-representative maps to an `I'` stage, proving surjectivity of the natural colimit map. If two `I'` representatives agree at an `I` stage, cofinality supplies a later `I'` stage where they agree, proving injectivity. The functionals match by compatibility. The theorem's cofinal clause is therefore correct.

The qualifier is indispensable. In the exact chain control `0 < 1 < 2`, take `V_0=V_1=C`, `V_2=C^2`, with the earlier line embedded as the first coordinate. The full colimit has dimension `2`; the noncofinal subsystem `{0,1}` has dimension `1` and misses the later direction.

### 5.5 Exact scope of uniqueness

Uniqueness is relative to the complete declared tuple

```text
(I, {V_i}, {J_ji}, {D_i})
```

and its canonical colimit injections. It is not uniqueness relative to a list of presentations, not selection of the `J_ji`, and not selection of a physical regional law. That distinction is load-bearing below.

## 6. Independent presentation controls

I rebuilt the two delivered embeddings without importing candidate code and added a third:

```text
J_3 = [(3/5,0), (4/5,0), (0,1)]^T,
J_4 = [(1/3,0), (2/3,0), (2/3,0), (0,1)]^T,
J_5 = [(1/5,0), (2/5,0), (2/5,0), (4/5,0), (0,1)]^T.
```

Each satisfies `J_n†J_n=I_2`. With

```text
R = [[3/5,4/5],[-4/5,3/5]],
U_n = R J_n†,
```

all three exact composites satisfy `U_n J_n = R`. Their row counts `3`, `4`, and `5` are presentation data only.

The incompatible-pullback mutant halves the first column of `J_5`. It gives

```text
J_bad†J_bad = diag(1/4,1),
(R J_5†)J_bad = [[3/10,4/5],[-2/5,3/5]] != R.
```

This confirms the narrow theorem: once the embeddings are supplied, compatible presentations agree and a bad pullback is detected. It does not show that the embeddings were selected.

## 7. Decisive comparison-doctrine counterexample

Consider the directed diagram with `a ≤ c` and `b ≤ c`. Use the same local objects and local functionals in both systems:

```text
V_a = V_b = C^2,
V_c = C^3,
D_a = D_b = I_2,
D_c = I_3,
unit = e_0.
```

Let `p=e_1` be the same marked non-unit direction in the two source presentations.

**System A (identified fed directions):**

```text
J_ca e_0=e_0, J_ca p=e_1,
J_cb e_0=e_0, J_cb p=e_1.
```

**System B (separated fed directions):**

```text
J_ca e_0=e_0, J_ca p=e_1,
J_cb e_0=e_0, J_cb p=e_2.
```

Every map is a unit-preserving isometry, so every local pullback equation and every positivity requirement passes in both systems. Yet

```text
D_c(J_ca p, J_cb p) = 1  in A,
D_c(J_ca p, J_cb p) = 0  in B.
```

Accordingly the squared norm of the coherent sum `J_ca p + J_cb p` is `4` in A and `2` in B. This is not removable by a change of basis: the intersection of the two marked presentation images has dimension `2` in A and `1` in B, an invariant of the comparison diagram. Both diagrams have the same terminal colimit space `C^3`; what changes is the physically relevant placement of the marked presentations inside it.

This is the protocol's mandatory narrowing. The theorem produces a representative-independent functional **within** either system, but the two allowed systems produce different calibrated comparisons. The `J_ji` are therefore either:

- selected by a still-missing part of the law;
- declared comparison doctrine carrying physical content; or
- quotiented only after proving that all such changes lie in an operational null/gauge ideal.

The candidate establishes none of these. “Presentation independent” must be replaced by “independent of representative after a declared compatible comparison doctrine.” The counterexample does not refute algebraic descent; it refutes the paper's promotion of that descent to a selected regulator-independent physical law.

## 8. Refinement is not ontic extension

An exact size-changing control shows why semantics alone is insufficient. The representation embedding `J_3:C^2->C^3` above is an isometry. A physical flag writer can also be an isometry:

```text
E:C^2->C^4,
E e_0 = e_00,
E e_1 = e_11,
E†E=I_2.
```

For the two output flag sectors, the calibrated expectation screen is exactly

```text
(P(flag=0), P(flag=1)) = (1,0) on E e_0,
(P(flag=0), P(flag=1)) = (0,1) on E e_1.
```

If that flag algebra is recoverable under all licensed continuations, `E` adds a durable relational fact and is ontic extension. By contrast, `J_3` must be inverted or identified in the colimit as another description of the same fact. Both arrows satisfy the same size-changing isometry equation, so matrix dimension and isometry cannot type them.

The paper states the distinction correctly in prose, and its `J_ji` are explicitly said not to be evolution. But it never constructs one typed structure containing both operations and preventing a physical writer from being inserted as a comparison map or vice versa. A double category/fibration with vertical refinements, horizontal physical fillings, and compatibility squares is the minimal repair. Durability must be joined to the record-recoverability law; a new output coordinate by itself is not an ontic fact.

## 9. Infinite extension audit

The candidate's infinite-extension wall is correct and must remain.

For a strongly positive decoherence functional on a cylinder algebra, the GNS construction gives a finitely additive Hilbert-space-valued vector premeasure

```text
mu(A) = [A],
D(A,B) = <mu(A),mu(B)>.
```

Extension of the decoherence functional to the generated sigma-algebra is equivalent, at the relevant scope, to extension of this associated vector measure. Algebraic directed-limit compatibility supplies neither norm-countable additivity nor continuity at the empty event. A necessary diagnostic is that for every decreasing cylinder sequence `A_n ↓ empty`,

```text
||mu(A_n)||^2 = D(A_n,A_n) -> 0.
```

The corresponding Cauchy/convergence requirements for disjoint countable unions are likewise absent from Theorem 1. Strongly positive cylinder systems can fail this extension test; finite-state unitary and causal-set growth examples are discussed by [Dowker, Johnston, and Surya, “On Extending the Quantum Measure”](https://arxiv.org/abs/1007.2725).

The paper explicitly says it proves only an algebraic cylinder law and does not claim a sigma-additive measure, atomless continuum, or manifold. Therefore the infinite-extension mandatory kill does not fire. It does, however, prevent any continuum or completed-infinite-history reading of the primary.

## 10. Comparison with neighboring frameworks

- **Causal sites.** [Christensen and Crane](https://arxiv.org/abs/gr-qc/0410104) supply the closest point-free kinematic precedent: regions carry containment and causal relations as explicit structure. That makes the missing RHL axioms visible; it does not supply RHL's quantum law or select its comparison maps.
- **General-boundary quantum theory.** [Oeckl's general-boundary formulation](https://arxiv.org/abs/hep-th/0306025) and [GBQFT](https://arxiv.org/abs/hep-th/0509122) organize states/amplitudes by boundaries and glue regions without a privileged time slice. Their spacetime regions and boundary data are supplied. They are precedent for composition, not evidence that RHL has dynamically selected a point-free region category.
- **Locally covariant QFT.** [LCQFT](https://arxiv.org/abs/hep-th/0403007) makes covariance functorial under a declared category of spacetime embeddings. It shows how naturality is typed once embeddings are fixed; it does not choose those embeddings or remove their background-spacetime input.
- **Quantum causal graph dynamics.** [QCGD](https://arxiv.org/abs/1607.06700) provides graph-relative causal evolution and useful finite representations. Its vertices and discrete update order cannot be promoted to RHL ontology. It does not establish a no-point/no-tick infinite regional law.
- **Spin-foam refinement.** [Spin-foam refinement and renormalization](https://arxiv.org/abs/2211.09578) treats discretizations as regulators and seeks consistent amplitudes under refinement. It is a close methodological precedent, but the embedding/coarse-graining maps and the continuum/renormalization conditions remain substantive data. It supports the need for RHL's comparison audit rather than resolving it.

The framework links used in this seat are conceptually appropriate, but the frozen paper also contains three title/URL mismatches. I checked the arXiv records independently:

1. [`2507.21192`](https://arxiv.org/abs/2507.21192) is **“Quantum Systems as Indivisible Stochastic Processes”**; **“The Stochastic-Quantum Correspondence”** is [`2302.10778`](https://arxiv.org/abs/2302.10778).
2. **“Quantum Mechanics as Quantum Measure Theory”** is [`gr-qc/9401003`](https://arxiv.org/abs/gr-qc/9401003); [`gr-qc/9507057`](https://arxiv.org/abs/gr-qc/9507057) is **“Quantum Measure Theory and its Interpretation.”**
3. [`1512.00589`](https://arxiv.org/abs/1512.00589) is **“Non-Markovian quantum processes: complete framework and efficient characterisation”**; **“Operational Markov condition for quantum processes”** is [`1801.09811`](https://arxiv.org/abs/1801.09811).

These are bibliographic repairs, not scientific kills: the linked neighboring papers still support the nearby conceptual discussion. None is an inherited result for RHL.

## 11. Mandatory kills and exact changed-object attacks

| attack | exact result | disposition |
|---|---|---|
| hidden point set, slice, graph atom, or tick in the proof | none needed for Theorem 1 or the abstract point-free completion | no-point kill not fired; R1 is underdefined instead |
| representative-dependent `D` within a fixed diagram | none; the proof is well defined | descent theorem survives |
| prediction-carrying comparison maps | cross term `1 -> 0`; joint-image intersection dimension `2 -> 1` | mandatory narrowing fired |
| unacknowledged infinite-extension failure | failure is explicitly acknowledged | continuum kill not fired |
| M1: move the `b`-presentation's fed direction from `e_1` to `e_2` | all pullbacks still pass; cross term and marked intersection move | kills unqualified presentation independence |
| M2: replace the noninjective source form `diag(1,0)` by `I_2` | pullback remains `diag(1,0)` and compatibility fails | confirms null-kernel condition |
| M3: discard a noncofinal terminal stage with one new direction | limit dimension `2 -> 1` | confirms cofinal qualifier is necessary |
| M4: halve the first column of `J_5` | pullback `diag(1/4,1)`; composite moves | incompatible pullback refused |
| M5: retype a size-changing isometry as a physical flag writer | same isometry equation, but flag screen `(1,0,0,1)` appears | shows arrow type is extra structure |

Independent exact audit program:

```text
/private/tmp/rhl_refinement_audit.py
script SHA-256: 0ae954c4fff0d3553b98f1f878f65710d19e8ff35a59183c06cb8bdaa2326ad5
canonical result SHA-256: 1d6b8b2f274df20e7f8531c2baddb56c1c0ddc06e5a240a17639d191a0968edc
arithmetic: fractions.Fraction only
```

## 12. Integrity, replay, and scorer audit

The integrity harness was independent of the candidate package:

```text
/private/tmp/rhl_integrity_audit.py
script SHA-256: 34e0c56540ba2b32b5b357242c46ac57052afcca6da47d02e48f47f400ad4b6c
canonical result SHA-256: 809a8774a7ccae40d0bb2ea187f2fdbee8b65364e6bb553f694a24f24cb8d022
```

### 12.1 Clean and off-tree replay

I regenerated core, regulator, and scorer artifacts from an alien working directory. I then copied only the three sources, pin, and candidate paper into a fresh off-tree hierarchy containing no `.git`, regenerated the two upstream bundles, and ran the scorer there. Both replays were byte-identical to all six frozen artifacts:

| artifact | clean replay SHA-256 | true off-tree/no-`.git` SHA-256 |
|---|---|---|
| core transcript | `c56c8e3dece8357d3af0e39ea2459b8a29b6fd58bc3ffc99e5ba1cabe85adafb` | same |
| core receipt | `cfd7f243c96f29b303d7c0ef6c283b40be3994b3f6eb1945a801f0677903e060` | same |
| regulator transcript | `1f020e41989007048cf2d864f966b90184e332622230f26028c8e90225befb68` | same |
| regulator receipt | `cea302918c101c7b2bd5973167776baa587681f4b83b8ebff041e38e0bfee944` | same |
| score transcript | `5ce9002848affabf91ea7ec46690465ba2d444738fb9beb68f891accd085fdaf` | same |
| score receipt | `77528f648954ee30ea36bc69785d5646fc73ca2ef145127bd39e1753638eca98` | same |

All receipt seals, transcript hashes, source hashes, and the paper hash reconcile independently. The exact substantive source path contains no decimal numeric tokens, NumPy, or `math.isclose`. All three built-in selftests return `0` with their advertised refusal controls.

### 12.2 Fifteen frozen mutants

All fifteen return status `1` and create neither requested artifact:

| mutant | principal failed gate(s) | no artifacts |
|---|---|---|
| `MUT-CORE-HASH` | `G-HASH-CORE-SOURCE` | yes |
| `MUT-REG-HASH` | `G-HASH-REG-SOURCE` | yes |
| `MUT-INTERFERENCE-DIAGONAL` | `G-NO-INTERMEDIATE-KERNEL-WITNESS`, eligibility | yes |
| `MUT-PRESENTATION-MISMATCH` | `G-PRESENTATION-DESCENT-CONTROL`, eligibility | yes |
| `MUT-TAMPER-INERT` | `G-PRESENTATION-DESCENT-CONTROL`, eligibility | yes |
| `MUT-RECORD-UNERASABLE` | `G-RECORD-ERASER-CONTROL`, eligibility | yes |
| `MUT-REDUNDANCY-LOST` | `G-RECORD-REDUNDANCY-CONTROL`, eligibility | yes |
| `MUT-CHARACTER-INERT` | `G-STRUCTURAL-NONSELECTION`, eligibility | yes |
| `MUT-FIXED-FACTOR-SIGNAL` | `G-FIXED-FACTOR-LOCALITY`, eligibility | yes |
| `MUT-DYNAMIC-TRANSPORT-SMUGGLED` | `G-DYNAMIC-LOCALITY-REFERENT`, eligibility | yes |
| `MUT-DELETE-DESCENT-THEOREM` | `G-ANALYTICAL-THEOREM-REGISTER`, eligibility | yes |
| `MUT-ONTOLOGIZE-MESH` | `G-NO-FORBIDDEN-PROMOTION` | yes |
| `MUT-PROMOTE-GEOMETRY` | `G-NO-FORBIDDEN-PROMOTION` | yes |
| `MUT-PROMOTE-GR` | `G-NO-FORBIDDEN-PROMOTION` | yes |
| `MUT-OUTCOME-TAMPER` | `G-OUTCOME-SCOPE`, eligibility | yes |

An unknown argument returns `2` with no artifacts. A missing pin in a true off-tree copy returns nonzero with no artifacts.

### 12.3 No-overwrite defect

The normal output-first sentinel test passes for core, regulator, and scorer: if the output path already exists, each refuses and leaves the output unchanged without creating a receipt.

The reciprocal test fails in **all three programs**. If the receipt path exists but the output path does not, each program writes the new output first and only then raises `FileExistsError` on the receipt. A partial output is left behind on a refused run. This is caused by sequential `write_new(output)` / `write_new(receipt)` calls without preflighting both destinations or staging an atomic pair.

This does not alter the already frozen receipts, and mutant/missing-anchor refusals write no artifacts because they return before the write path. It is nevertheless a mandatory integrity repair: “no overwrite” is asymmetric and a refusal is not artifact-free in the receipt-first case.

## 13. Claims surviving and claims killed or narrowed

### Analytical claims surviving

1. Algebraic presentation descent is correct for a **fixed declared directed comparison system**.
2. The proof covers noninjective maps; their kernels are necessarily null for the compatible form.
3. Finite-list strong positivity descends, and the GNS null quotient is well defined.
4. Cofinal subsystems give the same colimit pair; noncofinal subsystems need not.
5. No hidden point, graph atom, slice, or tick is required by that theorem.
6. The finite two-presentation control is correct and extends to a third exact presentation.
7. The infinite/sigma-additive extension is genuinely open and correctly walled.
8. Representational refinement and ontic extension are conceptually distinct and can be typed distinctly in a point-free completion.

### Claims killed or narrowed

1. `RHL-POINT-FREE-REGIONAL-KINEMATICS-CONSTRUCTED` is not delivered: causal mereology is named, not formally built.
2. “Presentation-independent law” is narrowed to “representative-independent after a declared compatible comparison doctrine.”
3. Theorem 1 does not select comparison maps, generator maps, regional weights, or a physical law.
4. The candidate does not yet place refinement and ontic extension in one formal type system, despite correctly distinguishing them in prose.
5. No algebraic cylinder result licenses an infinite history measure, continuum, manifold, or continuum dynamics.
6. The full delivered primary is too high from this seat, independent of the finite scorer's eligibility marker.

## 14. Ordered repairs

1. **Construct R1, do not name it.** Freeze an explicit point-free causal mereology/site: parthood, overlap, causal precedence, boundary assignment, gluing, disjoint tensor, and all compatibility axioms. Give at least one atomless consistency model without ontologizing that model.
2. **Use two arrow types.** Put presentation refinement and ontic extension in a double category, fibration, or equivalent typed structure. State which arrows are inverted/quotiented and which create recoverable record facts.
3. **Price or derive comparison maps.** Add the two-system counterexample as a mandatory gate. Either make `J_ji` part of the law, derive them from law-selected continuation data, or prove that every residual choice acts only in the continuation-stable operational null ideal.
4. **Narrow all verdict prose.** Until repair 3 passes, replace “presentation-independent” and “refinement-invariant physical law” with the exact conditional statement proved by Theorem 1.
5. **Extend the regulator controls.** Include the exact `C^5` presentation, null noninjective map, noncofinal subsystem, incompatible pullback, and marked-comparison counterexample. Keep them receipts rather than proofs.
6. **State the infinite-extension criterion.** Register vector-measure continuity/countable-additivity tests and retain `WALL-INFINITE-EXTENSION` until they pass on a defined infinite system.
7. **Repair artifact writes.** Preflight both output paths before either write, or stage both to fresh temporary paths and publish them atomically. Add the receipt-exists/output-absent order as a frozen refusal mutant for core, regulator, and scorer.
8. **Regenerate and re-review.** Because fixes 1–4 alter the claimed construction and primary rather than merely typography, they require a new authorized candidate generation and full hostile replay.

## 15. Required final schema

```text
grade: REJECT
recommended primary: RHL-BLOCKED-AT-POINT-FREE-REFERENT (conditional ceiling if primitive Reg is accepted: RHL-BLOCKED-AT-REFINEMENT-CONSISTENCY)
ontology surviving: one actual compatible relational-record web remains a coherent postulate; no point, mesh atom, graph vertex, global slice, or tick is required; actualization remains a postulate
analytical claims surviving: Theorem 1 for a fixed declared directed comparison system, including noninjective/null, finite-list positivity, GNS quotient, and cofinality; exact three-presentation controls; explicit infinite-extension wall
claims killed or narrowed: causal mereology only named; presentation independence narrowed to independence after declared comparison maps; refinement/extension formal weld absent; continuum/infinite-history promotion refused; delivered primary not earned
new counterexample hashes: refinement audit script 0ae954c4fff0d3553b98f1f878f65710d19e8ff35a59183c06cb8bdaa2326ad5; refinement result 1d6b8b2f274df20e7f8531c2baddb56c1c0ddc06e5a240a17639d191a0968edc; integrity script 34e0c56540ba2b32b5b357242c46ac57052afcca6da47d02e48f47f400ad4b6c; integrity result 809a8774a7ccae40d0bb2ea187f2fdbee8b65364e6bb553f694a24f24cb8d022
scope walls: algebraic cylinder level only; declared comparison doctrine; no sigma-additive extension, atomless continuum, manifold, geometry, GR, QFT, particles, or empirical law; finite matrices are regulators only
ordered repairs: (1) explicit causal-site axioms, (2) two-arrow refinement/extension typing, (3) derive/price/quotient comparisons, (4) narrow primary, (5) add exact controls, (6) vector-measure gate, (7) atomic paired writes, (8) new generation and full review
```

## 16. Report digests

Digest convention: the body digest covers every byte from the title through the end of the required final-schema code block, including its trailing newline and excluding this digest section. The normalized/self digest covers the complete report after replacing both 64-hex digest values in the next two lines by 64 zeroes.

```text
body ordinary SHA-256: 7509ecf5bb092258688884245f93bd17927ae5e468d7767a13ad6de36d00b801
normalized/self SHA-256: 48c63815e688fc112a9b39ec415fcc137555cfcf55fd12e16b40ba6765e10a1e
```
