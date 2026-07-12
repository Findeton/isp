# D3 hostile review round 1 — mathematics, measure, and profinite scope

**Referee:** independent mathematics/measure/profinite hostile review

**Date:** 2026-07-11

**Verdict:** **MAJOR REVISION**. The one-event extension theorem, bridge-shadow
mechanics, finite censuses, rational nonselection witness, and labeled-prefix
projective-limit/Radon theorem are correct. The registered kernels, however,
are consistent only along the end-deletion prefix tower; they fail even
ancestor-closed record restriction. The paper must not use unqualified
“projectivity” to transfer the witness into the stronger restriction or
covtree setting. Construction-order quotient compatibility is also asserted
more strongly than the current C2 receipt establishes.

## 1. Frozen artifacts and reproduction

Source hashes reviewed:

```text
ba1bc397a85881b2dcfdad5328dd67e58de6e805d873348e22c374a2e1335e6f  v10/note-d3-profinite-variable-history-extension.md
b44ccd233d6922efcd4100c4eae206ef05032952b3b7cb653d472f73dd414280  v10/relativistic-isp-v10-paper4-profinite-growth-preserves-past-not-law.md
c1d23fe3481e5245724d8625ade897f708e5ae70c788707110995a7b034d00c9  v10/code/d3_profinite_extension_exact.py
```

Command:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python3 v10/code/d3_profinite_extension_exact.py
```

The receipt exited `0` with `RECEIPT: 23/23 checks passed`. Two independent
runs produced identical output SHA-256:

```text
4f6b8a04c0b9db21ab8f4b08359fb6514460ff80ec7c23f9e92eea348958fd40
```

The printed internal payload digest is
`0f2f0ed7157811ec94bfa218b0487c39b3b58422afca1853f79050abb66538ec`.

## 2. Independent finite-order reconstruction

I independently enumerated every upper-triangular transitive strict relation
through five vertices in Ruby. The counts reproduce:

```text
n=0,1,2,3,4,5: 1,1,2,7,40,357
```

The number of disconnected orders over levels `2,...,5` is exactly `203`.
The sums of down-set counts at levels `1,...,4` are

```text
2,7,40,357
```

and therefore the covariance-loop count is

$$
2\sum_{n=1}^{4}n!\sum_{C\in\Omega_n}|J(C)|=17648,
$$

matching the receipt.

## 3. Extension/down-set theorem

Theorem 2.1 passes.

For a finite order `C`, adding a distinguished maximal event `e` above exactly
a down-set `D` preserves transitivity because every ancestor of an element of
`D` also lies in `D`. No relation leaves `e`, and every old relation is
unchanged. Conversely, the past of a distinguished maximal event in any
old-relation-preserving extension is necessarily a down-set. Covers into `e`
are precisely the maximal elements of that down-set.

End-deletion therefore gives a unique parent. It is surjective because the
empty precursor is always legal. The growth construction enumerates every
naturally labeled order because the past of the top natural label is exactly
such a down-set.

The theorem is also compatible at the **incidence** level with restriction:
for any retained old subset `K`,

$$
C[D]|_{K\cup\{e\}}
=
(C|_K)[D\cap K],
$$

and `D cap K` is a down-set of the induced order. This fact will matter below:
the deterministic arena restricts coherently even though the registered
probability kernels do not.

## 4. Bridge-shadow claims

The bridge terminology is adequately scoped. If `D` meets `k>=2` components
of the old undirected comparability graph, the new event connects exactly
those components through itself. The component count drops by `k-1`. Taking
`D=V` proves existence for every disconnected finite parent.

No old incomparable pair becomes comparable. The result is a common-future
incidence shadow, not a signal, metric adjacency, direct old-old edge, or
sealed interaction diamond. The paper states these nonclaims correctly.

## 5. Labeled-prefix inverse limit and Radon theorem

Theorem 3.1 has the hypotheses it needs.

- Every `Omega_n` is finite and discrete.
- End-deletion is a continuous surjection.
- The countable inverse limit is a closed subspace of a countable product of
  finite discrete spaces; hence it is nonempty, compact, metrizable, and
  zero-dimensional.
- Normalized child kernels give exact cylinder consistency.
- Cylinder sets generate the Borel sigma-algebra.

The countable projective-extension theorem therefore gives one Borel
probability measure on the labeled prefix limit. Every Borel probability on a
compact metrizable space is Radon. Conversely, child cylinders partition a
positive-mass parent cylinder, so

$$
K_n(C'|C)=\frac{\mu_{n+1}(C')}{\mu_n(C)}
$$

is exact. Zero-mass parent cylinders require a separately selected version,
as the paper says.

The receipt's B2/B3 calculation is valid: a child has one end-deletion parent,
and distinct precursors give distinct relations into the new event. Thus the
stored child mass is exactly parent mass times its registered precursor
probability.

## 6. Exact kernel nonselection witness

For the three-element antichain, all eight subsets are down-sets. With
`(a,b)=(1,1)` they are uniform, so the three pairs plus triple have bridge mass
`4/8=1/2`. With `(a,b)=(1,2)`, the empty, singleton, pair, and triple sectors
have total weights `1,3,6,4`; bridge mass is `10/14=5/7`. A fixed pair has
probability `1/8` versus `1/7`.

These formulas are exact, positive, and invariant under isomorphism of the
parent/precursor pair. Both kernels normalize on every finite parent and define
different end-deletion-consistent measures on the same labeled-prefix tower.
The common Decimal value for `exp(-1.1)` is only a report; changing the
placement kernel plainly leaves the v7 survival formula unchanged.

## 7. Major finding: prefix consistency is not restriction projectivity

The paper inherits two mathematically different uses of “projective”:

1. **prefix projectivity:** sum child cylinder masses under end-deletion;
2. **record/stem restriction naturality:** restrict the retained record set and
   compare the pushed-forward extension law with the law recomputed on the
   restricted parent.

D3 proves the first only. Both registered witness kernels fail the second,
even when the retained subset is ancestor-closed.

Take the two-event chain `0<1` and retain the one-element stem `K={0}`. The
full parent has three down-sets:

$$
\varnothing,\quad\{0\},\quad\{0,1\}.
$$

It has one comparability component, so both registered `b` values give each
down-set probability `1/3`. Under `D -> D cap K`, the pushforward is

$$
P(\varnothing)=\frac13,
\qquad
P(\{0\})=\frac23.
$$

But the kernel recomputed on the restricted one-event parent is

$$
P(\varnothing)=P(\{0\})=\frac12.
$$

Thus the restriction square fails exactly for **both** witness laws. This is
not caused by using a non-stem subset; `{0}` is ancestor-closed.

Consequences:

- variable-cardinality growth evades D2's fixed-vertex closure census, but it
  has not yet passed an analogue of D2's all-restriction gate;
- end-deletion consistency does not establish consistency on the stem/covtree
  observable tower;
- Theorem 4.1 may say “local isomorphism covariance plus labeled-prefix
  consistency do not select `b`,” but not unqualified “covariance and
  projectivity do not select the law”;
- the registered family cannot currently serve as a restriction-natural
  interacting record law.

Required repair: add a typed restriction-naturality definition and exact
census. Then either find two inequivalent bridge kernels that satisfy the
chosen restriction rule, prove a new no-go, or explicitly grade this
requirement `OPEN` and narrow every projectivity claim to end-deletion
cylinders.

## 8. Major finding: construction-order gauge is not executed on the witness laws

C1 proves local relabeling covariance of one parent/precursor formula. It does
not prove equality of natural-label path weights, and corrected construction
gauge does not require such equality. For example, under `(1,1)`, two natural
labelings of the same unlabeled chain-plus-isolate three-causet have exact path
weights

$$
\frac12\frac13=\frac16,
\qquad
\frac12\frac14=\frac18.
$$

Under `(1,2)` the corresponding weights are `1/6` and `1/10`. This is allowed
only if those scheduler presentations are pushed forward to a canonical
physical history.

The current C2 check—`1/4+3/4=1`—demonstrates the arithmetic possibility of an
unequal-weight pushforward but defines no scheduler space, quotient map, or
pushforward for `K_{a,b}`. It therefore does not establish that the registered
infinite measures descend to the intended physical quotient.

The finite nonselection signal can be repaired constructively. From the
three-antichain parent, canonicalizing children by precursor size gives

```text
sector             b=1      b=2
empty              1/8      1/14
one ancestor       3/8      3/14
pair bridge        3/8      6/14
triple bridge      1/8      4/14
```

so the two finite canonical pushforwards are visibly different. Add this
actual quotient audit, and distinguish it from the harder problem of a Borel
measure on the completed unlabeled/stem quotient. Until then, Section 9's
general gauge conclusion is an argument, not an executed D3 gate.

## 9. Prefix inverse limit versus covtree

The conceptual distinction in Section 6 is correct and important.

- The prefix level `n` is one naturally labeled `n`-event history, bonded by
  end-deletion of the newest presentation label.
- A covtree level-`n` node is a realizable set of exact-`n` stem types of a
  completed causet, bonded by observable refinement.

For the three-event order `0<1` plus isolated `2`, the ancestor-closed
two-subsets `{0,1}` and `{0,2}` induce a chain and an antichain. Thus its
exact-rank-two stem datum contains two nonisomorphic types, while a two-click
prefix is one order.

The executable establishes this finite stem fact, not the covtree inverse-limit
theorem by itself. To make the witness literally a completed-history covtree
node, extend the finite causet forever by adding each later event above all
existing events; no new two-stem is then created. The v9 stem-spectrum theorem
supplies the general identification of covtree levels with finite Stone
quotients. Paper 4 should identify that imported theorem as the load-bearing
infinite statement and the D3 receipt as only the smallest finite witness.

The paper correctly refuses to identify covtree rank with click time and
correctly says a covtree measure needs a committed-history filtration or
marked lift before becoming a SHARD next-record law.

## 10. Minor findings

### [Minor 1] A6 is a tautological executable gate

A6 checks `len(range(n+1))=len(range(n))+1`. It does not inspect an extension
object or a map into the D2 closure arena. The mathematical separation is
true by construction, but the receipt label overstates what this line tests.

### [Minor 2] C1 should be named local kernel covariance

The 17,648 cases correctly verify

$$
K(\pi D|\pi C)=K(D|C).
$$

They do not verify covariance of the recursively generated path measure under
construction-history quotienting. Rename the gate to prevent it from carrying
the stronger interpretation.

### [Minor 3] “Every legal extension” and cutoff wording should stay precise

The deletion/immutability loop covers children through five events, while the
bridge loop also constructs bridge children of five-event parents at level
six without enumerating the full six-event level. The reported 203-parent
bridge claim is correct, but prose should distinguish “every extension with
child size at most five” from “at least one bridge extension for each audited
parent through size five.”

## 11. Findings that pass

- Natural-order counts and the 203 disconnected-parent count reproduce.
- The extension/down-set correspondence and direct-parent theorem are exact.
- Bridge-shadow existence and component reduction are correct.
- No old-old relation is altered.
- Both rational kernels are positive, normalized, and locally
  isomorphism-covariant.
- Labeled-prefix cylinder consistency and positive-mass kernel recovery are
  exact.
- The inverse-limit Borel probability exists uniquely and is Radon.
- Bridge probabilities `1/2`, `5/7`, `1/8`, and `1/7` are correct.
- Full-history conditioning is not confused with Markov factorization.
- Prefix and covtree inverse limits are correctly distinguished in concept.
- Real/rational marks are correctly excluded from automatic profiniteness.
- The unmarked bridge is not promoted to a metric-local or sealed-diamond
  interaction.
- No cone, dimension, scale, quantum, or continuum result is inferred.

## 12. Verdict and claim ceiling

**Round-1 grade: MAJOR REVISION.** The central correction—new maximal events
can preserve the old past while carrying ancestry from several components—is
accepted. The measure family is a valid nonselection witness on the labeled
prefix tower. It has not passed restriction naturality or an actual
construction-order quotient audit.

Accepted claim ceiling before repair:

1. finite one-maximal-event extension/down-set correspondence;
2. coherent common-future bridge shadows with immutable old relations;
3. unique Radon measure from compatible finite distributions on the labeled
   prefix inverse limit, with ratio recovery on positive cylinders;
4. at least two positive, locally isomorphism-covariant,
   end-deletion-consistent labeled-prefix measures;
5. exact separation between prefix time and covtree observable rank;
6. orthogonality of the v7 conditional survival formula to the displayed
   placement weights.

Not yet accepted:

- a restriction-natural bridge kernel, even on ancestor-closed stems;
- nonselection after imposing the full D2-style restriction requirement;
- descent of the registered infinite measures to a canonical physical or
  covtree quotient;
- a marked, local, sealed-diamond bridge law;
- a selected interaction, click-rate, outcome, transport, geometry,
  continuum, profinite-mark, or quantum law.

## 13. Required openings before round 2

1. Add and execute the ancestor-closed restriction square; record the exact
   failure above.
2. Scope every “projective” claim to prefix/end-deletion consistency unless a
   stronger restriction theorem is proved.
3. Decide whether strong record restriction is required physics, an open
   selector, or a rejected axiom for birth kernels.
4. Replace C2's scalar arithmetic with an actual canonical pushforward of the
   registered child laws and state the remaining infinite-quotient gap.
5. Make the covtree witness a certified completed-history node or explicitly
   cite the v9 certificate theorem as imported input.
6. Rename C1 and repair the A6/cutoff gate wording.

