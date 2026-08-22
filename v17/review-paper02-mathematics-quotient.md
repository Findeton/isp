# Paper 02 blind review — Seat M: quotient mathematics and resources

- Date: 2026-08-22
- Reviewer lens: quotient categories, measurable fibers, naturality, and resource minima
- Bound construction commit: `bfaddd50a5006ea90933a5a6eb6f89e345a98315`
- Authenticated protocol HEAD: `5340b5c71b0f0cfdb7e424d5ac21f5cd3bbb1efc`
- Verdict: **ACCEPT-WITH-SCOPE**
- First decisive semantic counterexample: **none**
- Ordinary SHA-256: reported externally after freeze
- Normalized self-hash convention: replace exactly the 64 lowercase hexadecimal
  characters on the line beginning `normalized_self_sha256:` by 64 ASCII
  zeroes, preserving every other byte, then apply SHA-256.
normalized_self_sha256: 98c2ce6ca8a0423b0162b02592a60eae072b34d0215b22e5bcbb2af022e52646

## 1. Blindness and corpus authentication

I read the full Paper 02 protocol, pin, candidate, construction audit, Paper
01 terminal adjudication, and era charter. I did not inspect or communicate
with either sibling seat and did not read either forbidden report path:

```text
v17/review-paper02-quantum-foundations.md
v17/review-paper02-ontology-barandes.md
```

The frozen corpus reproduced exactly:

| Artifact | Recomputed SHA-256 | Result |
|---|---|---|
| `v17/note-paper02-operational-quotient-ontology-residue-pin.md` | `e26b91b7126046d4b9c8f579fa6147f48922dc7fb711851b5a0fe3501a2c49cf` | authenticated |
| `v17/paper-02-operational-quotient-ontology-residue.md` | `55edf811b2d80a628cae1d871994383e0013ec58dd77b70d340eebb836c93eec` | authenticated; immutable |
| `v17/note-paper02-construction-audit.md` | `6d3b63dad6866c725ee8cc621e2d5792c1532683de295b6fec3c45b72283627c` | authenticated; nonauthoritative |
| `v17/note-paper01-hostile-review-adjudication.md` | `3320414cb8161da33fbce3b1b8d3838cd3989d315de792c24cf24c0c322c2bb1` | authenticated |
| `v17/paper-00-reality-first-programme.md` | `a9f8456763447eaa25a6a840e8f221f51d961ecd9c3ced649ae35a8616457cbe` | authenticated |

No bound byte changed during this review. No implementation or numerical
artifact exists or could decide the mathematics.

## 2. Executive disposition

The central mathematical package reconstructs. Complete-continuation
equivalence is a typed congruence because every postcomposition, ancillary
extension, adaptive branch, and tensor test is already inside the quantified
profile. On the subcategory reachable from the accepted operational category,
the quotient forgets exactly the kernel of the decoder and is naturally
isomorphic to the decoded operational image. Extra native states are not
inverted.

The fiber and factorization results also reconstruct, but the force of the
second is deliberately conditional. If a proposed invariant must be natural
under a category that includes a many-to-one fiber-forgetting morphism, then
it cannot depend on the forgotten coordinate. That is a valid no-selection
theorem for the frozen interface; it is not a proof that the coordinate is
unreal.

Two exact scope clauses must accompany acceptance:

1. categorical quotient/naturality is on the **reachable operational image**;
   a zigzag through the quotient does not provide a direct microscopic
   isomorphism;
2. whenever the reduction is claimed as a measurable representation
   morphism, the reachable boundary spaces and decoder/profile maps must be
   standard-Borel/measurable (or otherwise belong to a declared measurable
   category). Finite-dimensional tomography makes this automatic for the
   intended packets, but it is not a theorem about arbitrary pathological
   measurable quotients.

These are already consistent with the candidate's scientific ceiling. No
admitted mathematical counterexample forces a revision of that ceiling.

## 3. Adequacy contract without circularity

The adequate-representation contract assumes:

- a compositional embedding $J_R$ of the accepted category;
- a decoder $K_R$ on the reachable operational image with
  $K_RJ_R\simeq\mathrm{id}$;
- equality of every complete registered probability; and
- preservation of the accepted wiring operations.

It does **not** assume that two representatives with equal complete profiles
are microscopically identical, that $J_RK_R$ is identity on extra states, or
that a direct inverse exists between two representations. The quotient
theorem is therefore not an ontology assumption. It is, however, a formal
consequence of a deliberately strong adequacy contract. Its empirical content
is inherited from the complete Paper 01 interface rather than newly derived.

The qualifier “reachable” is essential. Conditional profiles are defined for
admitted prepared boundary states or positive-probability conditioned
branches; a zero-mass branch with no separately declared boundary law has no
canonical conditional profile.

## 4. Complete quotient lineage

Fix a boundary type $A$ and an operational object $q$ at that boundary. The
complete lineage is

```text
operational boundary q in Q
-> adequate representative J_R(q) in B_R(A)
-> full profile Phi_R(J_R(q)) over every ancilla/continuation/reader
-> typed class [J_R(q)] in O_R(A)
-> decoded object Kbar_R([J_R(q)]) = q.
```

For arbitrary reachable $x,y$ of the same type,

$$
x\sim_R y
\iff \Phi_R(x)=\Phi_R(y)
\iff K_R(x)=K_R(y),
$$

where the final equivalence uses adequacy and operational separation. Hence

$$
\overline K_R([x])=K_R(x)
$$

is well defined and faithful. If $q:K_R(x)\to K_R(y)$ is a morphism in the
declared image, $J_R(q)$ is a quotient morphism from
$[J_RK_R(x)]=[x]$ to $[J_RK_R(y)]=[y]$; this supplies fullness on the image.
Every image object has $[J_R(q)]$, so essential surjectivity follows.

The inverse is therefore

$$
\overline J_R(q)=[J_R(q)],
$$

only on the declared image. An unreachable native state $u$ need not satisfy
$J_RK_R(u)=u$, and need not even lie in the decoder's domain.

## 5. Congruence reconstruction

If $x\sim_Ry$ and $f$ is a compatible continuation, any tester $C$ after
$f$ gives the tester $C\circ f$ before it. Therefore

$$
\Pr(o\mid C,f(x))=
\Pr(o\mid C\circ f,x)=
\Pr(o\mid C\circ f,y)=
\Pr(o\mid C,f(y)).
$$

For tensoring, the profile's ancillary quantifier includes every continuation
on $x\otimes z$, including entangled effects across the output and ancilla.
Thus equality is completely bounded rather than merely scalar. Applying this
argument to each factor proves bifunctorial congruence. Affine mixtures follow
from linearity. An adaptive policy is a sum/integral over recorded prefix
branches, on each of which the suffix is an admitted continuation. Discard
and record maps are themselves admitted postprocessings.

The proof would fail for a profile based on one terminal reader or only
unentangled probes. The candidate does not use either weaker relation.

## 6. Fiber and factorization lineage

Let $Z$ be a fixed standard-Borel space. Choose a normalized initial kernel
$\nu(dz_0\mid h_0)$ and measurable causal update kernels
$L_k(dz_k\mid z_{k-1},h_{\le k})$ from the realized prefix only. Then

$$
d\Gamma_R^Z=
d\Gamma_R(h)\,\nu(dz_0\mid h_0)
\prod_kL_k(dz_k\mid z_{k-1},h_{\le k}).
$$

Finite Ionescu--Tulcea iteration gives a normalized joint measure, and
integrating the entire $Z$ path returns $d\Gamma_R(h)$. A coherent kernel
family must be fixed across program extensions: the same prefix uses the same
kernel, independent of an unperformed future setting. For independently
prepared tensor factors the declared fiber kernel is the product kernel.

The lineage is

```text
R and representative x
-> R^Z and (x,z)-histories
-> projection pi_Z forgetting the complete Z path
-> identical registered profile in R
-> an invariant either commutes with pi_Z and factors through [x],
   or it is refused the label representation-natural.
```

For a family $I_R$ natural under the admitted projections,

$$
I_R(x)=I_{R_{\rm op}}(\pi_Rx).
$$

Thus $x\sim_Ry$ implies $I_R(x)=I_R(y)$, and
$\bar I([x])=I_R(x)$ is well defined and unique. The theorem is almost a
universal-property lemma once $\pi_R$ is admitted; its scientific content is
the explicit refusal to treat that naturality premise as a law of nature.

## 7. Measurability audit

For finite-dimensional states or fixed-slot combs, a finite independently
chosen tester basis maps a representative to a finite vector of probabilities.
If each reader probability is measurable in the boundary datum, this profile
map is measurable into a Euclidean space and its kernel is a smooth
equivalence relation. The decoder and quotient projection can then be chosen
measurably. The standard-Borel fiber product remains standard Borel for every
finite slot count.

Without this measurable-decoder hypothesis, a quotient of a standard-Borel
space by an arbitrary equivalence relation need not itself be standard Borel,
and the set-theoretic map $x\mapsto[x]$ need not be a measurable morphism of
the claimed kind. Accordingly:

- Theorems 1--2 are valid categorically on the declared small reachable
  category.
- Theorems 3--4 are valid as measurable representation statements for
  standard-Borel/measurably decoded packets, including the intended quantum
  representations.
- No universal claim over arbitrary nonsmooth measurable quotients is earned.

This is a scope boundary, not a counterexample in the printed physical class.

## 8. Mandatory Seat-M fresh attacks

| Attack | Exact reconstruction | Disposition |
|---|---|---|
| M1 equal immediate scalars, different types | Let terminal states of types `A` and `B` both give scalar 1 under their discard maps. There is no typed context comparing them and $\sim_R$ is defined separately in $B_R(A)$ and $B_R(B)$. | **KILLED** |
| M2 adaptive ancillary separator | Identity and `Z` conjugation both have immediate deterministic effect `I`. On $|+\rangle$, append an ancilla, coherently copy an `X`-basis outcome to it, and adapt the final reader to that record. The outcome is deterministic and opposite. Complete profiles separate the channels. | **KILLED** |
| M3 unreachable native state | Adjoin a typed state $u$ that no $J_R(q)$ or admitted prefix reaches. No inverse value is forced on $u$; Theorem 2 explicitly quotients only the reachable image. | **KILLED BY SCOPE** |
| M4 mutually singular conditional fiber measures | For two future-idle preparation tags use $\nu_0=$ Lebesgue measure and $\nu_1=$ Cantor measure on $[0,1]$, carried unchanged. They are mutually singular, their mixtures remain affine, and full marginalization returns the same registered law. | **KILLED** when the tags are unregistered and the kernels are declared measurably |
| M5 preparation label retained by reader | If an admitted reader returns the implementation label, the two preparations have different complete profiles. Their latent coordinate is not in one operational fiber and the forgetting projection is not an adequate reduction for that enlarged domain. | **KILLED** |
| M6 terminal-preserving but nonmonoidal reduction | Take two hidden bits with uniform local marginals but perfect joint parity. A map replacing the joint law by the product marginals preserves each local terminal statistic and changes a joint parity reader. It is not a representation morphism because it breaks tensor/joint pushforward. | **KILLED** |
| M7 zigzag only | Two packets may have only $R\to R_{\rm op}\leftarrow R'$ and no map $R\to R'$. This cospan is a length-two zigzag of reductions, not an equivalence or microscopic isomorphism. The candidate's conclusion uses only the common quotient. | **KILLED**, with terminology correction noted below |
| M8 gauge-invariant but not reduction-natural invariant | Fiber cardinality, fiber entropy relative to a chosen measure, and latent path correlation are invariant under bijective relabelling but change under $\pi_Z$. Theorem 4 correctly excludes them unless an independent principle rejects forgetting. | **KILLED** |
| M9 inflate a minimal dilation | A channel of Choi rank $r$ has minimal Stinespring environment dimension $r$. Appending an idle $m$-point fiber yields realized size at least $rm$ while the decoded minimum remains $r$. | **KILLED** |
| M10 terminal lookup as process memory | A table fitted to a finite reader list has no associative adaptive/tensor wiring and fails a held-out continuation. A table containing the entire continuation functional is a declared predictive object, not a finite composable microscopic memory minimum. | **KILLED** |

## 9. Source theorems versus Paper 02 bridges

The external theorems used in the resource section are narrower than the
candidate's quotient theorem:

- [Kuramochi's primary paper](https://arxiv.org/abs/1701.03394) defines
  statistical experiments as common-parameter families of normal states and
  proves minimal sufficiency up to normal isomorphism under CP/Schwarz
  coarse-graining. It does not select hidden ontology.
- [Buscemi's primary paper](https://arxiv.org/abs/1004.3794) compares
  finite-dimensional quantum statistical models through CPTP
  coarse-grainings/statistical morphisms and decision problems. Its
  sufficiency order is task- and parameter-family-relative.
- [McKague's primary paper](https://arxiv.org/abs/1109.0795) establishes
  real simulation of complex quantum computation using one added real qubit.
  It does not prove that the ordinary tensor product of independently
  realified systems is identical to the complex tensor product.
- [Gogioso and Scandolo](https://arxiv.org/abs/1701.08075) supply a
  categorical probabilistic framework, not the present quotient or ontology
  no-selection result.

Paper 02's bridge is proved internally: complete operational testers define
the congruence; adequate decoding identifies its quotient; explicit
inflations/projections establish nonidentifiability; and representation
naturality forces factorization. No cited source supplies or selects the
ontology conclusion.

## 10. Candidate-claim table

| Claim | Seat-M determination |
|---:|---|
| 1. complete-profile congruence | **PASS** for all admitted typed wiring |
| 2. reachable quotient naturally isomorphic to `Q` image | **PASS ON IMAGE**; no global inverse |
| 3. finite/countable/Borel fiber inflations | **PASS** for coherent measurable causal kernel families |
| 4. natural invariants factor through quotient | **PASS CONDITIONALLY** on naturality under the explicitly admitted reductions |
| 5. gauge/redundancy/hidden/physical taxonomy | **PASS**; noninvertible forgetting is not gauge |
| 6. phase-complete predictive states | **PASS** by separating testers |
| 7. exact realification and cost | algebraically **PASS**; scalar ontology remains nonunique |
| 8. positive contextual records survive no-gos | **PASS AT PREMISE-LEDGER SCOPE** |
| 9. resource invariants are class-relative | **PASS**; no universal microscopic size follows |
| 10. records descend; microtrajectory absent | **PASS** |
| 11. Barandes-style ontology represented but unselected | **PASS AS A BOUNDARY**, not reconstruction/refutation |
| 12. no discriminator in registered interface | **PASS BY EXACT EQUIVALENCE**, conditional on frozen interface |
| 13. rung-6 ceiling | **PASS** in this lens |

## 11. Registered controls C1--C18

| Control | Seat-M disposition |
|---|---|
| C1 Paper 01 record representation | **PASS**: decoder returns the accepted operational process, not dilation labels. |
| C2 hidden bit | **PASS**: product with a normalized two-point law doubles fibers and projects exactly. |
| C3 hidden continuum | **PASS**: Lebesgue/Cantor controls are singular and have identical inherited profiles. |
| C4 latent dynamics mutation | **PASS**: hold and prefix-controlled flip differ microscopically; normalized path integration removes both. |
| C5 Kraus rotation | **PASS** at unrecorded-label scope; a fine reader would change the instrument. |
| C6 minimal/padded Stinespring | **PASS**; decoded minimum and realized size are separated. |
| C7 equal density/different preparations | algebraically **PASS**; preparation labels must be unregistered for fiber equivalence. |
| C8 equal immediate effect/different channel | **PASS**, M2. |
| C9 Peres--Mermin | **PASS algebraically** with its sharp-product premises retained. |
| C10 CHSH | **PASS algebraically** under measurement independence and factorization. |
| C11 phase circle | **PASS**; complete tester state is not a diagonal vector. |
| C12 real/complex | **PASS WITH COMPOSITION SCOPE**; shared `J` and tensor mismatch are explicit. |
| C13 process memory | **PASS**; quotient state is the complete future comb, not a reduced snapshot. |
| C14 reader removal | **PASS**; the independently frozen physical tester family defines the domain. |
| C15 program-order permutation | **PASS**; no chronology inferred. |
| C16 actual record/no microtrajectory | **PASS**; fiber inflation supplies inequivalent completions. |
| C17 readable fiber | **PASS**; it refines the experiment domain and old quotient. |
| C18 simplicity selector | **PASS**; no coordinate-dependent description length is physicalized. |

## 12. Hostile attacks 1--42

| No. | Attack | Seat-M disposition |
|---:|---|---|
| 1 | one terminal reader | killed by the all-continuation profile |
| 2 | omit ancillary continuations | killed; ancillary tests are explicit and essential |
| 3 | post-selected tomography | killed; tester family is fixed independently |
| 4 | injectivity called equivalence | killed on image by fullness and essential surjectivity |
| 5 | omit tensor/adaptive wiring | killed by congruence proof and adequacy contract |
| 6 | merge nonisomorphic types | killed by typed equivalence |
| 7 | reader-dependent quotient | killed by frozen tester domain |
| 8 | on-image inverse called global | accepted as a boundary and printed explicitly |
| 9 | every idle variable called gauge | killed by five-way taxonomy |
| 10 | every idle variable called physical | no selection without discriminator; possibility remains open |
| 11 | uniform fiber without base measure | rejected |
| 12 | coordinate-dependent maximum entropy | rejected |
| 13 | correlated preparation datum deleted as gauge | rejected; projection is many-to-one |
| 14 | future setting in latent state | rejected by causal-prefix kernel condition |
| 15 | default law for absent variable | rejected; every `Z` and kernel is introduced explicitly |
| 16 | lookup-sized hidden memory | rejected by uniform compositional contract; see M10 |
| 17 | diagonal-only state | killed by common future separator |
| 18 | hidden real complex-structure carrier | exposed as `J` and composition cost |
| 19 | mismatch real/complex source assumptions | explicitly separated |
| 20 | local tomography assumed observed | retained as an extra reconstruction premise |
| 21 | complex numbers inferred fundamental | not claimed |
| 22 | real coordinates eliminate phase structure | rejected; `J` or equivalent constraint survives |
| 23 | Wigner theorem beyond scope | not used |
| 24 | reconstruction inputs counted derived | rejected |
| 25 | positive records imply noncontextuality | rejected |
| 26 | no-signalling implies Bell locality | rejected |
| 27 | context hidden in evaluator | adequate packet types every retained procedure field |
| 28 | Stinespring minimum becomes ontic size | rejected by M9 |
| 29 | Markov lower bound applied non-Markovianly | rejected; class qualifier retained |
| 30 | complexity selects ontology | rejected |
| 31 | finite precision merges exact states | rejected; relation is exact |
| 32 | one process-memory realization unique | rejected; only class-relative minimum claimed |
| 33 | actual record becomes microtrajectory | rejected |
| 34 | normalization becomes actualization | rejected |
| 35 | decoherence becomes selection | rejected |
| 36 | program slot becomes time | rejected |
| 37 | tensor factor becomes space | rejected |
| 38 | hidden order prepares successor | none introduced |
| 39 | discrete fiber becomes spacetime | none promoted |
| 40 | equivalence becomes evidence for ISP | expressly rejected |
| 41 | underdetermination makes all ontologies equal | expressly rejected |
| 42 | post-freeze physical postulate | none found |

## 13. Quantifier and resource ledger

| Axis | Surviving scope |
|---|---|
| representations | every adequate packet in the declared small schema; measurable statements require measurable decoder/profile maps |
| systems | finite-dimensional quantum ports |
| slots | each fixed finite count |
| causal class | definite supplied laboratory order |
| outcomes | finite explicitly; standard-Borel under countable additivity and measurable policies |
| quotient | exact, typed, reachable operational image only |
| testers | every compatible continuation; finite tomography may witness separation after independent freeze |
| fiber spaces | any fixed finite, countable, or standard-Borel `Z` |
| fiber dynamics | measurable causal-prefix kernels coherent under program restriction and tensor products |
| factorization | invariants natural under the explicitly admitted isomorphisms, refinements, and reductions |
| resource minima | fixed decoded channel/task/cut/Markov/tensor class only |
| memory | complete predictive profile may be non-Markovian; no universal finite microscopic bound |
| scalar result | phase-complete predictive structure; scalar ontology unselected |
| kind | mathematical and operational; no empirical ontology selection |
| order | external laboratory type, never emergent time |
| enlarged domain | a calibrated fiber reader refines the quotient and invalidates the old reduction |

## 14. Full 17-coordinate product

```text
contract       P02-ADEQUATE-REPRESENTATION-CLASS-CONSTRUCTED
               + SCOPE: SMALL TYPED SCHEMA; MEASURABLE DECODERS WHERE USED
quotient       P02-OPERATIONAL-QUOTIENT-CANONICAL
               + SCOPE: REACHABLE OPERATIONAL IMAGE ONLY
naturality     P02-QUOTIENT-NATURALITY-CONSTRUCTED
               + SCOPE: DECLARED COMPLETE CONTEXT AND ADMITTED MORPHISMS
fibers         P02-ONTOLOGY-FIBERS-CLASSIFIED
selection      P02-OPERATIONAL-NOSELECTION-THEOREM
               + PREMISE: NATURALITY UNDER REGISTERED FIBER REDUCTIONS
phase          P02-PHASE-COMPLETE-PREDICTIVE-STATE-FORCED
scalar         P02-COMPLEX-SCALAR-ONTOLOGY-REPRESENTATION-NONUNIQUE
positivity     P02-POSITIVE-RECORD-LAWS-SURVIVE
context        P02-NONCONTEXTUAL-MICROONTOLOGY-NOGO-WITH-
               AFFINITY-PERFECT-DISTINGUISHABILITY-SHARP-PRODUCT-PREMISES
bell           P02-BELL-LOCAL-COMPLETION-UNCONSTRUCTED
memory         P02-RESOURCE-INVARIANTS-CLASSIFIED
               + SCOPE: FIXED CHANNEL/TASK/CUT/MARKOV/TENSOR CLASSES
gauge          P02-GAUGE-REDUNDANCY-PHYSICAL-DIFFERENCE-CLASSIFIED
record         P02-OPERATIONAL-RECORD-INVARIANT
actuality      P02-RECORD-ACTUALITY-POSTULATED
               + MICROACTUALITY-UNCONSTRUCTED
barandes       P02-BARANDES-ONTOLOGY-UNSELECTED
discriminator  P02-EXTRA-ONTOLOGY-DISCRIMINATOR-NONE-IN-DOMAIN
ontology       P02-ONTOLOGY-UNDERDETERMINED
overall ceiling
               P02-CANONICAL-QUOTIENT-WITH-UNSELECTED-ONTOLOGY-FIBERS
```

## 15. Bounded corrections and clarifications

1. Section 3.3 calls $R\to\mathcal Q\leftarrow R'$ a “span.” With the arrows
   as printed it is a **cospan**; viewed without orientation it is a two-edge
   zigzag. No theorem depends on the nomenclature.
2. The CHSH display in Section 8.1 contains a comma after
   `$\mu(d\lambda)$`; it should be ordinary multiplication. The following
   derivation uses the intended integral and is unchanged.
3. The arbitrary-program kernel notation $\nu_P,L_{P,k}$ should always carry
   the already stated restriction/coherence condition: two programs sharing a
   physical prefix use the same prefix kernels. Otherwise a subscript `P`
   could hide future-program dependence. The constructed controls satisfy
   this condition.
4. “Record-only” $R_{\rm op}$ means operational predictive class **plus**
   setting/outcome records. A bare record string without the phase-complete
   predictive object would not be adequate.

These changes affect no definition, theorem, product row, or scope when the
surviving quantifier ledger is retained.

## 16. Verdict and implementation wall

**ACCEPT-WITH-SCOPE.** The typed congruence, reachable-image quotient,
explicit fiber freedom, conditional factorization/no-selection theorem, and
restricted resource classification reconstruct. No hidden selector or global
microscopic inverse was found. The measurable-decoder and coherent-kernel
conditions above must remain attached to the standard-Borel and
representation-morphism statements.

Implementation cannot change this semantic verdict. Code could only conform
to frozen finite examples; it could not make a nonsmooth quotient measurable,
turn a cospan into an ontic equivalence, or select a latent fiber.

This report is intentionally left unstaged and uncommitted on handoff.
