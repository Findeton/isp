# Paper 22 v2 independent delta review — Seat C

Date: 2026-08-21

Status: **FROZEN INDEPENDENT REPORT**

Verdict: **REVISE**

## 1. Authority, authentication, and blindness

The reviewed repository state was HEAD `42d815a`.  I authenticated every
scientific input before inspection and read the complete bound corpus.  The
ordinary SHA-256 values were:

| object | path | authenticated SHA-256 |
|---|---|---|
| v2 delta-review protocol | `v16/note-paper22-reversible-structural-instrument-v2-review-protocol.md` | `88a2609988628e8e9fe1ad2c96a0b65a9cf230a2750feab2207bca5ebfcfd30e` |
| terminal Paper 13D law | `v16/paper-13d-typed-executable-gamma.md` | `3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9` |
| predecessor adjudication | `v16/note-paper22-reversible-structural-instrument-adjudication.md` | `c261520aa142bf07a489f87cd0364628f094794c7523c03d8ba3dde05d824a07` |
| Paper 22 v2 pin | `v16/note-paper22-reversible-structural-instrument-v2-pin.md` | `a4c1c2ecd10edad73ed64b12f699c09d7cfd169d4cd264939990589554693627` |
| Paper 22 v2 candidate | `v16/paper-22-reversible-structural-instrument-v2.md` | `30340295ccd5f8371a9020cb76c0a93cc24ab14cbbf78f05c01a85ca5ce86468` |
| v2 construction note | `v16/note-paper22-reversible-structural-instrument-v2-construction.md` | `e90bdd14ca04742bb09eb3c9ec928b4aea04ff6429b0896158ce83170280a0ae` |

The v2 pin and candidate were reauthenticated immediately before this report
was written and again at final freeze.  Their bytes did not move.

I did not inspect or contact a sibling report, the old candidate outside the
binding adjudication, the frontier census, the semantic input audit, a Paper
23 file, or a private regional investigation.

## 2. Verdict and first decisive semantic counterexample

```text
REVISE
```

The homogeneous-source replacement repairs the predecessor's source,
functor, degenerate-restriction, and composition defects.  The first decisive
failure is instead an unauthorized change and underdefinition in the
supposedly immutable reversible-query seed purification.

Paper 13D fixes, for each new unordered cross pair, an independent uniform
seed

\[
 v_p\in[25],\qquad \Pr(v_p=k)=\frac1{25}.
\]

The bound predecessor adjudication expressly retains **uniform seed
purification**, and the v2 pin says that v2 changes only source/functor
domains and introduces no seed bias.  The corresponding one-pair pure state
is

\[
 |\Omega\rangle_p=\frac15\sum_{k=0}^{24}|k\rangle_p.
\tag{C.1}
\]

V2 Section 5.1 instead replaces that carrier and state by

\[
 |\sigma\rangle_p=\frac35|0\rangle_p+\frac45|1\rangle_p,
\tag{C.2}
\]

whose basis probabilities are `9/25` and `16/25`.  Equation (C.2) is not the
uniform `[25]` purification (C.1), has a different typed carrier, and is not a
source/functor-domain edit.  A complete open-query reader can distinguish the
two apparatuses.

There is a possible repair: the two qubit basis vectors could be declared to
represent the normalized uniform subspaces of the nine and sixteen original
seed values, with a source-controlled bond convention and an explicit
complementary isometry.  The candidate does not define that embedding,
complement, or even the deterministic bond rule inside the symbol
`w_F(X,z)`.  For equal endpoint colors the accepted rule is

\[
 \ell_p=1\iff v_p<9,
\]

while for unequal colors it is

\[
 \ell_p=1\iff v_p<16.
\]

A naked two-valued `z` does not specify both cases without an explicit
source-controlled interpretation.  Thus the v2 query is neither the frozen
uniform-seed query nor a completely defined authorized replacement.  This
fails the immutable-core condition and demotes the fiberwise-query
coordinate.  It is repairable without changing a child kernel, so the verdict
is `REVISE`, not wholesale `REJECT`.

A second exact defect appears in the partial-coherence statement.  For a
generally complex environment overlap `v`, the interference parameter is

\[
 q_\phi=\operatorname{Re}(v e^{i\phi}),
\tag{C.3}
\]

not `(Re v) cos(phi)` or an unqualified multiplication by `Re v`.  V2 states
only that `Re v` multiplies the interference term.  With `v=i` and
`phi=pi/2`, (C.3) equals `-1`, whereas the printed rule gives zero.  The full
pinned visibility family is therefore not reconstructed as written.

## 3. Independent source/category reconstruction

### 3.1 Source groupoid

Let `Sort_13D` be the finite set of exact atomic Paper 13D boundary tags,
including stage and record qualifiers.  For each sort `s`, an object of

\[
 \mathsf{Src}^{\ge2}_s
\]

is an unordered finite active component family with at least two nonempty,
pairwise-disjoint occurrence sets, all carrying complete values in
`B_s(I_alpha)`, together with an unordered spectator family of separately
typed complete Paper 13D values.  The active/spectator mark belongs to the
experiment frame.  It is transported, not decoded.

An arrow is a component transport plus accepted occurrence presentation
isomorphisms and local port-frame swaps preserving `s`, the mark, all fields,
and unordered incidence.  Every arrow is invertible.  The positive source is

\[
 \mathsf{Src}^{\ge2}_{\rm hom}
 =\coprod_{s\in\mathsf{Sort}_{13D}}\mathsf{Src}^{\ge2}_s.
\]

There are no arrows between coproduct summands.  No order, child, result,
probability, dimension, or geometry field is present.  This is a complete
point-free source referent for the triggered local scope.

### 3.2 Child experiment functors

For `X` in the `s` summand, let `underline X` be the formal tensor of active
and spectator values.  The tensor experiment is the identity history on that
formal tensor, with target retaining every component tag.  The fusion
experiment is

\[
 \Phi_s^{\{I_\alpha\}_{\alpha\in A}}\boxtimes\operatorname{id}_E,
\]

with atomic active target `B_s(disjoint-union I_alpha)` and spectator tensor
factors.  This is exactly one simultaneous Paper 13D generator.  At a
bond-carrying sort its output is a conditional stochastic history kernel, not
a deterministic point map.

All admitted active components have the required common sort, so both child
experiments have a typed source, arrow, target, history fiber, and normalized
conditional kernel.  Tensor and fusion remain predictively distinct because
one target retains the active partition and the other is an atomic target on
the union; a realized all-zero bond field does not erase that type
distinction.

### 3.3 Naturality squares

For a source isomorphism `g:X->X'` in one sort summand, inherited Paper 13D
covariance supplies

\[
 \mathcal T_s(g)\,\operatorname{id}_{\underline X}
 =\operatorname{id}_{\underline X'}\,\underline g
\]

and

\[
 \mathcal F_s(g)
 (\Phi_s^A\boxtimes\operatorname{id}_E)
 =
 (\Phi_s^{A'}\boxtimes\operatorname{id}_{E'})\,\underline g.
\]

The induced permutation of cross-pair addresses transports any product seed
state.  Witness transport intertwines `Q_{m,X}` and `Q_{m,X'}`; the fused
subspace projector is conjugated to the fused projector at `X'`; therefore
the inverse-query square follows.  Physical history orbits, complete readers,
and accepted futures transport by Paper 13D covariance.  Source-indexed
exhaust labels transform as

\[
 c_{[X],m,[H]}\longmapsto c_{[X'],m,[gH]},
\]

which yields the commit square.  A purported sort-changing map has no square:
it is not a source arrow.

These naturality statements pass for the candidate's printed product qubit
state as abstract mathematics, but that does not cure its failure to preserve
the frozen seed purification.

### 3.4 Restriction

If covariant restriction leaves at least two nonempty active components, the
source remains in the same sort summand.  Paper 13D restriction commutes with
formal tensor and simultaneous fusion, and marginalization of deleted factors
in either the correct uniform seed product or the candidate's qubit product
leaves the retained product state.  The accessible conditional kernels and
readers therefore commute with positive restriction.

If zero or one active component remains, there is no new positive source.
The already realized branch restricts to

\[
 (m_R,\operatorname{res}_J\mathsf Y_{m,s,X},
       \operatorname{res}_JH).
\]

The tensor target is respectively a formal unit or formal one-factor tensor;
the fusion target is the corresponding empty or one-occurrence atomic
boundary.  They remain different typed objects.  The stable mode record is
retained, and no new opportunity or `C_phi` law is assigned.  This repairs the
predecessor's false target conflation.

At the accessible stochastic-instrument level, positive restriction is
natural.  The chosen Stinespring exhaust is not itself shown to admit a
bijective restriction map: several full histories can restrict to one
history.  That is harmless after the exhaust is traced, but the strongest
claim should remain naturality of the accessible commit kernel, not of a
globally reversible restriction on exhaust vectors.

### 3.5 Composition

For disjoint source objects, external tensoring is the bifunctorial product
of two already typed instruments, including separate marks, modes, records,
and exhausts.  Symmetric braiding transports each whole factor and proves
formal order independence.

This does not create one source object with two internal marks.  No
same-source multi-mark commuting square is defined.  Likewise, the candidate
uses one simultaneous n-ary fusion; a staged binary word retains additional
traversed boundaries and is a different Paper 13D history.  No fusion algebra
is obtained.

## 4. Four source discriminators

| discriminator | result | reason |
|---|---|---|
| homogeneous positive pair | **ADMITTED** | Two complete nonempty `B_1^0` components lie in `Src_{B_1^0}^{>=2}`. |
| exact `(B_1^0,B_2^0)` heterogeneous pair | **REFUSED** | No common active-sort summand exists; refusal occurs before any child, query, commit, or probability. |
| sort-changing purported arrow | **ABSENT** | Source hom-sets are internal to one coproduct summand. |
| differently sorted spectator | **ADMITTED** | Spectator sorts are independent tensor-factor tags and do not change the active summand. |

The heterogeneous predecessor counterexample is therefore genuinely killed
at source membership rather than assigned zero probability.

## 5. C1–C6 dispositions

| duty | disposition | finding |
|---|---|---|
| C1 — source referent | **PASS** | The coproduct is unordered, source-side, marked, and free of downstream or geometry data. |
| C2 — membership and refusal | **PASS** | All four required discriminators have the correct pre-evaluation result. |
| C3 — child totality | **PASS** | Every admitted active family has one Paper 13D sort; tensor identity and one simultaneous stochastic fusion are completely typed. |
| C4 — naturality | **PASS for the printed maps, immutable-fidelity FAIL for the seed** | Child, witness, projector, inverse, commit, reader, future, and exhaust squares commute under allowed isomorphisms. The replacement seed state is natural but is not the frozen seed purification. |
| C5 — restriction | **PASS at accessible branch/kernel scope** | Positive restriction and branchwise zero/one restriction are typed; records remain and no new opportunity is forged. |
| C6 — composition | **PASS with the pinned negative walls** | External tensor is natural; same-source multi-mark composition and a fusion algebra remain unconstructed. |

## 6. Mandatory predecessor regressions

| predecessor regression | disposition |
|---|---|
| heterogeneous active-sort source | **KILLED** by coproduct membership |
| sort-changing source morphism | **KILLED** by empty cross-summand hom-set |
| zero/one-active target conflation | **KILLED** by branchwise dependent restriction with distinct target types |
| same-source multi-mark closure inferred from disjoint tensoring | **KILLED**; only external tensor is claimed |
| staged fusion identified with simultaneous fusion | **KILLED**; histories retain different traversed boundaries |

## 7. Immutable numerical and local-law controls

The following anchors reproduce correctly:

- `R` is orthogonal; its squared entry moduli equal `B`.
- `C_phi` has the printed diagonal and off-diagonal entries and normalized
  columns.
- `C_0`, `C_{pi/2}=B^2`, and `C_pi=I` are exact.
- Neutral tensor-input odds are `49/625` and `576/625`.
- `K_phi=C_phi B^{-1}` is the printed matrix and is nonnegative exactly for
  `-7/32 <= cos(phi) <= 7/18`.
- Equation (17) normalizes and supported mode conditioning cancels `C_phi`,
  leaving the accepted child kernel.

Two bound controls do not reproduce completely:

1. the uniform `[25]` seed purification is replaced by (C.2); and
2. the general partial-coherence law omits the phase of the environment
   overlap, as demonstrated by `v=i`, `phi=pi/2`.

No value of `B`, `R`, `C_phi`, the neutral odds, or an accessible child kernel
was otherwise changed.

## 8. All twenty-two hostile controls

| no. | hostile control | disposition |
|---:|---|---|
| 1 | heterogeneous `B_1^0/B_2^0` active pair | **PASS:** refused by source membership before fusion |
| 2 | sort-changing source morphism | **PASS:** absent from all hom-sets |
| 3 | empty active family as positive source | **PASS:** cardinality predicate refuses it |
| 4 | one-active family as positive source | **PASS:** cardinality predicate refuses it |
| 5 | tensor unit identified with empty atomic boundary | **PASS:** distinct types retained |
| 6 | one-factor tensor identified with atomic factor | **PASS:** no alignment is asserted |
| 7 | restriction forges a new mode opportunity | **PASS:** only an inherited realized branch is pushed forward |
| 8 | restriction silently drops the stable record | **PASS:** `m_R` is retained in `Res_J` |
| 9 | same-source two-mark commutation without a source type | **PASS:** explicitly unconstructed |
| 10 | staged binary fusion substituted for simultaneous fusion | **PASS:** trace types remain distinct |
| 11 | different sources share an unindexed exhaust | **PASS:** exhaust includes `[X]` |
| 12 | source odds inferred from exhaust orthogonality | **PASS:** no external coefficients are supplied |
| 13 | spectator identity changes `C_phi` | **PASS:** spectator is identity-carried and the mode law is source independent |
| 14 | route-dependent seed/witness/complement/environment residue | **PASS for the declared ideal query:** exact inverse restores the common pre-query state; seed-fidelity failure is separate |
| 15 | reversible query renamed accessible erasing fusion | **PASS:** no-hiding and query/commit types separate them |
| 16 | accessible dormant unchosen child | **PASS:** accessible output is a dependent coproduct |
| 17 | naked mode-label swap | **PASS:** only transport with all controlled operations is gauge |
| 18 | decoder changed at fixed instrument | **PASS:** that is a different instrument |
| 19 | phase selected after a downstream result | **PASS:** outside the fixed-input experiment |
| 20 | mutation of `B`, `R`, `C_phi`, neutral odds, or child kernel | **PASS for the values named by this control:** all are unchanged; the separate seed-purification mutation still violates the immutable architecture |
| 21 | activity/root odds inferred from local odds | **PASS:** arbitrary external source propensities give the same fiber law |
| 22 | chronology/dimension/metric/curvature/gravity/actuality inferred | **PASS:** absent and expressly unconstructed |

## 9. Fresh attacks

### C-F1 — equal-looking values at distinct atomic stage sorts

Choose two complete nonempty values whose serialized visible bits happen to
match but whose boundary tags are `B_1^0` and `B_2^0`.  Equality of displayed
bits does not erase stage fields or invariants.  As an active pair they lie in
no common summand.

**Result: pass; refused before evaluation.**

### C-F2 — spectator presentation-isomorphic to an active component

Add a spectator with the same atomic sort, occurrence cardinality, and field
values as one active component.  A component permutation that transports the
active mark merely changes presentation; a permutation that leaves the mark
fixed while exchanging their physical roles is not a source arrow.

**Result: pass; spectator identity cannot alter the active orbit or mode
law.**

### C-F3 — remove an entire active component orbit

With three active components, let one component form a covariantly identified
orbit and delete all its occurrences.  Two components remain, so the result
stays in the positive groupoid and the deleted cross-pair seed factors
marginalize to one.  If a symmetric orbit contains all active components,
deleting the whole orbit instead lands in the zero-active branchwise target
with `m_R` retained.

**Result: pass in both positive and degenerate cases.**

### C-F4 — attempted active/spectator braiding

Apply the external symmetric braiding to printed component positions.  If
the mark is transported, the same physical active component remains active.
If the mark is not transported, the proposed map violates Definition 2 and
is absent.

**Result: pass; braiding cannot exchange typed roles silently.**

### C-F5 — biased-qubit seed substituted for the uniform `[25]` seed

On a homogeneous bond-carrying source with one cross pair, compare complete
open-query seed readers for (C.1) and (C.2).  One has 25 equiprobable basis
outcomes; the other has two outcomes with probabilities `9/25` and `16/25`.
No declared source-groupoid transport relates those carriers.

**Result: decisive failure.**

### C-F6 — imaginary residual-environment overlap

Take normalized residual route states with overlap `v=i` and set
`phi=pi/2`.  The correct cross term is `Re(i*i)=-1`, not `Re(i)=0`.

**Result: failure of the printed general partial-visibility statement.**

### C-F7 — two source fibers with one accessible child

Let distinct classical source partitions and seeds reach the same accessible
fused history.  Their commit outputs remain orthogonal because the exhaust
labels include `[X]`, even when `m` and `[H]` agree.  Tracing the exhaust
leaves the correct fiberwise child in each case and supplies no source odds.

**Result: pass; source-indexing repairs the predecessor wall.**

### C-F8 — nontrivial active-component automorphism

Take identical homogeneous active components with a component-swap
automorphism.  It permutes pair addresses, fixes the product seed state,
transports the simultaneous fusion experiment, and preserves full physical
history-orbit mass.  `C_phi` is unchanged.

**Result: pass; automorphism count does not change route odds.**

### C-F9 — undefined heterogeneous child assigned zero probability

Attempt to extend equation (17) to the old heterogeneous active pair by
setting its fusion mode weight to zero.  The attempt fails before the
equation is formed because no source object, fusion target, or `Gamma_F`
exists.

**Result: pass; no zero-probability rescue is admitted.**

## 10. Full product vector

Each coordinate is decided independently:

```text
P22V2-HOMOGENEOUS-SOURCE-GROUPOID:
  CONSTRUCTED

P22V2-TOTAL-TENSOR-FUSION-CHILD-PAIR:
  CONSTRUCTED

P22V2-FIBERWISE-REVERSIBLE-QUERY:
  UNCONSTRUCTED
  (the printed query changes and underdefines the bound seed purification)

P22V2-FIBERWISE-COMMIT-INSTRUMENT:
  CONSTRUCTED

P22V2-EXACT-LOCAL-MODE-LAW:
  UNCONSTRUCTED
  (C_phi, B^2, and K_phi are exact; the claimed general visibility law is not)

P22V2-POSITIVE-RESTRICTION-NATURALITY:
  CONSTRUCTED
  (accessible child/instrument-kernel scope)

P22V2-DEGENERATE-BRANCHWISE-RESTRICTION:
  CONSTRUCTED

P22V2-EXTERNAL-TENSOR-COMPOSITION:
  CONSTRUCTED

P22V2-SAME-SOURCE-MULTIMARK-COMPOSITION:
  UNCONSTRUCTED

P22V2-SIMULTANEOUS-FUSION-ALGEBRA:
  UNCONSTRUCTED

P22V2-ACTIVITY-ROOT-LAW:
  UNCONSTRUCTED

P22V2-PHYSICAL-REGIONAL-REFERENT:
  UNCONSTRUCTED

P22V2-CHRONOLOGY-DIMENSION-METRIC-GR:
  UNCONSTRUCTED

P22V2-ACTUALIZATION:
  UNCONSTRUCTED
```

## 11. Strongest honest scope and required revision

The strongest result supported now is:

> Paper 22 v2 constructs the homogeneous point-free source groupoid, total
> tensor/simultaneous-fusion child pair, source-indexed dependent commit,
> positive and degenerate branchwise restriction laws, and external tensor
> composition for a triggered local instrument.  It correctly refuses the
> predecessor's heterogeneous source before child evaluation and retains all
> negative global walls.  Its reversible-query and full partial-coherence
> coordinates require correction before the entire local instrument can be
> accepted.

The smallest adequate revision is:

1. restore the uniform `[25]` cross-pair seed purification and the accepted
   color-dependent threshold computation in the query; or separately
   authorize and completely define a reversible coarse-bin dilation,
   including its unused complement and naturality;
2. replace the partial-overlap sentence with
   `q_phi=Re(v exp(i phi))` and reproduce the corresponding visibility law;
3. state positive restriction naturality at the accessible CP/kernel level,
   unless a many-to-one exhaust restriction channel is separately defined;
   and
4. keep every repaired source, degenerate-target, external-tensor,
   same-source-multimark, and staged-fusion boundary exactly as printed.

No retuning of `B`, `R`, `C_phi`, `B^2`, `K_phi`, the neutral odds, or a child
kernel is needed.

## 12. Permanent walls

Neither the surviving coordinates nor the proposed repair constructs:

- why a source exists or an active family is marked;
- a probability, amplitude, or root measure over source objects;
- an autonomous activity/opportunity law;
- a same-source multi-mark calculus;
- a fusion algebra or equality of staged and simultaneous fusion;
- a physical regional referent;
- a varying-history ensemble or operational chronology;
- dimension, Lorentzian signature, scale, metric, curvature, backreaction,
  gravity, continuum physics, or QFT; or
- actualization.

## 13. Process and freeze confirmation

I performed a mathematical review only.  I edited no corpus artifact,
inspected or ran no implementation, staged no file, and made no commit.  The
only workspace write made by this seat is this assigned report.

The ordinary whole-file SHA-256, LF line count, and byte count are computed
after the final write and returned in the panel handoff.  They are not
self-embedded; no normalized self-hash ceremony is used.
