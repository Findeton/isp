# Paper 03 v3.1 independent pin audit — quantum instruments and probability

## Integrated continuous records without fictitious point restart

Date: 2026-08-22

Lens: **Q — quantum instruments, operational probability, continuous
feedback, and relativistic measurement scope**

Verdict: **ACCEPT-FOR-CONSTRUCTION-WITH-BINDING-SCOPE**

First exact semantic or implementability blocker: **none**.

The v3.1 pin makes the necessary correction. It retains exact point-valued
`Ev` samples, but maps only admitted dominated **ensemble laws** to normal
states on the continuous hybrid algebra. It thereby preserves the complete
probability law of continuous measurements and feedback without asserting
that a generic nonatomic observed value is a normal restart state. Finite and
declared atomic records retain exact point-state semantics.

The finite direct-sum repair, continuous normal-extension requirements,
integrated `Ens`/`Ev`/`Heis` theorem, memory firewall, common domination,
nonsingular record maps, localized AQFT scope, and certified-concurrency
quantifiers form one coherent construction target. No v2 probability,
instrument, posterior law, or physical parameter need move.

This audit awards no Paper 03 v3.1 result. Its verdict authorizes only the
frozen mathematics-only construction, subject to every obligation below.

## 0. Authentication, chronology, and independence

Audit began at exact committed HEAD
`a4c4d4eb9aad2fa3e4ad1f06050b71fb4b6afb58`.

| Bound artifact | Recomputed SHA-256 | Exact size | Status |
|---|---|---:|---|
| `v17/note-paper03v31-integrated-hybrid-semantics-pin.md` | `b7ec12ad25c3ac6327cb242ad39ba03e1af541e544f11d32cb86dbce908b5fca` | 760 LF / 30,236 bytes | exact audit authority |
| `v17/note-paper03v3-pin-audit-adjudication.md` | `a4cba0b98ceafa65888bca1a57b8b8205b26c186f264a807a37daf4c5eecb087` | 422 LF / 16,061 bytes | exact v3.1 repair authority |
| `v17/note-paper03v3-hybrid-instrument-semantics-pin.md` | `ada49694c66911455c2980c896ea10f8741d668ebb8af909e2f061c9d6e6d9af` | 597 LF / 25,686 bytes | exact superseded evidence |
| `v17/note-paper03v3-pin-audit-category.md` | `5430ece42ca9e09c82442a9ea2abfa77127b579e06cc9be6b023cc7de780f3fc` | 422 LF / 19,117 bytes | exact prior adjudicated evidence |
| `v17/note-paper03v3-pin-audit-quantum.md` | `ca5d9d8e2e1c97c86862f813709cd1c42b3e0b4e74a67a4c8f764f6285190f28` | 597 LF / 28,350 bytes | exact prior adjudicated evidence |
| `v17/note-paper03v2-hostile-review-adjudication.md` | `74303ddd93b4aac35d3368760da4a0ad3d442570cb16320467076aa5f93ea358` | 476 LF / 22,617 bytes | exact physical repair boundary |
| `v17/paper-03v2-causal-frontier-relativistic-adequacy.md` | `93eaa95fba10831618512ab95447d3527ff5d8877ab5119237f73bb8c30e0181` | 958 LF / 36,711 bytes | exact immutable v2 construction |
| `v17/paper-00-reality-first-programme.md` | `a9f8456763447eaa25a6a840e8f221f51d961ecd9c3ced649ae35a8616457cbe` | 476 LF / 21,268 bytes | exact era charter |

I read the complete bound authority corpus before judgment. I did not open,
name, infer, or contact the independent v3.1 category audit or any future
hostile-review report. The worktree's unrelated pre-existing untracked
`v16/note-handoff-prompt-2026-08-22.md` was not inspected or changed. I wrote
only this assigned report and did not stage or commit it.

## 1. Exact finite and atomic instruments

For finite $R_D$,

$$
\mathcal O_D
=\ell^\infty(R_D)\otimes\mathcal A_D
\cong\bigoplus_{r\in R_D}\mathcal A_D
$$

has a central atom for each exact retained value. The state

$$
\omega_{\rho,r}((A_s)_s)=\rho(A_r)
$$

is positive, normalized, and normal. Thus an exact finite record can be a
restart input when the independently required future-sufficiency/division
test also passes.

For CP branches $\mathcal J_s:\mathcal A_E\to\mathcal A_D$ satisfying
$\sum_s\mathcal J_s(1)=1$, the complete arrow

$$
\widehat{\mathcal J}((A_s)_s)
=\sum_s\mathcal J_s(A_s)
$$

is CP and unital. CP follows at every matrix level by summing the positive
branch amplifications; unitality is exactly instrument normalization. A
central-summand insertion recovers a generally nonunital branch, while the
diagonal restriction recovers the nonselective channel. Neither restriction
is substituted for the complete instrument.

With an old record $r$, the required fiberwise map is

$$
(A_{r,s})_{r,s}
\longmapsto
\left(\sum_s\mathcal J_{r,s}(A_{r,s})\right)_r.
$$

It preserves both the old and new record coordinates. In particular, a
binary result followed by $I$ for result zero and $X$ for result one gives

$$
\widehat T(A)=(A,XAX),
\qquad
(\widehat{\mathcal J}\circ\widehat T)(A)
=\mathcal J_0(A)+\mathcal J_1(XAX),
$$

the exact v2 branchwise law. No probability is retuned.

For a countable declared atomic record, $\ell^\infty(R_D)$ has predual
$\ell^1(R_D)$. Each declared atom supports a normal point state. A mixed or
nonatomic space must be handled point by point: positive atoms may support
normal point states, but a point of zero reference mass may not.

Disposition: the finite theorem is exact; countable/atomic scope is coherent
under the pin's admission conditions.

## 2. The integrated continuous state is mathematically viable

Let the record marginal of an admitted ensemble $\Lambda$ be $\mu\ll\nu$,
with density $h=d\mu/d\nu$. Disintegrate the ensemble and take its conditional
predual barycenter $\bar\rho_r$, whose strong measurability is supplied by the
packet. Then

$$
\eta(r)=h(r)\bar\rho_r\in(\mathcal A_D)_*
$$

is a positive Bochner-integrable field with

$$
\int\|\eta(r)\|\,d\nu(r)=1.
$$

For a hybrid observable field $F$,

$$
\operatorname{Ens}_D(\Lambda)(F)
=\int\eta(r)(F(r))\,d\nu(r)
=\int\rho(F(r))\,\Lambda(d\rho,dr).
$$

This is representative independent because changing $F$ on a $\nu$-null set
changes it on a $\Lambda$-null set. It is positive and normalized. The
predual-valued integral defines a normal functional on
$\mathcal A_D\overline\otimes L^\infty(R_D,\nu_D)$; equivalently normality
can be verified by monotone convergence on bounded increasing positive
nets/sequences within the represented separable-predual packet.

The construction must print the conditional barycenter or an equivalent
predual density explicitly. Weak scalar measurability by itself is not the
pin's promised strong measurable predual field, and a generic vector
Radon--Nikodym inference may not be silently invoked outside the stated
hypotheses.

Crucially, `Ens` acts on laws, not individual nonatomic samples. If
$\nu(\{r\})=0$, then $[\chi_{\{r\}}]=0$ in $L^\infty(R,\nu)$ and evaluation
at $r$ is neither representative independent nor normal. The pin now refuses
that point state rather than trying to manufacture it.

Disposition: V31-T5 and T6 form a coherent positive theorem/refusal pair.

## 3. Continuous instruments: what NEP does and does not supply

Every admitted continuous instrument owes one state-independent normal UCP
arrow on the exact boundary algebras, not merely a family chosen separately
for each input state:

$$
\Phi_{\mathcal I}:\mathcal O_E\longrightarrow\mathcal O_D.
$$

Its instrument restriction must recover the frozen countably additive CP
measure, it must land inside the declared target algebra, and its predual must
preserve the admitted state/ensemble classes.

NEP is substantive. Okamura--Ozawa relate NEP instruments to measuring
processes and, under their hypotheses, to strongly measurable posterior
families for normal states; they also show that CP instruments without NEP
exist. Hence:

- scalar countable additivity is not a normal hybrid extension;
- a measuring process in an ambient $\mathcal B(\mathcal H)$ is insufficient
  unless the induced map lands in the registered local/target algebra;
- posterior existence separately for each state is insufficient unless the
  required state/record kernel is jointly measurable on the frozen input
  space;
- approximate NEP gives only an approximate comparator result; and
- a finite coarse-graining with an exact direct-sum arrow does not prove the
  raw continuous retained-record theorem.

The pin requires every item rather than inferring it from the acronym NEP.
It is therefore feasible but conditional, as physical measurement theory
requires.

## 4. Exact integrated duality across finite paths

The one-step statement must be formulated at ensemble level. For every
admitted $\Lambda_D$ and complete reader $F\in\mathcal O_E$, a primitive
arrow must satisfy

$$
\operatorname{Ens}_E(\Lambda_DK_p)(F)
=\operatorname{Ens}_D(\Lambda_D)(\Phi_p(F)).
$$

The left side is literally

$$
\int_{X_D}\int_{X_E}
\rho_E(F(r_E))
K_p(d\rho_E,dr_E\mid\rho_D,r_D)
\Lambda_D(d\rho_D,dr_D).
$$

It is not an undefined integral of an operator-valued symbol. In a
nonatomic regime the proof must not evaluate the $L^\infty$ class
$\Phi_p(F)$ at each exact $r_D$. That pointwise move would recreate the v3
counterexample. The primitive identity must instead be established between
normal ensemble functionals, or by representative calculations whose final
integrals are proved version independent.

Assume closure $\Lambda_DK_p\in\mathfrak E_E$ and the one-step theorem for
every primitive. If $p:D\to E$ is followed by $q:E\to F$, then

$$
\begin{aligned}
\operatorname{Ens}_F(\Lambda_DK_pK_q)(G)
&=\operatorname{Ens}_E(\Lambda_DK_p)(\Phi_q(G))\\
&=\operatorname{Ens}_D(\Lambda_D)(\Phi_p\Phi_q(G)).
\end{aligned}
$$

The tower property for kernels and contravariant composition
$\operatorname{Heis}(q\circ p)=\Phi_p\Phi_q$ prove the theorem by induction
for every finite path. No point restart is used.

This also exposes the exact sufficiency test for the `Ens` quotient. If two
admitted ensembles induce the same normal state but a licensed future gives
different integrated reader probabilities, then no single Heisenberg arrow
can satisfy the displayed identity for both. The packet has hidden
future-relevant memory or an incomplete boundary schema and must be refined
or refused.

Disposition: V31-T11 is coherent. Construction must prove the base case at
the integrated level and class closure at every induction step.

## 5. Continuous feedback preserves full-program predictions

A registered continuous policy is a measurable almost-everywhere field
$r\mapsto\Phi_r$ whose decomposable action is one normal UCP arrow. UCP gives
uniform norm one; the construction still owes the relevant measurability,
exact tagged endpoints, target landing, and ensemble-class closure.

If two versions agree $\nu$-almost everywhere, every admitted input ensemble
has a $\nu$-absolutely-continuous record marginal, so the complete output law
and every final-reader probability agree. The same remains true after every
admitted earlier path because target ensemble closure and common domination
are required. Therefore the complete program—including a continuous result
driving later feedback—is represented without finite discretization.

What is **not** obtained is a canonical conditional prediction after
postselecting the singleton $\{r\}$ when it has zero probability. The
physically licensed objects are:

1. the full joint continuous program law;
2. conditionals on positive-probability measurable events;
3. almost-everywhere posterior/control versions; and
4. exact point restarts at declared atoms.

An apparatus may implement one pointwise representative, but changing that
representative on a null set changes no admitted operational prediction. If
a newly admitted preparation concentrates probability on that set, it is a
singular route and forces a new common class or boundary refinement; it
cannot be inserted after seeing the desired point.

This is standard continuous stochastic control, not a weakening of the
record law and not an actualization rule. A sampled record remains sample
data in `Ev`; it is not automatically a sufficient Markov checkpoint.

## 6. Complete exposure of memory and preparation context

The normal ensemble state is generally a many-to-one image of sample
ensembles. That is harmless only if every licensed future factors through the
hybrid boundary state.

Suppose a hidden bit $m$ distinguishes two ensembles having the same
`Ens` state, and a later operation applies $I$ for $m=0$ and $X$ for $m=1$.
Their future reader laws differ while the Heisenberg right side is identical.
Integrated duality fails. The same counterexample applies to a hidden process
tensor memory, preparation label, source correlation, or posterior-version
cache.

Every future-relevant quantum memory must therefore be included in
$\mathcal A_D$ (or an exactly typed predictive extension with full
evaluation/update maps), and every future-relevant classical value must be a
retained coordinate. A preparation procedure name is not automatically such
a coordinate. If the future is physically allowed to read it, the interface
must expose the corresponding physical memory; otherwise the future must be
independent of the decomposition.

The pin states this condition explicitly. Construction must verify it for
the complete registered context family, including two-step delayed reads,
not merely immediate guards.

## 7. Common domination and normal record maps

One exact integrated boundary needs one sigma-finite measure class dominating
every admitted incoming record marginal. For finitely or countably many
routes $\mu_n$, a strictly positive weighted sum

$$
\nu=\sum_n2^{-n}\mu_n
$$

(after harmless normalization) supplies a common class. No corresponding
inference holds for arbitrary uncountable families. In particular, no
sigma-finite measure dominates all $\delta_x$ for $x\in[0,1]$.

For a deterministic record map $f:R_D\to R_E$, the Heisenberg pullback on
equivalence classes is well defined precisely when

$$
f_*\nu_D\ll\nu_E.
$$

This is invariant under equivalent representatives and composes. A constant
map between Lebesgue classes and a graph append into a blind product class
fail this condition.

The analogous requirement for a stochastic record kernel $K$ is that target
null sets remain null for the source reference law, e.g.

$$
\nu_E(N)=0
\Longrightarrow
K(r,N)=0\quad\text{for }\nu_D\text{-a.e. }r,
$$

so its Markov/Heisenberg operator is normal and representative independent.
The pin's demanded normal complete extension and ensemble closure must prove
this; checking nonsingularity only for deterministic maps is not enough for
the continuous instruments.

A faithful source state may construct a dominating law for one fixed normal
instrument. It is not a common physical prior and cannot select a state or
history. Equivalent technical choices must leave every prediction invariant.

Disposition: the measure-class architecture is exact, conditional, and
closed under composition if these duties are proved.

## 8. Localized AQFT and operational distinctions

The pin changes no localized system--probe map or comparator premise.
Fewster--Verch supports induced CP instruments from localized couplings and
their causally ordered/disjoint composition under named causal factorization.
It does not imply that arbitrary CP maps are local or that every apparent
spacelike pair commutes.

A retained localized result must be packaged as the complete hybrid arrow.
A complete nonselective operation may obey

$$
\sum_a p(a,b\mid\omega)=p(b\mid\omega),
$$

while a selected positive-support conditional changes the remote state. The
latter is steering, not signalling, because the random record is required to
identify the subensemble. Continuous selected outcomes are interpreted on
positive events or almost everywhere, not by normalizing a null singleton.

Bell compatibility retains the declared source independence and measurement
setting premises. Microcausality, parameter independence, outcome
independence, Bell factorization, and operational no-signalling remain
distinct. A QFT existence theorem for Bell-correlated observables is not a
construction of every ideal localized probe.

Type-III local states need not have density matrices or traces. Split/tensor
controls require their collar and model hypotheses. Nothing in `Ens`, NEP,
or the hybrid center changes those restrictions.

## 9. Certified concurrency

One exchange certificate must compare the complete Heisenberg maps and
complete `Ev` kernels, not merely the integrated scalar predictions of one
ensemble. It also carries output-record permutation, tagged endpoints,
source/apparatus/memory lineage, and measure-class compatibility.

The least category congruence generated by those full squares identifies
exactly paths linked by certified adjacent exchanges. Equality of all finite
linear extensions requires a certificate for every reachable co-enabled
incomparable pair in every reachable record context. An initial-frontier
check is insufficient for adaptive protocols.

In an integrated regime, two selected versions may define the same
Heisenberg operation and all admitted ensemble predictions while differing on
null point samples. That is not an exact `Ev`-kernel exchange certificate.
The construction must either supply equality of the frozen kernel versions
as the pin demands or state only the corresponding integrated operational
equivalence. It may not move between those quantifiers silently.

This theorem removes arbitrary serialization only on the certified domain.
It derives no microscopic time, causal order, foliation, or spacetime.

## 10. No-retuning ledger

| Frozen datum | v3.1 representation | Change in physical probability |
|---|---|---|
| finite branch maps | central restrictions of complete arrow | none |
| complete finite instrument | UCP direct-sum arrow | none |
| finite adaptive law | block/fiberwise continuation | none |
| continuous CP instrument | same CP measure plus admitted normal extension | none |
| exact continuous outcome sample | retained in `Ev` | none |
| nonatomic point normal state | explicitly not claimed | none; theorem scope corrected |
| posterior version | same a.e. kernel data | none |
| complete continuous feedback | integrated decomposable arrow | none |
| localized scattering/source | frozen exact input | none |
| no-signalling/steering/Bell laws | inherited quantifiers | none |
| positive histories/prefixes | inherited kernel law | none |
| schedule relation | only certified equality retained | no mechanism changed |
| reference class | null-ideal typing only | none; not a prior |

The repair removes a false representational identification. It neither
changes the observed law nor adds new physics.

## 11. Target theorem dispositions

| ID | Pin-audit disposition | Binding construction burden |
|---|---|---|
| V31-T1 | coherent inherited target | exact v2 frontier/path category |
| V31-T2 | coherent | one full tagged object per schema |
| V31-T3 | algebraically verified | CP/unital complete finite arrow |
| V31-T4 | coherent | finite exact; pointwise atomic status proved |
| V31-T5 | coherent conditional | common class, strong predual field, normal `Ens` |
| V31-T6 | exact refusal | no generic nonatomic evaluation state |
| V31-T7 | coherent obligation | nonsingularity for every deterministic primitive |
| V31-T8 | coherent conditional | one normal UCP arrow; NEP, landing, posterior, closure |
| V31-T9 | coherent | tagged identities, total matched composition, closure |
| V31-T10 | coherent | actual contravariant functor including records/memory |
| V31-T11 | coherent conditional | integrated base case and finite-path induction |
| V31-T12 | coherent conditional | measurable decomposable field and class closure |
| V31-T13 | coherent | removed information unavailable to future maps |
| V31-T14 | coherent | positive event/atom only; null point refused |
| V31-T15 | coherent | transport tags, classes, fields, maps, kernels, multiplicity |
| V31-T16 | coherent scoped target | constructor-complete two-layer contexts |
| V31-T17 | coherent conditional | exact full two-layer certificate |
| V31-T18 | coherent conditional | all reachable incomparable contexts certified |
| V31-T19 | unchanged inherited target | exact v2 AQFT/no-signalling/steering/Bell scope |
| V31-T20 | unchanged inherited target | normalized positive histories and prefixes |
| V31-T21 | coherent refusals | no model/type/frame collage |
| V31-T22 | coherent refusals | record/conditioning/division/actuality distinct |
| V31-T23 | correctly incomplete | no selected Barandes configuration/law/trajectory |
| V31-T24 | correctly unconstructed | no ontology, time, spacetime, or gravity |

All 24 targets are mutually compatible at their printed quantifiers. This
audit constructs none of them on behalf of the future candidate.

## 12. Two-way control dispositions

| ID | Disposition | Exact reason |
|---|---|---|
| C1 | coherent | direct sum is one hybrid record object; branch list is not |
| C2 | passes algebraically | complete arrow plus block guard gives exact `I/X` law |
| C3 | coherent | normalization belongs to sum; branch may be nonunital |
| C4 | exact distinction | atom evaluates normally; nonatomic point does not |
| C5 | coherent | dominated joint law maps under `Ens`; singular Dirac refused |
| C6 | coherent | posterior is a.e.; no canonical null-point version |
| C7 | binding admission | one class per exact boundary, not per route |
| C8 | exact | pullback needs $f_*\nu_D\ll\nu_E$ |
| C9 | exact | deterministic graph needs compatible target class |
| C10 | exact | equivalent classes canonically agree; singular change is new object |
| C11 | exact firewall | faithful technical state is no physical prior |
| C12 | coherent typing | tagged endpoints distinguish skip from empty path |
| C13 | coherent typing | only an already present record can guard |
| C14 | coherent conditional | measurable normal decomposable field required |
| C15 | binding | every future-readable memory coordinate exposed |
| C16 | coherent typing | discarded coordinate absent from later source |
| C17 | exact probability rule | positive event conditions; null point does not |
| C18 | coherent target | full quantum-state evaluation integral required |
| C19 | exact quantifier | complete map/kernel equality, not one test |
| C20 | exact quantifier | every reachable swap, not initial square |
| C21 | binding | output occurrence/permutation included |
| C22 | binding | correlated source is a joint mechanism |
| C23 | binding | transport includes null ideal and multiplicity |
| C24 | exact variance | full isomorphism differs from proper embedding |
| C25 | inherited exact scope | nonselective marginal versus selected steering |
| C26 | inherited exact scope | covariance permits physical rest frame |
| C27 | inherited refusal | normal functional does not imply density/trace |
| C28 | inherited conditional | split needs collar/model; touching/gauge refused |
| C29 | exact | retention is typed and may end by discard/erasure |
| C30 | exact | division requires future sufficiency |
| C31 | exact firewall | prediction does not choose actual sample |
| C32 | exact firewall | slots are protocol, not event web/time |
| C33 | exact firewall | comparator geometry is declared, not emergent |
| C34 | binding immutability | all v2 laws remain byte-for-byte mathematics |

No control requires a new physical postulate.

## 13. Fresh quantum/instrument countermodels

These are additional to the pin's mandatory 52 attacks.

### Q31-1 — Pointwise base case hidden inside ensemble induction

Prove the primitive identity by evaluating $\Phi(F)$ at every nonatomic input
record and only integrate afterward. **Required disposition:** reject the
proof. The base case itself must be an equality of normal ensemble
functionals; otherwise the old point-evaluation error remains.

### Q31-2 — Statewise posteriors without a joint Markov kernel

For every fixed input state choose a measurable posterior version, but make
the choices nonmeasurable as a function of the input state. **Required
disposition:** refuse the instrument from `Ev`/`Heis` duality until one jointly
measurable state/record kernel is supplied.

### Q31-3 — State-dependent “Heisenberg map”

For each input $\rho$ find a normal extension $\Phi_\rho$ reproducing its
outcome law, with no single linear $\Phi$ working for all states. **Required
disposition:** fail T8. A physical procedure needs one state-independent UCP
arrow.

### Q31-4 — Primitive duality without induction closure

Let the first primitive send an admitted ensemble outside
$\mathfrak E_E$, while both primitives separately pass on their calibration
classes. **Required disposition:** no two-step theorem. Closure of the first
output in the second input class is mandatory.

### Q31-5 — Stochastic singularization invisible to deterministic tests

Use a continuous outcome kernel that sends a positive-$\nu_D$ set into a
$\nu_E$-null point, although every deterministic record map in the packet is
nonsingular. **Required disposition:** refuse its normal hybrid extension or
change the target class before freezing the boundary. Instrument kernels also
must preserve null ideals.

### Q31-6 — Mixed atomic/continuous law

Take $\nu=\tfrac12\delta_0+\tfrac12\lambda$. **Required disposition:** the
point $0$ may have an exact normal state, while generic $r\ne0$ may not. Do
not classify every point by the word “continuous” or promote every point by
the presence of one atom.

### Q31-7 — Unbounded but integrable density

Choose $h=d\mu/d\nu\in L^1_+(\nu)$ with $h\notin L^\infty$. **Required
disposition:** do not reject it merely for unbounded density. If the
predual-valued field is Bochner integrable, `Ens` is still a normal state.
Essential boundedness belongs to observables/UCP fields, not necessarily to
state densities.

### Q31-8 — Weakly measurable posterior with no admitted strong version

Provide scalar measurability against a limited reader family but no strongly
measurable predual-valued barycenter. **Required disposition:** fail T5/T8 or
prove a theorem upgrading it under the declared separability hypotheses.
Reader-by-reader scalars do not automatically define the promised normal
ensemble state.

### Q31-9 — Two-step delayed hidden memory

Let all immediate readers agree on two `Ens`-identical ensembles, copy an
unexposed decomposition label through one idle-looking slot, and read it only
at the following slot. **Required disposition:** fail boundary sufficiency
and operational congruence. Memory exposure must cover every finite future,
not just the next primitive.

### Q31-10 — Null-version equality promoted to exact kernel equality

Choose two control/posterior versions that differ at one $\nu$-null point.
They give identical admitted ensemble predictions but different pointwise
`Ev` kernels there. **Required disposition:** they may be integrated-
operationally equivalent, but they are not an exact full-kernel exchange
certificate unless the frozen kernel representatives also agree.

### Q31-11 — Coarse event followed by singular fine re-preparation

Condition lawfully on a positive bin, discard the fine record, and then add a
mechanism that deterministically prepares a previously null fine point while
claiming the old boundary class. **Required disposition:** the re-preparation
is a new singular route requiring compatible class/schema data; the earlier
coarse conditioning does not authorize a fine-point restart.

### Q31-12 — Routewise common classes fail at a merge

Give each of countably many incoming routes its own class but omit the
strictly positive mixture at their common target. **Required disposition:**
the target object is not yet typed, even though a common class could be
constructed. Construction must choose it before semantic comparison, not
after a desired route is known.

### Q31-13 — Nonlinear access to ensemble decomposition

Let two distinct preparation ensembles have the same `Ens` state and add a
future mechanism whose probabilities are a nonlinear functional of the
decomposition rather than of the exposed hybrid state. **Required
disposition:** this is extra physical memory/context. Expose it in the
boundary or refuse the mechanism; otherwise no Heisenberg dual exists.

### Q31-14 — Infinite-horizon promotion

Take the proved family of finite-path identities and assert equality for an
infinite adaptive record stream without a projective-limit, tightness, or
normal convergence theorem. **Required disposition:** refuse the promotion.
v3.1 proves every finite path only.

### Q31-15 — A posterior version chosen after the sampled value

After observing a null point $r$, choose among a.e.-equivalent posterior
versions specifically to obtain a desired next action. **Required
disposition:** forbidden post-hoc selection. The complete program/version is
packet data before probabilities are evaluated.

### Q31-16 — Atomic input sent to a target-null point

Map a positive source atom deterministically to a point that is null in the
declared target class. **Required disposition:** the pullback is singular and
the primitive is refused, despite the source point being a lawful restart.
Atomicity at the source does not repair the target null ideal.

All sixteen countermodels have exact pin-consistent outcomes. None forces a
probability change or another pin revision.

## 14. Full product disposition

This is pin feasibility, not a claimed construction.

| Coordinate | Pin-audit status | Exact boundary |
|---|---|---|
| input | coherent/frozen | exact v2 laws and comparator packet |
| slot-skeleton | inherited | finite laboratory protocol only |
| frontier | inherited | lower-set boundary, not division |
| boundary | coherent target | tagged complete quantum/record/memory schema |
| sample-semantics | inherited | exact point-valued `Ev` samples and versions |
| ensemble-semantics | coherent conditional | dominated laws mapped by normal `Ens` |
| hybrid-object | coherent | finite exact; W* integrated conditional |
| heisenberg-functor | coherent target | actual UCP object/arrow assignment required |
| integrated-compatibility | coherent conditional | ensemble-level base case plus finite induction |
| point-restart | finite/atomic only | generic nonatomic point refused |
| presentation | coherent target | tags, null ideals, fields, multiplicity transported |
| quotient | coherent scoped target | complete two-layer context family |
| covariance | inherited conditional | full packet isomorphism; no proper-embedding push |
| state-class | conditional | strong field, common class, path closure |
| instrument | finite exact; continuous conditional | NEP, target landing, kernel, closure |
| causal-factorization | inherited conditional | exact localized complete-operation premise |
| certified-schedule | coherent conditional | exact certificates in all reachable contexts |
| no-signalling | inherited | complete nonselective localized map |
| steering | inherited control | selected positive event plus record cost |
| bell | inherited compatibility | source/settings premises; no universal probe |
| positive-model | inherited | normalized contextual memory-bearing prediction |
| context | coherent target | all guards/discards/coarse maps/ancillas included |
| fibers | inherited scoped | no ensemble/reference selection |
| type-III | refusal retained | normal functionals/maps, no generic trace/density |
| split | conditional control | separated collar/model hypothesis |
| gauge | refusal retained | no generic tensor/sector construction |
| particles | refusal retained | no preferred Fock/particle ontology |
| continuum | declared comparator | no interacting-model derivation |
| UV | refusal retained | no cutoff removal theorem |
| preferred-frame | scoped | physical KMS/apparatus frame allowed |
| record | coherent two-layer status | sample retained; normal point state only if atomic |
| division | unconstructed generally | independent future-sufficiency gate |
| actuality | unconstructed | no selected sample/trajectory |
| barandes | compatible but incomplete | no configuration/law/state/trajectory selection |
| ontology | unconstructed | algebra/ensemble/sample not promoted to beables |
| downstream | closed | no time, spacetime, metric, or gravity result |

The point-restart coordinate may consistently read
`FINITE/ATOMIC-CONSTRUCTED` and `NONATOMIC-GENERIC-UNCONSTRUCTED` while an
integrated continuous full-program theorem succeeds.

No rung is awarded. If construction satisfies every obligation, the strongest
pin-permitted rung is 8:

```text
P03V31-RELATIVISTIC-QUANTUM-OPERATIONAL-ADEQUACY-WITH-GLOBAL-ONTOLOGY-DEBT
```

## 15. Primary-source and physical-scope check

The pin uses its primary sources at defensible scope:

- Okamura--Ozawa, *Measurement theory in local quantum physics*,
  https://arxiv.org/abs/1501.00239, establishes NEP as a nonautomatic
  condition, its measuring-process relation, and the strongly measurable
  posterior connection under named hypotheses. It supplies no canonical
  posterior or normal state at every null singleton.
- Fewster--Verch, *Quantum fields and local measurements*,
  https://arxiv.org/abs/1810.06512, supports localized system--probe induced
  instruments and causally factorized ordered/disjoint composition. It does
  not localize arbitrary CP maps or erase source conditions.
- Coecke--Heunen--Kissinger, *Categories of Quantum and Classical Channels*,
  https://arxiv.org/abs/1305.3821, supports the finite classical--quantum CP
  channel control. It does not prove the infinite W* integrated theorem.
- The BFV locally covariant framework supports the inherited variance of
  algebras and state pullback. It does not supply a canonical state
  pushforward or choose a physical state.

The integrated architecture is operational representation mathematics. It
does not select which result occurs, turn a probability law into an actual
history, derive a time direction, or make the comparator spacetime dynamical.

## 16. Binding construction scope and final verdict

Construction is authorized only if it proves, rather than assumes:

1. exact finite/fiberwise complete instruments and atomic point states;
2. one tagged hybrid object for every exact boundary schema;
3. one common sigma-finite domination class for every integrated boundary;
4. a strongly measurable integrable predual field and normal `Ens` state;
5. explicit refusal of generic nonatomic point evaluation/restart;
6. nonsingularity/null-ideal preservation for deterministic and stochastic
   record transformations;
7. one state-independent normal UCP extension landing in the target algebra
   for every continuous instrument;
8. jointly measurable posterior kernels and ensemble/state-class closure;
9. ensemble-level one-step duality and the full finite-path induction;
10. decomposable continuous feedback preserving every admitted full-program
    prediction, with no pointwise restart promotion;
11. complete exposure of all future-relevant quantum, classical, source, and
    process memory;
12. exact localized AQFT/no-signalling/steering/Bell quantifiers;
13. full two-layer concurrency certificates in every reachable context;
14. presentation/packet transport of tags, classes, fields, kernels, maps,
    and occurrence multiplicity; and
15. every v2 probability and every ontology/downstream firewall unchanged.

Verdict: **ACCEPT-FOR-CONSTRUCTION-WITH-BINDING-SCOPE**.

The corrected pin is internally coherent and operationally honest. It keeps
continuous quantum measurement and feedback, but does not turn the exact
value of a measure-zero outcome into a fictitious normal checkpoint. The
first blocker is **none**. Any construction that uses pointwise evaluation in
the integrated proof, loses a common class, hides memory, or weakens a full
exchange certificate should fail at the corresponding frozen outcome rung;
it may not repair the pin or retune the physics.

## 17. Report authentication

Report line count: `000745`

Report byte count: `036220`

Normalized self-SHA-256: `6663a404044889dcc479ff89cedb6f581265977925142c5c6655feb7c8d5ddfc`

Normalization rule: replace the 64 hexadecimal characters on the preceding
line by 64 ASCII zeroes, preserve every other byte, and compute SHA-256. The
report ends in one LF and contains no trailing horizontal whitespace.
