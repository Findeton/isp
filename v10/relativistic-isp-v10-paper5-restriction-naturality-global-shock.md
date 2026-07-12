# Relativistic ISP v10 Paper 5: Strong Unmarked Restriction Naturality Collapses Birth to an Empty/Full Precursor Mixture

## Law-relative predictive quotients, fixed deterministic token capacity, and the profinite limit

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** revised after hostile-review round 1, 2026-07-11. Three independent
reviews returned MAJOR REVISION while confirming the core collapse theorem.
All concrete openings were investigated before round 2.

**Receipt:** `v10/code/d4_boundary_sufficiency_exact.py` — 23/23 exact checks.
All production source is under `v10/code/` and uses only the Python standard
library.

## Abstract

D3 established a clean separation: adding a maximal event above a down-set
commutes with restriction of the incidence structure, while two positive
global-prefix probability kernels fail even ancestor-closed autonomous
restriction. This paper asks whether SHARD's no-silent boundary principle can
repair that failure with a finite sufficient mark and thereby select a local
interacting click law.

First, the unmarked problem collapses. Assign to every finite unmarked poset
`P` a covariant probability distribution on its down-sets and require exact
naturality under every induced-subposet restriction. Then one constant
`p in [0,1]` exists such that

$$
\kappa_P=(1-p)\delta_\varnothing+p\delta_P.
$$

No proper nonempty precursor survives. The proof needs only a point, a
two-chain, and a three-point `V` order, followed by pair restriction in an
arbitrary poset. An independent exact census enumerates all labeled posets
through three vertices, 111 down-set variables, and 1,087 covariance,
normalization, and restriction equations. The signed affine solution space is
three-dimensional—not the one dimension preregistered—because equality
constraints allow two cancellation directions. Probability positivity is
load-bearing: exact zero-sum certificates kill every proper ideal. The
executable checks 1,304 such ideals through four vertices and all 3,671 cuts
of the surviving empty/full family.

The conclusion depends on the restriction category. Convex cuts retain the
same proof. Ancestor-closed stems do not: the minimal-layer ideal is a
nontrivial natural law. Causal intervals likewise admit independent
component-wise mixtures. Collar-complete and typed-carrier cuts are not
objects of the unmarked poset arena and remain conditional on a marked diamond
construction. The theorem is therefore about strong silent all-subset/convex
autonomy, not locality in general.

Second, a supplied non-natural law always admits an exact predictive quotient.
For a cut `K`, sum the full precursor weights over all completions with the
same visible intersection. For fixed law and retained structure, equality of
the normalized completion-weight vector is the coarsest deterministic exact
predictive partition. It is a decoder target, not a constructed record. It
reproduces all 7,342 audited D3 contexts. But it is law-relative: the same three-antichain cut gives
visible inclusion `1/2` under one D3 law and `9/14` under the other. The target
unpacks a supplied law; it does not derive one or construct its carrier.

Third, uniform fixed deterministic capacity fails for this repair. On an
`n`-chain retained to its minimal point, the uniform down-set law gives
`n/(n+1)`. These values are pairwise distinct, so exact prediction through
depth `N` requires at least `N` message states and `ceil(log2 N)` bits. A full
profinite residue tower may encode unbounded information, but no fixed finite
quotient does. Moreover `j!` converges to zero in the profinite integers while
`j!/(j!+1)` tends to one, so this exact prediction has no continuous extension
to the standard profinite integer completion.

The verdict is

$$
\boxed{
\texttt{ALL-SUBSET-UNMARKED-COLLAPSE}
+
\texttt{LAW-RELATIVE-UNBOUNDED-DETERMINISTIC-TARGET}.}
$$

This is not a no-go against stochastic marks, expanding boundaries,
unbounded-but-finite values, approximation, or specially factorized local
laws. It is a refusal of the hoped-for conclusion: no-silent accounting plus
unmarked all-subset autonomy does not select a bounded record-local
interacting extension law.

## 1. The problem left by D3

Let `P` be a finite causal-order shadow and `D` the down-set forming the past
of a candidate new maximal event. For retained old records `K`, incidence
restriction is exact:

$$
P[D]|_{K\cup\{e\}}=(P|_K)[D\cap K].
$$

But a full probability distribution on `D` need not push forward to the same
formula recomputed on `P|K`. D3's smallest witness is

$$
(1/3,2/3)\ne(1/2,1/2).
$$

The difference is information about discarded precursor completions. There
are two conceptually distinct repairs:

1. demand that the unmarked law be autonomous under every restriction;
2. retain a boundary mark recording enough discarded influence to reproduce
   the pushforward.

D4 classifies both.

## 2. Strong unmarked restriction naturality

For each finite poset `P`, let `J(P)` be its down-sets and let

$$
\kappa_P:J(P)\to[0,1]
$$

be a probability distribution. For every retained subset `K`, require

$$
\kappa_{P|K}(A)
=
\sum_{D\cap K=A}\kappa_P(D)
\qquad(A\in J(P|K)).
$$

The assignment is also natural under relabeling.

This is stronger than existence of a global path measure. It says every
unmarked retained subsystem is an autonomous instance of one universal law.
Barandes indivisibility does not force this axiom; D4 asks what follows if it
is imposed.

## 3. The unmarked global-collapse theorem

### Theorem 3.1

Every covariant probability family on down-sets of all finite unmarked posets
that is natural under every induced-subposet restriction has the form

$$
\kappa_P=(1-p)\delta_\varnothing+p\delta_P
$$

for one `p in [0,1]`, independent of `P`.

### Proof

Let `p` be the inclusion probability on the one-point poset.

Take a two-chain `a<b`. Its ideals are

$$
\varnothing,\quad\{a\},\quad\{a,b\}.
$$

Restriction to `{a}` says

$$
\kappa(\{a\})+\kappa(\{a,b\})=p,
$$

while restriction to `{b}` says

$$
\kappa(\{a,b\})=p.
$$

Hence the proper ideal `{a}` has probability zero.

Now take the `V` order `a<c`, `b<c`. Restriction to the chains `{a,c}` and
`{b,c}` gives the nonnegative zero sums

$$
\kappa(\{a\})+\kappa(\{a,b\})=0,
\qquad
\kappa(\{b\})+\kappa(\{a,b\})=0.
$$

Positivity forces all three displayed terms to vanish. Restriction to the
antichain `{a,b}` therefore gives zero probability to both singleton ideals.

Finally, let `D` be a proper nonempty ideal of any finite `P`. Pick `x in D`
and `y notin D`. Downward closure forbids `y<x`. If `x` and `y` are
incomparable, their pair is convex and `D` restricts to a forbidden antichain
singleton. If `x<y`, take a saturated chain from `x` to `y` and let `u<v` be
its first cover relation that leaves `D`. Then `u in D`, `v notin D`, the
two-point cover subset is convex, and `D` restricts to the forbidden bottom
singleton. In either case, naturality expresses the zero pair probability as
a sum of nonnegative probabilities including `kappa_P(D)`, hence
`kappa_P(D)=0`.

Only the empty and full ideals remain. Normalization gives masses `1-p_P` and
`p_P`; restriction to one point gives `p_P=p`. ∎

### Interpretation

The theorem does not select `p`. More importantly, its survivor is not local.
On the full branch, the new event has every existing event in its past. On the
empty branch it has none. Strong unmarked restriction autonomy has converted
the placement problem into an empty/full universal-precursor mixture. Calling
the full branch a “shock” would add unproved outcome or transport content; the
order establishes only global incidence.

This agrees with D2's symmetry obstruction: an unmarked law cannot select one
proper pair from a symmetric orbit. D4 strengthens that statement across all
finite posets and all induced restrictions.

## 4. Restriction category classification

Theorem 3.1 must not be called a theorem of locality without naming its cuts.
The receipt rebuilds the signed naturality systems through three vertices and
finds affine dimensions

```text
all induced / convex / ancestor-closed stem / causal interval
      3    /    3   /          8           /        8
```

The dimensions describe signed relaxations; positivity remains load-bearing.
More decisively, exact positive controls separate the categories.

### 4.1 All induced and convex cuts

Every cut used in the point/chain/`V` proof is convex. The last step also uses
only a convex pair: an incomparable inside/outside pair when available, or
the first cover crossing the ideal boundary along a saturated chain. Therefore
the same empty/full probability collapse follows if naturality is required for
every convex retained subset. The receipt verifies all 1,304 such proper-ideal
certificates through four vertices, not merely the small proof cells.

### 4.2 Ancestor-closed stems

Let `Min(P)` be the minimal elements of `P`. This is a down-set. If `K` is an
ancestor-closed stem, an element of `K` is minimal in `P|K` exactly when it was
minimal in `P`. Hence

$$
Min(P)\cap K=Min(P|K).
$$

The deterministic proper-precursor law `D=Min(P)` is therefore stem-natural.
It passes all 1,789 audited stem cuts and fails the top-only chain cut used by
Theorem 3.1. Stem naturality does not collapse to empty/full.

### 4.3 Causal intervals

For the finite audit, interval cuts comprise empty/full identity cuts,
singletons, and closed order intervals with comparable endpoints. Assign an
independent Bernoulli variable to each connected component of the undirected
comparability graph and include a component in full when its variable is one.
Every nontrivial order interval lies inside one component, so its marginal is
the same empty/full Bernoulli law. Across disconnected parents, proper unions
of components survive. The family passes all 2,210 audited interval cuts and
fails the convex cut retaining the two minima of a `V`, where recomputation
would replace inherited perfect correlation by independent variables.

Thus interval-only naturality also admits nontrivial families.

### 4.4 Collar-complete and typed-carrier cuts

An unmarked poset has no screen, collar, projected-joint provenance, or direct
carrier type. D4 cannot honestly rerun those categories by renaming a vertex
subset. They are **boundary-conditional** if a marked carrier is supplied and
**refused** otherwise. Their classification is the next marked-diamond
problem, not an unmarked theorem.

## 5. Exact linear audit and why positivity matters

The independent finite audit uses every labeled strict poset through three
vertices:

```text
1, 1, 3, 19.
```

It assigns one rational variable to every down-set probability, producing 111
variables and 1,087 exact equations from normalization, relabeling covariance,
and every induced-subset pushforward.

The preregistration predicted affine dimension one. Exact elimination instead
gives

```text
rank = 108
signed affine dimension = 3.
```

This does not refute Theorem 3.1. The linear system permits signed charges,
where positive and negative proper-ideal weights cancel in the `V`-order zero
sums. Probability positivity forbids those directions. The receipt verifies
that the chain singleton is an affine linear consequence, that the two
`V`-order sums vanish, and that nonnegativity kills their terms. It then
certifies the convex cover-or-incomparable pair argument for all 1,304 proper
ideals through four vertices (616 cover-chain and 688 antichain certificates).

This distinction is methodologically important: covariance and consistency
equations alone classify signed charges. A probability theorem must retain
the positive cone.

## 6. Exact completion quotients as decoder targets

Let a supplied law assign positive raw weight `w_P(D)` to every full
precursor. For a retained subset `K`, define

$$
W_{P,K}(A)=\sum_{D\cap K=A}w_P(D).
$$

Then the visible precursor distribution is exactly

$$
q_{P,K}(A)=\frac{W_{P,K}(A)}{\sum_BW_{P,K}(B)}.
$$

### Proposition 6.1 — conditional deterministic predictive sufficiency

Fix a supplied law `L`, a retained structure `S=P|K`, and the visible
precursor alphabet. Consider a deterministic encoder `m(c)` and decoder

$$
F_L(S,m(c))=q_c.
$$

For this decoder contract, equality of `q` is the coarsest exact predictive
partition: at fixed `L` and `S`, two contexts may share a token only if their
`q` vectors agree, and using `q` itself is sufficient.

The vector is a canonical representative of the partition, not a unique or
bit-minimal encoding. This is predictive minimality, not ontological
uniqueness. A finer mark may
retain ancestry, likelihood blocks, holonomy, or other physical data even
when `q` agrees.

The receipt verifies 7,342 contexts across every labeled poset and cut through
four vertices for both positive D3 laws through an independently rebuilt
pushforward. Fixed-law labeled-cover counts are `564/42` for `b=1` and
`601/45` for `b=2` (classes/maximum per raw retained structure). Jointly
canonicalizing the retained poset and probability vector gives fixed-law
counts `144/30` and `168/36`. Pooling both laws gives `756/66` on the labeled
cover and `199/42` on the canonical unmarked quotient. Pooled values diagnose
law dependence; they are not fixed-law minimal token counts.

Most importantly, `q` remains a **decoder target**. D4 supplies no typed
carrier, provenance, pre-sampling encoder, nested-cut update, or gluing law
that computes it from physically available boundary data. It is not yet a
born record.

### Proposition 6.2 — the quotient is law-relative

For the same three-antichain and the same retained point, the two D3 laws give

$$
q(\text{included})=\frac12,
\qquad
q'(\text{included})=\frac9{14}.
$$

Therefore the sufficient vector cannot be computed from the unmarked cut
alone. It is a conditional summary of the already supplied full law.

No-silent discipline can require that this predictive difference not be
erased. It cannot use the difference to derive the law without circularity.

## 7. Uniform deterministic token capacity

Consider the uniform D3 weight law on a chain of `n` old events and retain its
minimal event. The chain has `n+1` ideals: one empty ideal and `n` nonempty
prefixes. Hence

$$
q_n(\text{included})=\frac{n}{n+1}.
$$

### Theorem 7.1 — fixed-token exact no-go

For depths `1,...,N`, an exact deterministic sufficient mark requires at least
`N` distinguishable states and `ceil(log2 N)` bits. No fixed finite alphabet
is sufficient for unbounded chain depth.

**Proof.** The values `n/(n+1)` are strictly increasing. If two contexts share
one deterministic mark, their local predictive distributions must agree.
Therefore distinct depths need distinct marks. ∎

The executable checks 64 depths, six required bits, and the failure of a
three-bit alphabet by depth nine. It also refutes one coarse provenance flag:
both cuts carry `discarded-chain-context-present`, but require `2/3` and
`3/4`. The flag belongs to the cut context; it is not mislabeled as a parent
of the retained minimal record.

### Scope of the no-go

The theorem assumes the boundary mark is:

- present before the candidate extension is sampled;
- deterministic given the full cut context;
- drawn from one uniformly bounded finite alphabet;
- decoded with the fixed law and retained structure as side information;
- not supplemented by depth, a global clock, or any other full-context side
  channel;
- one token for the complete retained one-point boundary, rather than an
  expanding collection of records;
- and exactly sufficient in the zero-error sense, not approximately
  sufficient.

It does not forbid a context-dependent stochastic mark. With two stochastic
mark values and environment-dependent mixing probabilities, many distinct
marginals can be represented—but the mixing law then carries the missing
global information. Nor does it forbid an unbounded integer or rational mark,
an expanding collection of finite records, or approximation.

Consequently “every record contains finite information” is not by itself the
uniform-capacity premise. D4's fixed-alphabet theorem applies only if the
theory supplies a common upper bound on distinguishable boundary states.

### Exact loophole controls

The repaired receipt formalizes four alternatives rather than treating them
as footnotes:

1. **Stochastic token:** take a binary token `M` with
   `P(M=1|n)=n/(n+1)` and decode the precursor as `M`. This reproduces the
   marginal, but the global depth dependence is now in the encoder's mixing
   probability.
2. **Distributed boundary:** six binary carrier records encode depths 1–64;
   unbounded depth requires a growing number of records.
3. **Unbounded finite value:** store the integer `n` and decode
   `n/(n+1)`. Every realization is finite, but there is no uniform alphabet.
4. **Approximation:** beyond depth 99, predicting one has error at most one
   percent, so a finite tail bin suffices once exactness is relaxed.

These models evade Theorem 7.1 by changing one of its premises. None provides
a derived local compositional encoder.

## 8. Profinite boundary marks

A profinite mark is an inverse limit of finite readouts. It can encode more
information across the entire tower than any one finite quotient.

For a fixed residue mark `n mod m`, depths `n` and `n+m` are indistinguishable
but have different exact predictions. Thus no fixed residue stage suffices.

The full standard profinite-integer completion does not admit the exact chain
prediction as a continuous real readout. Indeed `j!` tends to zero
profinally—eventually it is zero modulo every fixed integer—while

$$
\frac{j!}{j!+1}\to1
$$

and the depth-zero prediction is zero. Continuity would require both limits to
agree.

The executable does not claim to prove convergence by eight samples. It
checks the finite shadow through `8!`: divisibility by every `m<=j`, the exact
identity

$$
1-\frac{j!}{j!+1}=\frac1{j!+1},
$$

strict decrease of these errors, and terminal error `1/40321`. The universal
limit is the analytic argument above.

This is not a theorem against every compact mark space. The one-point
compactification adapted to ordinary large depth, for example, can make the
limit continuous by adjoining a point with prediction one. But exact finite
depths remain distinguishable; no fixed finite quotient recovers them all.

This ceiling is specific to the **standard profinite-integer topology** and a
**continuous real-valued readout**. It is not a result about the v9 stem
spectrum, every Stone space, or merely measurable discontinuous decoders.

Profinite organization therefore relocates the growing boundary information
into a compatible tower. It does not make the full inverse-limit point one
finite sealed record.

## 9. Barandes ISP and subsystem memory

Barandes ISP allows a subsystem's future statistics to depend on its full
recorded past and on memory inherited from discarded degrees of freedom. It
does not require the retained unmarked subsystem to be autonomous.

Given a primitive full path measure, the completion quotient is obtained by
conditionalizing and marginalizing that measure. This explains where the
decoder target comes from in the primitive-measure program. It does not derive
the measure, physically locate a carrier, or prove bounded dimension or
capacity.

Representing the quotient by a supplied boundary state is compatible with indivisibility: it
does not assert that a whole interval law factors through ordinary endpoint
propagators. It only records the information required for one chosen
conditional prediction.

## 10. No-silent trichotomy, centers, and diamonds

D1's no-silent principle says physically relevant predictive residue cannot
be discarded without an appropriate center, boundary expansion, or failure
record. D1 did not prove a unique center or a uniformly bounded one. D4 makes
that limitation quantitative for the D3 controls.

Every proposed cut must therefore be typed as one of three sectors:

1. **autonomous:** the retained state alone obeys a proved natural kernel;
2. **boundary-conditional:** a typed carrier `m` is retained and a proved
   decoder/update law uses `(L,S,m)`;
3. **refused:** no permitted sufficient retained state has been supplied, so
   the cut is not a complete physical laboratory.

Theorem 3.1 classifies the first sector for all-subset/convex unmarked cuts.
The completion vector diagnoses what the second sector would need to predict,
but does not construct it. Collar-complete and direct-carrier cuts cannot
enter the second sector until their marks and gluing maps are supplied; they
remain refused otherwise.

A completion vector is not automatically a sealed-diamond center. A physical
mark needs typed provenance and a carrier on the retained boundary. It may
also need to preserve information for outcomes, transport, screens, collars,
and holonomy, not only the next precursor marginal.

D2 can compose supplied marked-support incidence after such a boundary object
is given. It does not derive the quotient's carrier, the full diamond law, or its local
realization.

## 11. What the result says about locality

Neither available route is yet local:

1. strong all-subset/convex unmarked naturality leaves
   universal-precursor incidence;
2. the exact predictive quotient is computed by summing full-history
   completions and has no local encoder.

A global probability measure need not entail a literal centralized machine,
but D4 supplies no finite local specification or decentralized sampler for
the completion quotients. The next positive route must exploit additional
factorization: finite diamond collars, bounded interfaces, or a record-native
Markov blanket that composes messages without inspecting the entire history.

Such a route would weaken “same unmarked law on every subset.” A restricted
history carrying a boundary carrier is not isomorphic to an isolated history
with no environment. This is precisely how marked restriction can evade
Theorem 3.1 without rewriting the old past.

## 12. Consequences for the interacting click law

The v7 survival law may still determine whether a seal occurs over a supplied
evidence increment. It does not determine the universal-precursor parameter
`p`, a physical encoder/carrier for the completion quotient, or the precursor
law summarized by that quotient.

D4 therefore narrows the remaining dynamics problem:

> Find a record-native factorization whose finite typed boundary carrier is
> sufficient under composition and whose update law determines both carrier
> evolution and common-future eligibility without a universe-wide
> normalization.

If no such factorization exists, SHARD must explicitly accept one of the
alternatives D4 leaves open: expanding/unbounded boundary memory, a primitive
global history measure, or approximate subsystem sufficiency.

## 13. Geometry remains downstream

No D4 theorem changes the v9 cone, dimension, stationarity, or scale results.
Universal-precursor incidence is not a plausible local geometry builder,
while the completion-quotient diagnostic has no supplied dynamics of its own. Every
geometric instrument must wait for a selected or explicitly posited marked
law.

## 14. Conclusion

Exact all-subset autonomy is too strong in the unmarked ontology. It does not
produce a local interacting law; it collapses precursor choice to

$$
\varnothing\quad\text{or}\quad P.
$$

For a supplied non-natural law, the normalized completion vector is the
canonical target of a coarsest predictive partition under the fixed decoder
contract. It does not repair the law physically until a carrier and encoder
are supplied. For the D3 controls the target varies with the law and requires
unboundedly many deterministic token values across growing chain contexts.

The resulting boundary is

$$
\boxed{
\texttt{ALL-SUBSET-UNMARKED-COLLAPSE}
+
\texttt{LAW-RELATIVE-UNBOUNDED-DETERMINISTIC-TARGET}.}
$$

The next investigation should not search another unmarked closure. It should
ask whether sealed-diamond collars supply a finite compositional sufficient
state—a marked local carrier/message algebra whose update can be derived or sharply
classified.

## Reproducibility

Run from the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python3 v10/code/d4_boundary_sufficiency_exact.py
```

The receipt uses exact integers and `Fraction` throughout and reports 23/23.

## References

1. J. A. Barandes, “The Stochastic-Quantum Correspondence,” Philosophy of
   Physics 3, 8 (2025), arXiv:2302.10778.
2. J. A. Barandes, “Quantum Systems as Indivisible Stochastic Processes,”
   arXiv:2507.21192.
3. Relativistic ISP v9 Papers 7 and 9.
4. Relativistic ISP v10 Papers 1–4.
