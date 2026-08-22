# Paper 18 version-2 independent hostile review — probability, projectivity, and identifiability

Date: 2026-08-21

Seat: P

Verdict: **REVISE**

Scope: frozen mathematics only. No implementation, fitted selector,
Paper 17 output, dimension, geometry, gravity, or repair was used.

## 1. Integrity and independence

The four files required by the assignment were authenticated before review
and read completely.

| role | expected ordinary SHA-256 | observed ordinary SHA-256 | LF / bytes | result |
|---|---|---|---:|---|
| version-2 candidate | `b9dbcbd40e4f2e2eb1b18c4b5e98ba4d33eb491a5af791e9106369a53c51e614` | `b9dbcbd40e4f2e2eb1b18c4b5e98ba4d33eb491a5af791e9106369a53c51e614` | 1,165 / 41,256 | match |
| version-2 construction note | `38d6ba1d80ceda6990d3d7c0cae614b26c5e59e64d299124dbd5bf2394827167` | `38d6ba1d80ceda6990d3d7c0cae614b26c5e59e64d299124dbd5bf2394827167` | 154 / 5,317 | match |
| version-2 review protocol | `e7b1b765e94e8f7cac63c1d1810a25f487eb39eb20aee2052b726eff23e14b44` | `e7b1b765e94e8f7cac63c1d1810a25f487eb39eb20aee2052b726eff23e14b44` | 224 / 10,112 | match |
| version-1 adjudication | `8310c4d0da15b0c56e7dbe599085a22b323e745eafeb90eb29e3db5ab365e144` | `8310c4d0da15b0c56e7dbe599085a22b323e745eafeb90eb29e3db5ab365e144` | 274 / 11,865 | match |

All ten hashes bound in version 2 were also reauthenticated:

| bound input | observed ordinary SHA-256 | result |
|---|---|---|
| Paper 13D law | `3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9` | match |
| Paper 13D terminal adjudication | `ae2c4ef066335c39a0b8057c897c947b06e4270be67d1ed3ec59bf8d6d0a00c9` | match |
| Paper 17B | `e426fd19d29fa0fa8621b4e6402e9b45fc3d4d820164dc6322b920dfa1e38ef9` | match |
| Paper 17C | `5b2c0b7dceaafa594527f19c5fe442f8e413a80b0c4f7bc2368c2aa5eae8a62c` | match |
| Paper 17D | `8448ebd7b2cf2d298814fb586341294a8a06d9a1ed893723b905aeb8e56e4ef9` | match |
| Paper 17E | `8fe6eb0fcbd0aa12edd7787c6bad099e4dc37cef900d7351a033c3141e20e7e7` | match |
| Paper 17F preparation | `224bd4341bc0b1e4ea4dce89cbe4905ffd0a4a67ffb4105e0a50351292a19f07` | match |
| Paper 17F preparatory note | `562efa2b38836b93e13e50a53d1b9a6bee9ade2404c27bc7c4a5e4b35c3ebad2` | match |
| rejected Paper 18 version 1 | `7f8c15b7205b044b06c63d44e4619e3749d6226f99af0c3b7015679cd01b6004` | match |
| version-1 adjudication | `8310c4d0da15b0c56e7dbe599085a22b323e745eafeb90eb29e3db5ab365e144` | match |

The accepted Paper 13D law was consulted only to reconstruct fusion,
generator, trace, quotient, and deletion semantics explicitly inherited by
version 2. No Paper 17 scientific result was used.

This report was produced mutually blind. I did not inspect, list, contact,
summarize, or infer any version-1 or version-2 sibling report or reviewer.
The required version-1 adjudication was read as part of the frozen corpus,
not as a substitute for independent reconstruction.

## 2. Verdict and first decisive issue

Version 2 correctly repairs the version-1 probability and projectivity
defects. Equations (3)–(6), the strictly positive-\(q\) theorem, its null-event
qualification, the character/channel-law distinction, and the un-dimensioned
residue all survive hostile reconstruction.

The first decisive new issue is Definition 12. It says nontrivial
selector-level branching requires at least two inequivalent **targets**.
That excludes multiple independently physical resolved channels with the
same target, even though Definition 10 retains resolved constructions and
Corollary 1 later assigns probabilities to resolved slots
\((c,\alpha)\), including multiplicity \(N_{ab}^{c}>1\).

### First decisive counterexample — two resolved channels, one target

Let the finite sector set be \(\{\mathbf1,a\}\). Give the unit its ordinary
deterministic channels, and let \(\mathsf{Ch}(a,a)\) contain exactly two
inequivalent physical resolved constructions
\(\kappa_0,\kappa_1\), both with target \(a\). They may differ by a retained
internal generator trace while ending at the same sector:

\[
 \tau(\kappa_0)=\tau(\kappa_1)=a.
\]

Resolved counting gives

\[
 \mathsf M_{a,a}=2\delta_a,\qquad
 \mathsf M_{\mathbf1,x}=\mathsf M_{x,\mathbf1}=\delta_x.
\]

This is associative. An \(n\)-fold nonunit word has raw measure
\(2^{n-1}\delta_a\), so every finite word is finite and bracketing
independent. The positive character

\[
 d(\mathbf1)=1,\qquad d(a)=2
\]

satisfies the character equation. Corollary 1 therefore assigns each
resolved slot probability

\[
 \mathsf P(\kappa_i\mid a,a)
 =\frac{d(a)}{d(a)^2}=\frac12,
\]

while the pushed-forward target law is the deterministic \(\delta_a\).
There is genuine selector-level branching over two physical channel
occurrences, but only one target. Definition 12 declares that this is not
nontrivial branching.

The failure is internal to the frozen general contract: resolved slots are
probabilistic objects in Corollary 1 but are excluded by the target-only
criterion in Definition 12. It does not refute the Paper 13D fusion fork,
because accepted fusion has one resolved unmarked generator and its fresh
bond values are histories. It also does not construct any physical Paper 18
channel measure. The defect is bounded, so the verdict is `REVISE`, not
`REJECT`. No repair is made here.

## 3. P1–P4 — Paper 13D fusion and selector-level alternatives

### P1. Independent fusion reconstruction

For a finite family of components of one atomic boundary sort, Paper 13D has
the single unordered n-ary generator

\[
 \Phi_s^{\{I_\alpha\}}:
 \boxtimes_\alpha B_s(I_\alpha)
 \longrightarrow
 B_s\!\left(\bigsqcup_\alpha I_\alpha\right).
\]

Its source retains component tags and has no cross-component bond field.
Fusion forgets the partition, unions every occurrence field, carries every
within-component bond unchanged, and draws one independent fresh seed for
each cross-component unordered pair. At sorts with bonds,

\[
 P(\ell_{ij}=1\mid d_i\ne d_j)=\frac{16}{25},\qquad
 P(\ell_{ij}=1\mid d_i=d_j)=\frac9{25}.
\]

At sorts without bonds fusion is deterministic. The generator, target
species, and simultaneous structural mode are fixed before seeds are drawn.
A fusion history retains its tensor source and fused target values, including
bonds, but not seeds, reader names, control metadata, or serialization order.
A deliberately staged fusion sequence is a different syntax tree and trace
from the single n-ary generator.

### P2. Total forgetting, complete retention, and every invariant coarse output

Let \(L\) denote the complete fresh cross-bond field and let \(G\) be the
accepted stabilizer.

- Total forgetting of \(L\) leaves the one unmarked \(\Phi_s\) construction
  and one target.
- Complete point-free retention gives the orbit \([L]_G\); its probability is
  the orbit pushforward of \(\mathbf\Gamma_D\), not representative mass.
- Every measurable invariant \(J(L)\) has law
  \(J_*\mathbf\Gamma_D\). This includes connectedness, bond count, parity,
  motif indicators, and any joint tuple of such invariants.

For a fresh explicit coarse control, take two cross bonds with conditional
probabilities \(p_1,p_2\in\{9/25,16/25\}\) and retain only their parity
\(J=L_1\oplus L_2\). Then

\[
 P(J=1)=p_1(1-p_2)+(1-p_1)p_2.
\]

The full four bond histories remain in the fiber; the two parity sectors are
coarse outputs; and their odds are fixed Gamma pushforwards. Partial
retention is therefore a third quotient convention but not a third source
of probability.

### P3. Search of all accepted generators

The Paper 13D generator inventory was checked:

- \(U_J,Q_J^0,Q_J^r,D,R_c\) have fixed typed syntax and target species;
- their stochastic target values are retained histories;
- stable endomorphisms, entry, and erasure are fixed deterministic arrows,
  except for the already typed \(R_c\) child kernel;
- tensor has a fixed product syntax and law;
- simultaneous fusion has the one fixed unmarked construction described
  above; and
- all composites are finite syntax trees whose intermediate boundaries are
  retained in the trace.

No accepted generator carries an autonomous probability over two unmarked
generator syntaxes or resolved structural channel objects. Random values
that later become genuine relational state remain child histories of their
supplied arrow.

### P4. Primitive, staged, fused, and disconnected alternatives

Paper 13D does contain inequivalent whole-complex alternatives. In
particular, \(U_J:B_0\to B_2^0\) is a primitive arrow while
\(D\circ Q_J^0:B_0\to B_2^0\) retains an intermediate \(B_1^0\) trace and
has a different endpoint kernel. Simultaneous and deliberately staged fusion
are likewise different traces; tensor/disconnected and fused complexes are
different typed constructions.

The accepted evaluator gives the child law after one such syntax is supplied.
It gives no probability for selecting among those syntax trees. They
therefore witness whole-selector residue, not an already derived law.

The decisive same-target countermodel shows an important general
qualification: if a future physical census and autonomous channel measure
did give positive support to several such inequivalent resolved paths, they
could become channel-level branching even with one target. No such measure
is present in Paper 13D.

## 4. P5–P8 — positive characters and occurrence propensity

### P5. Countable classification and induced kernel

For

\[
 \mathsf S=\mathbb N_0,\qquad
 \mathsf M_{m,n}=\delta_{m+n},
\]

the character equation is \(d(m+n)=d(m)d(n)\) with \(d(0)=1\).
Writing \(r=d(1)>0\), induction gives \(d(n)=r^n\); conversely every
\(r>0\) works. Since the space is discrete, all such characters are
measurable.

For every \(r\),

\[
 \mathsf P^{(r)}_{m,n}
 =\frac{r^{m+n}}{r^mr^n}\delta_{m+n}
 =\delta_{m+n}.
\]

The character family is continuous, but the conditional channel kernel is
one deterministic law. Version 2 labels that distinction correctly.

### P6. Continuous measurable classification and induced kernel

On \(\mathbb R_{\ge0}\) with its usual Borel structure, positivity and the
character equation give

\[
 g(a+b)=g(a)+g(b),\qquad g=\log d.
\]

A measurable additive \(g\) is linear, so every measurable positive
character is

\[
 d_\lambda(a)=e^{\lambda a},\qquad\lambda\in\mathbb R.
\]

Each local character integral is a finite Dirac evaluation. No global
integrability against an undeclared reference measure follows. For every
\(\lambda\),

\[
 \mathsf P^{(\lambda)}_{a,b}=\delta_{a+b}.
\]

Again there are many raw characters and one induced conditional law.

### P7. Two strictly positive occurrence propensities

Let the fixed channel output law on \(\{c_0,c_1\}\) be
\(P(c_0)=2/5\), \(P(c_1)=3/5\). Add a no-composition outcome \(\bot\) and
define

\[
 W_q(\bot)=1-q,\qquad W_q(c_i)=qP(c_i).
\]

The laws \(W_{1/5}\) and \(W_{4/5}\) are normalized, have the same output
law conditional on composition, and have different strictly positive
composition propensities. Theorem 7 is correct.

### P8. The null event at \(q=0\)

At \(q=0\), \(W_0=\delta_\bot\). For any two different candidate kernels
\(P\) and \(Q\), the constructions \(W_{0,P}\) and \(W_{0,Q}\) induce the
same whole probability measure. Neither \(P\) nor \(Q\) is identified by
conditioning that measure on the null composition event. Version 2 states
this qualification exactly.

## 5. P9–P13 — deletion and exact projectivity

### P9. Markov kernels and Chapman–Kolmogorov

For an unmarked size-\(n\) class \(x\), let

\[
 r_{n,m}(x,y)=
 \#\{A\subseteq\operatorname{Occ}(x):
       |A|=m,\ [x|_A]=y\}.
\]

Uniform retained-subset deletion is

\[
 K_{n,m}(x,y)=
 \frac{r_{n,m}(x,y)}{\binom nm}.
\]

At \(m=n-1\), this is equation (4):

\[
 K_{n,n-1}(x,y)=\frac{m(x,y)}n.
\]

The definition is representative independent because presentation
automorphisms permute the retained subsets. \(K_{n,n}\) is the identity.
Choosing a uniform \(k\)-subset and then a uniform \(m\)-subset inside it
gives a uniform \(m\)-subset of the original \(n\)-set, so

\[
 K_{n,m}=K_{n,k}K_{k,m}.
\]

Thus equation (3) is a correctly typed primary projectivity statement.

### P10. Direct derivation of equations (5) and (6)

For one-step deletion, projectivity says

\[
 \frac{w_n(y)}{Z_n}
 =\sum_x
   \frac{w_{n+1}(x)}{Z_{n+1}}
   \frac{m(x,y)}{n+1}.
\]

When \(w_n(y)>0\), division and rearrangement give

\[
 \sum_x\frac{m(x,y)}{n+1}
 \frac{w_{n+1}(x)}{w_n(y)}
 =\frac{Z_{n+1}}{Z_n},
\]

which is equation (5). Under groupoid base
\(w_n(y)=u_n(y)/a_y\),

\[
 \frac{w_{n+1}(x)}{w_n(y)}
 =\frac{a_y}{a_x}
  \frac{u_{n+1}(x)}{u_n(y)},
\]

which is equation (6). Both formulas are correct at their declared positive
weight scope.

### P11. One class, automorphisms, and labeled conventions

Let the unique size-\(n\) class be the unstructured \(n\)-set. Then

\[
 m(x_{n+1},x_n)=n+1,\qquad
 K_{n+1,n}=1,\qquad
 a_{x_n}=n!.
\]

For equal-orbit activity \(w_n=r^n\), equation (5) has both sides equal to
\(r\). For groupoid activity \(u_n=r^n\), the full class weight is
\(w_n=r^n/n!\); equation (6) has both sides equal to
\(r/(n+1)\). The automorphism ratio cancels the raw occurrence
multiplicity exactly as required.

If instead \(u_n\) is a weight per labeled representative, the point-free
class mass contains the orbit factor \(n!/a_x\), and its labeled partition
function has a different factorial convention. Direct derivation gives

\[
 \sum_x m(x,y)\frac{a_y}{a_x}
 \frac{u_{n+1}(x)}{u_n(y)}
 =\frac{\widetilde Z_{n+1}}{\widetilde Z_n}.
\]

Version 2 correctly refuses to identify this coefficient with either
equation (5) or (6).

### P12. Aggregate normalization is not retained-class projectivity

Let the size-one classes be red and blue with probability \(1/2\) each. At
size two put probability one on the all-red class. Both size laws normalize
to one, but uniform deletion of the size-two law is red with probability one,
not the declared size-one law. Aggregate size normalization therefore says
nothing about equation (3).

### P13. Fresh projective family with continuous freedom

For each \(p\in[0,1]\), let the labeled size-\(n\) graph be
\(G(n,p)\): each unordered edge is independently present with probability
\(p\). Restriction to a uniformly retained \(m\)-subset is exactly
\(G(m,p)\). Pushing these exchangeable laws to unmarked graph classes gives

\[
 P_n^{(p)}K_{n,m}=P_m^{(p)}
\]

for every \(n\ge m\), while \(p\) remains free. Mixtures over \(p\), and more
general exchangeable graph mixtures, give still more projective freedom.
Projectivity does not generally select a unique law.

## 6. P14–P19 — whole residue, traces, phases, descriptions, and ontology

### P14. Logical independence of the listed residues

With a fixed conditional output kernel, finite normalized whole-law controls
can vary separately:

- composition versus no composition through \(q\);
- primitive versus staged syntax through an odds parameter \(\alpha\);
- root number through root weights \(\rho_r\);
- bounded total size through a size law \(s_n\);
- disconnected component count through a fugacity \(z^k\); and
- retained trace length through activities \(a_k\).

Additional projectivity, coherence, or boundary equations may later couple
these data. The conditional channel law alone does not. Paper 13D's
\(2^{-(n+1)}\) cardinality law is restricted to its declared grand primitive
experiment and cannot be imported for new structural complexes.

### P15. Divergence despite periodic endpoint actions

Let \(F\) and \(G\) be two endpoint involutions whose generated endpoint
action is finite, but retain every length-\(k\) word in the physical process
trace. Give every letter activity \(a>0\). There are \(2^k\) words of length
\(k\), so

\[
 Z_{\rm trace}
 =\sum_{k\ge0}2^ka^k
 =\sum_{k\ge0}(2a)^k.
\]

It diverges for \(a\ge1/2\), despite periodicity and finiteness of the
extensional endpoint action. Version 2's finite-trace normalizability
firewall is correct.

### P16. Phase coexistence and boundary state

The zero-field nearest-neighbor ferromagnetic Ising specification on
\(\mathbb Z^2\) at sufficiently low temperature has plus and minus
infinite-volume Gibbs states with the same local conditional specification
and different magnetization. A local specification, stationarity, and
projective finite-volume data do not by themselves select the boundary
phase. Version 2 correctly leaves that state in the residue.

### P17. Post-hoc descriptions are nonidentifying

For any full-support probability \(\pi\) on a finite outcome set:

- \(K(x,y)=\pi(y)\) is stationary and reversible for \(\pi\);
- \(E_\pi(x)=-\log\pi(x)\) gives a Gibbs representation;
- choosing reference measure \(\pi\) makes \(\pi\) the unconstrained relative
  maximum-entropy law; and
- \(\lvert\psi_\pi\rangle=\sum_x\sqrt{\pi(x)}e^{i\theta_x}\lvert x\rangle\)
  with coordinate projectors gives a Born representation.

All four inputs can be adapted after \(\pi\) is chosen. Their post-hoc
existence therefore cannot identify \(\pi\). Physical selection requires the
kernel, energy, reference and constraints, or state and measurement to be
fixed independently first.

### P18. Type of the selector-residue object

Definition 17 treats \(\mathfrak R\) as an unconstructed set or groupoid of
complete positive solutions modulo explicitly declared gauge isomorphisms.
It does not silently assume addition, scalar multiplication, a topology, a
manifold atlas, or an algebraic quotient. Its outcome list distinguishes
empty, one class, finite, infinite, constructed topological/measurable, and
unclassified cases. No dimension is assigned. This repairs the version-1
typing defect.

### P19. Probabilistic consistency of every ontology branch

1. An enlarged universal law can give normalized objective propensities
   without actualizing an outcome.
2. A law family is normalized member by member but is not a unique prediction
   until its constants are fixed independently.
3. A contingent cosmological state supplies conditional boundary data, not a
   universal coupling.
4. A preparation state conditions a declared experiment and cannot be
   promoted to universal occurrence odds.
5. A gauge or reference-measure convention changes no physical law when only
   its invariant kernel is observed.
6. A calibratable structural parameter may be inferred from independent
   data, but is not derived merely from normalization.
7. One actual complex without a fundamental ensemble is not a delta
   distribution over possible complexes and supports no ensemble typicality
   claim.
8. An unselected datum remains an explicit predictive residue.

None of these classifications supplies actualization.

## 7. P20 — mandatory hostile controls

### Controls 13–24

| control | result | Seat-P finding |
|---|---|---|
| 13 history values as channels | rejected | Total, complete, and invariant coarse retention all remain Gamma history pushforwards. |
| 14 staged trace erased at equal endpoint | rejected for the accepted law | Paper 13D retains the intermediate trace. The new same-target countermodel shows that a future measured family of such paths must also count as channel branching. |
| 15 deterministic union as branching | rejected | Total bond forgetting leaves one fusion construction. |
| 16 desired probabilities as multiplicities | rejected | Theorem 6 exposes the circular representation \(\mathsf M=\mathsf P,d=1\). |
| 17 support normalized uniformly | rejected | Support has no probability without provenance. |
| 18 orbit/groupoid exchange | rejected | Equations (5) and (6) retain distinct bases and automorphism factors. |
| 19 topology/groupoid selects Haar | rejected | Definition 14 requires a separate measure-provenance theorem. |
| 20 pairwise finite, divergent triple convolution | rejected | Definition 13 requires every finite-word raw convolution to be finite. For example, masses \(2^{-n}\) followed by pair masses \(2^n\) give an infinite triple integral and are excluded. |
| 21 marginal associativity without pentagon | rejected | Definition 13 explicitly separates marginal equality from path-level associator and pentagon duties. |
| 22 spectator wreath factorial | rejected as a promotion | No physical channel measure is constructed; any future rooted law must test spectator automorphisms rather than import global inverse-automorphism weight. |
| 23 context averaged without state law | rejected | Section 7.5 requires an independently supplied distribution on context. |
| 24 hidden phase/clock/history/cache closure | rejected | Closure may not be obtained by undeclared state; the physical channel and whole residue remain unconstructed. |

### Controls 25–36

| control | result | Seat-P finding |
|---|---|---|
| 25 separately physical \(M,d\) from \(P\) alone | rejected | Theorem 5 identifies a gauge family and claims no complete gauge classification. |
| 26 normalized representation as selection | rejected | Theorem 6 is the exact representation no-go. |
| 27 character family called distinct channel physics | rejected | Sections 7.2–7.3 compute one deterministic kernel for each full character family. |
| 28 raw \(n+1\) as Markov probability | rejected | Equation (4) divides physical preimage multiplicity by \(n+1\). |
| 29 one orbit/labeled/groupoid coefficient | rejected | Equal-orbit, inverse-automorphism, and labeled formulas are separated. |
| 30 aggregate normalization for projectivity | rejected | The red/blue countermodel passes normalization and fails equation (3). |
| 31 independent parameter per size | rejected | One family must satisfy all Chapman–Kolmogorov and projectivity equations. |
| 32 hidden boundary phases | rejected | The Ising control has two phases for one local specification. |
| 33 equal activity on infinitely many traces | rejected | The two-involution control diverges already at \(a\ge1/2\). |
| 34 identified conditional at \(q=0\) | rejected | Distinct counterfactual kernels give the same \(W_0=\delta_\bot\). |
| 35 vector dimension on residual set | rejected | Definition 17 assigns no dimension-bearing structure. |
| 36 output odds used as fusion odds | rejected | \(W_{1/5}\) and \(W_{4/5}\) separate the two probabilities. |

### Positive controls 54–58

| control | result | witness |
|---|---|---|
| 54 Paper 13D structural/history fork | pass | One unmarked fusion generator; every retained cross-bond invariant has its Gamma pushforward law. |
| 55 one channel law, two positive composition propensities | pass | \(W_{1/5}\) and \(W_{4/5}\). |
| 56 identical child recovery, different complex odds | pass | Countermodel CM-P5 below. |
| 57 projective family with continuous parameter | pass | The unmarked pushforward of \(G(n,p)\). |
| 58 stable history without selector branch | pass | The positive-support Paper 13D record values remain stable child histories under the stable future grammar, with no law over alternative parent syntax. |

## 8. Fresh semantic countermodels

These are mathematical constructions for this review, not implementation
outputs or fitted physical models.

### CM-P1 — same-target resolved structural branching

The two-object convolution in Section 2 has two inequivalent resolved
channels \(\kappa_0,\kappa_1:a\boxtimes a\rightsquigarrow a\), counting
measure \(2\delta_a\), character \(d(a)=2\), and resolved probabilities
\(1/2,1/2\). It decisively falsifies Definition 12's two-target necessity.

### CM-P2 — partial retained-history invariant

Two cross-bond bits are retained only through parity. The parity sectors have
the explicit Gamma-pushforward probability
\(p_1(1-p_2)+(1-p_1)p_2\), while each has two complete histories above it.
This is neither total forgetting nor complete retention and creates no new
selector odds.

### CM-P3 — projective free graph family

The point-free pushforwards of \(G(n,p)\) commute with every uniform induced
subgraph deletion kernel. The parameter \(p\in[0,1]\) remains continuously
free, and mixtures enlarge the family.

### CM-P4 — divergent trace law with finite endpoint action

Two involutive endpoint maps generate a finite extensional action while all
physical words remain distinct. Equal letter activity \(a\) gives
\(\sum_k(2a)^k\), which diverges for \(a\ge1/2\).

### CM-P5 — identical child laws, different parent occurrence laws

Let the parent complexes be \(A,B\). Fix child laws
\(\Gamma_A(0,1)=(2/3,1/3)\) and
\(\Gamma_B(0,1)=(1/4,3/4)\). Define

\[
 \widehat\Gamma_\Pi(\chi,h)=\Pi(\chi)\Gamma_\chi(h).
\]

The parent laws
\(\Pi_1(A,B)=(1/4,3/4)\) and
\(\Pi_2(A,B)=(3/4,1/4)\) recover exactly the same conditional child law for
each supplied parent but assign different parent occurrence odds.

### CM-P6 — null-event counterfactual nonidentifiability

Choose two different output kernels \(P\ne Q\) and set occurrence propensity
to zero. Both resulting whole measures are \(\delta_\bot\). The conditional
kernel is extra counterfactual structure and cannot be recovered from the
whole measure.

## 9. P21–P22 — result typing and scope

### P21. Character families versus channel-law families

The countable \(d_r\) and continuous \(d_\lambda\) examples are full raw
character families with one identical deterministic induced kernel. They
support raw-character nonuniqueness only. They do not justify
`P18-CHANNEL-LAW-FAMILY-CONSTRUCTED`, and because neither example is the
physical Paper 13D channel measure, they do not promote the current physical
positive-character coordinate.

The same-target countermodel has a nontrivial law on **resolved channel
slots** but a deterministic pushed-forward target-sector kernel. This
further shows why result labels must declare whether they concern characters,
resolved channels, or target-sector laws.

### P22. General mathematics versus the accepted law

The following general results are verified:

- positive-character normalization on measurable kernels;
- finite-word marginal bracketing independence;
- the finite-word measure/character gauge under its finiteness hypothesis;
- the normalized-representation no-go;
- exact Markov projectivity and the base-specific weight equations;
- continuous projective nonuniqueness; and
- conditional channel versus positive composition-occurrence separation.

Those theorems construct no physical Paper 18 channel measure or selector.
The accepted-law result is narrower: Paper 13D simultaneous fusion has one
unmarked resolved generator, and every retained cross-bond invariant inherits
its law from \(\mathbf\Gamma_D\). No other accepted generator supplies an
autonomous selector-level law.

The Definition-12 defect belongs to the general contract. It changes neither
the accepted Paper 13D fork nor any conservative physical coordinate.

## 10. Full current product vector

Every unaffected coordinate is preserved:

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

No implementation, repair, staging, commit, parameter choice, Paper 17
evaluation, or downstream geometric selection is authorized by this report.
