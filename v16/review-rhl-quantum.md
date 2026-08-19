# Hostile review of RHL Paper 11 — Seat Q

**Lens:** quantum histories, instruments, normalization, and process-law type.

**Grade:** `ACCEPT-WITH-FIXES`.

**Highest registered rung supported by this seat:**
`RHL-STABLE-DIVISION-SHADOW-CONSTRUCTED`. The broader candidate primary
`RHL-REGIONAL-QUANTUM-LAW-CONSTRUCTED-BUT-GEOMETRY-UNENTERED` is not rejected
by this lens, but its point-free and physical clauses belong to the other
seats.

## 1. Executive verdict

The quantum core is real but narrower than the paper says.

The Gram/GNS construction is valid after making the additive relations and
null quotient explicit. Theorem 2 is correct exactly as stated: what excludes
an ordinary probability measure is a nonzero **total real cross term on some
registered union**, not merely a nonzero matrix entry. Theorem 3 is correct for
changing output sectors, arbitrary ancillas, coherent fine histories, and
trace-nonincreasing outcomes when all coherent histories are first grouped
into class operators. Its all-input identity is the right condition, and the
`diag(1,4)` control is decisive.

Theorem 4 is correct on the declared tensor-factor/conditional-expectation
append-only class. It is not a theorem that record stability follows from
algebra inclusion alone, and it does not survive an enlarged catalogue that
licenses reset. Its proof needs one wording repair: a normalized state on an
“extra factor” supplies a conditional expectation only when the future
algebra actually has the stated tensor-factor form, or when a CP conditional
expectation onto that form is separately assumed.

Theorem 5 contains the main mathematical failure. A character twist preserves
Hermiticity, strong positivity, gluing, monoidality, and refinement under its
stated hypotheses. It does **not** preserve total normalization in general,
and it preserves boundary covariance only if the character label is natural
under boundary isomorphisms. The frozen receipt displays one coarse weight
`1,1/2,0,1/2`; it never supplies the complementary outcomes needed to certify
a normalized law. The exact counterexample is immediate: a normalized total
amplitude `(1/2,1/2)` has total weight one, while the `i` twist has total weight
one half and the `-1` twist has total weight zero.

That failure narrows the universal theorem but does not kill its nonselection
conclusion. I constructed an exact complete two-port character family. For all
four fourth-root characters it has a Hermitian strongly positive history
functional, all-input complete division, normalized total event, compositional
phase law, and moving predictions. The same construction derives its
decoherence functional, class operations, division instrument, record algebra,
append-only copy isometry, and recovery from one boundary model. Thus the weld
required by the protocol can be built and the stable-division existence rung
survives. The frozen regulator did not contain this weld; an authorized repair
must replace the single-port receipt with the common-law family rather than
claim that the old row already proved it.

The microscopic law-type verdict also narrows. Theorem 2 excludes a positive
measure on the declared interfering alternatives. It does not prove that every
stochastic formulation on an enriched state must be indivisible, nor that a
decoherence functional rather than an equivalent phase-retaining
representation is uniquely required. At the microscopic grain the supported
coordinate is `METHOD-INCONCLUSIVE`; at the constructed stable boundary,
`DIVISION-KERNEL-SUFFICIENT` is correct.

## 2. Isolation and authentication

I reviewed protocol commit `67e911dc663473d120de7347c1663028ff5f26bc`
and candidate commit `b84225f0e5692b06708966e6e7028bb4e19a7adc`.
I read only the immutable candidate objects, the protocol, and the antecedent
needed by Seat Q. I did not read, list, request, or infer either sibling RHL
review, any external scratchpad, or the unrelated SCOUT-T material. Candidate
files remained unmodified.

The frozen hashes all authenticate:

| object | observed SHA-256 |
|---|---|
| `v16/note-rhl-pin.md` | `1d0df95fb074a688160e1a4554976268643e35835ef46b1d4918b90ee23505ee` |
| `v16/code/rhl_core.py` | `032ede336c8cf23b168e018ecd0748e0467d1ca25cb2b44ae750ae320ae9ba8a` |
| `v16/code/rhl_core_output.txt` | `c56c8e3dece8357d3af0e39ea2459b8a29b6fd58bc3ffc99e5ba1cabe85adafb` |
| `v16/code/rhl_core_receipt.json` | `cfd7f243c96f29b303d7c0ef6c283b40be3994b3f6eb1945a801f0677903e060` |
| `v16/code/rhl_regulator.py` | `d6d520a6a43451a889bfc40e2dd8df2f9afc08f032c202c3d8c206c02b4a3db9` |
| `v16/code/rhl_regulator_output.txt` | `1f020e41989007048cf2d864f966b90184e332622230f26028c8e90225befb68` |
| `v16/code/rhl_regulator_receipt.json` | `cea302918c101c7b2bd5973167776baa587681f4b83b8ebff041e38e0bfee944` |
| `v16/code/rhl_score.py` | `b2f1f780d5b907b628adcd4994ac5d6eeb2d2a5abb78783d0a18c06e6582e1c2` |
| `v16/code/rhl_output.txt` | `5ce9002848affabf91ea7ec46690465ba2d444738fb9beb68f891accd085fdaf` |
| `v16/code/rhl_receipt.json` | `77528f648954ee30ea36bc69785d5646fc73ca2ef145127bd39e1753638eca98` |
| `v16/paper-11-unsliced-regional-history-law.md` | `423f3cb56f6e0ccdd54ef59cfa0454509d14c005136e375307bb441133cac384` |
| `v16/note-rhl-candidate-verification.md` | `2a7de79764bd92174ceefbc3d64d3fab8c99fb7267edcdf1ee5b458195578f2b` |

My independent exact reconstruction is
`/private/tmp/rhl_quantum_independent.py`, SHA-256
`84a1225c42bfc9c8312ac85ef38b4016a848912554fba79f0ac74f1471787208`.
It imports no RHL source or scorer function. It uses exact rational and
Gaussian-rational arithmetic.

## 3. Strong positivity and the Gram/GNS representation

Let `F(E)` be the free complex vector space on proposition symbols. Extend
`D(A,B)` sesquilinearly:

```text
<sum_j c_j[A_j], sum_k d_k[B_k]>
    = sum_jk conjugate(c_j) d_k D(A_j,B_k).
```

The paper's finite-list strong-positivity axiom says exactly that this form is
positive semidefinite on every vector of `F(E)`. If `<x,x>=0`, positivity of
`<x+lambda y,x+lambda y>` for every complex `lambda` gives `<x,y>=0` for every
`y`. Hence the null set is a linear radical, and the form descends to a
positive-definite inner product on `F(E)/N`. Completion gives a Hilbert space.

Biadditivity also handles the event-algebra relations. For disjoint `A,B`, the
formal vector

```text
[A union B] - [A] - [B]
```

has zero inner product with every proposition and therefore lies in `N`.
Thus the construction factors through the additive proposition space instead
of treating synonymous event sums as distinct vectors. The resulting Hilbert
representation is unique up to the usual unitary carrying the represented
proposition vectors to one another. It is a representation of `D`, not a new
beable or a proof that `D` is the unique possible law language.

The frozen route matrix is the rank-one Gram matrix

```text
[[ 81/625, -144/625],
 [-144/625,  256/625]],
```

with determinant zero. This is a receipt for the general argument, not its
proof. The changed object `Q-NONPOSITIVE-GRAM` replaces it by
`[[1,2],[2,1]]`, whose determinant is `-3`; strong positivity fails exactly.

## 4. Theorem 2 — interference and intermediate probability

For a subset `S` of a disjoint refinement, Hermiticity and biadditivity give

```text
mu(union S) = sum_i D_ii + 2 Re sum_{i<j} D_ij.
```

An ordinary probability measure agreeing on the singleton events assigns only
the diagonal sum. Therefore a nonzero total cross term for even one registered
union is an exact contradiction. Conversely, if every registered union has
zero total cross term, the nonnegative singleton weights supplied by strong
positivity define an ordinary measure on that finite event algebra. Theorem 2
is consequently correct, and its “some union” quantifier is load-bearing.

The registered route amplitudes `9/25` and `-16/25` give

```text
coherent union = 49/625,
diagonal sum   = 337/625,
cross defect   = -288/625.
```

No positive probability measure on those two exclusive route events can
match all three numbers. I found no positive intermediate-kernel counterexample
at that declared event grain.

The cancellation control prevents an overreading. The exact Hermitian matrix

```text
[[1/2,  i/4],
 [-i/4, 1/2]]
```

is positive definite (determinant `3/16`) and has a nonzero individual
off-diagonal entry, yet its total cross contribution is zero. Its singleton
weights and union weight are `1/2,1/2,1`, exactly reproduced by an ordinary
measure. This does not refute Theorem 2; it proves that “nonzero entry” cannot
replace the theorem's total-cross-term premise.

The theorem excludes probabilities on the interfering alternatives. It does
not exclude a positive Markov law on a larger state that retains phase while
never treating those route labels as exclusive ontic states. Consequently the
later sentence “if stochastic, it must be indivisible” is not a theorem of
this argument without a no-enlargement premise.

## 5. Theorem 3 — CP instruments at a division

For each outcome define

```text
E_alpha = sum_r K_(alpha r)^dagger K_(alpha r).
```

The Kraus form is completely positive after tensoring with an arbitrary
ancilla. It is trace nonincreasing exactly when `E_alpha <= I`. If all outcomes
share the same input but have different codomains, place the codomains in the
direct sum `direct-sum_alpha H_out,alpha`; the effects still live on the common
input. The family is trace preserving for every positive input and every idle
ancilla exactly when

```text
sum_alpha E_alpha = I.
```

Necessity follows because positive trace-class states separate bounded
operators. Sufficiency follows by cyclicity of trace, with the identity
tensored by the ancilla identity. The theorem therefore survives changing
output sectors and arbitrary spectators.

The fine-history index must be typed correctly. If histories `r` inside one
outcome are unrecorded and coherent, first form each coherent class operator

```text
C_(alpha b) = sum_(r in coherence block b) A_(alpha r),
```

and only then set

```text
J_alpha(rho) = sum_b C_(alpha b) rho C_(alpha b)^dagger.
```

Using every `A_(alpha r)` as a separate Kraus operator would insert an
unlicensed record. With this correction of notation, the all-input identity is
unchanged.

An independent changing-sector control uses `K_0:C^2 -> C` equal to `[1,0]`
and `K_1:C^2 -> C^3` with only entry `[0,1]` nonzero. Their effects sum to
`I_2`. The `diag(1,2)` single operation has effect `diag(1,4)`: it normalizes
the prepared vector `(1,0)` but is not an all-input complete operation. The
paper's countercontrol is exact.

## 6. One common law: functional, division, record, and recovery

The frozen regulator places its interference functional, complete-instrument
identity, and record-erasure examples in neighboring fixtures. That receipt
does not itself weld them. The weld can nevertheless be constructed from the
paper's typed ingredients.

Let

```text
P_0, P_1                 route projections,
P_plus, P_minus          complementary output projections,
U_eta = diag(1, eta),    eta in {1,i,-1,-i}.
```

For final outcome `y` and fine route `r`, define one regional representation

```text
A_(y r) = P_y P_r U_eta,
K_y     = sum_r A_(y r) = P_y U_eta,
D_rho((y,r),(y',r'))
        = Tr[A_(y r) rho A_(y' r')^dagger].
```

These are not independent objects:

- `D_rho` is the Gram functional generated by the fine class operations;
- coherent fine routes are summed inside `K_y`;
- `J_y(rho)=K_y rho K_y^dagger` is the division instrument; and
- `sum_y K_y^dagger K_y = U_eta^dagger(P_plus+P_minus)U_eta = I`.

For every input and ancilla, this is a complete instrument. Cross terms between
the two final outcome sectors vanish, while route cross terms inside each
outcome remain. With `rho=P_plus`, the exact outcome probabilities are:

| `eta` | plus | minus | total |
|---|---:|---:|---:|
| `1` | 1 | 0 | 1 |
| `i` | 1/2 | 1/2 | 1 |
| `-1` | 0 | 1 | 1 |
| `-i` | 1/2 | 1/2 | 1 |

Let the record algebra be `C=span{P_plus,P_minus}`. The append/copy isometry

```text
V = P_plus tensor |0> + P_minus tensor |1>
```

satisfies `V^dagger V=I` exactly and copies the outcome sector to a new flag.
The Heisenberg embedding `c -> c tensor I` preserves `C`; partial evaluation of
the appended factor is a recovery map on `C`. Iterating the same construction
gives the append-only future class. Thus `D`, class operations, complete
division, record algebra, and recovery all arise from one typed boundary law.

Taking the free symmetric monoidal category generated by these region maps and
extending by composition/tensor product makes this a small nonempty regional
law, not merely three unrelated matrices. It is nontrivial because the
unrecorded route cross terms move the final record. Its generators and phase
remain supplied law data; it selects no physical dynamics or geometry.

This construction validates the existence content of
`RHL-STABLE-DIVISION-SHADOW-CONSTRUCTED`. It also shows exactly what the repaired
candidate must include. The old receipt cannot retroactively count as the
weld.

## 7. Theorem 4 — append-only stability

For a genuinely factorized future algebra `C tensor B`, a normalized state
`omega` on `B` gives the unital CP conditional expectation

```text
E_omega(c tensor b) = c omega(b).
```

If the continuation embeds `c` as `pi(c) tensor I`, then
`pi^(-1) o E_omega` is a left inverse on `C`. Automorphisms and appended
factors compose, so the recovery maps compose in reverse order after every
finite licensed continuation. Theorem 4 is correct on this class.

The phrase “inside a larger future algebra” is too broad. A normalized state
on a named discarded factor does not by itself produce a conditional
expectation from an arbitrary containing algebra. The theorem must assume the
future algebra is the stated tensor product, or assume a CP conditional
expectation onto it. The explicit common law in §6 satisfies the stronger
condition.

The distinctions are:

- algebra inclusion merely keeps a named copy present;
- recoverability requires a physical left inverse;
- recoverability preserves distinguishability of the classical record;
- redundancy permits recovery from a surviving copy after another is reset;
- actualization is not implied by any of these.

Exact controls agree. Append and pointer relabeling are recoverable. Reset maps
both pointer values to one and has no left inverse. Copying first and resetting
the first copy leaves recovery from the second. A future-catalogue enlargement
that licenses the reset demotes the formerly stable record. Therefore
append-only stability is a conditional nomological class, not absolute
permanence or an actualization theorem.

## 8. Theorem 5 — what the character twist preserves

For a finite alternative list, write the original functional as `D` and the
diagonal character matrix as `U_chi`. The twist is

```text
D_chi = U_chi^dagger D U_chi.
```

It is Hermitian and strongly positive. Character multiplicativity plus
additivity of `ell` proves gluing and monoidality. Refinement invariance follows
if `ell` is refinement invariant. These parts of Theorem 5 are correct.

Two additional properties do not follow:

1. **Normalization.** If `1` denotes the vector representing the total event,
   then normalization is `1^dagger D 1=1`. After twisting it becomes
   `(U_chi 1)^dagger D(U_chi 1)`, which need not equal one.
2. **Covariance.** Boundary covariance survives only if `ell` and its character
   are natural under the relevant boundary isomorphisms. Refinement invariance
   alone does not imply this. Swapping two boundary alternatives with labels
   zero and one changes the twisted pair `(1,i)` to `(i,1)` unless the
   covariance transport also carries the label data.

The frozen two-filling receipt demonstrates the normalization defect rather
than closing it. Starting from amplitudes `(1/2,1/2)`, the total weights under
`eta=1,i,-1,-i` are `1,1/2,0,1/2`. Only the first is a normalized total event;
the zero row cannot even be repaired by scalar renormalization. Hence the
paper's universal sentence that “normalization ... permit[s] both the trivial
character and prediction-moving characters” is unproved and false if read as
preservation of an arbitrary normalized law.

The exact common law in §6 supplies the correct replacement. Its complementary
port restores total normalization for every character, all-input completeness
holds, the functional remains strongly positive, and predictions move. Phase
gates compose according to the character and tensor on disjoint regions. If
`ell` is also boundary-natural, the family is covariant. Therefore:

- the **universal preservation theorem** is killed for normalization and
  covariance;
- the **existential structural-nonselection conclusion** survives by the
  complete two-port counterfamily.

That distinction must appear in the theorem statement, proof, receipt, and
primary gate.

## 9. Process-law classification by grain

The evidence supports the following strict classification:

| grain | supported statement |
|---|---|
| unrecorded route partition | no ordinary positive measure on those route alternatives reproduces the interfering union |
| microscopic ontology/law | `METHOD-INCONCLUSIVE`; enriched phase-retaining, Hilbert/class-operator, decoherence-functional, and indivisible formulations are not separated here |
| representation | the displayed `D` is Gram-equivalent to its Hilbert/class-operator construction, not a distinct ontology |
| stable division | `DIVISION-KERNEL-SUFFICIENT`; the complete CP instrument gives ordinary outcome probabilities |
| process tensor | available as a possible intervention-complete representation, not required by this fixed fixture |
| higher-order process | `METHOD-INCONCLUSIVE`; causal order is not an operational variable here |

The scorer's `HISTORY-DECOHERENCE-FUNCTIONAL-REQUIRED` and
`INDIVISIBLE-MULTITIME-LAW-REQUIRED` overstate Theorem 2. What is required is
retention of the operational cross information and refusal to factor through
exclusive route probabilities. The theorem does not uniquely select the
mathematical representation or forbid divisible dynamics on an enlarged state
that never promotes those routes to exclusive facts.

## 10. Changed-object attacks

Every changed object was generated independently as canonical exact JSON and
changes its named predicate:

| changed object | exact result | SHA-256 |
|---|---|---|
| `Q-NORMALIZATION-TWIST` | total weight `1 -> 1/2` under the `i` twist | `519b867a78db4c88e1fbf4d565cbfcc1d307e686014314f1492090702b9e635b` |
| `Q-IMAGINARY-CANCELLATION` | nonzero `i/4` off-diagonal but union remains additive | `9e131d671a30dc28f06a597c4940612ee8bb3faea7a184a7988daae50973a411` |
| `Q-INCOMPLETE-DIVISION` | deleting `P_minus` leaves effect `P_plus != I` | `a5ececdca493e4ec86421655cbe263961e265e202fcd8baa1a473c8ab9423347` |
| `Q-RESET-DESTROYS` | both pointer values map to zero; no recovery exists | `fb3958cd050b01e358f7402547e276b701b7133e7591b309fce50b142bfe2b1d` |
| `Q-COVARIANCE-TWIST` | non-natural label swap changes the twisted boundary assignment | `b8431a7b0462036d1619c6961fef0b5077cbd0928b0c55fec78c029b6a7c1731` |
| `Q-NONPOSITIVE-GRAM` | determinant `-3`; strong positivity fails | `e891cc94a77f36961bc88a0de6fec0c29aa65858ad01f26fb2658172266831b5` |

This exceeds the protocol requirement of four seat-specific attacks.

## 11. Frozen mutants and integrity

All 15 frozen mutants were executed. Every one returned nonzero and wrote no
target artifact:

```text
MUT-CORE-HASH
MUT-REG-HASH
MUT-INTERFERENCE-DIAGONAL
MUT-PRESENTATION-MISMATCH
MUT-TAMPER-INERT
MUT-RECORD-UNERASABLE
MUT-REDUNDANCY-LOST
MUT-CHARACTER-INERT
MUT-FIXED-FACTOR-SIGNAL
MUT-DYNAMIC-TRANSPORT-SMUGGLED
MUT-DELETE-DESCENT-THEOREM
MUT-ONTOLOGIZE-MESH
MUT-PROMOTE-GEOMETRY
MUT-PROMOTE-GR
MUT-OUTCOME-TAMPER
```

Further integrity results:

- A clean replay in `/private/tmp/rhl-q-clean.KchOJn` reproduced all six core,
  regulator, and scorer output/receipt hashes byte for byte.
- A true off-tree replay in `/private/tmp/rhl-q-offtree.FIQFXC`, invoked from
  `/private/tmp`, contained no `.git` and reproduced those six hashes exactly.
- Core, regulator, and scorer self-tests all pass.
- Unknown arguments exit 2.
- A missing pin exits 1 before writing either requested artifact, although it
  leaks a raw `FileNotFoundError` traceback instead of a typed refusal.
- Existing output as the first target is refused without changing either
  artifact.
- The two-target no-overwrite path is not transactional: when only the receipt
  target already exists, the scorer writes a fresh output and then fails on
  the receipt. Directory `/private/tmp/rhl-q-partial.tXopCo` reproduces this.
  This violates the strongest reading of no-artifact-on-refusal and requires a
  preflight check of both targets before either write.
- Source scans find no floating-point token, NumPy use, or tolerance
  comparison in the substantive core/regulator path.
- Transcript SHA, paper SHA, every core/regulator/score seal, and regulator
  data digest independently reconcile. The official measurement digest is
  `69ace50f79f6944c5dcc7f9c84da00d7eaa057a3b4e8e97010a9ec7f49fb6737`.

The mutant harness is `/private/tmp/rhl_mutant_audit.py`, SHA-256
`2ceae2286531721cf035300ade3712cf7505e07a7f266aee4c7fb5cc03bb0485`.
The seal audit is `/private/tmp/rhl_integrity_audit.py`, SHA-256
`1e0bc29827254a91db225aad0739da1582911c408b519231e86f1750524cd527`.

## 12. Ontology, law, and representation disposition

- **Ontology surviving:** none is derived by this seat. One actual compatible
  record history remains a candidate interpretation. Actualization remains a
  postulate. Fine alternatives, Hilbert vectors, matrices, and decoherence
  entries are not promoted to actual worlds or spacetime atoms.
- **Law surviving:** a nonempty regional composition law with coherent
  interiors, a complete stable division, and append-only recovery can be
  constructed. Its numerical generator maps, phase character, division
  catalogue, and append-only future class are supplied law data, not selected.
- **Representation surviving:** strong positivity admits a Gram/GNS Hilbert
  representation; the decoherence functional and class-operator calculation
  are equivalent descriptions at the constructed grain. Neither is additional
  substance.

The common law is nontrivial because cross terms move a stable output record.
It remains a deliberately small supplied-map law. Nothing in this seat turns
the free-category extension into selected physics or geometry.

## 13. Scope walls

The following walls remain absolute for this candidate:

1. no selected amplitudes, couplings, vacuum, species, dimension, topology,
   scale, or physical constants;
2. no derivation of division placement, append-only continuation catalogue, or
   actualization;
3. no sigma-additive infinite-history extension from algebraic cylinders;
4. no dynamically transported subsystem algebra or changing-boundary
   no-signalling theorem;
5. no calibrated causal metric, interval, volume, curvature, backreaction, or
   physical geometry;
6. no Lorentzian manifold, Einstein equation, GR limit, QFT vacuum, particles,
   scattering, or empirical prediction;
7. no selected clocked one-parameter group, Hamiltonian, energy law, or
   Lindbladian sector;
8. no conclusion that reality is fundamentally discrete, continuous, atomic,
   or atomless; and
9. no derivation of a unique ontology from the Hilbert/decoherence-functional
   representation.

## 14. Ordered repairs

1. Replace Theorem 5 by two statements: a preservation theorem for
   Hermiticity/positivity/composition/refinement, and an existential
   nonselection theorem using a complete normalized outcome family.
2. Add boundary-naturality of `ell` as an explicit covariance hypothesis.
3. Replace the single-port character receipt with the exact two-port common
   law of §6; gate total-event normalization and all-input completeness for
   every character.
4. Put `D`, the fine class operations, the division instrument, record algebra,
   append isometry, and recovery in one frozen typed object rather than
   neighboring fixtures.
5. State Theorem 4 for an actual tensor-factor future algebra or assume a CP
   conditional expectation; retain reset, relabel, redundancy, and catalogue-
   enlargement controls.
6. Make the Gram/GNS additive-relation quotient explicit.
7. Replace microscopic `HISTORY-DECOHERENCE-FUNCTIONAL-REQUIRED` and
   `INDIVISIBLE-MULTITIME-LAW-REQUIRED` by `METHOD-INCONCLUSIVE`, while keeping
   the exact no-probability theorem at the declared route grain and
   `DIVISION-KERNEL-SUFFICIENT` at the stable boundary.
8. Preflight both artifact paths before writing; type missing-anchor failures.
9. Regenerate candidate artifacts and rerun the full mutually blind panel.

## 15. Report checksum

Normalized/self SHA-256: `5aa9a4f5c052a3ad1619283a09040881be3ef50f1d4562c2a2bde6131033c8d2`

The normalized hash is computed after replacing the lowercase 64-hex value on
the preceding line by the literal token `<NORMALIZED-SELF-SHA256>`. The
ordinary SHA-256 is reported out of band after freezing the normalized value.

grade: ACCEPT-WITH-FIXES
recommended primary: RHL-STABLE-DIVISION-SHADOW-CONSTRUCTED (Seat-Q maximum; broader regional/geometry disposition reserved to the other lenses)
ontology surviving: one actual compatible record history remains a candidate; actualization remains postulated; no Hilbert vector, decoherence functional, route, graph cell, point, or tick is promoted to ontology
analytical claims surviving: Gram/GNS representation after additive/null quotient; Theorem 2 with total-cross-term quantifier; Theorem 3 with coherent class-operator grouping and all-input identity; Theorem 4 on the factorized append-only/conditional-expectation class; character preservation of Hermiticity, strong positivity, gluing, monoidality, and refinement; exact normalized prediction-moving two-port family; one common functional/instrument/record/recovery law; stable-boundary division-kernel sufficiency
claims killed or narrowed: Theorem 5 does not generally preserve normalization or covariance; frozen single-port receipt is not a normalized family; microscopic indivisible/decoherence-functional necessity narrowed to METHOD-INCONCLUSIVE; Theorem 4 needs factorization or a CP expectation; individual off-diagonal entries are insufficient without a nonzero union cross term; frozen neighboring fixtures do not themselves prove the weld; no-overwrite refusal is nontransactional in one target order
new counterexample hashes: Q-NORMALIZATION-TWIST 519b867a78db4c88e1fbf4d565cbfcc1d307e686014314f1492090702b9e635b; Q-IMAGINARY-CANCELLATION 9e131d671a30dc28f06a597c4940612ee8bb3faea7a184a7988daae50973a411; Q-INCOMPLETE-DIVISION a5ececdca493e4ec86421655cbe263961e265e202fcd8baa1a473c8ab9423347; Q-RESET-DESTROYS fb3958cd050b01e358f7402547e276b701b7133e7591b309fce50b142bfe2b1d; Q-COVARIANCE-TWIST b8431a7b0462036d1619c6961fef0b5077cbd0928b0c55fec78c029b6a7c1731; Q-NONPOSITIVE-GRAM e891cc94a77f36961bc88a0de6fec0c29aa65858ad01f26fb2658172266831b5
scope walls: no selected dynamics/constants/catalogue/divisions/actualization; no infinite quantum measure; no dynamic-subsystem locality; no geometry/backreaction; no Lorentz/GR/QFT/particles/scattering; no Hamiltonian or energy law; no empirical prediction; no atomicity/continuum verdict; no ontological promotion of representations
ordered repairs: 1 split and repair Theorem 5; 2 add boundary-naturality; 3 freeze complete normalized character family; 4 freeze one typed common law; 5 scope Theorem 4 to factorized/expected futures; 6 make GNS quotient explicit; 7 demote microscopic law-type necessity to METHOD-INCONCLUSIVE; 8 make writes transactional and failures typed; 9 regenerate and re-review
