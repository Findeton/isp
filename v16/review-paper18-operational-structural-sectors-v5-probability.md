# Paper 18 version-5 probability and identifiability review

Date: 2026-08-21

Seat: **P -- probability, projectivity, and identifiability**

Verdict: **REVISE**

First decisive issue: **the ordered composite assigns the global symbol
\(\mathfrak R\) to two incompatible objects.**

The version-5 observable-freeze idea and its probability controls are
otherwise coherent. In particular, the countable-modification coarse bundle
is a genuine measurable-kernel model, while the predeclared product-Borel
index model is not. The decisive defect is earlier and literal: version-2
Definition 17 defines \(\mathfrak R\) as the groupoid or set of complete
positive occurrence laws, while version-5 Definition 10B defines

\[
 \mathfrak R=(\mathcal C,\Xi,p,\tau,\mathcal O)
\]

as the resolved-channel observable contract. The former is a
measure-dependent selector-residue moduli object; the latter must be frozen
before any measure. Version 5 does not name a replacement of version-2
Definition 17, and its precedence rule leaves every unmentioned clause
literal. Consequently the composite's instructions to freeze, use theorems
relative to, and later report \(\mathfrak R\) are not uniquely typed. This
violates the claimed unique-composite contract and requires a new versioned
mathematical amendment. This report supplies no repair.

## 1. Integrity, scope, and blindness

I authenticated and read every assigned artifact completely. Ordinary
SHA-256, newline count, and byte count were:

| artifact | ordinary SHA-256 | lines | bytes |
|---|---:|---:|---:|
| version-2 base | `b9dbcbd40e4f2e2eb1b18c4b5e98ba4d33eb491a5af791e9106369a53c51e614` | 1165 | 41256 |
| version-3 amendment | `496942b2a742ee2fe81561790e185aba6a3fcc865630c23ca278c3067c80f6dd` | 318 | 10598 |
| version-4 amendment | `33f1e9a05bdc16b7aa96831fe1e8bc4c3bd4ca5095d2f79cbbe0c6d32abe8137` | 357 | 13093 |
| version-5 amendment | `d3bb5b6f20941319b650ba78a7d55e3e298090c1c7ba7d5647f1789da54ca41a` | 263 | 11030 |
| version-5 construction note | `d7187463e1ea4d91df89a8b1309741d0463d8b83214a5a11b8806832a3c1fedb` | 67 | 2887 |
| version-5 review protocol | `2c48e5d681b07ff802cd526c5e8c3de1f0000abd897e5b413b9c1da8d6a721ba` | 148 | 6985 |
| version-4 adjudication | `5671861f1db4a8070bc604c87d0aa7f57f3a2d173d2094a3edd9865b6f19f11f` | 104 | 4732 |

For inherited regressions, I additionally authenticated and read the bound
version-2 and version-3 adjudications at
`172f8fa73d3f3d06703c6128bb53ccf28f11936d8210a8e1a3603a9566f8468b`
and
`f35e91d9dd5b68aefcd75a55612f64ba15e9f1d6a30f856eb12f43ff914ec45c`.
I authenticated the accepted Paper 13D law at
`3b91766fe269e8145766f4622f99e9009c3270530670119735e6045a473de5c9`
before searching its relevant generator, trace, fusion, and history clauses.

I did not inspect, list, contact, summarize, or infer any sibling report or
reviewer. Frozen adjudications were read only as binding inputs. I wrote only
this designated report and performed no implementation, parameter fitting,
downstream evaluation, repair, staging, or commit.

## 2. P1--P2 -- frozen event algebra and the four sigma-algebra attacks

The probability law is correctly defined by the frozen total event algebra,
not by an external fiber numbering. The two non-Borel models can be made
fully explicit.

Let \(X\) be an uncountable standard Borel input space, let
\(\mathcal C=X\times\{0,1\}\), and give both points over \(x\) the same
target. Choose a non-Borel \(V\subset X\), and set

\[
 w(x)=
 \begin{cases}
  1/3,&x\in V,\\
  2/3,&x\notin V,
 \end{cases}
 \qquad
 \mu_x=w(x)\delta_{(x,0)}+(1-w(x))\delta_{(x,1)}.
\]

### Predeclared product-Borel index: rejected

With the full product-Borel algebra and predeclared descriptor
\(\ell(x,i)=i\), the total event

\[
 E_0=X\times\{0\}
\]

is measurable and has probability \(w(x)\). The event map is nonmeasurable,
so Definition 10A rejects the family. Deleting \(E_0\) after seeing that
failure changes the frozen referent and violates no-post-hoc-coarsening.

### Countable-modification coarse algebra: accepted

The intended coarse model is realized by

\[
 \Xi_c=\left\{
 (A_0\times\{0\})\cup(A_1\times\{1\}):
 A_0,A_1\in\mathcal B(X),\quad
 A_0\mathbin\triangle A_1\text{ is countable}
 \right\}.
\tag{P.1}
\]

This is a sigma algebra: complements preserve the symmetric difference, and
the symmetric difference of two countable unions is contained in the
countable union of the individual symmetric differences. It contains every
saturated cylinder \(p^{-1}A\), so \(p\) and a same-target map are
measurable. It induces the full two-point algebra on every fiber because
point-local events, such as \(\{(x,0)\}\), are admitted. It omits
\(X\times\{0\}\), since the two sheet projections of that set differ on
all of uncountable \(X\).

For an event in (P.1), put \(N=A_0\mathbin\triangle A_1\). Its event map is

\[
 x\longmapsto
 w(x)\mathbf1_{A_0}(x)+(1-w(x))\mathbf1_{A_1}(x).
\]

Outside countable \(N\), this is simply the common Borel indicator; on
\(N\), it is an arbitrary countable modification. It is therefore Borel.
Thus the same pointwise measures form a valid kernel on \(\Xi_c\), with
positive pointwise branching at every input and no physical uniform
channel-index event. Adding the absent external index after seeing the
kernel changes the referent and violates no-post-hoc-refinement.

The two attacks are symmetric. Coarsening does not rescue the first frozen
referent, and refinement does not retrospectively invalidate the second.
Each alteration defines a new referent proposal requiring its own
independent law evaluation.

## 3. P3 -- pointwise and descriptor-coherent positivity

For pointwise branching at fixed \(x\), each
\(A_i\in\Xi_x\) is typed because the trace-algebra definition supplies a
total extension \(E_i\in\Xi\). If disjoint total extensions are desired,
replace one extension by \(E_0\setminus E_1\); its fiber section remains
\(A_0\). The pointwise predicate itself makes no claim that one pair of
events tracks a branch across other inputs.

For a predeclared measurable descriptor \(\ell\) and measurable descriptor
event \(D_i\), put

\[
 f_i(x)=\mu_x\bigl((\ell^{-1}D_i)_x\bigr).
\]

The preimages are total events in the frozen \(\Xi\), so Definition 10A
makes each \(f_i\) measurable. Hence the positivity sets

\[
 \{x:f_i(x)>0\}
\]

and their intersection with the declared measurable region \(B\) are
measurable. This proves exactly the measurability claimed for
descriptor-coherent witnesses. The existential locus of all possible
pointwise witnesses need not be measurable; the first fresh countermodel in
Section 13 shows why the amendment correctly makes no such global claim.

## 4. P4 -- descriptor coherence supplies no probabilities

Freezing \(\ell\) makes its preimage events available for testing; it does
not assign their masses. On the same frozen product bundle with a physical
red/blue descriptor, both

\[
 \mu_x=\delta_{\mathrm{red}}
 \quad\text{and}\quad
 \nu_x=\tfrac12\delta_{\mathrm{red}}+\tfrac12\delta_{\mathrm{blue}}
\]

are measurable kernels. The first has no resolved branching, while the
second has descriptor-coherent branching everywhere. Choosing between them
still requires an independently physical provenance. Thus coherence is a
cross-input identity condition, not a probability source.

## 5. P5 -- resolved probability kernel and exact target pushforward

Write \(x=(a,b)\) and \(g(\kappa)=d(\tau\kappa)\). The function \(g\) is
positive and total-\(\Xi\)-measurable. For any fiber event
\(F\in\Xi_x\), choose a total extension and define

\[
 \mathsf P^{\rm res}_x(F)
 =\frac1{d(a)d(b)}\int_F g(\kappa)\,\mu_x(d\kappa).
\]

The value is extension-independent, is countably additive on the fiber, and
is measurable in \(x\) for every total event by (V4.1) applied to
\(\mathbf1_Eg\). Its total mass is

\[
 \frac{\int d(\tau\kappa)\,\mu_x(d\kappa)}{d(a)d(b)}
 =\frac{\int d(c)\,\mathsf M_x(dc)}{d(a)d(b)}=1.
\]

Thus (V4.5) remains a resolved probability kernel relative to the frozen
referent, not merely a pointwise family. No standard-Borel or regular
conditional probability hypothesis enters.

For every target event \(A\),

\[
\begin{aligned}
 (\tau_*\mathsf P^{\rm res}_x)(A)
 &=\frac1{d(a)d(b)}
   \int_{\tau^{-1}A}d(\tau\kappa)\,\mu_x(d\kappa)\\
 &=\frac1{d(a)d(b)}\int_A d(c)\,\mathsf M_x(dc)
 =\mathsf P^{\rm tgt}_x(A).
\end{aligned}
\]

Equation (V4.6) is therefore exactly the target pushforward.

## 6. P6 -- finite, nonatomic, multiple-target, varying, and hybrid laws

All inherited positive controls pass once their observable contracts are
frozen before their kernels.

1. **Finite same target.** For two channels
   \(\kappa_0,\kappa_1:a\boxtimes a\to a\), resolved counting measure gives
   \(\mathsf M_{a,a}=2\delta_a\), \(d(a)=2\), resolved probabilities
   \(1/2,1/2\), and deterministic target probability.
2. **Several targets.** In the finite based algebra
   \(a^2=\mathbf1+2a\), \(d(a)=1+\sqrt2\). The unit-target slot has
   probability \(d(a)^{-2}\), each of the two \(a\)-target slots has
   probability \(d(a)^{-1}\), and the two target probabilities are
   \(d(a)^{-2}\) and \(2d(a)^{-1}\).
3. **Nonatomic same target.** A Borel \([0,1]\) fiber with Lebesgue measure
   and constant target has two positive half-interval events although every
   singleton has zero mass.
4. **Varying finite fibers.** On a countable discrete input base, one or two
   uniformly weighted same-target channels chosen by a measurable input
   predicate form a genuine kernel.
5. **Hybrid fibers.** The trace-Borel bundle
   \((A\times\{0,1\})\cup(A^c\times[0,1])\), with half-half atomic measure
   on measurable \(A\) and Lebesgue measure on \(A^c\), has measurable
   event maps by section measurability and parameterized integration.
6. **Non-standard fibers.** An uncountable Bernoulli cube with its cylinder
   sigma algebra and directly constructed product measure is admissible on a
   finite input base. No disintegration theorem is invoked.

## 7. P7 -- six predicates remain distinct

| predicate | required datum | does not imply |
|---|---|---|
| set-level plurality | inequivalent elements of \(\mathcal C_x\) | measurable events or weights |
| pointwise branching | two disjoint positive \(\Xi_x\)-events at one \(x\) | a common cross-input identity |
| descriptor-coherent branching | a frozen physical descriptor and two positive descriptor events throughout \(B\) | measure provenance or target branching |
| target branching | positive mass on disjoint target events | resolved-channel identity |
| occurrence propensity | a whole-law factor \(q(a,b,\xi)\) | a change in either conditional law |
| actualization | selection of an actual complex or history | anything from normalization alone |

The coarse model separates pointwise from descriptor-coherent branching.
The same-target controls separate both resolved predicates from target
branching. Two distinct positive \(q\)'s preserve the same conditional law,
and at \(q=0\) that conditional is unidentifiable counterfactual structure.
No normalized law supplies actualization.

## 8. P8 -- target kernels cannot reconstruct resolved data

A target kernel contains no resolved total set, projection, event algebra,
descriptor family, or resolved kernel. Even on one fixed product bundle,
the two measurable resolved kernels with constant sheet weights
\((1/3,2/3)\) and \((2/3,1/3)\) have the same deterministic same-target
pushforward and different resolved laws. A fortiori, the target law cannot
choose between different bundles or sigma algebras. On a non-standard
branch, no regular disintegration may be inferred. Version 5 preserves all
of these no-go statements.

## 9. P9 -- measurable gauge and normalized representations

For positive measurable \(h\), the density

\[
 \frac{h(a)h(b)}{h(\tau\kappa)}
\]

is total measurable. Formula (V4.1) gives the transformed event maps, and
the stated finiteness assumption gives a resolved kernel. Substitution
cancels every \(h\)-factor in both resolved and target probability laws.
The transformation changes neither \(\Xi\) nor \(\mathcal O\); changing
either is a referent change, not gauge.

For a concrete nontrivial gauge, take \(a^2=\mathbf1+a\),
\(d(a)=\varphi\), and \(h(a)=s>0\). The transformed resolved weights at
\((a,a)\) are \(s^2\) on the unit-target channel and \(s\) on the
\(a\)-target channel, with \(d^h(a)=s\varphi\). Both levels retain
probabilities \(\varphi^{-2}\) and \(\varphi^{-1}\) for every \(s\).

Writing an already selected resolved kernel as
\(\mu=\mathsf P^{\rm res},d=1\), or an already selected target convolution
as \(\mathsf M=\mathsf P^{\rm tgt},d=1\), derives neither the frozen
referent nor the probabilities. The normalized-representation no-go remains
valid at both levels.

## 10. P10 -- target finite-word closure does not promote resolved paths

For any target bracketing, the transformed final measure is

\[
 \frac{d(z)}{\prod_i d(a_i)}\,\mathsf M^{(n)}(dz).
\]

The inherited convolution hypotheses make \(\mathsf M^{(n)}\) finite and
target-bracketing independent. This proves the corresponding target result.
It constructs no resolved composition category, resolved path kernel,
associator, or coherence law. Version 5 does not conflate the two levels.

## 11. P11 -- projectivity and deletion remain separate

Uniform deletion is

\[
 K_{n+1,n}(x,y)=\frac{m(x,y)}{n+1},
\]

not raw multiplicity. Projectivity is the class-level equation
\(P_nK_{n,m}=P_m\), with orbit, inverse-automorphism, and labeled bases kept
distinct. The binary count family

\[
 P_n^{(p)}(k)=\binom nkp^k(1-p)^{n-k}
\]

is projective for every \(p\in[0,1]\), and mixtures remain projective.
Deletion therefore need not identify a parameter or boundary state, and it
is not resolved-channel composition.

## 12. P12--P14 -- Paper 13D and inherited probability regressions

Paper 13D declares one permutation-invariant simultaneous n-ary fusion
generator for each fixed finite component family and atomic sort. Fresh
cross-component bonds are sampled by that generator's evaluator and retained
in its history fiber; their invariant outputs have Gamma pushforward laws,
not new resolved-channel identities.

The hidden-channel search again finds the explicit parallel whole-process
syntax: \(U_J\) and \(D\circ Q_J^0\) share endpoint boundary types but have
different traces and kernels, and a deliberately staged fusion sequence is
distinct from a simultaneous n-ary fusion. These are not second
simultaneous-fusion generators. The composite already retains them as
whole-process or resolved-path alternatives and correctly observes that
Paper 13D supplies neither a frozen total structural-channel observable
contract nor an autonomous kernel over them. They therefore promote no
branching or selector-law coordinate.

The remaining inherited probability regressions pass:

- countable and continuous deterministic addition admit character families
  but only one induced deterministic conditional law;
- support, topology, a groupoid, a descriptor, or a normalized
  representation supplies no physical measure provenance;
- pairwise finiteness does not replace finite-word finiteness;
- target associativity does not replace resolved path coherence;
- point masses are unnecessary for positive-family branching;
- orbit, groupoid, labeled, marked-restriction, and deletion conventions do
  not share a probability coefficient;
- exact projectivity can retain continuous parameter and mixture freedom;
- a conditional channel law does not fix composition propensity \(q\); and
- no current physical measure, character, resolved law, target law, whole
  selector, or actualization is constructed.

## 13. P15 -- six fresh semantic countermodels

These are additional to the frozen version-5 controls.

1. **A nonmeasurable pointwise-branching locus.** On the coarse algebra
   (P.1), let \(V\subset X\) be non-Borel and use weights
   \((1/2,1/2)\) for \(x\in V\) but \((1,0)\) for \(x\notin V\). Every
   admitted total-event map is still measurable by the countable-modification
   proof, so this is a valid kernel. Pointwise branching occurs exactly on
   non-Borel \(V\). This refutes any unstated inference that the existential
   pointwise-branching locus must be measurable; version 5 correctly claims
   measurability only for fixed total or descriptor-coherent witnesses.

2. **A nontrivial twofold cover without a physical sheet name.** Let
   \(X=\mathbb T^2\), \(\mathcal C=\mathbb T^2\), and
   \(p(z,w)=(z^2,w)\), with Borel structures and the uniform probability on
   each two-point fiber. Finite-fiber averaging makes every event map Borel.
   The cover has no continuous global sheet section, although an auxiliary
   Borel enumeration exists. If no such enumeration is independently
   physical and predeclared, the model has pointwise branching without a
   sheet descriptor. This refutes forced physical trivialization.

3. **One descriptor, two probability theories.** On the frozen red/blue
   product bundle, the deterministic-red kernel and the half-half kernel of
   Section 4 share the same descriptor family and event algebra. One has no
   branching and the other has descriptor-coherent branching. This refutes
   descriptor coherence as a source of weights.

4. **One target law, two resolved laws on one referent.** Keep the same
   frozen two-sheet bundle, descriptor, and constant target, but use constant
   resolved weights \((1/3,2/3)\) and \((2/3,1/3)\). Their target laws are
   identical while their descriptor-event probabilities differ. This
   refutes target-law identifiability even after the referent is fixed.

5. **Descriptor coherence across hybrid fibers.** Let \(A\subset X\) be
   Borel and take fibers \(\{0,1\}\) on \(A\) and \([0,1]\) on \(A^c\),
   with half-half atomic and Lebesgue kernels respectively. Freeze the
   descriptor \(\ell(x,t)=\mathbf1_{\{t\leq1/2\}}\). Both descriptor events
   have positive mass at every input, so branching is descriptor-coherent
   across the hybrid bundle, while a constant target law remains
   deterministic. This refutes coherent branching implying constant fiber
   type or target branching.

6. **Conditional law versus occurrence and actuality.** Fix any resolved
   conditional law and form whole laws with \(q_1=1/3\) and \(q_2=2/3\).
   They have identical conditional resolved and target laws and different
   no-composition mass. Neither normalized whole law selects an actual
   history. This separates conditional probability, occurrence propensity,
   and actualization.

## 14. Full version-5 product vector

The decisive typing defect does not justify any physical promotion. The
conservative vector remains:

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

No implementation, selector construction, parameter selection,
actualization, Paper 17 evaluation, or successor-paper work is authorized.
