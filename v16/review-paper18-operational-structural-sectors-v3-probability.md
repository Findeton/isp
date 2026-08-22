# Paper 18 version-3 composite hostile review — probability and identifiability

Date: 2026-08-21

Seat: P

Verdict: **REVISE**

Scope: the authenticated version-2 base plus the binding version-3
amendment, with the amendment taking precedence exactly where stated. No
implementation, fit, Paper 17 output, dimension, geometry, gravity, or repair
was used.

## 1. Integrity, composition, and blindness

All five assigned artifacts were authenticated before review and read
completely.

| role | expected ordinary SHA-256 | observed ordinary SHA-256 | LF / bytes | result |
|---|---|---|---:|---|
| complete version-2 base | `b9dbcbd40e4f2e2eb1b18c4b5e98ba4d33eb491a5af791e9106369a53c51e614` | `b9dbcbd40e4f2e2eb1b18c4b5e98ba4d33eb491a5af791e9106369a53c51e614` | 1,165 / 41,256 | match |
| binding version-3 amendment | `496942b2a742ee2fe81561790e185aba6a3fcc865630c23ca278c3067c80f6dd` | `496942b2a742ee2fe81561790e185aba6a3fcc865630c23ca278c3067c80f6dd` | 318 / 10,598 | match |
| version-3 construction note | `71d3bef893d772aff8c102915a570ffee76d4bbab15e48a47219bbef3de7876b` | `71d3bef893d772aff8c102915a570ffee76d4bbab15e48a47219bbef3de7876b` | 76 / 2,828 | match |
| version-3 review protocol | `cece6b5e44c1d3f5bdebe650d1723a03f828e5a107610bbacf9a24416852f910` | `cece6b5e44c1d3f5bdebe650d1723a03f828e5a107610bbacf9a24416852f910` | 137 / 6,250 | match |
| version-2 adjudication | `172f8fa73d3f3d06703c6128bb53ccf28f11936d8210a8e1a3603a9566f8468b` | `172f8fa73d3f3d06703c6128bb53ccf28f11936d8210a8e1a3603a9566f8468b` | 79 / 2,944 | match |

The accepted Paper 13D law and terminal adjudication were also
reauthenticated at
`3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9`
and
`ae2c4ef066335c39a0b8057c897c947b06e4270be67d1ed3ec59bf8d6d0a00c9`.
Only the explicit generator, trace, quotient, and fusion clauses needed by
P7–P8 were consulted.

This review was produced mutually blind. I did not inspect, list, contact,
summarize, or infer any version-3 sibling report or reviewer. The assigned
version-2 adjudication was read as immutable corpus, not as a substitute for
independent proof.

## 2. Verdict and first decisive issue

Version 3 correctly repairs version 2's target-only branching definition. It
also correctly separates resolved-channel probability from its target-sector
pushforward.

The first decisive new defect is that Definition 10A defines only a finite
measure \(\mu_{a,b}\) separately on each varying resolved-channel class
space. It does not construct:

1. a measurable total resolved-channel space over \((a,b)\);
2. a measurable field of the fiber sigma algebras; or
3. the kernel condition
   \((a,b)\mapsto\mu_{a,b}(E_{a,b})\) for measurable resolved events.

Nevertheless Replacement Theorem 3 concludes measurability by invoking “the
resolved kernel,” an object absent from its hypotheses. Pointwise
normalization is valid; a measurable conditional resolved-channel law does
not follow.

### First decisive counterexample — measurable target law, nonmeasurable resolved family

Let the input sector space be \(\mathbb R_{\ge0}\) with its Borel sigma
algebra and deterministic target convolution

\[
 \mathsf M_{a,b}=\delta_{a+b}.
\]

For \(a,b>0\), let the resolved fiber contain two inequivalent objects
\(\kappa_0(a,b),\kappa_1(a,b)\), both targeting \(a+b\). Choose a
non-Borel set \(V\subset(0,\infty)\). Place the nonunit fibers in the Borel
total space \((0,\infty)^2\times\{0,1\}\), with target map
\(\tau(a,b,i)=a+b\); the event \(E_0=\{i=0\}\) is measurable. Define the
pointwise finite resolved measures

\[
 \mu_{a,b}=
 \begin{cases}
 \delta_{\kappa_0(a,b)},&a\in V,\\
 \delta_{\kappa_1(a,b)},&a\notin V.
 \end{cases}
\]

Use the unique unit channel when \(a=0\) or \(b=0\). Every individual
\(\mu_{a,b}\) is finite, nonzero, and invariant, exactly as Definition 10A
requires. The target map is measurable, and every pushforward is the
measurable associative kernel \(\delta_{a+b}\). With \(d=1\), equation
(V3.2) holds and equation (V3.3) returns \(\mu\).

But on the measurable resolved event \(E_0\) selecting the \(\kappa_0\)
branch,

\[
 (a,b)\longmapsto
 \mathsf P^{\rm res}_{a,b}(\{\kappa_0(a,b)\})
 =\mathbf1_V(a),
\]

which is not measurable. Thus all stated pointwise measure conditions,
target-kernel conditions, and the character equation hold while the claimed
resolved conditional kernel does not exist.

This is a failed general probability definition/theorem, so the protocol
requires at least `REVISE`. It changes no current physical coordinate:
Paper 13D still has one resolved simultaneous-fusion generator, and no
physical resolved measure has been constructed. No repair is made here.

## 3. Seat-P review P1–P15

### P1. Version-2 same-target counterexample

Version 3 accepts the version-2 counterexample correctly. For
\(\mathsf S=\{\mathbf1,a\}\), two inequivalent channels
\(\kappa_0,\kappa_1:a\boxtimes a\rightsquigarrow a\) with resolved counting
measure give

\[
 \mu_{a,a}=\delta_{\kappa_0}+\delta_{\kappa_1},
 \qquad
 \mathsf M_{a,a}=2\delta_a.
\]

Together with the unit channels, an \(n\)-fold nonunit target convolution is
\(2^{n-1}\delta_a\), hence finite and bracketing independent. The character
\(d(\mathbf1)=1,d(a)=2\) gives

\[
 P^{\rm res}(\kappa_i\mid a,a)=\frac12,\qquad
 P^{\rm tgt}(a\mid a,a)=1.
\]

Replacement Definition 12 now classifies this as measure-supported resolved
branching without falsely requiring target plurality.

### P2. Normalization and target pushforward

For each fixed input pair, equations (V3.3)–(V3.4) are correct. Indeed,

\[
 \int
 \frac{d(\tau\kappa)}{d(a)d(b)}\,\mu_{a,b}(d\kappa)
 =
 \frac{\int d(c)\,\mathsf M_{a,b}(dc)}{d(a)d(b)}
 =1.
\]

For every measurable target set \(C\),

\[
 (\tau_*\mathsf P^{\rm res}_{a,b})(C)
 =
 \frac{1}{d(a)d(b)}
 \int_{\tau^{-1}C}d(\tau\kappa)\,\mu_{a,b}(d\kappa)
 =
 \mathsf P^{\rm tgt}_{a,b}(C).
\]

What fails is the additional claim of measurability in the input pair. The
counterexample above shows that target pushforward can erase precisely the
nonmeasurable resolved dependence. The theorem is valid as a pointwise
normalization identity, not as the claimed resolved kernel theorem under the
frozen hypotheses.

### P3. Finite resolved Frobenius–Perron probabilities

For resolved counting measure

\[
 \mu_{a,b}
 =\sum_{c,\alpha=1}^{N_{ab}^{c}}\delta_{(c,\alpha)},
\]

equation (V3.3) gives every slot

\[
 P^{\rm res}(c,\alpha\mid a,b)=\frac{d_c}{d_ad_b}.
\]

Summing over \(\alpha\) gives

\[
 P^{\rm tgt}(c\mid a,b)
 =\frac{N_{ab}^{c}d_c}{d_ad_b}.
\]

Summing over \(c\) is one by the character equation. These are the correct
resolved and target probabilities, conditional on independently physical
counting provenance.

### P4. One target, multiple targets, and continuous resolved families

All three regimes are mathematically distinct and are now admitted.

1. **Several channels, one target.** The P1 control has two positive atoms
   above \(a\) and deterministic target law.
2. **Several targets.** On \(\{\mathbf1,a\}\), the normalized convolution
   \[
    \mathsf M_{a,a}
    =p\delta_{\mathbf1}+(1-p)\delta_a,\qquad 0<p<1,
   \]
   is associative. Resolve it by one channel to each target with weights
   \(p,1-p\). With \(d=1\), both the resolved and target laws branch.
3. **Continuous channels.** Let
   \(\mathsf{Ch}(a,a)=[0,1]\), let every channel target \(a\), and use
   Lebesgue measure. Then
   \(\mathsf P^{\rm res}\) is nonatomic while
   \(\mathsf P^{\rm tgt}=\delta_a\). The two half-intervals have positive
   measure even though every individual channel has mass zero.

The positive-family criterion in Replacement Definition 12 handles the
continuous case correctly.

### P5. Plurality, support, and positive-measure branching

Two inequivalent channel objects establish structural plurality only. They
do not establish probabilities. If

\[
 \mathsf{Ch}(a,a)=\{\kappa_0,\kappa_1\},
 \qquad \mu_{a,a}=\delta_{\kappa_0},
\]

the structural catalogue is plural but there are not two disjoint
positive-measure channel families. Conversely, a nonatomic measure can
branch between positive-measure families without giving positive mass to any
singleton. Version 3 makes both distinctions correctly.

### P6. A primitive target kernel cannot determine resolved probabilities

Let both \(\kappa_0,\kappa_1\) target \(a\). For every \(p\in[0,1]\),

\[
 \mu^{(p)}_{a,a}
 =p\delta_{\kappa_0}+(1-p)\delta_{\kappa_1}
\]

pushes forward to the same primitive target kernel \(\delta_a\). With
\(d=1\), all target laws are \(\delta_a\), while the resolved laws are
different Bernoulli laws. A supplied target \(\mathsf M\) therefore cannot
create a resolved probability or choose a disintegration. Definition 10A
and the new outcome coordinates state this nonidentifiability correctly.

### P7. Paper 13D fusion and retained bond invariants

For a fixed component family of one atomic sort, Paper 13D has one unordered
n-ary fusion generator. Its source partition, occurrence union, target
species, and simultaneous structural syntax are fixed before fresh
cross-pair seeds are sampled. The generator carries within-component bonds
and draws one fresh seed for every cross-component unordered pair.

The complete bond field is a child history value. Its point-free orbit and
every invariant measurable coarse output \(J(H)\) have the accepted
pushforward law \(J_*\mathbf\Gamma_D\). Total forgetting leaves the one
resolved channel. Complete or partial retention creates no additional
resolved channel object.

### P8. Search for a hidden same-input resolved channel

The complete Paper 13D generator inventory was rechecked. Atomic
\(U_J,Q_J^0,Q_J^r,D,R_c\), stable maps, erasure, tensor, and the n-ary
fusion generator each have fixed typed syntax. Their stochastic values are
histories. No second resolved simultaneous-fusion generator is hidden by
target equality.

There are inequivalent whole-complex syntax trees: primitive \(U_J\) versus
staged \(D\circ Q_J^0\), simultaneous versus staged fusion, and tensor versus
fused complexes. These establish possible whole-complex plurality, but the
accepted law supplies no autonomous measure over them. They remain
whole-selector residue rather than constructed measure-supported branching.

### P9. Projectivity and the whole-selector residue

The amendment does not alter the exact deletion system. Uniform
one-occurrence deletion remains

\[
 K_{n+1,n}(x,y)=\frac{m(x,y)}{n+1},
\]

and projectivity remains

\[
 P_nK_{n,m}=P_m.
\]

For positive equal-orbit weights, direct rearrangement gives

\[
 \sum_x\frac{m(x,y)}{n+1}
 \frac{w_{n+1}(x)}{w_n(y)}
 =\frac{Z_{n+1}}{Z_n}.
\]

For groupoid activity \(u_n/a_y\), the ratio acquires
\((a_y/a_x)(u_{n+1}/u_n)\); labeled conventions retain their distinct
factorials. These equations remain correct.

As a fresh projective control, give every occurrence one of three iid colors
with probability vector
\(\theta=(\theta_1,\theta_2,\theta_3)\). The induced point-free color-count
laws commute with uniform deletion for every
\(\theta\) in the two-dimensional simplex. Projectivity therefore leaves a
continuous parameter space.

The residual whole-selector object remains an unconstructed set or groupoid.
No vector-space or manifold dimension is assigned.

### P10. Resolved, target, character, and outcome labels

The retired umbrella channel-law label was ambiguous. The replacement
coordinates correctly allow:

- a resolved-law family with one target law;
- one resolved law with several target outcomes;
- a character family whose resolved and target laws are both invariant;
- a target law with no constructed resolved lift; and
- both laws unconstructed when no physical channel measure exists.

The countable \(d_r\) and continuous \(d_\lambda\) controls still have many
characters and one deterministic target law. With a uniquely specified
single resolved channel over each target, they also have one resolved law.
They do not promote a physical result coordinate.

### P11. Resolved post-hoc representation no-go

At target level, every associative Markov convolution has the circular
representation

\[
 \mathsf M=\mathsf P^{\rm tgt},\qquad d=1.
\]

At resolved level, every already normalized resolved kernel \(R_{a,b}\)
whose target pushforward is associative has the circular representation

\[
 \mu=R,\qquad d=1.
\]

Both equations reproduce probabilities already supplied; neither derives
measure provenance. Moreover, the family \(\mu^{(p)}\) in P6 shows that a
target representation does not identify its resolved representation.

The resolved no-go is correct once “resolved kernel” is actually part of the
input. The composite's failure is that Definition 10A does not type such a
kernel before Theorems 3 and 6 use it.

### P12. Occurrence propensity is separate from both conditional laws

For any fixed normalized resolved law \(R\), add a no-composition outcome
\(\bot\) and define

\[
 W_q(\bot)=1-q,\qquad
 W_q(d\kappa)=qR(d\kappa).
\]

Any two \(q_1,q_2\in(0,1]\) give the same resolved law conditional on
composition and different occurrence propensities. Pushing through
\(\tau\) gives the same conclusion for the target conditional law. Neither
conditional level determines \(q\). At \(q=0\), both conditional kernels are
counterfactual structure not identified by the whole measure.

### P13. Affected version-2 regressions

| regression | composite result |
|---|---|
| same-target two-channel control | repaired and passed |
| total/full/coarse bond forgetting | passed; every retained invariant remains a Gamma pushforward |
| countable and continuous character families | passed; many characters, one deterministic conditional kernel at the relevant level |
| strictly positive \(q\) comparison and \(q=0\) | passed |
| deletion Markov kernel and Chapman–Kolmogorov | unchanged and passed |
| orbit, inverse-automorphism, and labeled transfer bases | unchanged and passed |
| aggregate normalization versus retained-class projectivity | unchanged and passed |
| projective continuous freedom | passed by the three-color control |
| trace normalizability under periodic endpoint action | unchanged; equal positive activity can diverge |
| boundary phase coexistence | unchanged; one local specification need not select one state |
| stationarity, reversibility, Gibbs, relative-MaxEnt, and Born forms | unchanged; post-hoc adapted inputs remain nonidentifying |
| selector-residue dimension | unchanged; no dimension is assigned |
| resolved versus target gauge | algebraic cancellation passes, subject to the same missing resolved-kernel typing |
| resolved conditional measurability | **failed** by the non-Borel-family countermodel |

### P14. Accepted-law result versus general controls

The exact accepted-law result is:

> A fixed Paper 13D simultaneous-fusion family has one resolved unmarked
> generator and one target class. Fresh cross-bond values and every invariant
> coarse output are child histories with Gamma-pushforward laws. No accepted
> autonomous measure over alternative whole-complex syntax is supplied.

The following are general controls only:

- same-target finite resolved branching;
- multiple-target hypergroup branching;
- nonatomic continuous resolved branching;
- positive-character normalization;
- resolved and target gauge invariance;
- target and resolved representation no-go theorems; and
- projective families with free parameters.

None constructs the physical channel census, \(\mu\), character,
composition closure, resolved law, target law, or whole selector.

### P15. Fresh semantic countermodels

The following constructions are fresh to this composite review and are not
implementation outputs or parameter fits.

1. **Nonmeasurable resolved family.** The non-Borel \(V\) construction in
   Section 2 has a measurable associative target kernel and normalized
   pointwise resolved measures but no measurable resolved conditional kernel.
2. **Primitive-target lift family.** The continuum
   \(\mu^{(p)}=p\delta_{\kappa_0}+(1-p)\delta_{\kappa_1}\) has one target law
   and continuously many resolved laws.
3. **Nonatomic same-target branching.** Lebesgue measure on a continuous
   channel interval gives positive-measure branches, zero singleton masses,
   and a deterministic target law.
4. **Multiple-target resolved hypergroup.**
   \(M_{a,a}=p\delta_{\mathbf1}+(1-p)\delta_a\) gives both resolved and target
   branching and is associative for every \(0<p<1\).
5. **Two-parameter projective family.** Three-color iid count laws are
   projective for every point in the probability simplex.
6. **Identical child laws, different parent odds.** Fix two parent complexes
   \(A,B\) and fixed child kernels \(\Gamma_A,\Gamma_B\). The whole laws
   \[
    \widehat\Gamma_i(\chi,H)
    =\Pi_i(\chi)\Gamma_\chi(H)
   \]
   with \(\Pi_1(A,B)=(1/4,3/4)\) and
   \(\Pi_2(A,B)=(3/4,1/4)\) recover identical child kernels and different
   parent occurrence laws.

## 4. Full version-3 product vector

Every conservative coordinate survives:

    P18-SECTOR-REFERENT-CONTRACT-CONSTRUCTED
    P18-BOUNDED-SECTOR-CENSUS-UNCONSTRUCTED
    P18-GLOBAL-SECTOR-COMPLETION-UNCONSTRUCTED
    P18-CURRENT-GAMMA-STRUCTURAL-BRANCHING-FORK-PROVED
    P18-NONTRIVIAL-STRUCTURAL-BRANCHING-UNCONSTRUCTED
    P18-PHYSICAL-CHANNEL-MEASURE-UNCONSTRUCTED
    P18-COMPOSITION-CLOSURE-UNPROVEN
    P18-POSITIVE-CHARACTER-UNTESTED-NO-PHYSICAL-CHANNEL-MEASURE
    P18-RESOLVED-CHANNEL-LAW-UNCONSTRUCTED
    P18-TARGET-SECTOR-LAW-UNCONSTRUCTED
    P18-WHOLE-SELECTOR-UNCONSTRUCTED
    P18-ACTUALIZATION-UNCONSTRUCTED
    P18-CHRONOLOGY-NOT-EVALUATED
    P18-DIMENSION-NOT-EVALUATED
    P18-SIGNATURE-NOT-EVALUATED
    P18-METRIC-NOT-EVALUATED
    P18-CURVATURE-NOT-EVALUATED
    P18-GRAVITY-NOT-EVALUATED

No implementation, repair, staging, commit, physical parameter selection,
Paper 17 evaluation, or downstream geometric selection is authorized by this
report.
