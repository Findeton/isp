# Paper 18 independent hostile review — probability, projectivity, and identifiability

Date: 2026-08-21

Seat: P

Verdict: **REVISE**

Scope: mathematics only. No implementation, sampler behavior, fitted
parameter, Paper 17 output, geometry target, or repair was used.

## 1. Integrity, corpus, and independence

The three required files were authenticated before review and read completely.

| file | expected ordinary SHA-256 | observed ordinary SHA-256 | LF / bytes | result |
|---|---|---|---:|---|
| `paper-18-operational-structural-sectors.md` | `7f8c15b7205b044b06c63d44e4619e3749d6226f99af0c3b7015679cd01b6004` | `7f8c15b7205b044b06c63d44e4619e3749d6226f99af0c3b7015679cd01b6004` | 1,335 / 44,728 | match |
| `note-paper18-operational-structural-sectors-construction.md` | `3a25bfb175624696685fcbd1db04fb5ff95572328bb345d9f97adda1dd46ae77` | `3a25bfb175624696685fcbd1db04fb5ff95572328bb345d9f97adda1dd46ae77` | 230 / 9,290 | match |
| `note-paper18-operational-structural-sectors-review-protocol.md` | `7611586515f10c73a1c99c064254130407aa758a243fa496dc31faab662f25c6` | `7611586515f10c73a1c99c064254130407aa758a243fa496dc31faab662f25c6` | 300 / 12,580 | match |

The eight inputs bound by the candidate were also reauthenticated:

| bound input | observed ordinary SHA-256 | result |
|---|---|---|
| Paper 13D law | `3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9` | match |
| Paper 13D terminal mathematical adjudication | `ae2c4ef066335c39a0b8057c897c947b06e4270be67d1ed3ec59bf8d6d0a00c9` | match |
| Paper 17B | `e426fd19d29fa0fa8621b4e6402e9b45fc3d4d820164dc6322b920dfa1e38ef9` | match |
| Paper 17C | `5b2c0b7dceaafa594527f19c5fe442f8e413a80b0c4f7bc2368c2aa5eae8a62c` | match |
| Paper 17D | `8448ebd7b2cf2d298814fb586341294a8a06d9a1ed893723b905aeb8e56e4ef9` | match |
| Paper 17E | `8fe6eb0fcbd0aa12edd7787c6bad099e4dc37cef900d7351a033c3141e20e7e7` | match |
| Paper 17F preparation | `224bd4341bc0b1e4ea4dce89cbe4905ffd0a4a67ffb4105e0a50351292a19f07` | match |
| Paper 17F construction note | `562efa2b38836b93e13e50a53d1b9a6bee9ade2404c27bc7c4a5e4b35c3ebad2` | match |

Only the accepted Paper 13D law and its terminal adjudication were consulted
to reconstruct the explicit inherited fusion, trace, quotient, generator, and
deletion claims. No earlier selector conclusion or Paper 17 scientific output
was imported.

This review was produced mutually blind. I did not read, list, message,
summarize, or infer any sibling review or sibling reviewer.

## 2. Verdict and first decisive counterexample

The main probability no-go, the structural/history conclusion, and the
conservative current product vector survive. The reason for `REVISE` is a
bounded semantic defect in Section 7.2, which is headed “Exact deletion
transfer.” The symbols \(D\), \(w_n\), and \(Z_n\) are not tied to a declared
base convention. In particular, the text does not say whether \(D\) is:

1. raw deletion-preimage multiplicity;
2. the class-level Markov kernel after uniform deletion;
3. a stabilizer-weighted transfer coefficient; or
4. a labeled-object transfer coefficient.

Those coefficients are different. Therefore the displayed equation is not
an exact, well-typed projectivity condition as frozen.

### First decisive counterexample

At every size \(n\), let there be exactly one point-free class
\(\star_n\), with \(w_n(\star_n)=Z_n=1\). Every one of the \(n+1\)
occurrences of \(\star_{n+1}\) deletes to \(\star_n\). Thus the raw preimage
multiplicity is

\[
 m(\star_{n+1},\star_n)=n+1.
\]

If the candidate's \(D\) is the preimage multiplicity requested by P10, its
equation gives \(n+1=1\). The actual uniform-deletion kernel is

\[
 K(\star_{n+1},\star_n)=\frac{m}{n+1}=1,
\]

which is projective. If instead \(D\) was intended to mean \(K\), that
meaning and the associated weight/base convention are absent from the frozen
definition; the required stabilizer factors likewise remain implicit. This
is not an implementation issue and is not resolved by aggregate
normalization.

The defect has bounded mathematical scope and does not select any physical
result, so `REVISE`, rather than `REJECT`, is the protocol verdict. I do not
repair the frozen candidate here.

Three additional scope defects do not change that verdict:

- The additive character families in Sections 6.2 and 6.3 are genuine, but
  every displayed character induces the same deterministic conditional
  kernel. They establish character nonuniqueness, not a family of channel
  probabilities.
- Theorem 7 allows \(q=0\) while speaking of the conditional law “given that
  composition occurs.” On a null occurrence event that conditional is not
  determined by the resulting probability measure. The nonidentifiability
  theorem remains valid by comparing any two strictly positive \(q\)'s.
- \(\mathcal X_{\rm res}\) has no declared carrier, algebraic operation,
  scalar field, topology, or exact quotient relation. Consequently its
  “dimension” is presently undefined, exactly as the current
  `WHOLE-SELECTOR-UNCONSTRUCTED` coordinate requires.

## 3. P1–P4 — inherited fusion semantics and the branching fork

### P1. Independent reconstruction of simultaneous fusion

For a finite family of Paper 13D components of one atomic boundary sort,

\[
 \Phi_s^{\{I_\alpha\}}:
 \boxtimes_\alpha B_s(I_\alpha)
 \longrightarrow B_s\!\left(\bigsqcup_\alpha I_\alpha\right)
\]

is a single n-ary generator indexed by an unordered finite family. Its source
retains the component partition and has no cross-component bonds. Fusion:

1. forgets that partition at the target;
2. unions every occurrence field;
3. retains all within-component bonds;
4. draws exactly one fresh independent seed for every cross-component
   unordered pair; and
5. uses the already accepted endpoint-bond rule, with bond-one probability
   \(16/25\) when the endpoint \(d\)-values differ and \(9/25\) when they
   agree.

At a boundary sort without bonds the target-value map is deterministic. At a
sort with bonds, the generator syntax and target boundary species are fixed,
while the target bond field is stochastic. A fusion history retains the
tensor source and fused target values, including bonds, but not the seeds.
Component order and seed-exposure order are presentation gauge. A sequence of
two fusion generators is a different physical trace from the one n-ary
fusion generator.

### P2. What each forgetting convention does

There are three useful levels, not two literal quotients:

- **Forget all realized cross-bond values.** One retains the single
  \(\Phi_s\) syntax, one target species, and one unmarked structural channel.
  This is deterministic structural union.
- **Retain the complete cross-bond field.** Distinct fields are distinct
  physical history outcomes except when the accepted experiment stabilizer
  carries them into the same orbit. Their orbit masses are the Paper 13D
  pushforward masses. If they are named output sectors, their conditional law
  is already \(\mathbf\Gamma_D\).
- **Retain a proper invariant of the cross-bond field.** For example retain
  connectedness or bond parity while forgetting the microconfiguration. This
  gives several coarse structural outputs with probabilities equal to the
  corresponding \(\mathbf\Gamma_D\) pushforwards.

The third convention is a genuine intermediate quotient, but not a third
probability source. Every retained bond-measurable sector has its law from
\(\mathbf\Gamma_D\); every forgotten bond coordinate remains in the history
fiber. Thus the candidate's probabilistic conclusion survives, although its
two-arm language is quotient-incomplete.

### P3. Both arms and omitted alternatives

The first arm is correct at the unmarked generator/species level. The second
arm is correct for complete retained bond configurations and, by pushforward,
for every partial invariant. No convention produces new occurrence odds.

A further logical possibility is that a realized bond field is both a
historical outcome of the fusion operation and the structural state used by
later operations. “History” and “structure after the event” are not mutually
exclusive predicates. This again falls under the second probabilistic arm:
its transition law is \(\mathbf\Gamma_D\), while the propensity to instantiate
the encompassing fusion complex remains outside \(\mathbf\Gamma_D\).

Accordingly, `P18-CURRENT-GAMMA-STRUCTURAL-BRANCHING-FORK-PROVED` is retained
as the conclusion that no new selector odds arise. It should not be read as
an exhaustive classification of all possible coarse-grainings.

### P4. Other accepted Paper 13D generators

No individual accepted generator supplies stochastic branching among two
unmarked generator syntaxes or target species. Every generator has a fixed
typed source and target; its stochastic boundary values are history values.

Paper 13D nevertheless contains inequivalent whole-complex alternatives:

- primitive \(U_J:B_0\to B_2^0\) versus staged
  \(D\circ Q_J^0:B_0\to B_2^0\);
- the queried record-carrying route \(R_c\circ Q_J^r\), which is a distinct
  typed complex but not a parallel target to \(U_J\); and
- one simultaneous n-ary fusion trace versus deliberately staged fusion
  traces.

These alternatives are not collapsed by equal endpoint types, but
\(\mathbf\Gamma_D\) supplies no probability for choosing one arrow syntax
over another. They therefore witness whole-selector residue, not an already
constructed positive-support structural branching law. The candidate's
`NONTRIVIAL-STRUCTURAL-BRANCHING-UNCONSTRUCTED` coordinate is correct.

## 4. P5–P7 — characters and conditional-versus-whole laws

### P5. Countable additive family

For \((\mathbb N_0,+)\) and
\(\mathsf M_{m,n}=\delta_{m+n}\), the character equation is

\[
 d(m+n)=d(m)d(n),\qquad d(0)=1.
\]

Every positive character is determined by \(r=d(1)>0\), and induction gives
\(d_r(n)=r^n\). Conversely every \(r>0\) satisfies the equation. Thus the
displayed family is correct and complete.

However,

\[
 \mathsf P^{(r)}_{m,n}
 =\frac{d_r(m+n)}{d_r(m)d_r(n)}\delta_{m+n}
 =\delta_{m+n}
\]

for every \(r\). The parameter is invisible to the conditional channel law.
It cannot by itself witness different occurrence probabilities.

### P6. Continuous additive family

For \((\mathbb R_{\geq0},+)\) and
\(\mathsf M_{a,b}=\delta_{a+b}\), every displayed
\(d_\lambda(a)=e^{\lambda a}\), \(\lambda\in\mathbb R\), is positive,
Borel measurable, has \(d_\lambda(0)=1\), and satisfies the character
equation. Conversely, if a positive character is measurable, then
\(g=\log d\) is a measurable additive function on
\(\mathbb R_{\geq0}\), hence \(g(a)=\lambda a\). The displayed family is
therefore the full measurable positive-character family.

Each character integral is finite because the convolution measure is a
single Dirac mass. No global integrability of \(d_\lambda\) against an
undeclared sector reference measure follows. Again,

\[
 \mathsf P^{(\lambda)}_{a,b}=\delta_{a+b}
\]

for every \(\lambda\). The example proves raw-character nonuniqueness, not
conditional-channel-law nonuniqueness.

### P7. Two normalized whole laws with one conditional channel law

Let the conditional fusion output law be

\[
 P(c_0)=\tfrac13,\qquad P(c_1)=\tfrac23.
\]

On \(\{\bot,c_0,c_1\}\), where \(\bot\) means no fusion, define

\[
 W_q(\bot)=1-q,\qquad W_q(c_i)=qP(c_i).
\]

Both \(W_{1/4}\) and \(W_{3/4}\) are normalized. Conditional on fusion, both
give \(P\), but their fusion-occurrence propensities differ. This proves the
substantive Theorem 7 claim. The theorem's inclusion of \(q=0\) needs the
null-event qualification recorded above.

## 5. P8–P13 — residue, bases, deletion, and traces

### P8. Residues tested separately

Each listed residue can vary while a fixed conditional channel law is held
constant:

- **Primitive versus staged.** Give the primitive and two-step traces
  positive prior odds \(\alpha:1\); the common conditional law inside either
  selected trace does not determine \(\alpha\).
- **Root.** Give otherwise identical connected complexes one-root and
  two-root weights \(\rho_1,\rho_2\). A local output kernel does not constrain
  their ratio.
- **Size.** Choose any normalized bounded size law \(s_n\). Paper 13D's
  \(2^{-(n+1)}\) law is explicitly restricted to its grand empty-program
  primitive family, so importing it to new sector complexes is invalid.
- **Disconnected components.** A component fugacity \(z^k\) changes the
  distribution of the number \(k\) of disconnected components without
  changing conditional fusion outputs inside a component.
- **Trace words.** An activity \(a^k\) changes the length law of retained
  \(F^k\) traces; the conditional endpoint channel does not determine \(a\).

All five residues therefore remain live until independent whole-law,
projective, or coherence equations constrain them.

### P9. Orbit base versus inverse-automorphism base

Take two point-free classes \(A,B\) with
\(|\operatorname{Aut}A|=1\) and \(|\operatorname{Aut}B|=2\), and equal
activities. Equal orbit weight gives

\[
 (P(A),P(B))=(\tfrac12,\tfrac12),
\]

whereas inverse-automorphism weight gives

\[
 (P(A),P(B))=(\tfrac23,\tfrac13).
\]

The two bases are not presentation variants of one another. One counts
point-free classes equally; the other is finite-groupoid cardinality. The
candidate correctly refuses to choose between them merely from
point-freeness.

### P10. Exact deletion transfer with multiplicities and stabilizers

Let

\[
 m(\chi',\chi)
 =\#\{v\in V(\chi'):[\chi'-v]=[\chi]\}.
\]

Uniform deletion induces the point-free Markov kernel

\[
 K_{n+1,n}([\chi'],[\chi])
 =\frac{m(\chi',\chi)}{n+1}.
\]

If the complete class weight is \(w_n\) and
\(P_n([\chi])=w_n([\chi])/Z_n\), exact projectivity is equivalent, for every
retained class of positive weight, to

\[
 \sum_{[\chi']}
 \frac{m(\chi',\chi)}{n+1}
 \frac{w_{n+1}([\chi'])}{w_n([\chi])}
 =\frac{Z_{n+1}}{Z_n}.
\tag{P10-orbit}
\]

If \(w_n([\chi])=u_n([\chi])/a_\chi\), where
\(a_\chi=|\operatorname{Aut}\chi|\), the same equation becomes

\[
 \sum_{[\chi']}
 \frac{m(\chi',\chi)}{n+1}
 \frac{a_\chi}{a_{\chi'}}
 \frac{u_{n+1}([\chi'])}{u_n([\chi])}
 =\frac{Z_{n+1}}{Z_n}.
\tag{P10-groupoid}
\]

Equivalently, if one begins with equal activity per labeled representative,
the class mass contains \(n!/a_\chi\); the common factorial changes the
partition-function convention and moves the \(n+1\) factor between the two
sides. The frozen candidate declares none of these conventions. This is the
decisive revision item.

### P11. Retained-class projectivity versus aggregate size

Let a point-free binary-color class at size \(n\) be indexed by its number of
ones. At size one choose

\[
 P_1(0)=P_1(1)=\tfrac12.
\]

At size two choose

\[
 P_2(0)=\tfrac34,\qquad P_2(2)=\tfrac14,
\]

and zero mass on the mixed class. Both levels have total mass one, so every
aggregate size check passes. Uniform deletion from level two instead gives
\((3/4,1/4)\) at level one, not \((1/2,1/2)\). Exact projectivity must be
checked class by class.

### P12. Uniqueness positive control and continuous projective freedom

Projectivity can be unique on a constrained support: if each level contains
only one admitted class and deletion maps it to the unique previous class,
there is exactly one normalized family.

It does not generally select a law. For \(p\in[0,1]\), put on the
binary-color classes

\[
 P_n^{(p)}(k)=\binom nk p^k(1-p)^{n-k}.
\]

Uniform deletion gives \(P_{n-1}^{(p)}\) exactly, so \(p\) is a free
continuous projective parameter. Mixtures
\(\int P_n^{(p)}\,\nu(dp)\) give the still larger family indexed by arbitrary
probability measures \(\nu\) on \([0,1]\). Exact projectivity alone therefore
does not identify a selector.

### P13. Periodic endpoints do not normalize physical traces

Let \(F\) act extensionally as an involution, \(F^2=\mathrm{id}\), but let
the accepted physical syntax retain each word \(1,F,F^2,\ldots\) as a
different trace. With factorized trace activity \(a^k\),

\[
 Z_{\rm trace}=\sum_{k\geq0}a^k.
\]

It is finite exactly for \(0\leq a<1\). At \(a=1\), equal positive trace
activity gives \(Z_{\rm trace}=\infty\), despite there being only two
extensional endpoint actions. The candidate's trace warning is correct.

## 6. P14–P17 — phases, adapted representations, typing, and ontology

### P14. Phase coexistence and boundary dependence

The nearest-neighbor ferromagnetic Ising specification on
\(\mathbb Z^2\) at zero field and sufficiently low temperature has distinct
plus and minus infinite-volume Gibbs measures. They satisfy the same local
conditional specification and translation symmetry but have opposite
magnetization, selected by boundary condition. This supplies an exact
semantic countermodel to any inference from one finite Gibbs specification
to one infinite selector. Phase, boundary condition, and infinite-volume
state must be reported separately, as the candidate requires.

### P15. Adapted-input nonselection lemma

Let \(\pi\) be any full-support probability law on a finite outcome set \(X\).
After \(\pi\) is chosen one can always construct:

- a stationary and reversible refresh kernel
  \(K(x,y)=\pi(y)\), since
  \(\pi(x)K(x,y)=\pi(x)\pi(y)=\pi(y)K(y,x)\);
- a Gibbs representation with energy
  \(E_\pi(x)=-\log\pi(x)\) at inverse temperature one;
- a relative-maximum-entropy representation by taking the reference measure
  itself to be \(\pi\) (or adapting sufficient statistics and constraints);
  and
- a Born representation on \(\ell^2(X)\) with
  \(|\psi_\pi\rangle=\sum_x\sqrt{\pi(x)}e^{i\theta_x}|x\rangle\) and the
  coordinate projectors.

Thus stationarity, reversibility, Gibbs form, relative maximum entropy, and a
Born representation are all surjective post-hoc descriptions of candidate
probabilities when their kernel, energy, reference, constraints, state, or
measurement is adapted to the desired \(\pi\). They select a law only when
their inputs and physical provenance are fixed independently first.

### P16. Whole-selector residue typing precedes dimension

The residual object is not currently typed well enough for a dimension:
positivity gives a cone rather than automatically a vector space; deletion
relations can be nonlinear; “boundary coboundaries” require a declared
complex; and the quotient requires a specified equivalence relation and
scope. A logarithmic character group, tangent dimension, algebraic dimension,
topological dimension, and number of identifiable parameters need not agree.

The candidate permits the answer “undefined” and claims no present residue
dimension, so no product promotion is lost. Definition 12 remains an evidence
obligation, not a constructed mathematical object.

### P17. Probabilistic consistency of the ontology branches

- A unique enlarged nomological selector can be a normalized propensity law
  without actualizing an outcome.
- A law family is probabilistically consistent member by member, but makes no
  unique unconditional prediction until its couplings are fixed or given a
  higher-level state law.
- A law plus contingent cosmological state is a kernel conditional on that
  state; unspecified state data remain genuine predictive residue.
- A contingent structural state alone can condition predictions but is not a
  universal occurrence law.
- A single actual complex with no fundamental ensemble carries no
  probabilities over alternative complexes. It cannot support typicality,
  entropy maximization, or likelihood claims across those alternatives. It
  can coexist with the conditional \(\mathbf\Gamma_D\) counterfactual law for
  a supplied complex, but it does not solve actualization of a history.
- “No coherent selector object” makes no probabilistic selection claim and is
  logically consistent with the accepted conditional law.

Normalization in none of these branches actualizes a complex or history.

## 7. P18 — mandatory controls

### Section 10.2 structural/history controls

| control | result | probability-seat finding |
|---|---|---|
| 9 HISTORY-AS-STRUCTURE | rejected | Full or coarse bond outputs are \(\mathbf\Gamma_D\) pushforwards; naming them sectors creates no new odds. |
| 10 STRUCTURE-AS-HISTORY | rejected | Paper 13D retains deliberately staged fusion and primitive/staged process traces as different whole complexes. |
| 11 DETERMINISTIC-AS-BRANCHING | rejected | Forgetting realized bonds leaves one deterministic union channel. |
| 12 PROBABILITY-AS-MULTIPLICITY | rejected | Theorem 6 correctly exposes \(\mathsf M=\mathsf P,d=1\) as representation, not provenance. |
| 13 SUPPORT-AS-PROBABILITY | rejected | Neither finite support nor a measurable support set selects uniform or any other weights. |
| 14 FUSION-OCCURRENCE-CONFLATION | rejected with null-event scope | \(W_{1/4}\) and \(W_{3/4}\) have one conditional output law and different occurrence odds; \(q=0\) needs separate wording. |

### Section 10.4 infinite/projective controls

| control | result | probability-seat finding |
|---|---|---|
| 23 SIZE-LAW-IMPORT | rejected | Paper 13D's size law belongs to its restricted grand primitive experiment, not new sector complexes. |
| 24 INDEPENDENT-SIZE-FIT | rejected | Class-level deletion equations must connect every adjacent size. |
| 25 AGGREGATE-DELETION | detected, but exact formula needs revision | The binary-color countermodel passes normalization at each size and fails exact retained-class transfer. Section 7.2 leaves its transfer convention undefined. |
| 26 TRACE-DIVERGENCE | rejected | Equal activity on distinct periodic trace words gives an infinite partition sum. |
| 27 PHASE-HIDING | rejected | One local specification can have multiple boundary-selected infinite-volume phases. |
| 28 ADAPTIVE-CUTOFF | rejected | A cutoff inspected or changed after outcomes is another fitted selector input. |

### Positive controls 44–46

| control | result | witness |
|---|---|---|
| 44 current Paper 13D fusion fork | pass | The single n-ary syntax has one unmarked target; retained bond outcomes have the accepted orbit-pushforward \(\mathbf\Gamma_D\) law. |
| 45 fixed conditional channel law, different fusion occurrence | pass | \(W_{1/4}\) and \(W_{3/4}\) above. |
| 46 identical child recovery, different complex odds | pass | The parent-law pair below. |

## 8. Fresh semantic countermodels

These countermodels were constructed for this review and are not outputs of
an implementation or parameter fit.

### CM-P1 — identical child law, different parent law

Let the complex set be \(\{A,B\}\), the child history set be \(\{0,1\}\), and
\(\Gamma_A=\Gamma_B=(1/2,1/2)\). Define

\[
 \widehat\Gamma_p(A,h)=p\Gamma_A(h),\qquad
 \widehat\Gamma_p(B,h)=(1-p)\Gamma_B(h).
\]

The laws \(p=1/3\) and \(p=2/3\) recover exactly the same child law after
conditioning on either parent, but give different parent-complex odds.

### CM-P2 — conditional channel versus occurrence propensity

The \(W_{1/4},W_{3/4}\) construction in P7 has one conditional output law
\((1/3,2/3)\) and distinct fusion-occurrence propensities. This separates the
channel theorem from the whole selector without changing child physics.

### CM-P3 — projective family with a free parameter

The binomial point-free color-count family
\(P_n^{(p)}(k)=\binom nkp^k(1-p)^{n-k}\) is exactly projective for every
\(p\in[0,1]\). Projectivity leaves at least one continuous parameter, and
mixtures leave an arbitrary mixing measure.

### CM-P4 — divergent periodic trace law

Let \(F^2=\mathrm{id}\) on endpoint values while all words \(F^k\) remain
physical traces. Equal activity one gives countably many unit weights and an
infinite partition function. Endpoint periodicity does not make the trace law
normalizable.

### CM-P5 — partial structural forgetting

Let fusion generate two independent fair cross-bond bits
\(L=(L_1,L_2)\). Retain only \(R=L_1\oplus L_2\) as an output sector while
retaining the full \(L\) in its history fiber. There are two structural
outputs, each with probability \(1/2\), and two microhistories above each.
This is neither total bond forgetting nor the complete-configuration
partition, but all odds are still a \(\mathbf\Gamma_D\) pushforward.

### CM-P6 — aggregate deletion without projectivity

The size-one uniform binary-color law and size-two \(3/4\) all-zero,
\(1/4\) all-one law both normalize and can be assigned any desired aggregate
size masses. Uniform deletion does not recover the size-one law.

### CM-P7 — one local Gibbs specification, two phases

The low-temperature zero-field ferromagnetic Ising specification admits plus
and minus infinite-volume Gibbs states with the same local conditional rule
and different macroscopic magnetization. A finite specification does not
select its boundary state.

### CM-P8 — probability-adapted representations

For arbitrary full-support finite \(\pi\), the refresh kernel, Gibbs energy,
relative-entropy reference, and Born state constructed in P15 all reproduce
\(\pi\). Their existence after fitting is therefore nonidentifying.

## 9. General contract versus accepted physical law

Theorems 3–6 are correct general conditional mathematics (subject to their
declared measurable-kernel hypotheses). They do not show that the accepted
Paper 13D system has a physical channel measure, a positive character, or a
channel selector. The countable and continuous examples are controls, not
accepted sectors.

Theorem 2 is the only reviewed result here that specializes to accepted
Paper 13D fusion. It shows that current bond randomness either remains in the
accepted history fiber or is carried to output sectors with the accepted
pushforward law. It does not provide an autonomous propensity over primitive,
staged, fused, disconnected, or differently sized whole complexes.

Consequently neither the revision item nor any positive control licenses a
physical measure, a selector parameter, a boundary state, a cutoff, an
actualized complex, or a downstream geometric evaluation.

## 10. Full bound product vector

Every surviving coordinate is preserved:

    P18-SECTOR-REFERENT-CONTRACT-CONSTRUCTED
    P18-BOUNDED-SECTOR-CENSUS-UNCONSTRUCTED
    P18-GLOBAL-SECTOR-COMPLETION-UNCONSTRUCTED
    P18-CURRENT-GAMMA-STRUCTURAL-BRANCHING-FORK-PROVED
    P18-NONTRIVIAL-STRUCTURAL-BRANCHING-UNCONSTRUCTED
    P18-PHYSICAL-CHANNEL-MEASURE-UNCONSTRUCTED
    P18-COMPOSITION-CLOSURE-UNPROVEN
    P18-POSITIVE-CHARACTER-UNTESTED-NO-PHYSICAL-CHANNEL-MEASURE
    P18-CHANNEL-LAW-UNCONSTRUCTED
    P18-WHOLE-SELECTOR-UNCONSTRUCTED
    P18-ACTUALIZATION-UNCONSTRUCTED
    P18-CHRONOLOGY-NOT-EVALUATED
    P18-DIMENSION-NOT-EVALUATED
    P18-SIGNATURE-NOT-EVALUATED
    P18-METRIC-NOT-EVALUATED
    P18-CURVATURE-NOT-EVALUATED
    P18-GRAVITY-NOT-EVALUATED

No implementation, repair, staging, commit, Paper 17 evaluation, parameter
selection, or geometry selection is authorized by this report.
