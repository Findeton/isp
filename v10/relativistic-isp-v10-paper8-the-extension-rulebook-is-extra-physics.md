# Relativistic ISP v10 Paper 8: The Extension Rulebook Is Extra Physics

## Complete mathematical target, v1–v9 corpus audit, exact nonselection witnesses, independent architectures, literature comparison, and the strongest admissible SHARD rulebook class

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** D7 research paper, 2026-07-11.  The problem specification was
frozen before the corpus audit; the candidate-architecture ledger was frozen
before the external literature search.  No claim of priority is made.

**Executable receipt:** `v10/code/d7_rulebook_nonselection_exact.py` — 68/68
checks in normal and optimized Python with byte-identical output.  All finite
probabilities and diamond identities use exact `Fraction` arithmetic.  The
reported KL divergence uses `Decimal` precision 110.

## Abstract

This paper asks the question left open by V10 Papers 2–7: what complete law
creates the next interacting sealed record?  The missing object is first
characterized without assuming a global clock, an emergent metric, a supplied
candidate, or a Markov state.  It is a null-inclusive probability kernel on
typed marked finite extension packages—or, equivalently up to almost-sure
versions, a probability measure on complete variable record histories.  It
must specify root birth, continuation, multileg bridges, outcome marks,
construction-order gauge, recorded locality, projective consistency,
commitment, and ownership.

A full audit of V1–V9 finds no such selected law.  The corpus supplies endpoint
kernels, comparison maps, full-history representations, martingales,
sufficiency criteria, factor composition, conditional commitment, Gibbs-like
model families, and in V9 a canonical marked support process conditional on
supplied exposures.  Each begins after at least one required field—extension
scope, support exposure, root/bridge activity, numerical weight, or outcome
instrument—has been supplied.

An independent construction campaign produces seven architectures.  The
strongest synthesis has four layers: a typed extension grammar, a record-local
transfer cocycle, a positive harmonic/projective completion, and a record
instrument/seal.  Exact finite witnesses prove that flat local transfer
weights can lose construction-order gauge after independent row
normalization, that a positive completion repairs normalization, and that a
free activity still changes physical terminal probabilities while every
tested structural gate remains satisfied.  Strict support-local and
closure-defect-only proposals cannot nucleate the first record.  Distinct
full-history measures remain exactly projectively consistent.

The primary literature contains close predecessors for every major
mathematical component: causal-set sequential growth and order-invariant
measures, covtree dynamics, chains with complete connections, Ruelle/Doob
transforms, Papangelou/Hawkes intensities, stochastic rewriting,
probabilistic event structures, quantum sequential growth, process tensors,
and causal boxes.  No searched source derives the full SHARD package from
sealed records alone, but this absence cannot establish originality.

The result is therefore a closure theorem and a refusal: SHARD's established
principles define an admissible **class** of rulebooks, not the unique final
rulebook.  A full-history law may honestly be taken as new primitive physics.
Deriving one requires an additional empirical or microscopic postulate.  Cone
roundness, dimension, metres, seconds, and finite propagation speed are
downstream validation targets and cannot be used as hidden primitive inputs.

## 1. What exactly is missing?

### 1.1 Physical state

Let `Hist` denote the measurable groupoid/category of finite committed typed
marked record histories.  A history `H` contains only durable physical data:

```text
record identities up to relabeling;
incidence and partial order;
typed oriented ports/collars;
outcome marks and sealed factors;
provenance and exactly-once ownership.
```

`H` may contain the whole committed past.  Calling the rule Markovian on `H`
does not assert finite memory; it only says that a complete history is a
sufficient mathematical state.

### 1.2 One extension is a package, not necessarily one vertex

For each `H`, let

$$
\operatorname{Ext}(H)
$$

be the space of admissible typed click packages.  A package `xi` may add one
record or a finite jointly sealed packet.  It contains new identities, its
incoming collar, proposed order/incidence, marks, factor data, ownership, and
the seal witness.  The physical alternative space also contains

$$
\varnothing_H,
$$

the explicit no-extension outcome.

The minimal discrete rulebook is therefore

$$
K_H(d\xi),
\qquad
K_H\!\left(\operatorname{Ext}(H)\cup\{\varnothing_H\}\right)=1.
$$

A continuous-time formulation may use an intensity
`Lambda_H(d xi)`, but then it must also define the intrinsic clock interval
and no-event survival law.  A bare intensity is not complete.

### 1.3 Path-measure equivalent

An initial law plus measurable extension kernels generates a measure `mu` on
complete variable marked histories.  Conversely, a primitive `mu` supplies
conditional next-extension laws relative to a filtration, but only
`mu`-almost surely.  Its action on zero-probability histories requires a
chosen version if those histories remain in the generative domain.

This yields two honest foundations:

```text
Primitive-law option: posit the full non-Markovian history measure mu.

Derived-law option: derive K_H and an initial/root law from more primitive
sealed-record physics.
```

The first is complete but postulates the rulebook.  The second is the open
derivation problem.

### 1.4 Five operations that earlier papers sometimes folded together

1. **Proposal/opportunity:** Which extension packages are offered, including
   no proposal?
2. **Comparison:** Given two positive laws on a common supplied domain, what
   is their relative RN field?
3. **Evidence:** What evidence is actually accumulated in a physical carrier?
4. **Commitment:** What random or deterministic operation accepts an outcome?
5. **Birth:** How is the sealed package durably added with its incidence and
   ownership?

V10 Paper 7 solves a conditional part of stage 2 and a numerical part of
stage 4.  It does not solve stages 1 or 5.

## 2. Mandatory mathematical constraints

### 2.1 Positivity, normalization, and local finiteness

`K_H` must be a measurable probability kernel.  In an intensity version,
bounded intrinsic intervals and finite record regions must have finite total
intensity; otherwise infinitely many offers can precede a defined click.

### 2.2 Leibniz covariance

For every typed history isomorphism `g:H -> H'`,

$$
K_{H'}=g_*K_H.
$$

Machine addresses, enumeration order, or analyst coordinates cannot alter a
physical probability.

### 2.3 Construction-order gauge

If packages `xi` and `eta` are physically compatible and commuting, and both
auxiliary orders yield the same marked history, their path weights must obey
the diamond equation, including declared multiplicities:

$$
K_H(\xi)K_{H+\xi}(\eta)
=
K_H(\eta)K_{H+\eta}(\xi).
$$

This must not be imposed on physically oriented or interacting protocols.
Their order can be recorded holonomy rather than gauge.

### 2.4 Candidate-relative recorded locality

D4 proved that autonomous naturality under every unmarked subset is too
strong.  The replacement is candidate-relative: each offered package has a
record-carried collar or predictive boundary state `B_H(xi)`.  Within its
licensed proposal class,

$$
B_H(\xi)=B_{H'}(\xi')
\quad\Longrightarrow\quad
K_H(\xi)=K_{H'}(\xi').
$$

If discarded history changes the probability, the relevant difference must
be carried across the boundary.  This is recorded locality, not autonomous
ignorance.

### 2.5 Projective consistency

Finite cylinder laws must agree under admissible deletion/coarse graining.
Fine extensions that disappear must either have zero future response or leave
a retained residue.  Arbitrary induced-subset naturality is not required.

### 2.6 Root and bridge closure

A strictly support-local continuation rule has no move from the empty
history.  It also cannot join existing disconnected components.  A complete
theory must provide:

```text
an initial/root or immigration law;
a typed multileg bridge sector, or a zero-bridge theorem;
weights for those sectors.
```

A bridge need not mean action at an emergent spatial distance.  Before
spacetime, its locality test is whether all participating collar legs and
later propagation are explicitly recorded.

### 2.7 Capacity and conservation

Finite records constrain channel content, not automatically the number of
records that may participate.  Multichannel rank, port compatibility, charge,
orientation, or gauge conditions can restrict eligibility.  They select a
probability law only if they leave exactly one normalized alternative, which
the present corpus does not establish.

## 3. Mandatory physical constraints

1. **No universe clock.** A sequential sampler is allowed, but its total
   enumeration must disappear from physical predictions.
2. **Local proper time.** A record chain may count its own clicks.  Different
   chains need not share a global present.
3. **No metric smuggling.** Primitive inputs may use incidence, collars,
   factor support, and recorded dependence—not metres, seconds, dimension, or
   a pre-existing light cone.
4. **Entanglement is not adjacency.** Statistical dependence can motivate a
   multileg factor but does not by itself establish a direct spatial edge.
5. **Record projection is physical.** Hidden implementations are equivalent
   only when they induce the same committed-record law.

## 4. Full V1–V9 audit

The audit asked of every candidate object: does it provide eligibility,
relative weights, null mass, root birth, bridge birth, marks, and seal—or does
it begin after one of these has already been supplied?

The corpus inventory contains 384 Markdown files: 23, 11, 37, 45, 18, 87,
54, 37, and 72 in V1 through V9 respectively.  A corpus-wide thematic sweep
for click/extension law, full history, birth/spawn/bridge, construction order,
diamonds, profinite growth, hazards/intensities, Gibbs/positive transforms,
and quantum instruments identified 288 directly relevant files.  The audit
read the version archive/ledger documents, every load-bearing candidate-law
paper identified by that sweep, and their backward dependencies.  Numerical
geometry and run receipts were checked for whether they declared an input law;
they were not mistaken for derivations merely because they instantiated one.

### 4.1 V1 — supplied localized endpoint laws

V1 begins from endpoint kernels, localized operations, and sector structure.
Fock-sector changes enlarge the domain on which a law may act.  They do not
derive which sector-changing event occurs or its probability.  The seed of a
rulebook is present as supplied kernels, not as an extension selector.

### 4.2 V2 — projective endpoint consistency

V2 develops projective/naturality conditions for endpoint descriptions.  It
constrains how already supplied finite laws must agree.  Projectivity is a
hosting theorem: inequivalent projective families can satisfy it exactly.

### 4.3 V3 — smooth-lapse candidates and construction diamonds

V3 studies candidate smooth-lapse kernels and adjacent-spacelike exchange.
Its diamond reasoning correctly separates foliation/build order from physical
history, conditional on supplied transition/comparison maps.  The actual-law
worksheets and value gaps remain: allowed maps are not numerical selection.

### 4.4 V4 — explicit nonselection

V4 most clearly diagnoses the issue.  Many scores and stochastic matrices
fit the same admissibility data.  Detailed balance is arbitrary until its
score or stationary law is physically sourced.  Uniform admissible rows and
minimum-residual choices are model assumptions.  A write register can reveal
a mode without creating the base probability mass that excites it.

### 4.5 V5 — a primitive indivisible path law is allowed

V5's Barandes-compatible stance permits a complete non-Markovian stochastic
process to be primitive.  That is an ontologically valid rulebook.  It does
not choose one process from the space of such processes.  Bell-compatible
no-signaling also does not supply the missing path weights.

### 4.6 V6 — complete history identifies a supplied law

V6 shows that a complete history cochain or log-density ledger can identify a
finite law and that evidence can drive a conditional commitment mechanism.
The identification has essentially the same degrees of freedom as the law it
identifies.  “Future-relevant contrast” is law-relative: relevance cannot
derive the future law without circularity.  Commitment begins after the mode,
scope, and evidence process exist.

### 4.7 V7 — martingales, sufficiency, centers, and positive transforms

V7 supplies powerful constraints and diagnostic tools: martingales,
sufficient states, centers/shadows, likelihood bases, and positive
`h`-transforms.  They restrict or re-express a candidate law.  They do not
generate the first opportunity/support, root activity, bridge activity, or
local transfer weights.

### 4.8 V8 — the click law is conditional on content

V8 explicitly says the click law answers **when**, given content.  Placement,
kill/spawn/no-op, root birth, and branching remain open.  Gibbs move scores
and inverse temperature are a model family.  The count measure does not
select the desired geometry and in some tests biases it the wrong way.

### 4.9 V9 — closest existing generative construction

V9 Paper 9 provides the closest answer: a canonical marked-history quotient
and a classical support process using unit Poisson clocks in supplied evidence
exposures.  It proves exact renewal, restriction properties, and a common-
cause construction.  But the following remain inputs:

```text
which supports/exposures exist;
the root and branch process;
likelihood/evidence blocks;
shared-evidence allocation c;
transfer coefficient g;
the outcome/quantum instrument.
```

Thus V9 gives a conditional family of builders and proves an
underdetermination boundary.  Its geometry experiments are valid for that
builder class but not yet predictions of a final SHARD law.

### 4.10 Corpus verdict

No V1–V9 object fills every rulebook field.  The recurrent pattern is:

$$
\text{law representation or consistency}
\;\neq\;
\text{law selection}.
$$

## 5. Independent candidate architectures

The constructions below were frozen before the literature search.

### 5.1 Direct covariant kernel

Posit `K_H(d xi)` directly on canonical histories.  This is complete if its
root law, null mass, bridges, marks, and seal are included.  It is the
rulebook, not a derivation of one.

### 5.2 Local transfer plus positive completion

Assign a local unnormalized transfer weight

$$
w_H(\xi)=
a_{\tau(\xi)}
\mathbf 1_{\rm adm}(H,\xi)
e^{-\Delta_\xi\Phi(H)}c_H(\xi).
$$

Here `a_tau` is a root/continuation/bridge activity, admissibility enforces the
typed grammar, `Delta Phi` is a recorded local increment, and `c` is any
independently justified outcome/commitment factor.  A positive completion
function gives

$$
K_H(\xi)=
\frac{w_H(\xi)h(H+\xi)}{
w_H(\varnothing)h(H)+
\sum_{\eta\in\operatorname{Ext}(H)}w_H(\eta)h(H+\eta)}.
$$

The local transfer cocycle controls commuting diamonds; `h` supplies the
projective/future boundary class and normalization.  The formula is a
compiler for a law once `w`, `h`, and the grammar are supplied.

### 5.3 Closure-defect proposals

Weight a proposal by how much unscreened future dependence it would repair.
This is attractive because it makes no-silent closure active.  It is circular
when future relevance is defined using the unknown future law, and it stalls
on an empty zero-defect seed without a base activity.

### 5.4 Residual-capacity reactions

Treat extensions as typed reactions consuming record ports and producing new
records, with explicit multileg bridges.  This gives clear carriers,
conservation, and finite propensities, but its reaction list and rate constants
are new primitive physics.

### 5.5 Self-exciting marked support

Use root intensities plus excitation along recorded ancestry.  This extends
V9 naturally and has an exact no-event law.  The base intensity, response
kernel, and support affinity are precisely the missing interaction law.

### 5.6 Projective decoherence/instrument

Use a strongly positive consistent decoherence functional or quantum
instrument on extension cylinders, with sealing producing the classical
recorded shadow.  This is probably necessary for quantum completeness but the
functional itself remains free.

### 5.7 Maximum caliber or uniform admissibility

Rejected as fundamental selection.  It is an inference rule relative to a
reference measure and constraints.  Reparameterization or changing the offer
menu changes its answer.

## 6. Exact finite results

### 6.1 Row normalization can break a flat diamond

Let the unnormalized commuting transfers be

$$
w_0(A)=2,quad w_0(B)=3,quad
w_A(B)=3,quad w_B(A)=2.
$$

They are exactly flat:

$$
2\cdot3=3\cdot2=6.
$$

Add unit null weight and independently normalize each row.  The two path
weights become

$$
P(A\text{ then }B)=\frac14,
\qquad
P(B\text{ then }A)=\frac13.
$$

So “normalize the local scores” is not a valid construction-order-gauge
theorem.  State-dependent denominators matter.

### 6.2 Positive completion repairs the sampler but not selection

Let `A` and `B` commute and jointly reach terminal history `AB`; let `C` be a
distinct terminal.  With equal local `A/B` transfers and positive `C`
activity `r`, the completion law gives equal auxiliary `AB` order weights and

$$
P(AB)=\frac{2}{2+r},
\qquad
P(C)=\frac{r}{2+r}.
$$

The exact receipt tests `r=1/2,1,3`, producing respectively

| `r` | `P(AB)` | `P(C)` |
|---:|---:|---:|
| `1/2` | `4/5` | `1/5` |
| `1` | `2/3` | `1/3` |
| `3` | `2/5` | `3/5` |

All are positive, normalized, relabeling-covariant, and flat on the commuting
diamond.  Therefore those principles do not select `r`.

### 6.3 Root and bridge no-bootstrap

A rule whose candidate must attach to existing support has no candidate at
the empty history.  With two disconnected components it offers only separate
continuations, not a joining move.  Explicit root and two-legged bridge types
repair the grammar, but their activities remain free.

### 6.4 Projectivity does not select the law

Bernoulli full-history measures with `p=1/3` and `p=2/3` have exactly
normalized and projectively consistent cylinder laws through every tested
level, but different next-click kernels.  Their one-click relative
information is

$$
D(1/3\Vert2/3)
=0.23104906018664843647241070715272552269183337812008508\ldots>0.
$$

Consistency hosts both.

## 7. Literature and originality audit

Primary sources locate every major component in prior work:

1. Rideout–Sorkin causal-set growth derives a broad covariant causal family,
   not one law: [Classical Sequential Growth](https://arxiv.org/abs/gr-qc/9904062).
2. Brightwell–Luczak directly formalize order-invariant growth measures and
   show multiplicity/nonexistence phenomena:
   [Order-invariant measures](https://arxiv.org/abs/0901.0240).
3. Covtree random walks provide a manifestly covariant history arena while
   leaving physical walk selection open:
   [covtree framework](https://arxiv.org/abs/1910.07292).
4. Complete-past conditional laws and their Gibbs relation predate SHARD:
   [chains with complete connections](https://arxiv.org/abs/math/0305026).
5. Ruelle operators and generalized Doob transforms contain the positive
   transfer/`h` mathematics:
   [Ruelle–DLR](https://arxiv.org/abs/1608.03881),
   [generalized Doob transform](https://arxiv.org/abs/1405.5157).
6. Conditional birth intensities and excitation are established in
   Papangelou/Hawkes theory:
   [Papangelou intensities](https://arxiv.org/abs/math/0401402),
   [Hawkes](https://doi.org/10.1093/biomet/58.1.83).
7. Typed graph rewriting with CTMC rates supplies the reaction architecture:
   [stochastic rewriting](https://arxiv.org/abs/2003.09395).
8. True concurrency and probability already distinguish causal configurations
   from arbitrary interleavings:
   [probabilistic stable event structures](https://arxiv.org/abs/2012.10188).
9. Quantum sequential growth, quantum combs, process tensors, and causal
   boxes contain projective quantum histories, memory, typed interfaces, and
   instruments:
   [quantum sequential growth](https://arxiv.org/abs/1303.0433),
   [quantum networks](https://arxiv.org/abs/0904.4483),
   [operational quantum memory](https://arxiv.org/abs/1801.09811),
   [causal boxes](https://arxiv.org/abs/1512.02240).
10. Barandes explicitly supplies the non-Markovian indivisible-process
    ontology but not a unique particular history law:
    [Indivisible Stochastic Processes](https://arxiv.org/abs/2507.21192).

The independent formula is therefore not original at component level.  The
searched sources did not reveal the entire finite-sealed-record assembly with
SHARD provenance, no-silent collars, root/bridge accounting, and seal
semantics.  That supports only the conservative label
`SHARD-specific synthesis/apparently distinct assembly in searched sources`.
It does not establish priority.

## 8. The strongest rulebook now justified

The corpus and literature jointly support a **minimal complete rulebook
schema**, not unique numerical dynamics:

```text
Layer 1 — extension grammar
  root, continuation, bridge, and null packages with typed collars;

Layer 2 — local transfer cocycle
  admissibility, conservation, activities, and record-carried increments;

Layer 3 — positive/projective completion
  normalization, boundary phase, full-history consistency, order quotient;

Layer 4 — quantum/classical record instrument
  outcome, evidence carrier, seal, provenance, and D5 factor ownership.
```

This schema is the answer to “what mathematical object is missing?”  Filling
its four free sectors is the answer to “what new physics is required?”

It also clarifies the canonical relative RN field from Paper 7: once two
candidate rulebooks are supplied on the same extensions, their RN field tells
how their predictions differ.  It cannot create either candidate.

## 9. No derivation from the current foundations

The established foundational principles force substantial constraints but
leave exact freedom:

```text
finite records                 -> capacity/accounting, not rates;
full history                   -> permitted conditioning domain, not values;
sealed holonomy                -> relative ordered change, not opportunity;
diamonds                       -> composition/gauge tests, not birth weights;
profinite consistency          -> compatible towers, not a unique measure;
no-silent records              -> sufficiency/admissibility, not proposal;
Barandes indivisibility        -> ontology of a whole path law, not its choice;
relativistic covariance        -> quotient constraints, not couplings.
```

Consequently, there is no honest final interacting click law derivable from
the present axioms alone.  Any paper writing one number per admissible move
must either:

1. declare those numbers or a full path measure primitive;
2. add a new physical selection postulate; or
3. hide a prior, metric, action, future boundary, or training target.

Only the first two are acceptable foundations.

## 10. Physical research decision

The cleanest immediate theory is to take a covariant full marked-history
measure/instrument as primitive new physics, expressed through the four-layer
schema so no field is hidden.  This is analogous in status to supplying an
action plus couplings, not to deriving dynamics from kinematics.

The derived-law ambition should remain open.  Candidate extra principles must
make distinct, falsifiable choices among the exact `r`-like freedoms.  The
most credible selection program is:

1. define a small parameterized grammar of root, continuation, and bridge
   activities with a quantum-capable instrument;
2. impose only the proven covariance, locality, capacity, and projective
   gates;
3. derive the record-order propagation law without a background metric;
4. propagate each surviving law into the V9 measurement pipeline;
5. test cone anisotropy, scale ladder, dimension stationarity, finite
   propagation, Bell/no-signaling behavior, and black-hole-like screening;
6. reject laws rather than retrofitting the axioms to select the preferred
   geometry.

Round cones or four-dimensional behavior may select empirically among
rulebooks.  They cannot retroactively be called a derivation from records.

## 11. Final verdict

```text
RULEBOOK-MATHEMATICALLY-CHARACTERIZED
+ V1–V9-NO-COMPLETE-SELECTION
+ EXACT-STRUCTURAL-NONSELECTION
+ FOUR-LAYER-ADMISSIBLE-CLASS
+ COMPONENTS-PRECEDED-IN-LITERATURE
+ FINAL-LAW-REQUIRES-NEW-PRIMITIVE-OR-EMPIRICAL-POSTULATE
```

The investigation did find the correct shape of a complete rulebook and the
precise location of every missing datum.  It did not find an honest unique
law already latent in SHARD, diamonds, profinite spaces, or Barandes ISP.  The
next advance is no longer another consistency identity.  It is an explicit
physical postulate for the extension grammar/weights/instrument, followed by
its geometry and quantum consequences.
