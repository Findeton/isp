# Relativistic ISP v10 Paper 4: Profinite Growth Preserves the Past but Does Not Select the Law

## Common-future extensions, two inverse limits, and the remaining interacting click-law boundary

**Author:** Felix Robles Elvira (ORCID: 0009-0009-2017-4394; independent researcher)

**Status:** hostile-review passed at the scoped result, 2026-07-11. Three
independent round-1 reviews returned MAJOR REVISION while confirming the core
finite theorem. All concrete openings were executed before round 2; final
mathematics, independent-rebuild, and ontology/locality reviews passed.

**Receipt:** `v10/code/d3_profinite_extension_exact.py` — 27/27 exact and
high-precision checks. All production source is under `v10/code/` and uses
only the Python standard library.

## Abstract

V10 Paper 3 proved that a deterministic, extensive, idempotent,
all-restriction-natural closure on a fixed record set cannot create its first
pair carrier if an isolated pair is forbidden to acquire one. This paper
audits whether the phrase “add nothing; preserve exactly the relationships
already present” was promoted beyond that model.

The correction is structural. A history need not be closed on a fixed vertex
set. It may grow by a new maximal record `e` whose ancestor set is a down-set
`D` of the old finite history. End-deleting `e` restores the old history
exactly and no old-old relation changes, yet `D` may meet several previously
disconnected components. The new event then records a common future of those
components. Its direct parents are the maximal elements of `D`. Thus exact
past preservation is compatible with new incidence; novelty is written into
the new record rather than retroactively inserted between old records.

The exact receipt independently enumerates every naturally labeled order
through five events (`1,1,2,7,40,357`), checks every legal extension and all
203 disconnected parents, and verifies end-deletion, past immutability,
common-future bridge-shadow existence, and direct-parent typing. Two positive rational,
isomorphism-covariant extension kernels generate exactly consistent cylinder
measures on the same finite-prefix tower. On the three-event antichain they
assign different total bridge probabilities, `1/2` and `5/7`, while retaining
the identical v7 conditional click survival $\exp(-\Delta I)$. The resulting
verdict is `CONSISTENT-FAMILY`: immutable-past common-future extension is
coherent, but no local marked interaction law is selected.

Hostile review found a load-bearing limitation and it is now executable. The
deterministic extension arena commutes with all audited old-subset
restrictions, but both positive kernels fail even ancestor-closed restriction
naturality: restricting the chain `0<1` to `{0}` pushes the full kernel to
`(1/3,2/3)`, while recomputing it on the retained point gives `(1/2,1/2)`.
Thus end-deletion prefix consistency is not autonomous subsystem
projectivity. Actual canonical unlabeled **order-shadow** pushforwards nevertheless remain
inequivalent at finite levels: the three-antichain has mass `1/8` versus
`1/10`. A third controlled-zero kernel shows that eligibility is likewise
unselected under the weaker prefix gates, but it earns no stronger
restriction or locality claim.

The profinite connection requires a second correction. The labeled history
inverse limit is a tower of sequential prefixes under end-deletion. The v9
Stone/covtree inverse limit is a tower of finite quotients by stem-observable
resolution. A covtree node can contain several nonisomorphic stems of one
rank, so a covtree step is not automatically one physical record birth.
Covtree dynamics define a covariant stem-observable/spectrum measure. Because
the evaluation map has rogue fibers, this is not automatically a unique
measure on completed causets. A full-history law requires a lift, and a SHARD
next-record interpretation additionally requires a marked physical
filtration. Profinite topology supplies a compact arena and exact consistency
conditions; it does not supply numerical probabilities.

Barandes's indivisible-stochastic formulation is compatible with taking a
complete path measure as primitive. Conditionalizing that measure on the full
committed history then supplies the next-extension law, but this is a
disintegration of an already supplied rulebook, not a derivation of it and
not a claim of Markov divisibility. Once a typed marked support skeleton is
supplied, Paper 3 composes its incidence downstream; full sealed-diamond
gluing and root/bridge selection remain open.

## 1. The assumption under review

Paper 3 considered an operation

$$
F:\mathcal H(V)\longrightarrow\mathcal H(V)
$$

on support systems over one fixed finite vertex set `V`. Under deterministic
covariance, extensivity, idempotence, exact commutation with every induced
restriction, and refusal to add an edge to an edgeless pair, the identity was
forced.

That theorem remains correct. Its scope is now stated more sharply:

> A fixed-vertex shadow-preserving closure cannot bootstrap a first pair
> relation under the frozen refusal axiom.

Neither Barandes ISP, the sealed-record principles, nor the diamond ontology
requires the universe to evolve by such a closure. A birth law changes the
underlying event set:

$$
H_n\longrightarrow H_{n+1}=H_n\cup\{e_n\}.
$$

The physical preservation principle should first mean that committed facts
about old records are not rewritten. It should not be expanded without proof
into a prohibition on every new record having old records as parents.

## 2. One-event extensions

Let $C=(V,\prec)$ be a finite partial order and let $D\subseteq V$ be a
down-set: if $x\in D$ and $y\prec x$, then $y\in D$. Define $C[D]$ by adjoining
one new element $e$ and setting

$$
x\prec e \quad\Longleftrightarrow\quad x\in D,
$$

while retaining every old relation and adding no relation from `e` to an old
element.

### Theorem 2.1 — extension/down-set correspondence

`C[D]` is a partial order with `e` maximal. Deleting `e` returns `C` exactly.
Conversely, every extension of `C` by one distinguished maximal element that
changes no old relation is `C[D]` for the down-set `D=Past(e)`. The direct
parents of `e` are exactly the maximal elements of `D`.

**Proof.** Transitivity involving $e$ is the only point to check. If
$y\prec x\prec e$, then $x\in D$; downward closure gives $y\in D$, hence
$y\prec e$. No relation leaves $e$, so there is no other new transitivity
condition. Deletion is immediate. In the converse direction, transitivity of
the extended order makes `Past(e)` downward closed. An ancestor `x` is a cover
of `e` precisely when no larger member of `Past(e)` lies between them, which
is precisely maximality in `D`. ∎

### Definition 2.2 — bridge shadow

Forget directions temporarily and connect two old elements when they are
comparable in `C`. If `D` meets `k` components of this undirected
comparability graph, adjoining `e` merges those `k` components through `e`.
Call the extension a **bridge shadow** when $k\ge 2$.

The name is deliberately weak. It means that one new record has ancestry in
multiple old components. It does not mean that two old records become
comparable, that a signal passed between them, or that they were nearby in an
emergent metric.

### Corollary 2.3 — bridge existence

Every finite order with at least two comparability components admits a bridge
shadow: take `D=V`, which is a down-set. More selectively, any down-set meeting
multiple components gives one.

The receipt checks all 203 disconnected naturally labeled orders through five
events. The number of components decreases by exactly `k-1`, while all old
relations remain byte-for-byte unchanged.

### Corollary 2.4 — separation from Paper 3

The transition `C -> C[D]` changes cardinality. Paper 3's exhaustive census of
maps on the same vertex set does not contain these transitions. To transfer
its no-go to variable-history growth would require an additional theorem
showing that every legitimate new-event incidence descends to a forbidden
old-old closure. The explicit end-deletion construction refutes that descent
for the causal-order shadow.

## 3. What a primitive history measure supplies

Let $\Omega_n$ be the finite set of naturally labeled $n$-event histories and
let

$$
d_n:\Omega_{n+1}\longrightarrow\Omega_n
$$

delete the top-labeled event. The labeled history space is

$$
\widetilde\Omega=\varprojlim(\Omega_n,d_n).
$$

Every normalized extension kernel

$$
K_n(C'\mid C),\qquad d_n(C')=C,
$$

and initial distribution $\mu_0$ recursively defines

$$
\mu_{n+1}(C')=\mu_n(d_n C')K_n(C'\mid d_n C').
$$

### Theorem 3.1 — kernel/measure equivalence

The resulting finite distributions are **end-deletion prefix consistent**:

$$
\mu_n(C)=\sum_{d_n(C')=C}\mu_{n+1}(C').
$$

Because the tower is countable and finite at every level, these distributions
define a unique Borel probability measure on the compact inverse limit. It is
Radon. Conversely, for any such measure and every positive-mass cylinder,

$$
K_n(C'\mid C)=\frac{\mu_{n+1}(C')}{\mu_n(C)}
$$

recovers the conditional next-extension probabilities. Zero-mass histories
require a separately chosen version and make no on-support prediction.

**Proof.** Normalization of `K_n` gives the displayed consistency identity.
The finite-dimensional distributions therefore satisfy the countable
projective extension theorem; the inverse limit is compact metrizable, so its
Borel probability is Radon. The converse ratio is ordinary conditioning on a
finite partition. ∎

This theorem clarifies, rather than solves, the rulebook problem. If $\mu$ is
primitive, it is the rulebook. Its conditional support supplies the allowed
extensions and its ratios supply their probabilities. If SHARD aims to derive
$\mu$ from finite sealed-record principles, the theorem merely identifies the
object still missing.

## 4. Exact nonselection

For a parent `C` and down-set `D`, the preregistered witness family assigns

$$
w_{a,b}(D\mid C)=a^{|D|}b^{\beta_C(D)},
$$

where `a,b>0` are rational and

$$
\beta_C(D)=\max(0,k_C(D)-1)
$$

with `k_C(D)` the number of old comparability components met by `D`.
Normalizing over all down-sets gives `K_{a,b}`.

This family is not proposed physics. Its component statistic can inspect the
whole finite history and therefore makes an intentionally strong
nonselection witness. Every weight is positive; all laws have exactly the
same possible extensions. Isomorphic parent/precursor pairs have identical
$|D|$ and $\beta$, so the one-step kernels are locally relabeling covariant.

### Theorem 4.1 — local covariance and prefix consistency do not select bridge-shadow weight

The laws `(a,b)=(1,1)` and `(1,2)` are normalized, positive,
locally isomorphism-covariant, and induce end-deletion-consistent measures on
the same history tower, but on the three-element antichain

$$
P_{1,1}(\beta\ge1)=\frac12,
\qquad
P_{1,2}(\beta\ge1)=\frac57.
$$

For any fixed pair precursor the probabilities are `1/8` and `1/7`.

**Proof.** For `b=1`, all eight subsets of the antichain are equally weighted;
the three pairs and the triple are bridges. For `b=2`, the empty set has
weight one, the three singletons total three, the three pairs total six, and
the triple has weight four. The bridge weight is therefore `10/14=5/7`.
The general covariance and consistency statements follow from the invariant
weight formula and Theorem 3.1. The receipt checks 17,648 explicit relabeled
precursor cases and every cylinder through five events. ∎

### Corollary 4.2 — full-history dependence is permission, not selection

Allowing the conditional law to inspect the full recorded history enlarges
the possible law class. It does not provide numerical weights. The two laws
above inspect the same complete parent history and disagree.

### Theorem 4.3 — incidence restricts naturally; the witness probabilities do not

For every retained old subset $K$, the deterministic extension obeys

$$
C[D]|_{K\cup\{e\}}=(C|_K)[D\cap K].
$$

The receipt verifies 6,064 such squares. The probability kernels do not obey
the corresponding autonomous-subsystem equation.

Take the chain $0\prec1$ and retain the ancestor-closed stem $K=\{0\}$. The
full parent has the three down-sets

$$
\varnothing,\quad\{0\},\quad\{0,1\},
$$

each of probability $1/3$ under both positive witness laws. Projecting
$D\mapsto D\cap K$ therefore gives

$$
P_{\mathrm{push}}(\varnothing)=\frac13,
\qquad
P_{\mathrm{push}}(\{0\})=\frac23.
$$

Recomputing the same formula on the isolated retained point instead gives

$$
P_{\mathrm{recompute}}(\varnothing)
=P_{\mathrm{recompute}}(\{0\})=\frac12.
$$

The exhaustive audit finds 212 failed ancestor-closed restriction squares for
`b=1` and 296 for `b=2` through the registered cutoff.

This failure is not a contradiction in the global path measure. Pushforward
subsystem predictions still exist. It says that after records are discarded,
the retained unmarked history is not sufficient to run the same kernel as an
autonomous closed system. A marked no-silent restriction would have to retain
the relevant boundary/environment residue. Whether such marks repair
naturality is open.

Thus D3 proves temporal prefix consistency, not D1/D2-style record-restriction
naturality. Requiring the same unmarked kernel on every retained subset is an
additional autonomy axiom, not a consequence of Barandes indivisibility or of
the prefix inverse limit.

### Proposition 4.4 — actual finite unlabeled order-shadow pushforwards remain inequivalent

At every audited level, the receipt sends each naturally labeled order to its
canonical unlabeled isomorphism class and sums the complete fiber mass. The
orbit probabilities normalize exactly for both laws. Some fibers contain
unequal raw natural-label masses, as permitted by the corrected v9 quotient
discipline, while their finite unmarked pushforward is one orbit mass.

The two pushed-forward laws remain inequivalent. At three events, the
antichain orbit has probability

$$
\frac18\quad\text{for }b=1,
\qquad
\frac1{10}\quad\text{for }b=2.
$$

This is a finite unmarked-quotient nonselection witness. It does not yet
construct a canonical marked-history pushforward or an
infinite measure on an unlabeled prefix inverse limit: deleting “the last”
element is not a canonical bonding map on an unlabeled order. Nor does it
prove consistency on covtree. Those are separate lift/descent problems.

### Proposition 4.5 — prefix-level eligibility is also unselected

Round-1 review required the distinction between weighting and eligibility.
The two preregistered positive laws prove only weighting nonselection because
their supports coincide. A post-review controlled-zero law therefore assigns
zero weight to every precursor with $\beta>0$ and uniform positive weight to
the remaining down-sets. It is normalized on every parent because the empty
precursor always survives. On the three-antichain its bridge-shadow mass is
zero, versus $1/2$ for the positive uniform law.

This establishes eligibility nonselection under local covariance and
end-deletion prefix consistency. It earns no restriction-natural or local
physics claim; it is another global-prefix control.

### Corollary 4.6 — the v7 clock does not place the event

Separate the conditional survival of no seal over evidence increment
$\Delta I$ from the conditional extension type after a seal:

$$
P(\text{no seal}\mid H,\Delta I)=e^{-\Delta I},
\qquad
P(C'\mid\text{seal},H)=K(C'\mid H).
$$

Changing $K$ leaves the first equation untouched. At $\Delta I=1.1$ the
receipt evaluates the common survival at 140-digit working precision while
the bridge-shadow probability changes from `1/2` to `5/7`.

Thus the v7 result fixes an evidence clock conditional on an exposure and a
candidate channel. It does not specify the channel's participating precursor.

## 5. Barandes ISP: no conflict, no selector

Barandes's stochastic-quantum correspondence represents supplied generic,
non-Markovian stochastic dynamics in Hilbert-space language and reconstructs
quantum systems as indivisible stochastic processes. The physical stochastic
law is part of the starting system; the correspondence does not select a
particular law.

A complete path measure can be conditioned on the sigma-algebra generated by
the whole committed history. Writing the resulting conditional probabilities
as one-step kernels is a mathematical disintegration. It does **not** assert
that the physical process is Markovian in a present configuration, nor that a
whole diamond factors through intermediate endpoint kernels. The conditional
may depend on the entire path, and an indivisible interval law need not be
reconstructible from coarse endpoint propagators.

The committed-history filtration, variable extension domain, and conditional
version are therefore part of the primitive rulebook. Barandes indivisibility
does not supply them. On positive prefix cylinders the ratios in Theorem 3.1
fix the version; zero-mass histories retain the stated ambiguity.

Therefore Barandes ISP is compatible with either of two SHARD programs:

1. **primitive-measure program:** posit the full indivisible path law and use
   its conditionals as the click/extension rulebook;
2. **derivation program:** derive that measure from sealed records, diamonds,
   and additional physical principles.

D3 shows that local covariance, end-deletion prefix consistency, past
preservation, and full-history access do not complete the second program.

## 6. Two profinite spaces, two filtrations

V9 established two related but different light profinite spaces.

### 6.1 Labeled prefix history space

The finite quotient at level `n` is one naturally labeled `n`-event prefix.
The bonding map end-deletes the newest construction label. This tower is the
arena used in Theorem 3.1. Its labels are presentation data to be quotiented
or pushed forward when physical covariance is imposed.

### 6.2 Stem spectrum and covtree

The Stone spectrum `X` is the inverse limit of the finite Boolean algebras
generated by stem questions of rank at most `n`. Equivalently, its finite
quotients are covtree nodes: realizable **sets of exact-`n` stem types** of a
completed causet.

These `n` values do not count the committed prefix. They count the resolution
of the questions being asked about a completed history.

The receipt's smallest witness is a three-event causet consisting of a
two-chain plus an isolated event. It contains both a two-chain stem and a
two-antichain stem. Its exact-rank-two covtree datum therefore contains two
nonisomorphic orders. A sequential prefix at two clicks is one order, not a
set of both orders. The receipt extends this finite causet through nine events
by repeatedly adding a universal top and checks that its exact-rank-two stem
theory does not change. The general infinite covtree/spectrum identification
is imported from v9 Paper 7's certificate theorem, not inferred from that
finite check alone.

### Proposition 6.1 — covtree transition is not automatically click birth

A random walk on covtree can define a manifestly covariant measure on the stem
sigma-algebra and hence, in the v9 spectral formulation, a Radon measure on
`X`. But its level transition refines a completed history's stem theory; it is
not by itself the end-deletion transition `C -> C[D]`.

Consequently a covtree law is a primitive covariant
**stem-observable/spectrum measure**. It is not automatically a unique
full-history measure: the evaluation map from completed causets to `X` has
rogue fibers, and surjectivity removes ghost spectrum points without selecting
a lift through those fibers. A full-history law requires such a lift.
Recovering a SHARD next-record law additionally requires a physical
committed-history filtration or marked extension kernel relating
stem-observable refinement to actual seal birth.

### 6.3 What profiniteness really buys

Profinite structure supplies:

- compact spaces of compatible infinite histories;
- finite clopen/cylinder approximations;
- exact consistency conditions on each explicitly chosen inverse tower;
- Radon extension for classical probability states;
- a covariant observable quotient through the stem spectrum.

It does not supply:

- a preferred probability measure;
- common-future eligibility or its weight;
- event marks, screens, collars, or holonomy;
- a physical identification of observable rank with click time;
- an emergent metric or locality rule.

For real or rational marks, the finite-level spaces are not automatically
finite. A marked profinite completion requires finite observable partitions
at each resolution, a compact zero-dimensional mark space, or another
explicit compact topology. D3 claims none of these constructions.

## 7. Diamonds after the correction

The unmarked extension `C[D]` is only the causal-incidence shadow of a possible
new sealed record. If it becomes a genuine joint diamond, the record `e` must
also carry at least:

- its typed participating ports;
- direct parents and ancestry provenance;
- lower/upper screens and any collar data;
- its likelihood/evidence block;
- content, outcome, transport, and retained holonomy marks.

If `D` meets two old components, `e` is a new common-future record. It does not
make its old ancestors comparable. Calling it an `A-B` interaction is licensed
only if the marked event law says both ports jointly affect the sealed outcome.

Once a typed marked support skeleton is supplied, Paper 3's pushout theorem
can compose its **incidence**. It does not compose full probability, screen,
collar, source, transport, or holonomy data. Paper 2's no-silent center can
test its finite boundary logic. A full sealed-diamond gluing theorem remains
open. Neither D1 nor D2 chooses `D`, creates the marked event proposition, or
assigns `K(C[D]|C)`.

## 8. The locality and universe-ledger problem remains

The common-future construction proves logical consistency, not physical
locality. The witness kernel enumerates every legal down-set, inspects the
component structure of the entire finite prefix, and globally normalizes one
next event. It is therefore explicitly a **universe-ledger/global-prefix
control**, unsuitable as a claimed local law. It was preregistered only to
prove nonselection under broad prefix gates.

A primitive global path measure likewise need not imply a machine that scans
the universe at each step; a global probability law can admit local
specifications or decentralized realizations. But no such realization follows
merely from existence of the measure. SHARD still needs one of:

1. an inherited connected root/branch structure, so later joint events are
   licensed by recorded common ancestry;
2. a record-readable bridge eligibility test on finite boundary data;
3. a primitive bridge-sector law whose apparent nonlocality is fundamental;
4. a covariant eternal-history measure with no physical global commit step,
   plus an account of local conditional observations.

The first is an initial-condition answer. The second would be a derivation.
The third is a new postulate. The fourth changes the ontology of becoming.
D3 does not choose among them.

## 9. Construction-order gauge after the correction

Construction order remains presentation when different scheduler histories
push forward to the same canonical marked history. Equal raw path weights are
not required. The repaired receipt now forms the actual canonical unlabeled
pushforward of every audited finite level for both witness laws. It finds
orbits whose raw natural-label masses differ, sums every fiber exactly, and
shows that the resulting unmarked finite distributions remain different—for
example, three-antichain mass `1/8` versus `1/10`.

The labeled prefix tower is therefore a computational cover. A physical law
must either:

- descend consistently to canonical marked histories;
- be defined on a covariant spectrum together with any required history lift;
- or specify why some recorded ordering distinction is physical.

This gauge requirement constrains how a supplied kernel is presented. It does
not select the kernel's orbit weights. D3 proves finite quotient
nonselection, not an infinite unlabeled-prefix descent or a covtree measure
for these kernels.

## 10. Consequences for cone shape and dimension

D3 changes the admissible architecture of the builder but produces no cone or
dimension result. The correct downstream order is:

$$
\text{selected/posited marked extension measure}
\longrightarrow
\text{generated record histories}
\longrightarrow
\text{v9 cone, dimension, and scale-ladder instruments}.
$$

The old v9 diffusion builder remains evidence that gentle continuous transfer
reduces its measured anisotropy. D3 neither derives that transfer nor predicts
that a common-future law makes cones rounder. When a full marked law is available,
its implications for anisotropy, effective dimension, stationarity, and scale
dependence must be rerun rather than inferred verbally.

## 11. Conclusion

The foundational correction is:

$$
\boxed{
\text{preserve every old recorded relation}
\;\not\Rightarrow\;
\text{forbid new common-future incidence to a new record}.}
$$

One-record maximal extensions provide the exact mechanism. A new record may
have parents in previously disconnected parts of the old history, while
end-deletion restores the past and no old relation is rewritten. This evades
the fixed-vertex closure no-go without refuting it.

But the correction does not finish the dynamics. Compatible prefix kernels
and labeled path measures are equivalent on their positive support; local
covariance and end-deletion consistency allow inequivalent finite unmarked
pushforwards; both positive witnesses fail autonomous record-restriction
naturality; and the v7 evidence clock does not place the event. Barandes ISP
permits a primitive full-history law but does not select its filtration,
extension domain, or measure. D2 composes only supplied marked-support
incidence. The two profinite towers distinguish sequential birth from
covariant observable refinement, while a spectrum measure still needs a
history lift and marked click filtration.

The D3 verdict is therefore

$$
\boxed{\texttt{CONSISTENT-FAMILY}:\quad
\text{immutable-past common-future extension is coherent;}
\quad\text{no local marked law is selected}.}
$$

The next decisive problem is narrower than before: construct or rule out a
record-readable **local common-future eligibility and weighting law** on
marked sealed-diamond histories, including the no-silent boundary marks needed
for subsystem restriction. If none exists, SHARD must explicitly choose
between a connected boundary seed, a primitive nonlocal bridge sector, and a
lifted eternal covariant history measure.

## Reproducibility

Run from the repository root:

```bash
PYTHONDONTWRITEBYTECODE=1 \
  python3 v10/code/d3_profinite_extension_exact.py
```

The executable uses exact integers and `Fraction` for every theorem gate and
`Decimal` at precision 140 only for the printed exponential survival value.
It reports 27/27 checks after round-1 repairs. The separate
`v10_self_containment_audit.py` includes D3 and verifies the standard-library,
location, duplicate-source, and cache-artifact gates.

## References

1. J. A. Barandes, “The Stochastic-Quantum Correspondence,” Philosophy of
   Physics 3, 8 (2025), arXiv:2302.10778.
2. J. A. Barandes, “The Stochastic-Quantum Theorem,” arXiv:2309.03085.
3. J. A. Barandes, “Quantum Systems as Indivisible Stochastic Processes,”
   arXiv:2507.21192.
4. D. P. Rideout and R. D. Sorkin, “A Classical Sequential Growth Dynamics
   for Causal Sets,” Phys. Rev. D 61, 024002 (2000), gr-qc/9904062.
5. F. Dowker, N. Imambaccus, A. Owens, R. D. Sorkin, and S. Zalel, “A
   manifestly covariant framework for causal set dynamics,” Class. Quantum
   Grav. 37, 085003 (2020), arXiv:1910.07292.
6. G. Brightwell, F. Dowker, R. García, J. Henson, and R. D. Sorkin,
   “Observables in causal set cosmology,” Phys. Rev. D 67, 084031 (2003),
   gr-qc/0210061.
7. Relativistic ISP v9 Paper 7, “The stem spectrum.”
8. Relativistic ISP v9 Paper 9, “Construction-order gauge and the
   underdetermination of the interacting record click law.”
9. Relativistic ISP v10 Papers 1–3.
