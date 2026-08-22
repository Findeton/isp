# Paper 02 hostile review — Seat Q

## Quantum foundations, contextuality, and scalar structure

Date: 2026-08-22

Status: **INDEPENDENT BLIND REPORT — UNSTAGED AND UNCOMMITTED ON HANDOFF**

Verdict: **ACCEPT-WITH-SCOPE**

## 0. Independence and authentication

This is the sole Seat Q report required by the frozen Paper 02 hostile-review
protocol. I did not inspect or communicate with either forbidden sibling
report:

- `v17/review-paper02-mathematics-quotient.md`;
- `v17/review-paper02-ontology-barandes.md`.

I did not delegate, inspect code, or edit any bound artifact.

The authenticated worktree HEAD was
`5340b5c71b0f0cfdb7e424d5ac21f5cd3bbb1efc`. The protocol's construction
commit `bfaddd50a5006ea90933a5a6eb6f89e345a98315` exists, and every
scientific artifact is byte-identical between that commit and the reviewed
worktree. The sole pre-existing unrelated worktree item was the untracked
`v16/note-handoff-prompt-2026-08-22.md`.

| Artifact | Authenticated SHA-256 | Result |
|---|---|---|
| `v17/note-paper02-hostile-review-protocol.md` | `4c032bc72696bc17375fb7b05e07771301205e1f7990c3cf847925580c7da532` | exact |
| `v17/note-paper02-operational-quotient-ontology-residue-pin.md` | `e26b91b7126046d4b9c8f579fa6147f48922dc7fb711851b5a0fe3501a2c49cf` | exact |
| `v17/paper-02-operational-quotient-ontology-residue.md` | `55edf811b2d80a628cae1d871994383e0013ec58dd77b70d340eebb836c93eec` | exact |
| `v17/note-paper02-construction-audit.md` | `6d3b63dad6866c725ee8cc621e2d5792c1532683de295b6fec3c45b72283627c` | exact |
| `v17/note-paper01-hostile-review-adjudication.md` | `3320414cb8161da33fbce3b1b8d3838cd3989d315de792c24cf24c0c322c2bb1` | exact |
| `v17/paper-00-reality-first-programme.md` | `a9f8456763447eaa25a6a840e8f221f51d961ecd9c3ced649ae35a8616457cbe` | exact |

The candidate had 1,456 LF lines and 63,328 bytes. No bound byte changed
during this review.

## 1. Executive finding

The quantum-foundational core survives. Complete future profiles recover the
ordinary quantum operational state or process, rather than one preferred
coordinate representation. Equal diagonal probabilities do not remove phase;
exact realification removes complex coordinates only by retaining an
equivalent complex structure and paying a global composition/source cost.
The parity-oblivious, six-rotation, Peres--Mermin, and CHSH witnesses correctly
rule out stated conjunctions of noncontextuality or Bell locality while
leaving ordinary positive contextual record laws intact.

This result does not select an ontology. In particular:

1. scalar nonuniqueness is proved only among representations of the same
   encoded operational image; natural real quantum theory with unrestricted
   real tensor products and product-state-independent sources is a different
   comparator;
2. quasiprobability negativity is a statement about a fixed affine frame and
   noncontextual calculus, not a negative probability of an actual record;
3. resource minima are invariant only after their task, cut, tensor,
   Markovianity, and representation class are fixed; and
4. Peres--Mermin outcome determinism requires a bridge from preparation
   noncontextuality and perfect predictability, or else must remain an explicit
   premise.

The candidate explicitly prints the last premise but does not reconstruct the
bridge. The bridge is valid under the conjunction already assumed by Theorem
6 and is supplied in Section 5.3 below. This is a bounded proof/scope
qualification, not a counterexample to the contextuality theorem or the
overall ceiling.

First decisive semantic counterexample: **none**.

## 2. Primary-source scope audit

Only primary sources were used for inherited theorem scope.

| Primary source | Scope independently checked | Candidate bridge |
|---|---|---|
| [Spekkens, generalized contextuality](https://arxiv.org/abs/quant-ph/0406166) | operational equivalence defines preparation, measurement, and transformation noncontextuality; preparation noncontextuality can derive sharp outcome determinism | the six-rotation and sharp-measurement premise ledgers are candidate reconstructions |
| [Spekkens et al., parity-oblivious multiplexing](https://arxiv.org/abs/0805.1463) | a noncontextuality inequality bounds parity-oblivious multiplexing | the candidate derives the two-bit `3/4` bound pointwise |
| [McKague, real simulation](https://arxiv.org/abs/1109.0795) | complex circuits can be simulated over real Hilbert spaces with one extra global carrier | the candidate reconstructs the realification map and classifies its global cost |
| [Li et al., real-quantum network test](https://arxiv.org/abs/2111.15128) | the tested natural-real network uses independent-source/product constraints | the candidate refuses to generalize this to every real encoding |
| [Hoffreumon and Woods, operational independence](https://arxiv.org/abs/2603.19208) | a 2026 unrefereed preprint distinguishes product-state from operational source independence and claims finite-network/sequential equivalence under the latter | the candidate treats this as an adversarial comparator, not settled authority |
| [Ferrie and Emerson, frame negativity](https://arxiv.org/abs/0711.2658) | negativity is forced only under a fixed frame/noncontextual classical-calculus contract | the candidate correctly leaves positive contextual histories alive |
| [Bell, EPR locality obstruction](https://doi.org/10.1103/PhysicsPhysiqueFizika.1.195) | measurement-independent factorization gives the Bell bound | the candidate derives the CHSH form rather than importing “locality” by name |

## 3. Mandatory complete lineages

### 3.1 Operational profile to quotient

Let `x` be a reachable representative of a qubit boundary in an adequate
representation and let `rho=K_R(x)`. Its complete profile is

$$
\Phi_R(x):(C,o)\longmapsto \Pr_R(o\mid C,x).
$$

For every effect `E`, adequacy supplies a continuation-reader pair with

$$
\Pr_R(E\mid x)=\operatorname{tr}(\rho E).
$$

If `x sim_R y`, all effects give equal values. Since effects span the
Hermitian operator space, `K_R(x)=K_R(y)`. Conversely, equal decoded states
have equal probabilities under every represented continuation. Hence the
typed class `[x]_R` decodes to the operational density operator. The same
argument with complete comb testers recovers a process class. This is an
on-image operational quotient, not a microscopic inverse.

### 3.2 Fiber inflation and refusal of ontic selection

Starting with the representative `x`, adjoin a bit `z` with any normalized
law and let every inherited reader ignore it. The representatives `(x,0)`
and `(x,1)` have identical complete profiles and project to `x). A
representation-natural invariant required to commute with this projection
must satisfy

$$
I_{R\times Z}(x,z)=I_R(x),
$$

so it cannot select the bit. The inference is conditional on admitting the
forgetting morphism. It does not prove that a hidden bit cannot be contingent
reality.

### 3.3 Equal immediate data and phase-complete future

The states

$$
|+\rangle=\frac{|0\rangle+|1\rangle}{\sqrt2},
\qquad
|-\rangle=\frac{|0\rangle-|1\rangle}{\sqrt2}
$$

have identical `Z` diagonals. The same held-out Hadamard sends them to
`|0>` and `|1>`, so a common `Z` reader distinguishes them perfectly.
More generally,

$$
U_\phi=|0\rangle\langle0|+e^{i\phi}|1\rangle\langle1|,
\qquad
U_\phi U_\theta=U_{\phi+\theta},
$$

and an adequate representation must retain the full circle action. An
incomplete tester family can quotient away phase only by changing the
experiment domain.

### 3.4 Registered record to microscopic ambiguity

If two record values `r,r'` are distinguished by a calibrated future reader,
their complete profiles differ and they descend to distinct operational
classes in every adequate representation. Fiber inflation then gives many
microscopic representatives `(r,z)` over the same registered record.
Therefore record identity and its probabilities are invariant while one
complete microscopic trajectory remains unselected.

## 4. Exact realification reconstruction

For `M=A+iB`, define

$$
\mathfrak R(M)=
\begin{pmatrix}A&-B\\B&A\end{pmatrix},
\qquad
J=\begin{pmatrix}0&-I\\I&0\end{pmatrix}.
$$

Direct block multiplication gives

$$
\mathfrak R(MN)=\mathfrak R(M)\mathfrak R(N),
\qquad
\mathfrak R(M^\dagger)=\mathfrak R(M)^T,
\qquad
[\mathfrak R(M),J]=0.
$$

If `rho` is a density operator and `E` an effect, then

$$
\rho_R=\frac12\mathfrak R(\rho),
\qquad E_R=\mathfrak R(E)
$$

are real positive operators, `tr_R rho_R=1`, and

$$
\operatorname{tr}_R(\rho_RE_R)
=\frac12\operatorname{tr}_R\mathfrak R(\rho E)
=\operatorname{Re}\operatorname{tr}_C(\rho E)
=\operatorname{tr}_C(\rho E).
$$

The normalization and trace rule are exact. The scalar conclusion is not
“complex structure disappears.” It is “complex coordinates are replaceable
on the encoded image, while `J` or an equivalent phase-composition
constraint remains.”

For two systems,

$$
\dim_R\mathfrak R(H_A\otimes_C H_B)=2d_Ad_B
$$

but

$$
\dim_R(\mathfrak R(H_A)\otimes_R\mathfrak R(H_B))=4d_Ad_B.
$$

Thus independent local realification followed by the unrestricted ordinary
real tensor product is not the same functor. A faithful simulation must use
a shared complex-structure carrier, constrain the extra tensor sector, or
alter the composition rule. A network experiment can reject the natural-real
product-state model without rejecting every real encoding. Conversely, a
real model using nonproduct but operationally independent source states has
paid a global source-structure cost; it has not recovered product-state
independence for free.

## 5. Contextuality and Bell reconstructions

### 5.1 Parity-oblivious multiplexing

For uniformly distributed `x=(x1,x2)`, the four states have Bloch vectors

$$
\frac{(-1)^{x_1}X+(-1)^{x_2}Z}{\sqrt2}.
$$

The even and odd mixtures are both `I/2`. Under preparation
noncontextuality and affine mixing, at each ontic state of nonzero weight the
posterior probabilities `a,b,c,d` for `00,01,10,11` obey

$$
a+d=b+c=\frac12.
$$

The best conditional average success is

$$
s_\lambda=\frac12[
\max(a+b,c+d)+\max(a+c,b+d)].
$$

Writing `d=1/2-a`, `c=1/2-b` gives

$$
s_\lambda
=\frac12+\frac12(
|a+b-1/2|+|a-b|)
\leq\frac34.
$$

The quantum protocol succeeds with

$$
p_Q=\frac12\left(1+\frac1{\sqrt2}\right)>\frac34.
$$

If an implementation label leaks the parity to Bob, the operational
parity-oblivious premise is false; that is not a countermodel to the witness.

### 5.2 Six-rotation transformation witness

Let `mu_k` be the ontic output density after rotation `T_(k pi/3)` of a
fixed pure input in the `xz` plane. Opposite rotations yield orthogonal
states, so positive response functions for their perfect distinguishing
measurement imply disjoint supports:

$$
\mu_k(\lambda)\mu_{k+3}(\lambda)=0.
$$

Transformation noncontextuality and affinity transfer the five equal-channel
decompositions to one density `mu`. At any point where `mu>0`, put
`r_k=mu_k/mu`. Then

$$
r_0+r_3=r_1+r_4=r_2+r_5=2,
$$

and disjointness makes every pair `(2,0)` or `(0,2)`. But the two
three-rotation decompositions require

$$
r_0+r_2+r_4=3,
\qquad r_1+r_3+r_5=3.
$$

Each left side is even, a contradiction. A contextual model may assign
different kernels to the operationally equal average-channel procedures;
doing so drops transformation noncontextuality rather than positivity.

### 5.3 Peres--Mermin premises and the outcome-determinism bridge

The square's row products and first two column products are `+I`; the final
column product is `-I`. A deterministic context-independent value assignment
respecting functional products is impossible.

Outcome determinism is not implied by measurement noncontextuality alone. The
route available under Theorem 6's larger conjunction is:

1. for a rank-one PVM `{P_k}`, prepare each eigenstate `rho_k=P_k`;
2. perfect prediction and nonnegative normalized responses imply
   `xi_k=1` on the support of `mu_k` and zero on the supports of the other
   eigenpreparations;
3. the uniform mixture of every eigenbasis is `I/d`;
4. preparation noncontextuality assigns one distribution `mu_(I/d)` to all
   these mixtures, so the eigenpreparation supports cover the operationally
   relevant ontic space; and
5. each sharp response is therefore deterministic almost everywhere.

Coarse-graining extends the conclusion to higher-rank PVMs. The commuting
functional-product rule remains an additional compatibility premise. The
candidate names sharp outcome determinism and the product rule but omits
steps 1--5. Adjudication should bind this bridge or leave sharp determinism
explicit. Without preparation noncontextuality or sharp functional
composition, Peres--Mermin alone does not rule out a positive ontological
model.

### 5.4 CHSH premise ledger

For a setting-independent `mu(dlambda)` and Bell factorization,

$$
p(a,b|x,y,\lambda)=p_A(a|x,\lambda)p_B(b|y,\lambda),
$$

the conditional means lie in `[-1,1]`, and pointwise

$$
|A_0(B_0+B_1)+A_1(B_0-B_1)|\leq2.
$$

Hence `|S|<=2`, while the registered quantum experiment reaches
`2 sqrt(2)`. If `mu` depends on `x,y`, measurement independence has been
dropped and the bound does not follow. If the joint response fails to
factorize, Bell locality has been dropped. Operational no-signalling supplies
neither premise. The candidate keeps these distinctions.

## 6. Mandatory Seat Q fresh attacks

| Attack | Reconstruction | Disposition |
|---|---|---|
| equal diagonals plus held-out Hadamard | Section 3.3 gives certainty-separated outputs | **PASS** |
| incomplete tester removes phase | restricting readers to `Z` makes `|+>` and `|->` equal, but adding the frozen Hadamard tester splits them | **PASS**; the coarser quotient is a different domain |
| local real simulation with bad tensor rule | separately doubled carriers have dimension `4d_A d_B`, not `2d_A d_B`; ordinary product source cannot implement global realification without constraints | **PASS-WITH-COST** |
| parity leak through preparation label | a parity-readable label lets Bob win but violates operational parity obliviousness; an idle inaccessible label does not | **PASS** |
| equal average channels, different ontic decompositions | decomposition-dependent transition kernels are a valid positive **transformation-contextual** escape, not a noncontextual countermodel | **PASS** |
| one POVM, unequal postmeasurement channels | for `E_±=(I±eta Z)/2`, `A_±(rho)=sqrt(E_±)rho sqrt(E_±)` and `B_±(rho)=X sqrt(E_±)rho sqrt(E_±)X` have equal effects; on `|0>`, a later `Z` reader separates them | **PASS** |
| drop sharp repeatability/functional composition | indeterministic or context-dependent responses evade the square; the candidate scopes the no-go to the sharp-product premises | **PASS-WITH-SCOPE**; outcome-determinism bridge supplied above |
| CHSH with setting-dependent hidden state | `mu_(xy)` can evade CHSH, but explicitly violates measurement independence | **PASS** |
| positive contextual record model called noncontextual | Paper 01's whole-program record law is positive and contextual; the candidate classifies it accordingly | **PASS** |
| frame-dependent negativity | changing the operator frame can move which coefficients are negative while leaving `tr(rho E)` fixed; only the no-all-positive-frame result under fixed affine noncontextual assumptions is invariant | **PASS** |

## 7. Candidate claim audit

| Claim | Seat Q disposition |
|---|---|
| complete-profile congruence | **PASS** in the fixed represented continuation domain |
| on-image quotient is quantum operational category | **PASS-WITH-SCOPE**; no statement about extra native real/Hilbert effects |
| finite/countable/Borel fiber inflation | **PASS** as a nonidentifiability construction; physical source-independence rules remain declared |
| natural invariants factor through quotient | **PASS-WITH-PREMISE**; naturality under noninvertible forgetting is substantive, not forced by empirical adequacy |
| five-way gauge/physical taxonomy | **PASS** |
| phase-complete predictive state | **PASS** |
| exact realification and global cost | **PASS-WITH-SCOPE** on the encoded finite operational image |
| positive records survive contextuality/Bell | **PASS** |
| resource invariants only in fixed classes | **PASS** in the quantum-foundations lens |
| operational records versus microscopic actuality | **PASS** |
| Barandes ontology represented but not selected | **PASS-WITH-SCOPE**; no reconstruction or refutation is earned |
| no discriminator in registered interface | **PASS** by definition of exact operational equivalence, conditional on the fixed interface |
| rung-6 ceiling | **PASS** |

## 8. Registered controls C1--C18

| ID | Verdict | Reason |
|---|---|---|
| C1 | **PASS** | the record representative decodes to its complete operational process rather than dilation labels |
| C2 | **PASS** | a hidden bit changes microscopic fibers and no registered profile |
| C3 | **PASS** | mutually singular Lebesgue/Cantor laws are both legitimate introduced measures and are marginalized |
| C4 | **PASS** | hold/flip latent dynamics differ microscopically while inherited readers ignore them |
| C5 | **PASS** | isometric Kraus mixing preserves the CP map unless the index is recorded |
| C6 | **PASS** | minimal Stinespring size is restricted-class data; padding does not falsify an ontology |
| C7 | **PASS** | POM gives equal `I/2` mixtures and the exact `3/4` preparation-noncontextual bound |
| C8 | **PASS** | equal effect is separated from full channel by a common future reader |
| C9 | **PASS-WITH-SCOPE** | product contradiction is exact; the sharp-determinism route requires preparation noncontextuality/perfect prediction as reconstructed in Section 5.3 |
| C10 | **PASS** | measurement independence plus factorization gives `2`; quantum gives `2 sqrt(2)` |
| C11 | **PASS** | full phase circle and common continuation reject diagonal sufficiency |
| C12 | **PASS-WITH-COST** | realification is exact on its image and carries `J`, doubling, and nonordinary tensor/source structure |
| C13 | **PASS** | complete future comb, not reduced state alone, defines predictive equivalence |
| C14 | **PASS** | changing the fixed reader class changes the domain rather than retroactively changing ontology |
| C15 | **PASS** | program serialization is not physical time |
| C16 | **PASS** | actual record class has arbitrarily many microscopic fiber completions |
| C17 | **PASS** | a new calibrated fiber reader enlarges the experiment domain and splits the class |
| C18 | **PASS** | description length without a physical coding/selection law is not an invariant selector |

## 9. Hostile attacks 1--42

| No. | Disposition |
|---:|---|
| 1 | **PASS** — equivalence uses every complete continuation, not one reader. |
| 2 | **PASS** — ancillary testers are in the profile. |
| 3 | **PASS** — the separating family is fixed independently. |
| 4 | **PASS-WITH-SCOPE** — inverse/fullness is only on the reachable operational image. |
| 5 | **PASS** — tensor and adaptive wiring are admitted. |
| 6 | **PASS** — different boundary types are never merged by scalar coincidence. |
| 7 | **PASS** — the physical reader domain is fixed before quotienting. |
| 8 | **PASS** — no global inverse on extra native objects is claimed. |
| 9 | **PASS** — noninvertible forgetting is not coordinate gauge. |
| 10 | **PASS** — contingent hidden structure remains possible but unselected. |
| 11 | **PASS** — no coordinate-free uniform fiber law is inferred. |
| 12 | **PASS** — maximum entropy is not a selector without fixed variables/constraints. |
| 13 | **PASS** — preparation-correlated reduction is many-to-one empirical forgetting. |
| 14 | **PASS** — registered kernels use preparation and realized prefix, not unperformed future settings. |
| 15 | **PASS** — every latent law is explicitly introduced. |
| 16 | **PASS-WITH-SCOPE** — each fiber rule is fixed by typed program/prefix; no terminal answer table is licensed. |
| 17 | **PASS** — common continuations force phase completeness. |
| 18 | **PASS** — `J` and the doubled/global carrier are explicit. |
| 19 | **PASS-WITH-SCOPE** — product-state and operational independence are not interchangeable; scalar nonselection uses matched contracts only. |
| 20 | **PASS** — local tomography is classified as an added postulate/experiment. |
| 21 | **PASS** — no fundamental complex-scalar conclusion is drawn. |
| 22 | **PASS** — real encoding retains phase-complete structure. |
| 23 | **PASS** — Wigner uniqueness is not used. |
| 24 | **PASS** — Jordan/reconstruction assumptions remain inputs. |
| 25 | **PASS** — positive records are not called universally noncontextual. |
| 26 | **PASS** — no-signalling is not Bell factorization. |
| 27 | **PASS** — physical preparation/transformation procedures carry context; it is not evaluator metadata. |
| 28 | **PASS** — minimal Stinespring dimension is not universal ontology size. |
| 29 | **PASS** — Markovian lower bounds are not applied to whole-history realizers. |
| 30 | **PASS** — complexity is not an ontology selector. |
| 31 | **PASS** — equivalence is exact. |
| 32 | **PASS** — fixed-cut memory minimum is not uniqueness of realization. |
| 33 | **PASS** — actual record remains weaker than complete trajectory. |
| 34 | **PASS** — normalization selects no actual outcome. |
| 35 | **PASS** — decoherence supplies records, not selection. |
| 36 | **PASS** — laboratory slot order remains external. |
| 37 | **PASS** — tensor factors are operational systems, not space. |
| 38 | **PASS** — no hidden order is inserted. |
| 39 | **PASS** — discrete fibers are nonidentifiability controls, not spacetime atoms. |
| 40 | **PASS** — empirical equivalence is not evidence for ISP. |
| 41 | **PASS** — underdetermination does not make all ontologies equally plausible. |
| 42 | **PASS** — no new physical postulate repairs a no-go. |

## 10. Exact scope and quantifiers

| Axis | Accepted scope |
|---|---|
| systems | all finite-dimensional complex systems and finite ancillas in the accepted Paper 01 category |
| slots | every fixed finite number in supplied definite laboratory order |
| outcomes | finite explicitly; standard-Borel only with countably additive instruments, measurable policies, and almost-everywhere conditioning |
| quotient | exact complete-continuation quotient on the reachable represented image |
| phase | predictive phase structure forced by the complete tester domain; no claim that complex scalars are ontic |
| realification | exact finite global encoding or suitably constrained composite encoding; not unrestricted natural RQT with product-state-independent sources |
| contextuality | no universally noncontextual affine positive model under the printed preparation/transformation/sharp-product premises |
| Bell | no measurement-independent Bell-factorizable completion; no-signalling and positivity survive |
| negativity | representation-relative coefficients in a fixed frame; no negative actual-record probabilities |
| memory | task/cut/representation-class minima only; no universal microscopic dimension |
| naturality/no-selection | only invariants natural under the explicitly admitted refinements and noninvertible reductions |
| actuality | one operational record history may be postulated; microscopic actualization remains unconstructed |
| empirical status | exact representation/nonidentifiability theorem, no new discriminator or experiment |

## 11. Full 17-coordinate product

```text
contract       P02-ADEQUATE-REPRESENTATION-CLASS-CONSTRUCTED
quotient       P02-OPERATIONAL-QUOTIENT-CANONICAL
               + SCOPE: REACHABLE REGISTERED IMAGE
naturality     P02-QUOTIENT-NATURALITY-CONSTRUCTED
               + SCOPE: FIXED COMPLETE-CONTINUATION DOMAIN
fibers         P02-ONTOLOGY-FIBERS-CLASSIFIED
selection      P02-OPERATIONAL-NOSELECTION-THEOREM
               + PREMISE: NATURAL UNDER ADMITTED NONINVERTIBLE REDUCTIONS
phase          P02-PHASE-COMPLETE-PREDICTIVE-STATE-FORCED
scalar         P02-COMPLEX-SCALAR-ONTOLOGY-REPRESENTATION-NONUNIQUE
               + COST: GLOBAL-J/CONSTRAINED-TENSOR/SOURCE CONTRACT
positivity     P02-POSITIVE-RECORD-LAWS-SURVIVE
context        P02-NONCONTEXTUAL-MICROONTOLOGY-NOGO-WITH-AFFINITY-
               PERFECT-DISTINGUISHABILITY-PREPARATION-NONCONTEXTUALITY-
               SHARP-OUTCOME-AND-FUNCTIONAL-PRODUCT-PREMISES
bell           P02-BELL-LOCAL-COMPLETION-UNCONSTRUCTED
               + PREMISES: MEASUREMENT-INDEPENDENCE-AND-FACTORIZATION
memory         P02-RESOURCE-INVARIANTS-CLASSIFIED
               + SCOPE: FIXED TASK/CUT/MARKOV/TENSOR CLASSES
gauge          P02-GAUGE-REDUNDANCY-PHYSICAL-DIFFERENCE-CLASSIFIED
record         P02-OPERATIONAL-RECORD-INVARIANT
actuality      P02-RECORD-ACTUALITY-POSTULATED
               + P02-MICROACTUALITY-UNCONSTRUCTED
barandes       P02-BARANDES-ONTOLOGY-UNSELECTED
discriminator  P02-EXTRA-ONTOLOGY-DISCRIMINATOR-NONE-IN-DOMAIN
ontology       P02-ONTOLOGY-UNDERDETERMINED

overall ceiling
               P02-CANONICAL-QUOTIENT-WITH-UNSELECTED-ONTOLOGY-FIBERS
```

## 12. Verdict and correction classification

**Verdict: `ACCEPT-WITH-SCOPE`.**

First decisive semantic counterexample: **none**.

The phase, realification, contextuality, Bell, positivity, and restricted
resource claims survive. The following qualifications are binding:

1. real/complex equivalence is on an encoded finite operational image and
   carries the printed global composition/source-independence cost;
2. Peres--Mermin sharp outcome determinism is either an explicit premise or
   follows from preparation noncontextuality plus perfect predictability and
   common maximally mixed decompositions; measurement noncontextuality alone
   is insufficient;
3. negativity is not a representation-invariant property of one state or
   process outside a fixed frame contract; and
4. no-selection is conditional on naturality under the admitted forgetting
   maps and therefore proves nonidentifiability, not metaphysical absence.

The candidate already states items 1, 3, and 4. Item 2 is a bounded missing
bridge in its Peres--Mermin subsection; it does not change Theorem 6's
conjunction, because preparation noncontextuality is already one of that
theorem's premises, and the independent POM/transformation contradictions
already defeat universal noncontextuality.

Implementation cannot change this semantic verdict. Code could only conform
to or misimplement the frozen quotient, witnesses, and scope.

## 13. Freeze statement

This report is left unstaged and uncommitted on handoff. Its ordinary
post-freeze SHA-256, LF line count, and byte count are necessarily returned
outside the bytes whose hash they describe. No normalized self-hash convention
is used.
